#!/usr/bin/env vpython3
import logging
from .far3cffi import ffi, ffic
from .fardialog import Dialog
from . import fardialogsizer as sizer


log = logging.getLogger(__name__)


class Element(sizer.Window):
    varname = None
    def __init__(self,
        varname=None,
        text=ffi.NULL,
        width=None,
        height=1,
        param=None,
        history=ffi.NULL,
        mask=ffi.NULL,
        flags=0,
        maxlength=0,
        userdata=None
    ):
        super().__init__(varname)

        if width is None:
            if text != ffi.NULL:
                width=len(text)
            elif mask != ffi.NULL:
                width=len(mask)
            else:
                width=1
        if param is None:
            param = {'Selected': ffi.cast("intptr_t", 0)}
        if userdata is None:
            userdata = ffi.cast("intptr_t", 0)

        self.text = text
        self.width = width
        self.height = height
        self.history = history
        self.mask = mask
        self.flags = flags
        self.param = param
        self.maxlength = maxlength
        self.userdata = userdata

    def get_best_size(self):
        return (self.width, self.height)

    def makeItem(self, dlg):
        w, h = self.get_best_size()
        text = self.text
        if text != ffi.NULL:
            text = dlg.s2f(text)
        mask = self.mask
        if mask != ffi.NULL:
            mask = dlg.s2f(mask)
        dlg.dialogItems.append((
            getattr(ffic, self.dit),
            ffi.cast("intptr_t", self.pos[0]),
            ffi.cast("intptr_t", self.pos[1]),
            ffi.cast("intptr_t", self.pos[0] + w - 1),
            ffi.cast("intptr_t", self.pos[1] + h - 1),
            self.param,
            self.history,
            mask,
            self.flags,
            text,
            self.maxlength,
            self.userdata
        ))

class TEXT(Element):
    dit = "DI_TEXT"

class EDIT(Element):
    dit = "DI_EDIT"

    def __init__(self, varname, width=None, mask=ffi.NULL, maxlength=None):
        if mask != ffi.NULL:
            flags = ffic.DIF_MASKEDIT
            maxlength = len(mask)
            width = len(mask)
        else:
            param = {'Selected':ffi.cast("intptr_t", 0)}
            flags = 0
            assert width is not None
        super().__init__(varname, width=width, mask=mask, flags=flags, maxlength=maxlength or width)

    def get_best_size(self):
        return (self.width+1, self.height)

class PASSWORD(EDIT):
    dit = "DI_PSWEDIT"


class MASKED(EDIT):
    dit = "DI_FIXEDIT"

    def __init__(self, varname, mask):
        super().__init__(varname, width=len(mask), mask=mask, maxlength=len(mask))


class BUTTON(Element):
    dit = "DI_BUTTON"

    def __init__(self, varname, text, flags):
        super().__init__(varname, text=text, flags=flags)

    def get_best_size(self):
        # [ text ]
        return (2 + len(self.text) + 2, 1)

class CHECKBOX(Element):
    dit = "DI_CHECKBOX"

    def __init__(self, varname, text, checked=0):
        param = {'Selected': checked}
        super().__init__(varname, text=text, param=param)

    def get_best_size(self):
        # [?] text
        return (1 + 1 + 1 + 1 + len(self.text), 1)

class RADIOBUTTON(Element):
    dit = "DI_RADIOBUTTON"

    def __init__(self, varname, text, checked=0):
        param = {'Selected': checked}
        super().__init__(varname, text=text, param=param)

    def get_best_size(self):
        # (?) text
        return (1 + 1 + 1 + 1 + len(self.text), 1)

class COMBOBOX(Element):
    dit = "DI_COMBOBOX"

    def __init__(self, varname, selected, *items):
        super().__init__(varname)
        self.selected = selected
        self.items = items
        self.maxlen = max([len(s) for s in self.items])
        self.flist = None
        self.fitems = None
        self.s2f = None

    def get_best_size(self):
        return (2 + self.maxlen, 1)

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
        dlg.dialogItems.append((
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w - 2,
            self.pos[1] + h - 1,
            0,
            param,
            0,
            0,
            ffi.NULL,
            0,
        ))


class LISTBOX(Element):
    dit = "DI_LISTBOX"

    def __init__(self, varname, selected, *items):
        super().__init__(varname)
        self.selected = selected
        self.items = items
        self.maxlen = max([len(s) for s in self.items])
        self.flist = None
        self.fitems = None
        self.s2f = None

    def get_best_size(self):
        return (4 + self.maxlen, len(self.items))

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
        dlg.dialogItems.append((
            getattr(ffic, self.dit),
            self.pos[0],
            self.pos[1],
            self.pos[0] + w - 1,
            self.pos[1] + h - 1,
            0,
            param,
            ffic.DIF_LISTNOBOX,
            0,
            ffi.NULL,
            0,
        ))


class BOX(Element):
    dit = 'DI_DOUBLEBOX'

class USERCONTROL(Element):
    dit = "DI_USERCONTROL"

    def __init__(self, varname, width, height):
        super().__init__(varname, width=width, height=height)
        self.width
        self.height

    def get_best_size(self):
        return (self.width, self.height)

class HLine(Element):
    dit = "DI_TEXT"

    def __init__(self):
        super().__init__(None, width=1, height=1, flags=ffic.DIF_SEPARATOR)

class HSizer(sizer.HSizer):
    def __init__(self, *controls, border=(0, 0, 1, 0), center=False):
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
            control.makeItem(dlg)


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
    def __init__(self, plugin, dialogProc, title, helptopic, flags, contents, border=(2, 1, 2, 1)):
        super().__init__(border)
        self.plugin = plugin
        self.dialogProc = dialogProc
        self.title = title
        self.helptopic = helptopic
        self.flags = flags
        self.contents = contents
        self.add(contents, border)

    def build(self, x, y):

        dlg = Dialog(self.plugin)

        w, h = self.get_best_size()
        w = max(w + 1, len(self.title) + 2)

        dlg.width = w
        dlg.height = h

        self.contents.makeID(dlg)
        self.size(3, 1, w, h)

        box = BOX(None, self.title, w, h)
        box.pos = (3, 1)
        box.makeItem(dlg)
        self.contents.makeItem(dlg)

        if 1:
            log.debug('{} build'.format('*'*20))
            for elem in dlg.dialogItems:
                xdit, xx, xy, xw, xh, xparam, xhistory, xmask, xflags, xtext, xmaxlength, xuserdata = elem
                log.debug('dit={} pos={} param={} hist={} mask={} flags={} text={} maxlength={} user={}'.format(
                    xdit, (xx, xy, xw, xh), xparam, xhistory, xmask, xflags, xtext, xmaxlength, xuserdata
                ))

        dlg.fdi = ffi.new("struct FarDialogItem []", dlg.dialogItems)
        dlg.hDlg = dlg.Info.DialogInit(
            self.plugin.UUID2GUID(self.plugin.pyguid),
            self.plugin.UUID2GUID(self.plugin.guid),
            ffi.cast("intptr_t", x),
            ffi.cast("intptr_t", y),
            ffi.cast("intptr_t", w + 4),
            ffi.cast("intptr_t", h + 2),
            dlg.s2f(self.helptopic),
            dlg.fdi,
            len(dlg.fdi),
            ffi.cast("intptr_t", 0),
            0,
            self.dialogProc,
            ffi.NULL
        )
        return dlg
