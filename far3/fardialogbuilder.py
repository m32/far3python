#!/usr/bin/env vpython3
import logging
from far3.far3cffi import ffi, ffic
from far3 import fardialogsizer as sizer
from far3.fardialog import Dialog


log = logging.getLogger(__name__)


def dialogitem(Type=0, X1=0, Y1=0, X2=0, Y2=0, Param=None, History=None, Mask=None, Flags=0, Data=None, MaxLength=0, UserData=None, Reserved=None):
    Param = Param or {'Selected':0}
    History = History or ffi.NULL
    Mask = Mask or ffi.NULL
    Data = Data or ffi.NULL
    UserData = UserData or 0
    Reserved = Reserved or (0, 0)
    di = [
        Type, X1, Y1, X2, Y2, Param, History, Mask, Flags, Data, MaxLength, UserData, Reserved
    ]
    return di

class Element(sizer.Window):
    no = 0
    varname = None
    def __init__(self, varname=None):
        Element.no += 1
        self.varname = varname
        self.no = Element.no

    def makeID(self, dlg):
        if self.varname is not None:
            setattr(dlg, "ID_"+self.varname, self.no)

    def makeItem(self, dlg):
        return None


class Spacer(Element):
    def __init__(self, width=1, height=1):
        super().__init__()
        # non countable ID
        Element.no -= 1
        self.width = width
        self.height = height

    def get_best_size(self):
        return (self.width, self.height)


class TEXT(Element):
    dit = "DI_TEXT"

    def __init__(self, text):
        super().__init__()
        self.text = text

    def get_best_size(self):
        return (len(self.text), 1)

    def makeItem(self, dlg):
        w, h = self.get_best_size()
        item = dialogitem(
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w + 1,
            self.pos[1] + h - 1,
            Data = dlg.s2f(self.text)
        )
        dlg.dialogItems.append(item)
        return item


class EDIT(Element):
    dit = "DI_EDIT"

    def __init__(self, varname, width, maxlength=None):
        super().__init__(varname)
        self.width = width
        self.height = 1
        self.maxlength = maxlength or 0
        self.mask = None

    def get_best_size(self):
        return (self.width + 2, self.height)

    def makeItem(self, dlg):
        w, h = self.get_best_size()

        param = {'Selected':0}
        mask = None
        flags = 0
        if self.mask is not None:
            mask = dlg.s2f(self.mask)
            flags = ffic.DIF_MASKEDIT

        item = dialogitem(
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + self.width,
            self.pos[1] + h - 1,
            Param = param,
            Mask = mask,
            Flags = flags,
            MaxLength = self.maxlength,
        )
        dlg.dialogItems.append(item)
        return item


class PASSWORD(EDIT):
    dit = "DI_PSWEDIT"


class MASKED(EDIT):
    dit = "DI_FIXEDIT"

    def __init__(self, varname, mask):
        super().__init__(varname, len(mask), maxlength=len(mask))
        self.mask = mask


class MEMOEDIT(EDIT):
    #dit = "DI_MEMOEDIT"

    def __init__(self, varname, width, height, maxlength=None):
        super().__init__(varname, width, maxlength)
        self.height = height


class BUTTON(Element):
    dit = "DI_BUTTON"

    def __init__(self, varname, text, flags=0):
        super().__init__(varname)
        self.text = text
        self.flags = flags

    def get_best_size(self):
        # [ text ]
        return (2 + len(self.text) + 2, 1)

    def makeItem(self, dlg):
        w, h = self.get_best_size()
        item = dialogitem(
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w,
            self.pos[1] + h - 1,
            Flags = self.flags,
            Data = dlg.s2f(self.text),
        )
        dlg.dialogItems.append(item)
        return item


class CHECKBOX(Element):
    dit = "DI_CHECKBOX"

    def __init__(self, varname, text, checked=False):
        super().__init__(varname)
        self.text = text
        self.checked = checked

    def get_best_size(self):
        return (4 + len(self.text), 1)

    def makeItem(self, dlg):
        w, h = self.get_best_size()
        item = dialogitem(
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w,
            self.pos[1] + h - 1,
            Data = dlg.s2f(self.text),
        )
        dlg.dialogItems.append(item)
        return item


class RADIOBUTTON(Element):
    dit = "DI_RADIOBUTTON"

    def __init__(self, varname, text, selected=False, flags=0):
        super().__init__(varname)
        self.text = text
        self.selected = selected
        self.flags = flags

    def get_best_size(self):
        return (4 + len(self.text), 1)

    def makeItem(self, dlg):
        w, h = self.get_best_size()
        item = dialogitem(
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w,
            self.pos[1] + h - 1,
            Flags = self.flags,
            Data = dlg.s2f(self.text),
        )
        dlg.dialogItems.append(item)
        return item


