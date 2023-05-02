from far3 import *

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
        self.v = None
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
            elif item.Type == ffic.FST_DATA:
                self.v = ffi.new("char[]", value)
                item.Value.Data.Data = self.v
                item.Value.Data.Size = len(value)
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
            elif item.Type == ffic.FST_DATA:
                nb = item.Value.Data.Size
                value = b''.join(ffi.cast('char *', item.Value.Data.Data)[0:nb])
            else:
                value = None
            print('set: name={} type={} value={}'.format(name, item.Type, value))
            self.dct[name] = value
            return 1
        else:
            print('what? h={} op={} z={}, item={}'.format(h, op, z, item))
            print('v.size={} v.root={} v.value={}'.format(item.StructSize, item.Root, f2s(item.Value)))
            return 1
        return 0

from far3.plugin import PluginBase
from far3.farsettings import Settings

class Plugin(PluginBase):
    name = 'pyconfig'
    flags = ffic.PF_NONE
    title = "Python plugin config"
    author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
    description = title
    guid = uuid.UUID('{FB57FE63-08FE-4CF1-9BE4-1E1CB44C12B1}')

    openFrom = ['PLUGINSMENU']

info = Info()
plugin = Plugin(info)

cls = Settings()
cls.Open(plugin)
try:
    print('string', 'ala', 'ala')
    cls.Set('ala', 'ala')
    result = cls.Get('ala', '')
    print('result', result)
    print('number', 'ola', 1)
    cls.Set('ola', 1)
    result = cls.Get('ola', 0)
    print('result', result)
    cls.Set('olek', b'123456abc')
    result = cls.Get('olek')
    print('result', result)
finally:
    cls.Close()
