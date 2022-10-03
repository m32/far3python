from far3.far3cffi import ffi, ffic
from far3 import farsettings
from far3 import pluginmanager

import os
cwd = os.getcwd().encode('ascii')
fcwd = ffi.new("char []", cwd)

pluginmanager.PySetup(fcwd)

def s2f(s):
        return ffi.new("wchar_t []", s)

def f2s(s):
    return ffi.string(ffi.cast("wchar_t *", s))

class Info:
    def __init__(self):
        self.dct = {}
    def SettingsControl(self, h, op, z, item):
        if op == ffic.SCTL_CREATE:
            print('create')
            return 1
        elif op == ffic.SCTL_FREE:
            print('free')
            return 1
        elif op == ffic.SCTL_GET:
            name = f2s(item.Name)
            value = self.dct[name]
            if item.Type == ffic.FST_STRING:
                item.Value.String = s2f(value)
            elif item.Type == ffic.FST_QWORD:
                item.Value.Number = value
            else:
                value = None
            print('get: name={} type={} value={}'.format(name, item.Type, value))
            return 1
        elif op == ffic.SCTL_SET:
            name = f2s(item.Name)
            if item.Type == ffic.FST_STRING:
                value = f2s(item.Value.String)
            elif item.Type == ffic.FST_QWORD:
                value = item.Value.Number
            else:
                value = None
            print('set: name={} type={} value={}'.format(name, item.Type, value))
            self.dct[name] = value
            return 1
        return 0

info = Info()
cls = farsettings.Settings(None, info)
cls.Open()
try:
    print('string', 'ala', 'ala')
    cls.SetString('ala', 'ala')
    result = cls.GetString('ala')
    print('result', result)
    print('number', 'ola', 1)
    cls.SetNumber('ola', 1)
    result = cls.GetNumber('ola')
    print('result', result)
finally:
    cls.Close()
