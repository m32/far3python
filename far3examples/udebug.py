import logging
import uuid

from far3.far3cffi import ffi, ffic
from far3.plugin import PluginBase
from far3 import fardialogbuilder as dlgb
import debugpy


log = logging.getLogger(__name__)


class Config:
    configured = False
    logto = 'w:/temp'
    host = '127.0.0.1'
    port = 5678

class Plugin(PluginBase):
    class PluginInfo:
        name = 'udebug'
        flags = ffic.PF_NONE
        title = "Python debugpy"
        author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
        description = title
        pyguid = uuid.UUID('{308868BA-5773-4C89-8142-DF877868E06A}')
        guid = uuid.UUID('{A01E7520-F997-46BD-AB47-4F0AD76436FB}')
        version = (1, 0, 0, 0, ffic.VS_SPECIAL)

        openFrom = ["PLUGINSMENU", "COMMANDLINE", "EDITOR", "VIEWER"]

    def debug(self):
        if not Config.configured:
            Config.configured = True
            log.debug('debug.1')
            try:
                debugpy.log_to(Config.logto)
            except:
                log.exception('debug')
            debugpy.configure(python=r'W:\binw\Python-3.9.13.amd64\python.exe', subProcess=False)
            log.debug('debug.2')
            # in vs code debuger select attach, port = 5678
            # commands in shell:
            #   py:debug
            # elsewhere in python code:
            #   import debugpy
            #   debugpy.breakpoint()
            log.debug('debug.3')
            info = debugpy.listen((Config.host, Config.port))
        else:
            info = None
        log.debug('debug.4 {}'.format(info))
        debugpy.wait_for_client()
        log.debug('debug.5')
        #debugpy.breakpoint()
        log.debug('debug.6')

    def breakpoint(self):
        debugpy.breakpoint()

    @staticmethod
    def HandleCommandLine(line):
        return line in ('debug', 'breakpoint')

    def CommandLine(self, line):
        try:
            getattr(self, line)()
        except:
            log.exception('debugpy.CommandLine')

    def OpenW(self, info):
        @ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)

        b = dlgb.DialogBuilder(
            self,
            DialogProc,
            "Python debugpy",
            "helptopic",
            0,
            dlgb.VSizer(
                dlgb.HSizer(dlgb.TEXT("Log path:"), dlgb.Spacer(), dlgb.EDIT("logpath", 60, 120)),
                dlgb.HSizer(dlgb.TEXT("Host:"), dlgb.Spacer(), dlgb.EDIT("host", 32, 32)),
                dlgb.HSizer(dlgb.TEXT("Port:"), dlgb.Spacer(), dlgb.EDIT("port", 5, 5)),
                dlgb.HSizer(
                    dlgb.BUTTON('ok', "Ok", True, flags=ffic.DIF_CENTERGROUP),
                    dlgb.BUTTON('cancel', "Cancel", flags=ffic.DIF_CENTERGROUP),
                ),
            ),
        )
        dlg = b.build(
            self.UUID2GUID(self.PluginInfo.pyguid),
            self.UUID2GUID(self.PluginInfo.guid),
            -1,
            -1
        )

        dlg.SetText(dlg.ID_logpath, Config.logto)
        dlg.SetText(dlg.ID_host, Config.host)
        dlg.SetText(dlg.ID_port, str(Config.port))

        rc = self.info.DialogRun(dlg.hDlg)
        
        log.debug('result: rc={}'.format(rc))
        if rc != -1:
            logto = dlg.GetText(dlg.ID_logpath)
            host = dlg.GetText(dlg.ID_host)
            port = dlg.GetText(dlg.ID_port)
            log.debug('result: host={}, port={} logto={}'.format(host, port, logto))
        self.info.DialogFree(dlg.hDlg)
