import logging

from .far3cffi import ffi, ffic
from .plugin import PluginBase


log = logging.getLogger(__name__)


class Settings(PluginBase):
    def __init__(self, parent, info):
        super().__init__(parent, info)
        self.Handle = None

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
        self.Handle = psettings.Handle

    def Close(self):
        log.debug('setting.close')
        assert self.Handle is not None
        rc = self.info.SettingsControl(self.Handle, ffic.SCTL_FREE, 0, ffi.NULL)
        if rc == 0:
            raise IOError(2, 'closed settings ?')

    def GetString(self, name):
        log.debug('setting.getString')
        assert self.Handle is not None
        item = ffi.new("struct FarSettingsItem *", (
            ffi.sizeof("struct FarSettingsItem"),
            0, self.s2f(name), ffic.FST_STRING, {"Number": 0}
        ))
        rc = self.info.SettingsControl(self.Handle, ffic.SCTL_GET, 0, item)
        if rc == 1 and item.Value.String:
            result = self.f2s(item.Value.String)
        else:
            result = None
        log.debug('setting.getString rc={} result={}'.format(rc, result))
        return result

    def GetNumber(self, name):
        log.debug('setting.getInt')
        assert self.Handle is not None
        item = ffi.new("struct FarSettingsItem *", (
            ffi.sizeof("struct FarSettingsItem"),
            0, self.s2f(name), ffic.FST_QWORD, {"Number": 0}
        ))
        rc = self.info.SettingsControl(self.Handle, ffic.SCTL_GET, 0, item)
        if rc == 1:
            result = item.Value.Number
        else:
            result = None
        log.debug('setting.getNumber rc={} result={}'.format(rc, result))
        return result

    def SetString(self, name, value):
        log.debug('setting.setString')
        assert self.Handle is not None
        item = ffi.new("struct FarSettingsItem *", (
            ffi.sizeof("struct FarSettingsItem"),
            0, self.s2f(name), ffic.FST_STRING, {"String": self.s2f(value)}
        ))
        rc = self.info.SettingsControl(self.Handle, ffic.SCTL_SET, 0, item)
        log.debug('setting.SetString rc={}'.format(rc))
        return rc

    def SetNumber(self, name, value):
        log.debug('setting.setNumber')
        assert self.Handle is not None
        item = ffi.new("struct FarSettingsItem *", (
            ffi.sizeof("struct FarSettingsItem"),
            0, self.s2f(name), ffic.FST_QWORD, {"Number": value}
        ))
        rc = self.info.SettingsControl(self.Handle, ffic.SCTL_SET, 0, item)
        log.debug('setting.setNumber rc={}'.format(rc))
        return rc
