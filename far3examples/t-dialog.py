from far3.far3cffi import ffi, ffic
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
    def Message(self, PluginId, Id, Flags, HelpTopic, Items, ItemsNumber, ButtonsNumber):
        print('Message',
PluginId, Id, Flags, HelpTopic, Items, ItemsNumber, ButtonsNumber
        )
        return 0

    def DialogInit(self, PluginId, Id, x1, y1, x2, y2, HelpTopic, Item, ItemsNumber, Reserved, Flags, DlgProc, Param):
        print('DialogInit',
PluginId, Id, x1, y1, x2, y2, HelpTopic, Item, ItemsNumber, Reserved, Flags, DlgProc, Param
        )
        return 12345678
    def DialogRun(self, hDlg):
        print('DialogRun', hDlg)
        return 0
    def DialogFree(self, hDlg):
        print('DialogFree', hDlg)

def main():
    info = Info()
    import utranslate
    cls = utranslate.Plugin(None, info)
    cls.OpenW(None)
    cls.Dialog()
main()
