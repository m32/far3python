import logging
import uuid

from far3.far3cffi import ffi, ffic
from far3.plugin import PluginBase


log = logging.getLogger(__name__)


class Plugin(PluginBase):
    class PluginInfo:
        name = 'ucharmap'
        flags = ffic.PF_NONE
        title = "Python Character Map"
        author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
        description = title
        pyguid = uuid.UUID('{308868BA-5773-4C89-8142-DF877868E06A}')
        guid = uuid.UUID('{C0D1792D-9A6A-4535-B178-5077B6CC6CB6}')
        version = (1, 0, 0, 0, ffic.VS_SPECIAL)

        openFrom = ["PLUGINSMENU", "COMMANDLINE", "EDITOR", "VIEWER"]

    def __init__(self, parent, info):
        super().__init__(parent, info)
        self.guid1 = uuid.UUID('{F2F08223-800D-4DA8-B32C-40319D342529}')

    def Rebuild(self, hDlg):
        self.info.SendDlgMessage(hDlg, ffic.DM_ENABLEREDRAW, 0, ffi.NULL)
        prefix = ["", "&"]
        for i in range(len(self.symbols)):
            row = i // self.max_col
            col = i % self.max_col
            p = prefix[row == self.cur_row and col == self.cur_col]
            offset = self.first_text_item+row*self.max_col+col
            ch = self.s2f(p+self.symbols[i])
            self.info.SendDlgMessage(hDlg, ffic.DM_SETTEXTPTR, offset, ffi.cast("void *", ch))
        self.info.SendDlgMessage(hDlg, ffic.DM_ENABLEREDRAW, 1, ffi.NULL)

    def OpenW(self, info):
        try:
            return self.xOpenW(info)
        except:
            log.exception('ucharmap')

    def xOpenW(self, info):
        if 0:
            import debugpy
            debugpy.breakpoint()
        symbols = []
        for i in range(256):
            symbols.append(chr(i))
        symbols.extend([
            "Ђ", "Ѓ", "‚", "ѓ", "„", "…", "†", "‡", "€", "‰", "Љ", "‹", "Њ", "Ќ", "Ћ", "Џ", "ђ", "‘", "’", "“", "”", "•", "–", "—", "", "™", "љ", "›", "њ", "ќ", "ћ", "џ",
            " ", "Ў", "ў", "Ј", "¤", "Ґ", "¦", "§", "Ё", "©", "Є", "«", "¬", "­", "®", "Ї", "°", "±", "І", "і", "ґ", "µ", "¶", "·", "ё", "№", "є", "»", "ј", "Ѕ", "ѕ", "ї",
            "А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я",
            "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я",
            "░", "▒", "▓", "│", "┤", "╡", "╢", "╖", "╕", "╣", "║", "╗", "╝", "╜", "╛", "┐", "└", "┴", "┬", "├", "─", "┼", "╞", "╟", "╚", "╔", "╩", "╦", "╠", "═", "╬", "╧",
            "╨", "╤", "╥", "╙", "╘", "╒", "╓", "╫", "╪", "┘", "┌", "█", "▄", "▌", "▐", "▀", "∙", "√", "■", "⌠", "≈", "≤", "≥", "⌡", "²", "÷", "ą", "ć", "ę", "ł", "ń", "ó",
            "ś", "ż", "ź", "Ą", "Ć", "Ę", "Ł", "Ń", "Ó", "Ś", "Ż", "Ź", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
        ])
        Items = [
            (ffic.DI_DOUBLEBOX,   3,  1, 38, 18, {'Selected':0}, ffi.NULL, ffi.NULL, 0, self.s2f("Character Map"), 0, 0, (0, 0)),
            (ffic.DI_BUTTON,      0, 17,  0, 18, {'Selected':0}, ffi.NULL, ffi.NULL, ffic.DIF_CENTERGROUP|ffic.DIF_DEFAULTBUTTON, self.s2f("OK"), 0, 0, (0, 0)),
            (ffic.DI_BUTTON,      0, 17,  0, 18, {'Selected':0}, ffi.NULL, ffi.NULL, ffic.DIF_CENTERGROUP, self.s2f("Cancel"), 0, 0, (0, 0)),
            (ffic.DI_USERCONTROL, 3,  2, 38, 16, {'Selected':0}, ffi.NULL, ffi.NULL, ffic.DIF_FOCUS, ffi.NULL, 0, 0, (0, 0)),
        ]
        self.cur_row = 0
        self.cur_col = 0
        self.max_col = 32
        self.max_row = len(symbols) // self.max_col
        self.first_text_item = len(Items)
        self.symbols = symbols
        self.text = None

        for i in range(len(symbols)):
            row = i // self.max_col
            col = i % self.max_col
            Items.append((
                ffic.DI_TEXT,
                5+col, self.first_text_item-2+row, 5+col, self.first_text_item-2+row,
                {'Selected':0},
                ffi.NULL, ffi.NULL, 0, ffi.NULL,
                0, 0, (0, 0),
            ))

        @ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            if Msg == ffic.DN_INITDIALOG:
                self.Rebuild(hDlg)
                return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)
            elif Msg == ffic.DN_BTNCLICK:
                return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)
            elif Msg == ffic.DN_CONTROLINPUT:
                rec = ffi.cast('INPUT_RECORD *', Param2)
                et = rec.EventType
                if et == ffic.KEY_EVENT:
                    ev = rec.Event.KeyEvent
                    if not ev.bKeyDown or Param1 != self.first_text_item-1:
                        return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)
                    vk = ev.wVirtualKeyCode
                    log.debug('kkey DialogProc({}, {}, {})'.format(Param1, vk, Param1 == self.first_text_item-1))
                    if vk == ffic.VK_LEFT:
                        self.cur_col -= 1
                    elif vk == ffic.VK_UP:
                        self.cur_row -= 1
                    elif vk == ffic.VK_RIGHT:
                        self.cur_col += 1
                    elif vk == ffic.VK_DOWN:
                        self.cur_row += 1
                    elif vk == ffic.VK_RETURN:
                        return 0
                    elif vk == ffic.VK_ESCAPE:
                        return 0
                    else:
                        return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)
                    if self.cur_col == self.max_col:
                        self.cur_col = 0
                    elif self.cur_col == -1:
                        self.cur_col = self.max_col - 1
                    if self.cur_row == self.max_row:
                        self.cur_row = 0
                    elif self.cur_row == -1:
                        self.cur_row = self.max_row - 1
                    self.Rebuild(hDlg)
                    return 1
                elif et == ffic.MOUSE_EVENT:
                    ev = rec.Event.MouseEvent
                    ch = Param1 - self.first_text_item
                    log.debug('mou DialogProc({}, {}, {})'.format(Param1, ch, Param1, self.first_text_item))
                    if ch >= 0:
                        focus = self.info.SendDlgMessage(hDlg, ffic.DM_GETFOCUS, 0, ffi.NULL)
                        if focus != self.first_text_item-1:
                            self.info.SendDlgMessage(hDlg, ffic.DM_SETFOCUS, self.first_text_item-1, ffi.NULL)
                        self.cur_row = ch // self.max_col
                        self.cur_col = ch % self.max_col
                        self.cur_col = min(max(0, self.cur_col), self.max_col-1)
                        self.cur_row = min(max(0, self.cur_row), self.max_row-1)
                        self.Rebuild(hDlg)
                    return 1
                return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)
            #else:
            #    log.debug('unk DialogProc({0}, {1}, {2}, {3})'.format(hDlg, Msg, Param1, Param2))
            return self.info.DefDlgProc(hDlg, Msg, Param1, Param2)

        fdi = ffi.new("struct FarDialogItem []", Items)
        hDlg = self.info.DialogInit(
            self.UUID2GUID(self.PluginInfo.pyguid),
            self.UUID2GUID(self.guid1),
            -1, -1, 42, 20,
            self.s2f("Character Map"),
            fdi, len(fdi),
            0, 0,
            DialogProc,
            ffi.NULL
        )
        res = self.info.DialogRun(hDlg)
        log.debug('result={} text={}'.format(res, self.text))
        if res == 1 and self.text:
            offset = self.cur_row*self.max_col+self.cur_col
            try:
                text = self.symbols[offset]
                log.debug('offset:{} row:{} col:{}, ch:{}'.format(offset, self.cur_row, self.cur_col, text))
                self.info.FSF.CopyToClipboard(ffic.FCT_STREAM, self.s2f(text))
            except IndexError:
                log.exception('offset:{} row:{} col:{}'.format(offset, self.cur_row, self.cur_col))
        self.info.DialogFree(hDlg)
