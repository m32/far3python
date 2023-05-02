from far3.far3cffi import ffi, ffic
from far3 import pluginmanager
from far3 import fardialogbuilder as dlgb

import os
cwd = os.getcwd().encode('ascii')
fcwd = ffi.new("char []", cwd)

pluginmanager.PySetup(fcwd)

def s2f(s):
    return ffi.new("wchar_t []", s)

def f2s(s):
    return ffi.string(ffi.cast("wchar_t *", s))

class Info:
    def Message(self, guid1, guid2, Flags, HelpTopic, Items, ItemsNumber, ButtonsNumber):
        print('Message', guid1, guid2, Flags, HelpTopic, Items, ItemsNumber, ButtonsNumber
        )
        return 0

    def SendDlgMessage(self, hdlg, cmd, p1, p2):
        print('SendDlgMessage', hdlg, cmd, p1, p2)
        s = s2f('result abc')
        return s

    def DialogInit(self, guid1, guid2, x1, y1, x2, y2, HelpTopic, Item, ItemsNumber, Reserved, Flags, DlgProc, Param):
        print('DialogInit', guid1, guid2, x1, y1, x2, y2, HelpTopic, Item, ItemsNumber, Reserved, Flags, DlgProc, Param
        )
        return 12345678

    def DialogRun(self, hDlg):
        print('DialogRun', hDlg)
        return 0

    def DialogFree(self, hDlg):
        print('DialogFree', hDlg)

def main():
    info = Info()
    from far3 import upythonconfig
    cls = upythonconfig.Plugin(info)
    #cls.OpenW(None)

    @ffi.callback("FARWINDOWPROC")
    def DialogProc(hDlg, Msg, Param1, Param2):
        return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)

    # { DI_DOUBLEBOX, L-2,1, E+2,2+H, 0, nullptr,nullptr, 0, title.c_str() },
    b = dlgb.DialogBuilder(
        cls,
        DialogProc,
        "Python path",
        "pythonpath",
        0,
        dlgb.VSizer(
            dlgb.HSizer(
                dlgb.TEXT(text="Python path:"),
                dlgb.EDIT("path", width=60, maxlength=120)
            ),
            dlgb.HSizer(
                dlgb.BUTTON('vok', text="OK", flags=ffic.DIF_DEFAULTBUTTON|ffic.DIF_CENTERGROUP),
                dlgb.BUTTON('vcancel', text="Cancel", flags=ffic.DIF_CENTERGROUP),
            ),
        ),
    )

    dlg = b.build(-1, -1)
    dlg.SetText(dlg.ID_path, 'abc')
    res = dlg.Info.DialogRun(dlg.hDlg)
    path = dlg.GetText(dlg.ID_path)
    print('DialogRun={}, path={}'.format(res, path))
    dlg.close()
main()
