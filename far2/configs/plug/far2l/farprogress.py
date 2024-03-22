import threading
import logging
from datetime import datetime

from far2lc import CheckForEscape
from far2l.fardialogbuilder import (
    Spacer,
    TEXT,
    EDIT,
    PASSWORD,
    MASKED,
    MEMOEDIT,
    BUTTON,
    CHECKBOX,
    RADIOBUTTON,
    COMBOBOX,
    LISTBOX,
    USERCONTROL,
    HLine,
    HSizer,
    VSizer,
    DialogBuilder,
)

log = logging.getLogger(__name__)

class ProgressState:
    def __init__(self, tproc, tsize, csize):
        if tproc:
            self.lock = threading.Lock()
            self.started = threading.Condition()
            self.started.acquire()

        # file info
        self.fname = ""
        self.foffset = 0
        self.fsize = 0
        self.fprog = 0
        # total size
        self.toffset = 0
        self.tsize = tsize
        self.tprog = 0
        # total count
        self.coffset = 0
        self.csize = csize
        self.cprog = 0
        # file time
        self.fspent = 0
        self.fspentrem = 0
        # total time
        self.tspent = 0
        self.tspentrem = 0
        # speed
        self.speedcurr = 0
        self.speedavg = 0

        self.exc = None
        self.rc = 0

        if tproc:
            tproc.daemon = True
            tproc.start()

    def nextFile(self, fname, fsize):
        self.state.lock.acquire(True)
        self.fname = fname
        self.foffset = 0
        self.fsize = fsize

        self.speedcurr = 0
        self.coffset += 1
        self.tsize += fsize
        self.state.lock.release()

class ProgressDialog:
    def __init__(self, plugin, state):
        self.plugin = plugin
        self.state = state
        self.prevstate = ProgressState(None, 0, 0)

        self.info = plugin.info
        self.ffi = plugin.ffi
        self.ffic = plugin.ffic
        self.hplugin = self.ffi.cast("void *", id(self))

    def s2f(self, s):
        return self.ffi.new("wchar_t []", s)

    def f2s(self, s):
        return self.ffi.string(self.ffi.cast("wchar_t *", s))

    def FormatSize(self, n):
        suffix = ['B', 'KB', 'MB', 'GB', 'TB']
        i = 0
        while n > 999:
            n //= 1024
            i += 1
        return "{} {}".format(n, suffix[i])

    def OnIdle(self, dlg):
        self.state.lock.acquire(False, 1)
        if not self.state.lock.locked():
            return
        try:
            self._OnIdle(dlg)
        except:
            log.exception('progress')
        finally:
            self.state.lock.release()

    def _OnIdle(self, dlg):
        if self.prevstate.fname != self.state.fname:
            self.prevstate.fname = self.state.fname
            dlg.SetText(dlg.fname, self.state.fname[:40])

        fprog = False
        if self.prevstate.foffset != self.state.foffset:
            fprog = True
            self.prevstate.foffset = self.state.foffset
            dlg.SetText(dlg.foffset, self.FormatSize(self.state.foffset))
        if self.prevstate.fsize != self.state.fsize:
            self.prevstate.fsize = self.state.fsize
            dlg.SetText(dlg.fsize, self.FormatSize(self.state.size))
        if fprog:
            n = self.prevstate.foffset * 10 // self.prevstate.fsize
            fprog = (('='*n)+' '*10)[:10]
            dlg.SetText(dlg.fprog, '[{}]'.format(fprog))

        if self.prevstate.toffset != self.state.toffset:
            dlg.SetText(dlg.toffset, self.FormatSize(self.state.toffset))
            n = self.prevstate.toffset * 10 // self.prevstate.tsize
            tprog = (('='*n)+' '*10)[:10]
            dlg.SetText(dlg.tprog, '[{}]'.format(tprog))

        if self.prevstate.coffset != self.state.coffset:
            dlg.SetText(dlg.coffset, self.FormatSize(self.state.coffset))
            n = self.prevstate.coffset * 10 // self.prevstate.csize
            cprog = (('='*n)+' '*10)[:10]
            dlg.SetText(dlg.cprog, '[{}]'.format(cprog))

        dlg.SetText(dlg.fspent, "")
        dlg.SetText(dlg.fspentrem, "")

        dlg.SetText(dlg.tspent, "")
        dlg.SetText(dlg.tspentrem, "")

        dlg.SetText(dlg.speedcurr, "")
        dlg.SetText(dlg.speedavg, "")

    def Run(self):
        @self.ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            if Msg == self.ffic.DN_INITDIALOG:
                log.debug("INITDIALOG")
                try:
                    # file
                    dlg.SetText(dlg.fname, "")
                    dlg.SetText(dlg.foffset, "")
                    dlg.SetText(dlg.fsize, "")
                    dlg.SetText(dlg.fprog, "")
                    # total size
                    dlg.SetText(dlg.toffset, "")
                    dlg.SetText(dlg.tsize, self.FormatSize(self.state.tsize))
                    dlg.SetText(dlg.tprog, "")
                    # total count
                    dlg.SetText(dlg.coffset, "")
                    dlg.SetText(dlg.csize, str(self.state.csize))
                    dlg.SetText(dlg.cprog, "")
                    # file time
                    dlg.SetText(dlg.fspent, "")
                    dlg.SetText(dlg.fspentrem, "")
                    # total time
                    dlg.SetText(dlg.tspent, "")
                    dlg.SetText(dlg.tspentrem, "")
                    # speed
                    dlg.SetText(dlg.speedcurr, "")
                    dlg.SetText(dlg.speedavg, "")
                except:
                    log.exception("bang")
                log.debug("/INITDIALOG")
                self.state.started.release()
            elif Msg == self.ffic.DN_ENTERIDLE:
                self.OnIdle(dlg)
            return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)

        b = DialogBuilder(
            self,
            DialogProc,
            "Progress",
            "progress",
            self.ffic.FDLG_REGULARIDLE,
            VSizer(
                TEXT(None, "Current file:"),
                TEXT("fname", " "*40),
                HLine(),
                HSizer(
                    TEXT(None, "File size:"), TEXT("foffset", "12345"), TEXT(None, "of"), TEXT("fsize", "123456"), TEXT("fprog", "[==========]"),
                ),
                HSizer(
                    TEXT(None, "Total size:"), TEXT("toffset", "12345"), TEXT(None, "of"), TEXT("tsize", "123456"), TEXT("tprog", "[==========]"),
                ),
                HSizer(
                    TEXT(None, "Total count:"), TEXT("coffset", "12345"), TEXT(None, "of"), TEXT("csize", "123456"), TEXT("cprog", "[==========]"),
                ),
                HSizer(
                    TEXT(None, "File time  SPENT:"), TEXT("fspent", "###:##.##"), TEXT(None, "REMAIN"), TEXT("fspentrem", "###:##.##"),
                ),
                HSizer(
                    TEXT(None, "Total time SPENT:"), TEXT("tspent", "###:##.##"), TEXT(None, "REMAIN"), TEXT("tspentrem", "###:##.##"),
                ),
                HSizer(
                    TEXT(None, "Speed CURRENT:"), TEXT("speedcurr", "####"), TEXT(None, "AVERAGE"), TEXT("speedavg", "#######"),
                ),
                HLine(),
                HSizer(
                    BUTTON("BG", "&Background", flags=self.ffic.DIF_CENTERGROUP),
                    BUTTON("PAUSE", "&Pause", default=True, flags=self.ffic.DIF_CENTERGROUP),
                    BUTTON("CANCEL", "&Cancel", flags=self.ffic.DIF_CENTERGROUP),
                ),
            ),
        )
        dlg = b.build(-1, -1)

        res = self.info.DialogRun(dlg.hDlg)
        #res.dlg.BG
        #res.dlg.PAUSE
        #res.dlg.CANCEL
        self.info.DialogFree(dlg.hDlg)

        return res

