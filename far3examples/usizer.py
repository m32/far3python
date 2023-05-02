import logging
from far3.plugin import PluginBase
from far3.fardialogbuilder import (
    Spacer,
    TEXT, EDIT, PASSWORD, MASKED, MEMOEDIT,
    BUTTON, CHECKBOX, RADIOBUTTON, COMBOBOX,
    LISTBOX, USERCONTROL,
    HLine,
    HSizer, VSizer,
    DialogBuilder
)

log = logging.getLogger(__name__)


class Plugin(PluginBase):
    label = "Python Dialog Demo"
    openFrom = ["PLUGINSMENU"]
    name = "usizer"
    flags = ffic.PF_NONE
    author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
    description = title
    guid = uuid.UUID("{D75C02FC-FBC7-4CF7-8B0C-B617001A732C}")

    def OpenW(self, Info):
        @self.ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            if Msg == self.ffic.DN_INITDIALOG:
                try:
                    dlg.SetText(dlg.ID_vapath, "vapath initial")
                    dlg.SetText(dlg.ID_vbpath, "vbpath initial")
                    dlg.Disable(dlg.ID_vbpath)
                    dlg.SetCheck(dlg.ID_vallow, 1)
                    dlg.SetFocus(dlg.ID_vseconds)
                    # override value from constructor
                    dlg.SetCheck(dlg.ID_vr1, self.ffic.BSTATE_CHECKED)
                    dlg.SetCheck(dlg.ID_vc3, self.ffic.BSTATE_CHECKED)
                except:
                    log.exception('bang')
            elif Msg == self.ffic.DN_BTNCLICK:
                pass
            elif Msg == self.ffic.DN_KEY:
                if Param2 == self.ffic.KEY_LEFT:
                    pass
                elif Param2 == self.ffic.KEY_UP:
                    pass
                elif Param2 == self.ffic.KEY_RIGHT:
                    pass
                elif Param2 == self.ffic.KEY_DOWN:
                    pass
                elif Param2 == self.ffic.KEY_ENTER:
                    pass
                elif Param2 == self.ffic.KEY_ESC:
                    pass
            elif Msg == self.ffic.DN_MOUSECLICK:
                pass
            return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)

        b = DialogBuilder(
            self,
            DialogProc,
            "Python dialog",
            "helptopic",
            0,
            VSizer(
                HSizer(
                    TEXT("a path"),
                    EDIT("vapath", 33, 40),
#                    TEXT("X"),
                ),
                HSizer(
                    TEXT("b path"),
                    EDIT("vbpath", 20, 30),
#                    TEXT("X"),
                ),
                HLine(),
                HSizer(
                    CHECKBOX('vallow', "Allow"),
                    TEXT("Password"),
                    PASSWORD("vuserpass", 8, 15),
                    TEXT("Seconds"),
                    MASKED("vseconds", "9999"),
#                    TEXT("X"),
                ),
                #MEMOEDIT("vmemo", 40, 5, 512),
                HLine(),
                HSizer(
                    RADIOBUTTON('vr1', "p1", flags=self.ffic.DIF_GROUP),
                    RADIOBUTTON('vr2', "p2"),
                    RADIOBUTTON('vr3', "p3", self.ffic.BSTATE_CHECKED),
#                    TEXT("X"),
                ),
                HSizer(
                    LISTBOX("vlist", 1, "element A", "element B", "element C", "element D"),
                    COMBOBOX("vcombo", 2, "element A", "element B", "element C", "element D"),
                    VSizer(
                        CHECKBOX('vc1', "c1"),
                        CHECKBOX('vc2', "c2"),
                        CHECKBOX('vc3', "c3", self.ffic.BSTATE_CHECKED),
                    ),
#                    TEXT("X"),
                ),
                HLine(),
                HSizer(
                    BUTTON('vok', "OK", True, flags=self.ffic.DIF_CENTERGROUP),
                    BUTTON('vcancel', "Cancel", flags=self.ffic.DIF_CENTERGROUP),
                ),
            ),
        )
        dlg = b.build(-1, -1)

        res = self.info.DialogRun(dlg.hDlg)
        log.debug('''\
ok={} \
a path=[{}] \
b path=[{}] \
allow={} \
pass=[{}] \
seconds=[{}] \
radio1={} \
radio2={} \
radio3={} \
checkbox1={} \
checkbox2={} \
checkbox3={} \
vlist={} \
vcombo={} \
'''.format(
    res == dlg.ID_vok,
    dlg.GetText(dlg.ID_vapath),
    dlg.GetText(dlg.ID_vbpath),
    dlg.GetCheck(dlg.ID_vallow),
    dlg.GetText(dlg.ID_vuserpass),
    dlg.GetText(dlg.ID_vseconds),
    dlg.GetCheck(dlg.ID_vr1),
    dlg.GetCheck(dlg.ID_vr2),
    dlg.GetCheck(dlg.ID_vr3),
    dlg.GetCheck(dlg.ID_vc1),
    dlg.GetCheck(dlg.ID_vc2),
    dlg.GetCheck(dlg.ID_vc3),
    dlg.GetCurPos(dlg.ID_vlist),
    dlg.GetCurPos(dlg.ID_vcombo),
))
        self.info.DialogFree(dlg.hDlg)
