import sys
import logging
import uuid
from .far3cffi import ffi, ffic


log = logging.getLogger(__name__)


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    log.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


def handle_error(func):
    def __inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            exc_type, exc_value, exc_tb = sys.exc_info()
            handle_exception(exc_type, exc_value, exc_tb)
    return __inner

class PluginBase:
    farguid = uuid.UUID('{00000000-0000-0000-0000-000000000000}')
    pyguid = uuid.UUID("{308868BA-5773-4C89-8142-DF877868E06A}")
    flags = ffic.PF_NONE
    version = (1, 0, 0, 0, ffic.VS_SPECIAL)
    name = ""
    title = ""
    author = ""
    description = ""
    guid = None
    openFrom = []

    Configure = None # override with method when configuration dialog is needed

    def __init__(self, Info):
        assert self.name != ''
        assert self.title != ''
        assert self.author != ''
        assert self.description != ''
        assert isinstance(self.guid, uuid.UUID)
        self.Info = Info
        self.hplugin = ffi.cast("void *", id(self))

    def s2f(self, s):
        return ffi.new("wchar_t []", s)

    def f2s(self, s):
        return ffi.string(ffi.cast("wchar_t *", s))

    def GUID2UUID(self, guid):
        c = 0
        for i in guid.Data4[2:len(guid.Data4)]:
            c = c<<8 | i
        g = uuid.UUID(fields=(guid.Data1, guid.Data2, guid.Data3, guid.Data4[0], guid.Data4[1], c))
        return g

    def UUID2GUID(self, uuid, asPtr=True):
        s = uuid.hex[16:]
        b = []
        for i in range(0, len(s), 2):
            b.append(int(s[i:i+2], 16))
        b = bytes(b)
        g = (
            uuid.fields[0],
            uuid.fields[1],
            uuid.fields[2],
            b,
        )
        if asPtr:
            g = ffi.new("GUID *", g)
        return g

    def Message(self, title, helptopic, *args):
        _MsgItems = [
            self.s2f(title),
            self.s2f(""),
        ]
        _MsgItems.extend([
            self.s2f(s) for s in args
        ])
        _MsgItems.extend([
            self.s2f(""),
            self.s2f("\x01"),
            self.s2f("&Ok"),
        ])
        MsgItems = ffi.new("wchar_t *[]", _MsgItems)
        self.Info.Message(
            self.UUID2GUID(self.pyguid),
            self.UUID2GUID(self.guid),
            ffic.FMSG_WARNING|ffic.FMSG_LEFTALIGN,  # Flags
            self.s2f(helptopic),                   # HelpTopic
            MsgItems,                               # Items
            len(MsgItems),                          # ItemsNumber
            1                                       # ButtonsNumber
        )
        return None

    @staticmethod
    def canHandleCommandLine(line):
        return False

    def CommandLine(self, line):
        pass

    ##################################
    @handle_error
    def AnalyseW(self, Info):
        # HANDLE
        Info = ffi.cast("struct AnalyseInfo *", Info)
        return None
    @handle_error
    def CloseAnalyseW(self, Info):
        Info = ffi.cast("struct CloseAnalyseInfo *", Info)
        pass
    @handle_error
    def ClosePanelW(self, Info):
        Info = ffi.cast("struct ClosePanelInfo *", Info)
        pass
    @handle_error
    def CompareW(self, Info):
        # intptr_t
        Info = ffi.cast("struct CompareInfo *", Info)
        return None
    @handle_error
    def ConfigureW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ConfigureInfo *", Info)
        return None
    @handle_error
    def DeleteFilesW(self, Info):
        # intptr_t
        Info = ffi.cast("struct DeleteFilesInfo *", Info)
        return None
    @handle_error
    def ExitFARW(self, Info):
        Info = ffi.cast("struct ExitInfo *", Info)
        pass
    @handle_error
    def FreeFindDataW(self, Info):
        Info = ffi.cast("struct FreeFindDataInfo *", Info)
        pass
    @handle_error
    def GetFilesW(self, Info):
        # intptr_t
        Info = ffi.cast("struct GetFilesInfo *", Info)
        return None
    @handle_error
    def GetFindDataW(self, Info):
        # intptr_t
        Info = ffi.cast("struct GetFindDataInfo *", Info)
        return None
    @handle_error
    def GetOpenPanelInfoW(self, Info):
        Info = ffi.cast("struct OpenPanelInfo *", Info)
        pass
    @handle_error
    def GetPluginInfoW(self, Info):
        Info = ffi.cast("struct PluginInfo *", Info)
        pass
    @handle_error
    def MakeDirectoryW(self, Info):
        # intptr_t
        Info = ffi.cast("struct MakeDirectoryInfo *", Info)
        return None
    @handle_error
    def OpenW(self, Info):
        # HANDLE
        Info = ffi.cast("struct OpenInfo *", Info)
        return None
    @handle_error
    def ProcessDialogEventW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessDialogEventInfo *", Info)
        return None
    @handle_error
    def ProcessEditorEventW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessEditorEventInfo *", Info)
        return None
    @handle_error
    def ProcessEditorInputW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessEditorInputInfo *", Info)
        return None
    @handle_error
    def ProcessPanelEventW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessPanelEventInfo *", Info)
        return None
    @handle_error
    def ProcessHostFileW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessHostFileInfo *", Info)
        return None
    @handle_error
    def ProcessPanelInputW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessPanelInputInfo *", Info)
        return None
    @handle_error
    def ProcessConsoleInputW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessConsoleInputInfo *", Info)
        return None
    @handle_error
    def ProcessSynchroEventW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessSynchroEventInfo *", Info)
        return None
    @handle_error
    def ProcessViewerEventW(self, Info):
        # intptr_t
        Info = ffi.cast("struct ProcessViewerEventInfo *", Info)
        return None
    @handle_error
    def PutFilesW(self, Info):
        # intptr_t
        Info = ffi.cast("struct PutFilesInfo *", Info)
        return None
    @handle_error
    def SetDirectoryW(self, Info):
        # intptr_t
        Info = ffi.cast("struct SetDirectoryInfo *", Info)
        return None
    @handle_error
    def SetFindListW(self, Info):
        # intptr_t
        Info = ffi.cast("struct SetFindListInfo *", Info)
        return None
    @handle_error
    def GetContentFieldsW(self, Info):
        # intptr_t
        Info = ffi.cast("struct GetContentFieldsInfo *", Info)
        return None
    @handle_error
    def GetContentDataW(self, Info):
        # intptr_t
        Info = ffi.cast("struct GetContentDataInfo *", Info)
        return None
    @handle_error
    def FreeContentDataW(self, Info):
        Info = ffi.cast("struct GetContentDataInfo *", Info)
        pass
