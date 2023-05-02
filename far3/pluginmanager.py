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

def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return

    if log is not None:
        log.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    else:
        print(exc_type, exc_value, exc_traceback)
        print()

#sys.excepthook = handle_exception

from .plugin import PluginBase

# commands in shell window:
#     py:load <python modulename>
#     py:unload <registered python module name>


from .far3cffi import ffi, ffic

class PluginManager(PluginBase):
    name = "Python plugin manager"
    flags = ffic.PF_NONE
    title = "Python plugin manager"
    author = "Grzegorz Makarewicz <mak@trisoft.com.pl"
    description = "Python plugin manager"
    guid = PluginBase.pyguid
    version = (1, 0, 0, 0, ffic.VS_SPECIAL)
    openFrom = ["CONFIGURE"]

    Info = None

    def __init__(self):
        super().__init__(None)
        self.openplugins = {}
        self.plugins = []

    def pluginRemove(self, name):
        log.debug("remove plugin: {}".format(name))
        for i in range(len(self.plugins)):
            pinfo = self.plugins[i].Plugin
            if pinfo.name == name:
                del self.plugins[i]
                del sys.modules[name]
                return
        log.error("uninstall plugin: {} - not installed".format(name))

    def pluginInstall(self, name):
        log.debug("install plugin: {}".format(name))
        for plugin in self.plugins:
            if plugin.Plugin.name == name:
                log.error("install plugin: {} - allready installed".format(name))
                return
        plugin = __import__(name)
        log.debug("plugin={}".format(plugin))
        cls = getattr(plugin, "Plugin", None)
        log.debug("cls={}".format(cls))
        if issubclass(cls, PluginBase):
            self.plugins.append(plugin)
        else:
            log.error("install plugin: {} - not a far3 python plugin {}".format(name, cls))
            del sys.modules[name]

    def pluginGet(self, hPlugin):
        v = self.openplugins.get(hPlugin, None)
        if v is None:
            class Nop:
                def __getattr__(self, name):
                    log.debug("Nop."+name)
                    return self

                def __call__(self, *args):
                    log.debug("Nop({})".format(args))
                    return None

            v = Nop
            log.error("unhandled pluginGet({})".format(hPlugin))
        return v

    ################
    def PySetup(self, pluginDir):
        global log
        self.PLUGINROOT = ffi.string(ffi.cast("char *", pluginDir)).decode("utf-8")
        fname = os.path.join(self.PLUGINROOT, "logger.ini")
        if os.path.isfile(fname):
            with open(fname, "rt") as fp:
                ini = configparser.ConfigParser()
                ini.read_file(fp)
                logging.config.fileConfig(ini)
        log = logging.getLogger(__name__)
        fname = os.path.join(self.PLUGINROOT, "python.ini")
        try:
            if os.path.isfile(fname):
                with open(fname, "rt") as fp:
                    ini = configparser.ConfigParser()
                    ini['python'] = {'pluginspath': ''}
                    ini.read_file(fp)
                    pluginspath = ini['python'].get('pluginspath').strip()
                    if pluginspath != '':
                        sys.path.insert(2, pluginspath)
        except:
            log.exception("PySetup")
        log.debug("%s start" % ("*"*20))
        log.debug("sys.path={}".format(sys.path))
        log.debug("PLUGINROOT={}".format(self.PLUGINROOT))

    def SetStartupInfoW(self, _PSI, _FSF):
        log.debug("SetStartupInfoW({:08X}, {:08X})".format(_PSI, _FSF))
        self.Info = ffi.cast("struct PluginStartupInfo *", _PSI)
        self.FarStd = ffi.cast("struct FarStandardFunctions *", _FSF)
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

        log.debug("GetPluginInfo({:08X})".format(Info))
        Info = ffi.cast("struct PluginInfo *", Info)
        self._DiskString = []
        self._DiskGuid = []
        self._PluginGuid = []
        self._PluginString = []
        self._ConfigString = []
        self._ConfigGuid = []
        self.commandPrefix = self.s2f("py")

        for plugin in self.plugins:
            pinfo = plugin.Plugin
            log.debug("plugin:{} openfrom:{}".format(
                pinfo.title, pinfo.openFrom
            ))
            openFrom = pinfo.openFrom
            if "DISKMENU" in openFrom:
                self._DiskString.append(self.s2f(pinfo.title))
                self._DiskGuid.append(guid(pinfo.guid))
            if "PLUGINSMENU" in openFrom:
                self._PluginString.append(self.s2f(pinfo.title))
                self._PluginGuid.append(guid(pinfo.guid))
            if "CONFIGURE" in openFrom:
                self._ConfigString.append(self.s2f(pinfo.title))
                self._ConfigGuid.append(guid(pinfo.guid))
        log.debug("GetPluginInfo.1: disk:{} plugin:{} config:{}".format(
            len(self._DiskString),
            len(self._PluginString),
            len(self._ConfigString)
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

        Info.Flags = ffic.PF_EDITOR | ffic.PF_VIEWER | ffic.PF_DIALOG | ffic.PF_FULLCMDLINE
        Info.CommandPrefix = self.commandPrefix
        #self.Message("Python", "contents", "line1", "line2")

    def OpenW(self, Info):
        Info = ffi.cast("struct OpenInfo *", Info)
        g = self.GUID2UUID(Info.Guid)
        log.debug("Open({}, {}, {}, {})".format(Info.OpenFrom, g, Info.Data, Info.Instance))
        if Info.OpenFrom == ffic.OPEN_COMMANDLINE and g == self.farguid:
            cmdline = ffi.cast("struct OpenCommandLineInfo *", Info.Data)
            line = ffi.string(cmdline.CommandLine).strip()
            log.debug("cmd:{}".format(line))
            linesplit = line.split(" ", 1)
            if linesplit[0] == "py:unload":
                if len(linesplit) > 1:
                    self.pluginRemove(linesplit[1])
                else:
                    log.debug("missing plugin name in py:unload <plugin name>")
                return None
            elif linesplit[0] == "py:load":
                if len(linesplit) > 1:
                    self.pluginInstall(linesplit[1])
                else:
                    log.debug("missing plugin name in py:load <plugin name>")
            else:
                for plugin in self.plugins:
                    if plugin.Plugin.canHandleCommandLine(linesplit[0]) is True:
                        try:
                            cls = plugin.Plugin(self.Info)
                            rc = cls.CommandLine(line)
                        except:
                            log.exception("CommandLine({})".format(plugin.Plugin.title))
                            rc = None
                        return rc
                else:
                    log.debug("no handler for {}".format(line))
            return None
        for plugin in self.plugins:
            if plugin.Plugin.guid == g:
                log.debug("OpenW({})".format(plugin.Plugin.title))
                try:
                    cls = plugin.Plugin(self.Info)
                    rc = cls.OpenW(Info)
                    if rc is not None:
                        self.openplugins[rc] = cls
                    return rc
                except:
                    log.exception("OpenW({})".format(plugin.Plugin.title))
                    return None
        return None

    def ConfigureW(self, Info):
        Info = ffi.cast("struct ConfigureInfo *", Info)
        g = self.GUID2UUID(Info.Guid)
        log.debug("ConfigureW({}, {})".format(g, Info.Instance))
        for plugin in self.plugins:
            pinfo = plugin.Plugin
            if pinfo.guid == g:
                plugin = plugin.Plugin(self.Info)
                plugin.ConfigureW(Info)
                return

    def ExitFARW(self, Info):
        log.debug("ExitFARW({})".format(Info))
