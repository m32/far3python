import logging
import uuid

from .far3cffi import ffi, ffic
from .plugin import PluginBase
from . import fardialogbuilder as dlgb
from .farsettings import Settings

log = logging.getLogger(__name__)


class Plugin(PluginBase):
    name = "pyconfig"
    flags = ffic.PF_NONE
    title = "Python plugin config"
    author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
    description = title
    guid = uuid.UUID("{FB57FE63-08FE-4CF1-9BE4-1E1CB44C12B1}")

    openFrom = ["CONFIGURE"]

    def ConfigureW(self, Info):
        log.debug("Open".format(self.title))
        settings = Settings()
        try:
            settings.Open(self)
            try:
                path = settings.Get("PLUGINSPATH", "")
            finally:
                settings.Close()
        except:
            log.exception("setting.getString")
            path = ""

        log.debug("setting.getString={}".format(path))

        @ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)

        b = dlgb.DialogBuilder(
            self,
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
                    dlgb.BUTTON("vok", text="OK", flags=ffic.DIF_DEFAULTBUTTON|ffic.DIF_CENTERGROUP),
                    dlgb.BUTTON("vcancel", text="Cancel", flags=ffic.DIF_CENTERGROUP),
                ),
            ),
        )
        dlg = b.build(
            -1,
            -1
        )
        log.debug("SetText({}, {})".format(dlg.ID_path, path))
        dlg.SetText(dlg.ID_path, path)
        res = self.Info.DialogRun(dlg.hDlg)
        path = dlg.GetText(dlg.ID_path)
        dlg.close()
        if res == -1:
            return
        log.debug("path: {0}".format(path))
        settings = Settings()
        try:
            settings.Open(self)
            try:
                settings.Set("PLUGINSPATH", path)
            finally:
                settings.Close()
        except:
            log.exception("setting.setString")