PROGRESS_WIDTH = 30

class ProgressMessage(object):
    def __init__(self, plugin, title, message, maxvalue):
        super().__init__()
        self.info = plugin.info
        self.ffi = plugin.ffi
        self.ffic = plugin.ffic

        self.visible = False
        self.title = title
        self.message = message
        self.maxvalue = maxvalue
        self.setbar(0)

    def s2f(self, s):
        return self.ffi.new("wchar_t []", s)

    def f2s(self, s):
        return self.ffi.string(self.ffi.cast("wchar_t *", s))

    def adv(self, cmd, par):
        self.info.AdvControl(
            self.info.ModuleNumber,
            cmd,
            self.ffi.cast("void *", par)
        )

    def show(self):
        if not self.visible:
            self.adv(self.ffic.ACTL_SETPROGRESSSTATE, self.ffic.PGS_INDETERMINATE)
            self.visible = True
        msg = [ self.s2f(self.title), self.s2f(self.message), self.s2f(self.bar) ]
        cmsg = self.ffi.new("wchar_t *[]", msg)
        self.info.Message(
            self.info.ModuleNumber,
            0,
            self.ffi.NULL,
            cmsg,
            len(msg),
            0
        )

    def hide(self):
        if not self.visible:
            return
        self.adv(self.ffic.ACTL_PROGRESSNOTIFY, 0)
        self.adv(self.ffic.ACTL_SETPROGRESSSTATE, self.ffic.PGS_NOPROGRESS)
        self.visible = False

        PANEL_ACTIVE    =self.ffi.cast("HANDLE", -1)
        PANEL_PASSIVE   =self.ffi.cast("HANDLE", -2)
        self.info.Control(PANEL_ACTIVE, self.ffic.FCTL_REDRAWPANEL, 0, 0)
        self.info.Control(PANEL_PASSIVE, self.ffic.FCTL_REDRAWPANEL, 0, 0)

    def setbar(self, value):
        assert type(value) == int
        assert value <= self.maxvalue

        percent = value * 100 // self.maxvalue

        pv = self.ffi.new('struct PROGRESSVALUE *', (percent, 100))
        self.info.AdvControl(self.info.ModuleNumber, self.ffic.ACTL_SETPROGRESSVALUE, pv)

        nb = int(percent*PROGRESS_WIDTH // 100)
        self.bar =  '\u2588'*nb + '\u2591'*(PROGRESS_WIDTH-nb)

    def update(self, value):
        self.setbar(value)
        self.show()

    def aborted(self):
        return CheckForEscape()

    def close(self):
        self.hide()
