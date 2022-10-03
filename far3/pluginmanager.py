import os
import os.path
import sys
import types
import uuid
import configparser
import logging
import logging.config

logging.basicConfig(level=logging.INFO)
log = None
PLUGINROOT = None

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    if log is not None:
        log.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

#sys.excepthook = handle_exception

from .plugin import PluginBase

# commands in shell window:
#     py:load <python modulename>
#     py:unload <registered python module name>


from .far3cffi import ffi, ffic

class PluginManager:
    guid = uuid.UUID('{308868BA-5773-4C89-8142-DF877868E06A}')

    Info = None

    def __init__(self):
        self.openplugins = {}
        self.plugins = []

    def s2f(self, s):
        return ffi.new("wchar_t []", s)

    def f2s(self, s):
        s = ffi.string(ffi.cast("wchar_t *", s))
        return s

    def GUID2UUID(self, g0):
        c = 0
        for i in g0.Data4[2:len(g0.Data4)]:
            c = c<<8 | i
        g = uuid.UUID(fields=(g0.Data1, g0.Data2, g0.Data3, g0.Data4[0], g0.Data4[1], c))
        return g

    ################
    def pluginRemove(self, name):
        log.debug("remove plugin: {0}".format(name))
        for i in range(len(self.plugins)):
            pinfo = self.plugins[i].Plugin.PluginInfo
            if pinfo.name == name:
                del self.plugins[i]
                del sys.modules[name]
                return
        log.error("install plugin: {0} - not installed".format(name))

    def pluginInstall(self, name):
        log.debug("install plugin: {0}".format(name))
        for plugin in self.plugins:
            if plugin.Plugin.PluginInfo.name == name:
                log.error("install plugin: {0} - allready installed".format(name))
                return
        plugin = __import__(name)
        log.debug("plugin={}".format(plugin))
        cls = getattr(plugin, 'Plugin', None)
        log.debug("cls={} type(cls)={}".format(cls, type(cls)))
        if type(cls) == type(PluginBase):
            self.plugins.append(plugin)
        else:
            log.error("install plugin: {0} - not a far3 python plugin {1}".format(name, type(cls)))
            del sys.modules[name]

    def pluginGet(self, hPlugin):
        v = self.openplugins.get(hPlugin, None)
        if v is None:

            class Nop:
                def __getattr__(self, name):
                    log.debug("Nop."+name)
                    return self

                def __call__(self, *args):
                    log.debug("Nop({0})".format(args))
                    return None

            v = Nop
            log.error("unhandled pluginGet{0}".format(hPlugin))
        return v

    ################
    def PySetup(self, pluginDir):
        global log, PLUGINROOT
        PLUGINROOT = ffi.string(ffi.cast("char *", pluginDir)).decode('utf-8')
        fname = os.path.join(PLUGINROOT, 'logger.ini')
        if os.path.isfile(fname):
            with open(fname, "rt") as fp:
                ini = configparser.ConfigParser()
                ini.read_file(fp)
                logging.config.fileConfig(ini)
        log = logging.getLogger(__name__)
        log.debug('%s start' % ('*'*20))
        log.debug('sys.path={0}'.format(sys.path))
        log.debug('PLUGINROOT={0}'.format(PLUGINROOT))

    ################
    def SetStartupInfoW(self, _PSI, _FSF):
        log.debug("SetStartupInfoW({0:08X})".format(_PSI))
        self.Info = ffi.cast("struct PluginStartupInfo *", _PSI)
        #self.FarStd = ffi.cast("struct PluginStartupInfo *", _PSI)
        from . import upythonconfig
        self.plugins.append(upythonconfig)

    def GetPluginInfoW(self, Info):
        def guid(uuid):
            s = uuid.hex[16:]
            b = []
            for i in range(0, len(s), 2):
                b.append(int(s[i:i+2], 16))
            g = (
                uuid.fields[0],
                uuid.fields[1],
                uuid.fields[2],
                b,
            )
            return g

        log.debug("GetPluginInfoW({0:08X})".format(Info))
        Info = ffi.cast("struct PluginInfo *", Info)
        self._DiskString = []
        self._DiskGuid = []
        self._PluginGuid = []
        self._PluginString = []
        self._ConfigString = []
        self._ConfigGuid = []
        log.debug("GetPluginInfoW")
        for plugin in self.plugins:
            pinfo = plugin.Plugin.PluginInfo
            log.debug('plugin:{} openfrom:{} configure:{}'.format(
                pinfo.title, pinfo.openFrom, plugin.Plugin.Configure is not None
            ))
            openFrom = pinfo.openFrom
            if "DISKMENU" in openFrom:
                self._DiskString.append(ffi.new("wchar_t []", pinfo.title))
                self._DiskGuid.append(guid(pinfo.guid))
            if "PLUGINSMENU" in openFrom:
                self._PluginString.append(ffi.new("wchar_t []", pinfo.title))
                self._PluginGuid.append(guid(pinfo.guid))
            if plugin.Plugin.Configure is not None:
                self._ConfigString.append(ffi.new("wchar_t []", pinfo.title))
                self._ConfigGuid.append(guid(pinfo.guid))
        log.debug("GetPluginInfoW.1: disk:{} plugin:{} config:{}".format(
            len(self._DiskString), len(self._PluginString), len(self._ConfigString)
        ))
        if self._DiskString:
            self.DiskString = ffi.new("wchar_t *[]", self._DiskString)
            self.DiskGuid = ffi.new("GUID []", self._DiskGuid)
            Info.DiskMenu.Strings = self.DiskString
            Info.DiskMenu.Guids = self.DiskGuid
            Info.DiskMenu.Count = len(self._DiskString)
        if self._PluginString:
            self.PluginString = ffi.new("wchar_t *[]", self._PluginString)
            self.PluginGuid = ffi.new("GUID []", self._PluginGuid)
            Info.PluginMenu.Strings = self.PluginString
            Info.PluginMenu.Guids = self.PluginGuid
            Info.PluginMenu.Count = len(self._PluginString)
        if self._ConfigString:
            self.ConfigString = ffi.new("wchar_t *[]", self._ConfigString)
            self.ConfigGuid = ffi.new("GUID []", self._ConfigGuid)
            Info.PluginConfig.Strings = self.ConfigString
            Info.PluginConfig.Guids = self.ConfigGuid
            Info.PluginConfig.Count = len(self._ConfigString)
        Info.Flags = ffic.PF_EDITOR | ffic.PF_VIEWER | ffic.PF_DIALOG
        Info.CommandPrefix = ffi.new("wchar_t []", "py")

	# HANDLE   WINAPI AnalyseW(const struct AnalyseInfo *Info);
	# void     WINAPI CloseAnalyseW(const struct CloseAnalyseInfo *Info);
	# void     WINAPI ClosePanelW(const struct ClosePanelInfo *Info);
	# intptr_t WINAPI CompareW(const struct CompareInfo *Info);
	# intptr_t WINAPI ConfigureW(const struct ConfigureInfo *Info);
	# intptr_t WINAPI DeleteFilesW(const struct DeleteFilesInfo *Info);
	# void     WINAPI ExitFARW(const struct ExitInfo *Info);
	# void     WINAPI FreeFindDataW(const struct FreeFindDataInfo *Info);
	# intptr_t WINAPI GetFilesW(struct GetFilesInfo *Info);
	# intptr_t WINAPI GetFindDataW(struct GetFindDataInfo *Info);
	# void     WINAPI GetGlobalInfoW(struct GlobalInfo *Info);
	# void     WINAPI GetOpenPanelInfoW(struct OpenPanelInfo *Info);
	##void     WINAPI GetPluginInfoW(struct PluginInfo *Info);
	# intptr_t WINAPI MakeDirectoryW(struct MakeDirectoryInfo *Info);
	# HANDLE   WINAPI OpenW(const struct OpenInfo *Info);
	# intptr_t WINAPI ProcessDialogEventW(const struct ProcessDialogEventInfo *Info);
	# intptr_t WINAPI ProcessEditorEventW(const struct ProcessEditorEventInfo *Info);
	# intptr_t WINAPI ProcessEditorInputW(const struct ProcessEditorInputInfo *Info);
	# intptr_t WINAPI ProcessPanelEventW(const struct ProcessPanelEventInfo *Info);
	# intptr_t WINAPI ProcessHostFileW(const struct ProcessHostFileInfo *Info);
	# intptr_t WINAPI ProcessPanelInputW(const struct ProcessPanelInputInfo *Info);
	# intptr_t WINAPI ProcessConsoleInputW(struct ProcessConsoleInputInfo *Info);
	# intptr_t WINAPI ProcessSynchroEventW(const struct ProcessSynchroEventInfo *Info);
	# intptr_t WINAPI ProcessViewerEventW(const struct ProcessViewerEventInfo *Info);
	# intptr_t WINAPI PutFilesW(const struct PutFilesInfo *Info);
	# intptr_t WINAPI SetDirectoryW(const struct SetDirectoryInfo *Info);
	# intptr_t WINAPI SetFindListW(const struct SetFindListInfo *Info);
	##void     WINAPI SetStartupInfoW(const struct PluginStartupInfo *Info);
	# intptr_t WINAPI GetContentFieldsW(const struct GetContentFieldsInfo *Info);
	# intptr_t WINAPI GetContentDataW(struct GetContentDataInfo *Info);
	# void     WINAPI FreeContentDataW(const struct GetContentDataInfo *Info);

    def OpenW(self, Info):
        Info = ffi.cast("struct OpenInfo *", Info)
        g = self.GUID2UUID(Info.Guid)
        log.debug("OpenW({}, {}, {}, {})".format(Info.OpenFrom, g, Info.Data, Info.Instance))
        rc = None
        if Info.OpenFrom == ffic.OPEN_COMMANDLINE:
            cmdline = ffi.cast("struct OpenCommandLineInfo *", Info.Data)
            line = ffi.string(cmdline.CommandLine).strip()
            log.debug("cmd:{}".format(line))
            linesplit = line.split(' ', 1)
            if linesplit[0] == "unload":
                if len(linesplit) > 1:
                    self.pluginRemove(linesplit[1])
                else:
                    log.debug("missing plugin name in py:unload <plugin name>")
            elif linesplit[0] == "load":
                if len(linesplit) > 1:
                    self.pluginInstall(linesplit[1])
                else:
                    log.debug("missing plugin name in py:load <plugin name>")
            else:
                for plugin in self.plugins:
                    pinfo = plugin.Plugin.PluginInfo
                    if plugin.Plugin.HandleCommandLine(linesplit[0]) is True:
                        try:
                            cls = plugin.Plugin(self, self.Info)
                            rc = cls.CommandLine(line)
                        except:
                            log.exception('CommandLine({})'.format(pinfo.title))
                            rc = None
                        return rc
                else:
                    log.debug("no handler for {}".format(line))
        else:
            for plugin in self.plugins:
                pinfo = plugin.Plugin.PluginInfo
                if pinfo.guid == g:
                    log.debug('OpenW({})'.format(pinfo.title))
                    try:
                        cls = plugin.Plugin(self, self.Info)
                        rc = cls.OpenW(Info)
                    except:
                        log.exception('OpenW({})'.format(pinfo.title))
                        rc = None
                    if rc is not None:
                        rc = id(cls)
                        self.openplugins[rc] = cls
        return rc

    ################
    def ClosePlugin(self, hPlugin):
        log.debug("ClosePlugin %08X" % hPlugin)
        plugin = self.openplugins.get(hPlugin, None)
        if plugin is not None:
            plugin.Close()
            del self.openplugins[hPlugin]

    def Compare(self, hPlugin, PanelItem1, PanelItem2, Mode):
        log.debug("Compare({0}, {1}, {2}, {3})".format(hPlugin, PanelItem1, PanelItem2, Mode))
        plugin = self.pluginGet(hPlugin)
        return plugin.Compare(PanelItem1, PanelItem2, Mode)

    def Configure(self, ItemNumber):
        log.debug("Configure({0})".format(ItemNumber))
        for plugin in self.plugins:
            if plugin.Plugin.Configure is not None:
                if ItemNumber == 0:
                    plugin = plugin.Plugin(self, self.Info)
                    plugin.Configure()
                    return
                ItemNumber -= 1

    def DeleteFiles(self, hPlugin, PanelItem, ItemsNumber, OpMode):
        log.debug("DeleteFiles({0}, {1}, {2})".format(hPlugin, PanelItem, ItemsNumber, OpMode))
        plugin = self.pluginGet(hPlugin)
        return plugin.DeleteFiles(PanelItem, ItemsNumber, OpMode)

    def ExitFAR(self):
        log.debug("ExitFAR()")

    def FreeFindData(self, hPlugin, PanelItem, ItemsNumber):
        log.debug("FreeFindData({0}, {1}, {2})".format(hPlugin, PanelItem, ItemsNumber))
        plugin = self.pluginGet(hPlugin)
        return plugin.FreeFindData(PanelItem, ItemsNumber)

    def FreeVirtualFindData(self, hPlugin, PanelItem, ItemsNumber):
        log.debug("FreeVirtualData({0}, {1}, {2})".format(hPlugin, PanelItem, ItemsNumber))
        plugin = self.pluginGet(hPlugin)
        return plugin.FreeVirtualFindData(PanelItem, ItemsNumber)

    def GetFiles(self, hPlugin, PanelItem, ItemsNumber, Move, DestPath, OpMode):
        log.debug("GetFiles({0}, {1}, {2}, {3}, {4}, {5})".format(hPlugin, PanelItem, ItemsNumber, Move, DestPath, OpMode))
        plugin = self.pluginGet(hPlugin)
        return plugin.GetFiles(PanelItem, ItemsNumber, Move, DestPath, OpMode)

    def GetFindData(self, hPlugin, PanelItem, ItemsNumber, OpMode):
        log.debug("GetFindData({0}, {1}, {2}, {3})".format(hPlugin, PanelItem, ItemsNumber, OpMode))
        plugin = self.pluginGet(hPlugin)
        return plugin.GetFindData(PanelItem, ItemsNumber, OpMode)

    def GetMinFarVersion(self):
        log.debug("GetMinFarVersion()")

    def GetOpenPluginInfo(self, hPlugin, OpenInfo):
        log.debug("GetOpenPluginInfo({0}, {1},)".format(hPlugin, OpenInfo))
        plugin = self.pluginGet(hPlugin)
        return plugin.GetOpenPluginInfo(OpenInfo)

    def GetVirtualFindData(self, hPlugin, PanelItem, ItemsNumber, Path):
        log.debug("GetVirtualFindData({0}, {1}, {2}, {3})".format(hPlugin, PanelItem, ItemsNumber, Path))
        plugin = self.pluginGet(hPlugin)
        return plugin.GetVirtualFindData(PanelItem, ItemsNumber, Path)

    def MakeDirectory(self, hPlugin, Name, OpMode):
        log.debug("MakeDirectory({0}, {1}, {2})".format(hPlugin, Name, OpMode))
        plugin = self.pluginGet(hPlugin)
        return plugin.MakeDirectory(Name, OpMode)

    def OpenFilePlugin(self, Name, Data, DataSize, OpMode):
        log.debug("OpenFilePlugin({0}, {1}, {2}, {3})".format(Name, Data, DataSize, OpMode))

    def ProcessDialogEvent(self, Event, Param):
        # log.debug("ProcessDialogEvent({0}, {1}))".format(Event, Param))
        pass

    def ProcessEditorEvent(self, Event, Param):
        # log.debug("ProcessEditorEvent({0}, {1})".format(Event, Param))
        pass

    def ProcessEditorInput(self, Rec):
        log.debug("ProcessEditorInput({0})".format(Rec))

    def ProcessEvent(self, hPlugin, Event, Param):
        # log.debug("ProcessEvent({0}, {1}, {2})".format(hPlugin, Event, Param))
        plugin = self.pluginGet(hPlugin)
        return plugin.ProcessEvent(Event, Param)

    def ProcessHostFile(self, hPlugin, PanelItem, ItemsNumber, OpMode):
        log.debug("ProcessHostFile({0}, {1}, {2}, {3})".format(hPlugin, PanelItem, ItemsNumber, OpMode))
        plugin = self.pluginGet(hPlugin)
        return plugin.ProcessHostFile(PanelItem, ItemsNumber, OpMode)

    def ProcessKey(self, hPlugin, Key, ControlState):
        log.debug("ProcessKey({0}, {1}, {2})".format(hPlugin, Key, ControlState))
        plugin = self.pluginGet(hPlugin)
        return plugin.ProcessKey(Key, ControlState)

    def ProcessSynchroEvent(self, Event, Param):
        # log.debug("ProcessSynchroEvent({0}, {1})".format(Event, Param))
        pass

    def ProcessViewerEvent(self, Event, Param):
        # log.debug("ProcessViewerEvent({0}, {1})".format(Event, Param))
        pass

    def PutFiles(self, hPlugin, PanelItem, ItemsNumber, Move, SrcPath, OpMode):
        log.debug("PutFiles({0}, {1}, {2}, {3}, {4}, {5})".format(hPlugin, PanelItem, ItemsNumber, Move, SrcPath, OpMode))
        plugin = self.pluginGet(hPlugin)
        return plugin.PutFiles(PanelItem, ItemsNumber, Move, SrcPath, OpMode)

    def SetDirectory(self, hPlugin, Dir, OpMode):
        log.debug("SetDirectory({0}, {1}, {2})".format(hPlugin, Dir, OpMode))
        plugin = self.pluginGet(hPlugin)
        return plugin.SetDirectory(Dir, OpMode)

    def SetFindList(self, hPlugin, PanelItem, ItemsNumber):
        log.debug("SetFindList({0}, {1}, {2})".format(hPlugin, PanelItem, ItemsNumber))
        plugin = self.pluginGet(hPlugin)
        return plugin.SetFindList(PanelItem, ItemsNumber)
