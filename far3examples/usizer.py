import logging
import uuid

from far3.far3cffi import ffi, ffic
from far3.plugin import PluginBase, handle_error
from far3.fardialogbuilder import (
    TEXT, EDIT, PASSWORD, MASKED,
    #MEMOEDIT,
    BUTTON, CHECKBOX, RADIOBUTTON, COMBOBOX,
    LISTBOX, BOX, USERCONTROL,
    HLine,
    HSizer, VSizer,
    DialogBuilder
)

log = logging.getLogger(__name__)


class Plugin(PluginBase):
    name = "usizer"
    flags = ffic.PF_NONE
    title = "Python Dialog Demo"
    author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
    description = title
    guid = uuid.UUID("{D75C02FC-FBC7-4CF7-8B0C-B617001A732C}")
    version = (1, 0, 0, 0, ffic.VS_SPECIAL)
    openFrom = ["PLUGINSMENU"]

    @handle_error
    def OpenW(self, Info):
        def pyDialogProc(hDlg, Msg, Param1, Param2):
            if Msg == ffic.DN_INITDIALOG:
                try:
                    dlg.SetText(dlg.ID_vapath, "vapath initial")
                    dlg.SetText(dlg.ID_vbpath, "vbpath initial")
                    dlg.Disable(dlg.ID_vbpath)
                    dlg.SetCheck(dlg.ID_vallow, 1)
                    dlg.SetFocus(dlg.ID_vseconds)
                    # override value from constructor
                    dlg.SetCheck(dlg.ID_vr1, ffic.BSTATE_CHECKED)
                    dlg.SetCheck(dlg.ID_vc3, ffic.BSTATE_CHECKED)
                except:
                    log.exception('bang')
            return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)

        @ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            try:
                return pyDialogProc(hDlg, Msg, Param1, Param2)
            except:
                log.exception('dialog proc')

        b = DialogBuilder(
            self,
            DialogProc,
            "Python dialog",
            "helptopic",
            0,
            VSizer(
                HSizer(
                    TEXT(None, "a path"),
                    EDIT("vapath", 33, 40),
#                    TEXT("X"),
                ),
                HSizer(
                    TEXT(None, "b path"),
                    EDIT("vbpath", 20, 30),
#                    TEXT("X"),
                ),
                HLine(),
                HSizer(
                    CHECKBOX('vallow', "Allow"),
                    TEXT(None, "Password"),
                    PASSWORD("vuserpass", 8, 15),
                    TEXT(None, "Seconds"),
                    MASKED("vseconds", "9999"),
#                    TEXT("X"),
                ),
                #MEMOEDIT("vmemo", 40, 5, 512),
                HLine(),
                HSizer(
                    RADIOBUTTON('vr1', "p1", flags=ffic.DIF_GROUP),
                    RADIOBUTTON('vr2', "p2"),
                    RADIOBUTTON('vr3', "p3", ffic.BSTATE_CHECKED),
#                    TEXT("X"),
                ),
                HSizer(
                    LISTBOX("vlist", 1, "element A", "element B", "element C", "element D"),
                    COMBOBOX("vcombo", 2, "element A", "element B", "element C", "element D"),
                    VSizer(
                        CHECKBOX('vc1', "c1"),
                        CHECKBOX('vc2', "c2"),
                        CHECKBOX('vc3', "c3", ffic.BSTATE_CHECKED),
                    ),
#                    TEXT("X"),
                ),
                HLine(),
                HSizer(
                    BUTTON('vok', "OK", flags=ffic.DIF_DEFAULTBUTTON|ffic.DIF_CENTERGROUP),
                    BUTTON('vcancel', "Cancel", flags=ffic.DIF_CENTERGROUP),
                ),
            ),
        )
        dlg = b.build(-1, -1)
        res = self.Info.DialogRun(dlg.hDlg)
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
        self.Info.DialogFree(dlg.hDlg)
