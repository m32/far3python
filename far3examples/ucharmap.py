import logging
import uuid

from far3.far3cffi import ffi, ffic
from far3.plugin import PluginBase, handle_error
from far3.fardialog import Dialog
from far3.fardialogbuilder import (
    TEXT, EDIT, PASSWORD, MASKED,
    #MEMOEDIT,
    BUTTON, CHECKBOX, RADIOBUTTON, COMBOBOX,
    LISTBOX, BOX, USERCONTROL,
    HLine,
    HSizer, VSizer,
    Dialog, DialogBuilder
)


log = logging.getLogger(__name__)


class Plugin(PluginBase):
    name = 'ucharmap'
    flags = ffic.PF_NONE
    title = "Python Character Map"
    author = "Grzegorz Makarewicz <mak@trisoft.com.pl>"
    description = title
    guid = uuid.UUID('{C0D1792D-9A6A-4535-B178-5077B6CC6CB6}')
    version = (1, 0, 0, 0, ffic.VS_SPECIAL)

    openFrom = ["PLUGINSMENU", "COMMANDLINE", "EDITOR", "VIEWER"]

    def OpenW(self, info):
        symbols = []
        for i in range(256):
            symbols.append(chr(i))
        symbols.extend([
            "Ђ", "Ѓ", "‚", "ѓ", "„", "…", "†", "‡", "€", "‰", "Љ", "‹", "Њ", "Ќ", "Ћ", "Џ",
            "ђ", "‘", "’", "“", "”", "•", "–", "—", "", "™", "љ", "›", "њ", "ќ", "ћ", "џ",
            " ", "Ў", "ў", "Ј", "¤", "Ґ", "¦", "§", "Ё", "©", "Є", "«", "¬", "­", "®", "Ї",
            "°", "±", "І", "і", "ґ", "µ", "¶", "·", "ё", "№", "є", "»", "ј", "Ѕ", "ѕ", "ї",
            "А", "Б", "В", "Г", "Д", "Е", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П",
            "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "Ъ", "Ы", "Ь", "Э", "Ю", "Я",
            "а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
            "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я",
            "░", "▒", "▓", "│", "┤", "╡", "╢", "╖", "╕", "╣", "║", "╗", "╝", "╜", "╛", "┐",
            "└", "┴", "┬", "├", "─", "┼", "╞", "╟", "╚", "╔", "╩", "╦", "╠", "═", "╬", "╧",
            "╨", "╤", "╥", "╙", "╘", "╒", "╓", "╫", "╪", "┘", "┌", "█", "▄", "▌", "▐", "▀",
            "∙", "√", "■", "⌠", "≈", "≤", "≥", "⌡", "²", "÷", "ą", "ć", "ę", "ł", "ń", "ó",
            "ś", "ż", "ź", "Ą", "Ć", "Ę", "Ł", "Ń", "Ó", "Ś", "Ż", "Ź", " ", " ", " ", " ",
            " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ",
        ])
        self.cur_row = 2
        self.cur_col = 0
        self.max_col = 32
        self.max_row = len(symbols) // self.max_col
        self.symbols = symbols
        self.first_text_item = None
        dlg = None

        def Rebuild(off, on):
            dlg.SuspendDialog()
            for ((row, col), prefix) in (
                (off, ""),
                (on, "&"),
            ):
                dlgid = getattr(dlg, 'ID_t_{}_{}'.format(row, col))
                ch = prefix+self.symbols[row*self.max_col+col]
                dlg.SetText(dlgid, ch)
            dlg.ResumeDialog()

        def pyDialogProc(hDlg, Msg, Param1, Param2):
            if Msg == ffic.DN_INITDIALOG:
                Rebuild((self.cur_row, self.cur_col), (self.cur_row, self.cur_col))
                return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)
            elif Msg == ffic.DN_BTNCLICK:
                return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)
            elif Msg == ffic.DN_CONTROLINPUT:
                focus = dlg.GetFocus()
                if focus != dlg.ID_cmap:
                    return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)
                rec = ffi.cast('INPUT_RECORD *', Param2)
                et = rec.EventType
                prev_row = self.cur_row
                prev_col = self.cur_col
                if et == ffic.KEY_EVENT:
                    ev = rec.Event.KeyEvent
                    if not ev.bKeyDown:
                        return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)
                    vk = ev.wVirtualKeyCode
                    if vk == ffic.VK_LEFT:
                        self.cur_col -= 1
                    elif vk == ffic.VK_UP:
                        self.cur_row -= 1
                    elif vk == ffic.VK_RIGHT:
                        self.cur_col += 1
                    elif vk == ffic.VK_DOWN:
                        self.cur_row += 1
                    #elif vk == ffic.VK_RETURN:
                    #    return 0
                    #elif vk == ffic.VK_ESCAPE:
                    #    return 0
                    else:
                        return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)
                    if self.cur_col == self.max_col:
                        self.cur_col = 0
                    elif self.cur_col == -1:
                        self.cur_col = self.max_col - 1
                    if self.cur_row == self.max_row:
                        self.cur_row = 0
                    elif self.cur_row == -1:
                        self.cur_row = self.max_row - 1
                    Rebuild((prev_row, prev_col), (self.cur_row, self.cur_col))
                    return 1
                elif et == ffic.MOUSE_EVENT:
                    ev = rec.Event.MouseEvent
                    ch = Param1 - self.first_text_item - 1
                    if ch >= 0:
                        self.cur_row = ch // self.max_col
                        self.cur_col = ch % self.max_col
                        self.cur_col = min(max(0, self.cur_col), self.max_col-1)
                        self.cur_row = min(max(0, self.cur_row), self.max_row-1)
                        Rebuild((prev_row, prev_col), (self.cur_row, self.cur_col))
                        return 1
                    return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)
                return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)
            #else:
            #    log.debug('unk DialogProc({0}, {1}, {2}, {3})'.format(hDlg, Msg, Param1, Param2))
            return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)

        @ffi.callback("FARWINDOWPROC")
        def DialogProc(hDlg, Msg, Param1, Param2):
            try:
                return pyDialogProc(hDlg, Msg, Param1, Param2)
            except:
                log.exception('dialog proc')
            return self.Info.DefDlgProc(hDlg, Msg, Param1, Param2)

        class MyDialog(Dialog):
            def Ready(this, builder):
                for i in range(len(symbols)):
                    row = i // self.max_col
                    col = i % self.max_col
                    if self.first_text_item is None:
                        self.first_text_item = this.elementid
                    itm = TEXT('t_{}_{}'.format(row, col), symbols[i], width=1)
                    itm.pos = (5+col, 2+row)
                    itm.makeID(this)
                    itm.makeItem(this)

        dlg = MyDialog(self)
        b = DialogBuilder(
            dlg,
            DialogProc,
            "Character Map",
            "helptopic",
            0,
            VSizer(
                USERCONTROL("cmap", self.max_col+1, self.max_row+1, flags=ffic.DIF_FOCUS),
                HLine(),
                HSizer(
                    BUTTON('vok', "OK", flags=ffic.DIF_DEFAULTBUTTON|ffic.DIF_CENTERGROUP),
                    BUTTON('vcancel', "Cancel", flags=ffic.DIF_CENTERGROUP),
                ),
            )
        )
        b.build(-1, -1)
        res = dlg.Run()
        dlg.close()

        log.debug('result={} ok={}'.format(res, res == dlg.ID_vok))
        if res == dlg.ID_vok:
            offset = self.cur_row*self.max_col+self.cur_col
            try:
                text = self.symbols[offset]
                #log.debug('offset:{} row:{} col:{}, ch:{}'.format(offset, self.cur_row, self.cur_col, text))
                self.Info.FSF.CopyToClipboard(ffic.FCT_STREAM, self.s2f(text))
            except:
                log.exception('offset:{} row:{} col:{}'.format(offset, self.cur_row, self.cur_col))
