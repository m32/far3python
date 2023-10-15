from .far3cffi import ffi, ffic

class Dialog:
    def __init__(self, plugin):
        self.plugin = plugin
        self.Info = plugin.Info
        self.s2f = plugin.s2f
        self.f2s = plugin.f2s

        self.width = 0
        self.height = 0
        self.dialogItems = []
        self.fdi = None
        self.hDlg = None
        # for building dlg.ID_<varname>
        self.elementid = 0

    def close(self):
        self.Info.DialogFree(self.hDlg)
        self.Info = None
        self.s2f = None
        self.f2s = None
        self.fdi = None
        self.hDlg = None
        self.plugin = None

    def Ready(self, builder):
        pass

    def Run(self):
        return self.Info.DialogRun(self.hDlg)

    def SuspendDialog(self):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_ENABLEREDRAW, 0, ffi.NULL)

    def ResumeDialog(self):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_ENABLEREDRAW, 1, ffi.NULL)

    def RedrawDialog(self):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_REDRAW, 0, ffi.NULL)

    def GetDlgData(self):
        return self.Info.SendDlgMessage(self.hDlg, ffic.DM_GETDLGDATA, 0, ffi.NULL)

    def SetDlgData(self, Data):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_SETDLGDATA, 0, Data)

    def GetDlgItemData(self, ID):
        return self.Info.SendDlgMessage(self.hDlg, ffic.DM_GETITEMDATA, 0, ffi.NULL)

    def SetDlgItemData(self, ID, Data):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_SETITEMDATA, 0, Data)

    def GetFocus(self):
        return self.Info.SendDlgMessage(self.hDlg, ffic.DM_GETFOCUS, 0, ffi.NULL)

    def SetFocus(self, ID):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_SETFOCUS, ID, ffi.NULL)

    def Enable(self, ID):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_ENABLE, ID, ffi.cast('void *', 1))

    def Disable(self, ID):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_ENABLE, ID, ffi.NULL)

    def IsEnable(self, ID):
        return self.Info.SendDlgMessage(self.hDlg, ffic.DM_ENABLE, ID, ffi.cast('void *', -1))

    def GetText(self, ID):
        sptr = self.Info.SendDlgMessage(self.hDlg, ffic.DM_GETCONSTTEXTPTR, ID, ffi.NULL)
        return self.f2s(sptr)

    def SetText(self, ID, Str):
        sptr = self.s2f(Str)
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_SETTEXTPTR, ID, sptr)

    def GetCheck(self, ID):
        return self.Info.SendDlgMessage(self.hDlg, ffic.DM_GETCHECK, ID, ffi.NULL)

    def SetCheck(self, ID, State):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_SETCHECK, ID, ffi.cast('void *', State))

    def AddHistory(self, ID, Str):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_ADDHISTORY, ID, Str)

    def AddString(self, ID, Str):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTADDSTR, ID, Str)

    def GetCurPos(self, ID):
        return self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTGETCURPOS, ID, ffi.NULL)

    #def SetCurPos(self, ID, NewPos):
    #    struct FarListPos LPos={NewPos, -1}
    #    self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTSETCURPOS, ID, (LONG_PTR)&LPos)

    def ClearList(self, ID):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTDELETE, ID, ffi.NULL)

    #def DeleteItem(self, ID, Index):
    #    struct FarListDelete FLDItem={Index, 1}
    #    self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTDELETE, ID, (LONG_PTR)&FLDItem)

    def SortUp(self, ID):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTSORT, ID, ffi.NULL)

    def SortDown(self, ID):
        self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTSORT, ID, ffi.cast('void *', 1))

    def GetItemData(self, ID, Index):
        return self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTGETDATA, ID, ffi.cast('void *', Index))

    #def SetItemStrAsData(self, ID, Index, Str):
    #    struct FarListItemData FLID{Index, 0, Str, 0}
    #    self.Info.SendDlgMessage(self.hDlg, ffic.DM_LISTSETDATA, ID, (LONG_PTR)&FLID)
