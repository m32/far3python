import logging
import uuid

from far3.far3cffi import ffi, ffic
from far3.plugin import PluginBase
from far3.far3dialog import Dialog
from far3 import fardialogbuilder as dlgb


log = logging.getLogger(__name__)


import debugpy
import shlex
import optparse
from far3packages import googletranslate

log = logging.getLogger(__name__)

class OptionParser(optparse.OptionParser):
    def error(self, msg):
        log.error('utranslate: {}'.format(msg))
        raise ValueError('bad option')

class Plugin(PluginBase):
    openFrom = ["PLUGINSMENU", "COMMANDLINE", "EDITOR", "VIEWER"]
    name = 'utranslate'
    flags = ffic.PF_NONE
    title = "Python Translate"
    author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
    description = title
    guid = uuid.UUID('{A01E7520-F997-46BD-AB47-4F0AD76436FB}')
    guid1 = uuid.UUID('{F0432EB3-A7A7-4FAA-A1B0-046EDF328A03}')

    def __init__(self, info):
        super().__init__(info)

    def CommandLine(self, line):
        cmd = line.split(' ', 1)
        if cmd[0] == 'utranslate':
            if len(cmd) > 1 and cmd[1] == 'debug':
                debugpy.breakpoint()
            return self.Dialog()
        if len(cmd) == 1:
            return
        line = cmd[1]
        cmd = cmd[0]
        if cmd == 'spell':
            args = shlex.split(line)
            parser = OptionParser()
            parser.add_option('--lang', action="store", dest="lang", default='en')
            parser.add_option('--text', action="store", dest="text", default='en')
            try:
                opts, args = parser.parse_args(args)
            except ValueError:
                return
            log.debug('spell: opts={} args={}'.format(opts, args))
            try:
                t = googletranslate.get_translate(opts.text, opts.lang, opts.lang)
            except:
                log.exception('spell')
                return
            log.debug('spell result: {}'.format(t))
            s = t['revise']
        elif cmd == 'translate':
            args = shlex.split(line)
            parser = optparse.OptionParser()
            parser.add_option('--from', action="store", dest="lfrom", default='en')
            parser.add_option('--to', action="store", dest="lto", default='en')
            parser.add_option('--text', action="store", dest="text", default='')
            try:
                opts, args = parser.parse_args(args)
            except ValueError:
                return
            log.debug('translate: opts={} args={}'.format(opts, args))
            try:
                t = googletranslate.get_translate(opts.text, opts.lfrom, opts.lto)
            except:
                log.exception('translate')
                return
            log.debug('translate result: {}'.format(t))
            s = t['result'][0]
        else:
            log.error('bad command:{} line={}'.format(cmd, line))
            return
        self.info.FSF.CopyToClipboard(ffic.FCT_STREAM, self.s2f(s))

    def Dialog(self):
        @ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            if Msg == ffic.DN_INITDIALOG:
                try:
                    data = self.s2f('0'*120)
                    nb = self.info.FSF.PasteFromClipboard(ffic.FCT_STREAM, data, 120)
                    s = self.f2s(data)
                except:
                    log.exception('DN_INITDIALOG.1')
                    s = "And do beautiful things"
                try:
                    dlg.SetText(dlg.ID_text, s)
                    dlg.SetCheck(dlg.ID_spell, 1)
                    dlg.SetText(dlg.ID_from, "en")
                    dlg.SetText(dlg.ID_to, "pl")
                    dlg.SetFocus(dlg.ID_text)
                except:
                    log.exception('DN_INITDIALOG.2')
            elif Msg == ffic.DN_BTNCLICK:
                if dlg.ID_perform == Param1:
                    text = dlg.GetText(dlg.ID_text)
                    spell = dlg.GetCheck(dlg.ID_spell)
                    translate = dlg.GetCheck(dlg.ID_translate)
                    lfrom = dlg.GetText(dlg.ID_from)
                    lto = dlg.GetText(dlg.ID_to)
                    log.debug('DN_BTNCLICK(spell={}, translate={} nfrom={} nto={} text={})'.format(spell, translate, lfrom, lto, text))
                    try:
                        if spell:
                            t = googletranslate.get_translate(text, lfrom, lfrom)
                            s = t['revise']
                            if s is None:
                                s = t['result'][0]
                        else:
                            t = googletranslate.get_translate(text, lfrom, lto)
                            s = t['result'][0]
                        log.debug('translate result: {} full={}'.format(s, t))
                        self.info.FSF.CopyToClipboard(ffic.FCT_STREAM, self.s2f(s))
                    except:
                        log.exception('DN_INITDIALOG.3')
                        s = 'connection error'
                    dlg.SetText(dlg.ID_result, s)
            return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)

        dlg = Dialog(self)
        b = dlgb.DialogBuilder(
            dlg,
            DialogProc,
            "Python utranslate",
            "helptopic",
            0,
            dlgb.VSizer(
                dlgb.HSizer(
                    dlgb.TEXT("Text:"),
                    dlgb.EDIT("text", 60, 120)
                ),
                dlgb.HSizer(
                    dlgb.TEXT("Operation:"),
                    dlgb.RADIOBUTTON('spell', "Spell", True, flags=ffic.DIF_GROUP),
                    dlgb.Spacer(),
                    dlgb.RADIOBUTTON('translate', "Translate"),
                ),
                dlgb.HSizer(
                    dlgb.TEXT("From:"),
                    dlgb.EDIT("from", 4, 4)
                ),
                dlgb.HSizer(
                    dlgb.TEXT("To:"),
                    dlgb.EDIT("to", 4, 4)
                ),
                dlgb.HLine(),
                dlgb.HSizer(
                    dlgb.TEXT("Result:"),
                    dlgb.EDIT("result", 60, 120)
                ),
                dlgb.HLine(),
                dlgb.HSizer(
                    dlgb.BUTTON('perform', "Perform", flags=ffic.DIF_CENTERGROUP|ffic.DIF_DEFAULTBUTTON|ffic.DIF_BTNNOCLOSE),
                    dlgb.BUTTON('close', "Close", flags=ffic.DIF_CENTERGROUP),
                ),
            ),
        )
        b.build(
            -1,
            -1
        )

        self.info.DialogRun(dlg.hDlg)
        dlg.close()

    def OpenW(self, info):
        self.Message(
            "Python Translate/Spellcheck",
            "utranslate",
            "From shell:",
            "  py:translate --from=en --to=pl --text='And do beautiful things'",
            "  py:spell --lang=en --text='And do beautifull things'",
            "  py:utrnaslate",
            "",
            "Result is in clipboard :)",
        )
        return None
