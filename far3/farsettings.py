import logging

from .far3cffi import ffi, ffic
from .plugin import PluginBase


log = logging.getLogger(__name__)


class Settings(PluginBase):
    def __init__(self, parent, info):
        super().__init__(parent, info)
        self.Handle = None
        self.Root = None

    def Open(self):
        log.debug('setting.open')
        _settings = (
            ffi.sizeof("struct FarSettingsCreate"),
            self.UUID2GUID(self.PluginInfo.pyguid, False),
            ffic.INVALID_HANDLE_VALUE
        )
        psettings = ffi.new("struct FarSettingsCreate *", _settings)
        rc = self.info.SettingsControl(ffic.INVALID_HANDLE_VALUE, ffic.SCTL_CREATE, 0, psettings)
        if rc == 0:
            raise IOError(2, 'closed settings')

        Handle = psettings.Handle
        _settings = (
            ffi.sizeof("struct FarSettingsValue"),
            0,
            self.s2f('{'+str(self.PluginInfo.guid)+'}'),
        )
        psettings = ffi.new("struct FarSettingsValue *", _settings)
        rc = self.info.SettingsControl(Handle, ffic.SCTL_OPENSUBKEY, 0, psettings)
        if rc == 0:
            rc = self.info.SettingsControl(Handle, ffic.SCTL_CREATESUBKEY, 0, psettings)
        if rc == 0:
            raise IOError(2, 'closed settings')
        self.Handle = Handle
        self.Root = 0

    def Close(self):
        log.debug('setting.close')
        assert self.Handle is not None
        rc = self.info.SettingsControl(self.Handle, ffic.SCTL_FREE, 0, ffi.NULL)
        if rc == 0:
            raise IOError(2, 'closed settings ?')
        self.Handle = None
        self.Root = None

    def Get(self, name, default=None):
        log.debug('setting.get')
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
            self.Root, self.s2f(name),
            t, {"Number": 0}
        ))
        rc = self.info.SettingsControl(self.Handle, ffic.SCTL_GET, 0, item)
        if rc == 1:
            if t == ffic.FST_STRING:
                result = self.f2s(item.Value.String)
            elif t == ffic.FST_QWORD:
                result = item.Value.Number
            else:
                nb = item.Value.Data.Size
                result = b''.join(ffi.cast('char *', item.Value.Data.Data)[0:nb])
        else:
            result = default
        log.debug('setting.get rc={} result={}'.format(rc, result))
        return result

    def Set(self, name, value):
        log.debug('setting.set')
        assert self.Handle is not None
        t = type(value)
        if t == str:
            item = ffi.new("struct FarSettingsItem *", (
                ffi.sizeof("struct FarSettingsItem"),
                self.Root, self.s2f(name),
                ffic.FST_STRING, {
                    "String": self.s2f(value)
                }
            ))
        elif t == int:
            item = ffi.new("struct FarSettingsItem *", (
                ffi.sizeof("struct FarSettingsItem"),
                self.Root, self.s2f(name),
                ffic.FST_QWORD, {
                    "Number": value
                }
            ))
        elif t == bytes:
            item = ffi.new("struct FarSettingsItem *", (
                ffi.sizeof("struct FarSettingsItem"),
                self.Root, self.s2f(name),
                ffic.FST_DATA, {
                    "Data": {
                        "Data": ffi.new("char[]", value),
                        "Size": len(value)
                    }
                }
            ))
        else:
            raise TypeError("Unsupported value type", value)
        rc = self.info.SettingsControl(self.Handle, ffic.SCTL_SET, 0, item)
        log.debug('setting.set rc={}'.format(rc))
        return rc
