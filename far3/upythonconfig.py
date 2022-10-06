import logging
import uuid

from .far3cffi import ffi, ffic
from .plugin import PluginBase
from . import fardialogbuilder as dlgb
from .farsettings import Settings

log = logging.getLogger(__name__)


class Plugin(PluginBase):
    class PluginInfo:
        name = 'pyconfig'
        flags = ffic.PF_NONE
        title = "Python plugin config"
        author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
        description = title
        pyguid = uuid.UUID('{308868BA-5773-4C89-8142-DF877868E06A}')
        guid = uuid.UUID('{FB57FE63-08FE-4CF1-9BE4-1E1CB44C12B1}')
        version = (1, 0, 0, 0, ffic.VS_SPECIAL)

        openFrom = ['PLUGINSMENU']

    def __init__(self, parent, info):
        super().__init__(parent, info)
        self.settings = Settings(self, self.info)

    def OpenW(self, Info):
        log.debug('plg: {}.OpenW'.format(self.PluginInfo.title))
        try:
            self.settings.Open()
            try:
                path = self.settings.Get('PLUGINSPATH', '')
            finally:
                self.settings.Close()
        except:
            log.exception('setting.getString')
            path = None
        path = path or ''

        @ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)

        b = dlgb.DialogBuilder(
            self,
            DialogProc,
            "Python path",
            "pythonpath",
            0,
            dlgb.VSizer(
                dlgb.HSizer(dlgb.TEXT("Python path:"), dlgb.Spacer(), dlgb.EDIT("path", 60, 120)),
            ),
        )
        dlg = b.build(
            self.UUID2GUID(self.PluginInfo.pyguid),
            self.UUID2GUID(self.PluginInfo.guid),
            -1,
            -1
        )
        dlg.SetText(dlg.ID_path, path)
        res = self.info.DialogRun(dlg.hDlg)
        path = dlg.GetText(dlg.ID_path)
        self.info.DialogFree(dlg.hDlg)
        if res == -1:
            return
        log.debug('path: {0}'.format(path))
        try:
            self.settings.Open()
            try:
                rc = self.settings.Set('PLUGINSPATH', path)
            finally:
                self.settings.Close()
            return
        except:
            log.exception('setting.setString')

        _MsgItems = [
            self.s2f("Python"),
            self.s2f(""),
            self.s2f("Error setting python path"),
            self.s2f(""),
            self.s2f("\x01"),
            self.s2f("&Ok"),
        ]
        MsgItems = ffi.new("wchar_t *[]", _MsgItems)
        self.info.Message(
            self.UUID2GUID(self.PluginInfo.pyguid),
            self.UUID2GUID(self.PluginInfo.guid),
            ffic.FMSG_WARNING|ffic.FMSG_LEFTALIGN,  # Flags
            self.s2f("Contents"),                   # HelpTopic
            MsgItems,                               # Items
            len(MsgItems),                          # ItemsNumber
            1                                       # ButtonsNumber
        )
        return None
