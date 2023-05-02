import logging

from .far3cffi import ffi, ffic


class Settings(object):
    def Open(self, plugin):
        _settings = (
            ffi.sizeof("struct FarSettingsCreate"),
            plugin.UUID2GUID(plugin.pyguid, False),
            ffic.INVALID_HANDLE_VALUE
        )
        psettings = ffi.new("struct FarSettingsCreate *", _settings)
        rc = plugin.Info.SettingsControl(ffic.INVALID_HANDLE_VALUE, ffic.SCTL_CREATE, 0, psettings)
        if rc == 0:
            raise IOError(2, "closed settings")

        Handle = psettings.Handle
        _settings = (
            ffi.sizeof("struct FarSettingsValue"),
            0,
            plugin.s2f("{"+str(plugin.guid)+"}"),
        )
        psettings = ffi.new("struct FarSettingsValue *", _settings)
        rc = plugin.Info.SettingsControl(Handle, ffic.SCTL_OPENSUBKEY, 0, psettings)
        if rc == 0:
            rc = plugin.Info.SettingsControl(Handle, ffic.SCTL_CREATESUBKEY, 0, psettings)
        if rc == 0:
            raise IOError(2, "closed settings")
        self.Handle = Handle
        self.Root = 0
        self.plugin = plugin

    def Close(self):
        assert self.Handle is not None
        rc = self.plugin.Info.SettingsControl(self.Handle, ffic.SCTL_FREE, 0, ffi.NULL)
        if rc == 0:
            raise IOError(2, "closed settings ?")
        self.Handle = None
        self.Root = None
        self.plugin = None

    def Get(self, name, default=None):
        assert self.Handle is not None
        t = type(default)
        if t == str:
            t = ffic.FST_STRING
        elif t == int:
            t = ffic.FST_QWORD
        else:
            t = ffic.FST_DATA
        item = ffi.new("struct FarSettingsItem *", (
            ffi.sizeof("struct FarSettingsItem"),
            self.Root, self.plugin.s2f(name),
            t, {"Number": 0}
        ))
        rc = self.plugin.Info.SettingsControl(self.Handle, ffic.SCTL_GET, 0, item)
        if rc == 1:
            if t == ffic.FST_STRING:
                result = self.plugin.f2s(item.Value.String)
            elif t == ffic.FST_QWORD:
                result = item.Value.Number
            else:
                nb = item.Value.Data.Size
                result = b"".join(ffi.cast("char *", item.Value.Data.Data)[0:nb])
        else:
            result = default
        log = logging.getLogger(__name__)
        log.debug("setting.get({},{})={} result={}".format(name, default, rc, result))
        return result

    def Set(self, name, value):
        assert self.Handle is not None
        root = self.plugin.s2f(name)
        t = type(value)
        if t == str:
            s = self.plugin.s2f(value)
            item = ffi.new("struct FarSettingsItem *", (
                ffi.sizeof("struct FarSettingsItem"),
                self.Root, root,
                ffic.FST_STRING, {
                    "String": s
                }
            ))
        elif t == int:
            item = ffi.new("struct FarSettingsItem *", (
                ffi.sizeof("struct FarSettingsItem"),
                self.Root, root,
                ffic.FST_QWORD, {
                    "Number": value
                }
            ))
        elif t == bytes:
            data = ffi.new("char[]", value)
            item = ffi.new("struct FarSettingsItem *", (
                ffi.sizeof("struct FarSettingsItem"),
                self.Root, self.plugin.s2f(name),
                ffic.FST_DATA, {
                    "Data": {
                        "Data": data,
                        "Size": len(value)
                    }
                }
            ))
        else:
            raise TypeError("Unsupported value type", value)
        rc = self.plugin.Info.SettingsControl(self.Handle, ffic.SCTL_SET, 0, item)
        log = logging.getLogger(__name__)
        log.debug("setting.set({}, {})={}".format(name, value, rc))
        return rc