class COMBOBOX(Element):
    dit = "DI_COMBOBOX"

    def __init__(self, varname, selected, *items):
        super().__init__(varname)
        self.selected = selected
        self.items = items
        self.maxlen = 1+max([len(s) for s in self.items])
        self.flist = None
        self.fitems = None
        self.s2f = None

    def get_best_size(self):
        return (self.maxlen, 1)

    def makeItem(self, dlg):
        w, h = self.get_best_size()

        s2f = []
        fitems = ffi.new("struct FarListItem []", len(self.items))
        for i in range(len(self.items)):
            fitems[i].Flags = ffic.LIF_SELECTED if i == self.selected else 0
            s = dlg.s2f(self.items[i])
            s2f.append(s)
            fitems[i].Text = s

        flist = ffi.new("struct FarList *")
        flist.ItemsNumber = len(self.items)
        flist.Items = fitems

        self.flist = flist
        self.fitems = fitems
        self.s2f = s2f

        param = {'ListItems':flist}
        item = dialogitem(
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w - 1,
            self.pos[1] + h - 1,
            Param = param,
        )
        dlg.dialogItems.append(item)
        return item


class LISTBOX(Element):
    dit = "DI_LISTBOX"

    def __init__(self, varname, selected, *items):
        super().__init__(varname)
        self.selected = selected
        self.items = items
        self.maxlen = 4+max([len(s) for s in self.items])
        self.flist = None
        self.fitems = None
        self.s2f = None

    def get_best_size(self):
        return (self.maxlen, len(self.items))

    def makeItem(self, dlg):
        w, h = self.get_best_size()

        s2f = []
        fitems = ffi.new("struct FarListItem []", len(self.items))
        for i in range(len(self.items)):
            fitems[i].Flags = ffic.LIF_SELECTED if i == self.selected else 0
            s = dlg.s2f(self.items[i])
            s2f.append(s)
            fitems[i].Text = s

        flist = ffi.new("struct FarList *")
        flist.ItemsNumber = len(self.items)
        flist.Items = fitems

        self.flist = flist
        self.fitems = fitems
        self.s2f = s2f

        param = {'ListItems':flist}
        item = dialogitem(
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w - 1,
            self.pos[1] + h - 1,
            Param = param,
            Flags = ffic.DIF_LISTNOBOX,
        )
        dlg.dialogItems.append(item)
        return item


class USERCONTROL(Element):
    dit = "DI_USERCONTROL"

    def __init__(self, varname, width, height):
        super().__init__(varname)
        self.width
        self.height

    def get_best_size(self):
        return (self.width, self.height)

    def makeItem(self, dlg):
        w, h = self.get_best_size()
        item = dialogitem(
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w,
            self.pos[1] + h - 1,
        )
        dlg.dialogItems.append(item)
        return item


class HLine(Element):
    dit = "DI_TEXT"

    def get_best_size(self):
        return (1, 1)

    def makeItem(self, dlg):
        item = dialogitem(
            getattr(ffic, self.dit),
            0,
            self.pos[1],
            0,
            self.pos[1],
            0,
            Flags = ffic.DIF_SEPARATOR,
        )
        dlg.dialogItems.append(item)
        return item


class HSizer(sizer.HSizer):
    def __init__(self, *controls, border=(0, 0, 0, 0), center=False):
        super().__init__()
        self.controls = controls
        self.center = center
        for control in controls:
            self.add(control, border)

    def makeID(self, dlg):
        for control in self.controls:
            control.makeID(dlg)

    def makeItem(self, dlg):
        for control in self.controls:
            item = control.makeItem(dlg)
            if item is not None and (item[8]&ffic.DIF_CENTERGROUP) != 0:
                item[1] = 0
                item[3] = 0


class VSizer(sizer.VSizer):
    def __init__(self, *controls, border=(0, 0, 0, 0)):
        super().__init__()
        self.controls = controls
        for control in controls:
            self.add(control, border)

    def makeID(self, dlg):
        for control in self.controls:
            control.makeID(dlg)

    def makeItem(self, dlg):
        for control in self.controls:
            control.makeItem(dlg)


class DialogBuilder(sizer.HSizer):
    def __init__(self, plugin, dialogProc, title, helptopic, flags, contents, border=(1, 1, 1, 1)):
        super().__init__(border)
        self.plugin = plugin
        self.dialogProc = dialogProc
        self.title = title
        self.helptopic = helptopic
        self.flags = flags
        self.contents = contents
        self.add(contents, border)

    def build(self, pyguid, guid, x, y):
        # for building dlg.ID_<varname>
        Element.no = 0

        dlg = Dialog(self.plugin)

        w, h = self.get_best_size()
        w = max(w + 1, len(self.title) + 4)

        dlg.width = w
        dlg.height = h

        self.contents.makeID(dlg)
        self.size(3, 1, w, h)

        item = dialogitem(
            ffic.DI_DOUBLEBOX,
            3,
            1,
            w,
            h,
            Data = dlg.s2f(self.title),
        )
        dlg.dialogItems.append(item)
        self.contents.makeItem(dlg)

        dlg.fdi = ffi.new("struct FarDialogItem []", dlg.dialogItems)
        dlg.hDlg = dlg.info.DialogInit(
            pyguid, guid,
            x,
            y,
            w + 4,
            h + 2,
            dlg.s2f(self.helptopic),
            dlg.fdi,
            len(dlg.fdi),
            0,
            0,
            self.dialogProc,
            ffi.NULL
        )
        return dlg
