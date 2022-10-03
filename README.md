# Far Manager Plugins API bindings for Python

The python plugin has only one purpose - to facilitate the writing of scripts that extend the capabilities of FarManager.

## Useful links

* [Far Manager website](https://www.farmanager.com/index.php?l=en)
* [Far Manager Plugins API reference](https://api.farmanager.com/ru/index.html)

## Howto

* Just place far3python.dll and far3 directory inside plugins path searched by FarManager.

* Logging and logger configuration
There is a logger.ini file, you can set your own log information preferences there.
By default, the log is saved to the file w:/temp/far3-py.log.

* Fundamentals

** plugins must be accessible via PYTHONPATH
** the plugins are loaded with the command "py:load filename" for example py:load ucharmap
** unloading the plugin is done with the command "py:unload filename" for example py:unload ucharmap

** ['ucharmap](far3examples/ucharmap.py) - an example plugin showing part of the UTF-8 character set
    F11 + "Python Character Map" - display its dialog
    after pressing Enter/OK selected character is coppied into clipboard, character selection is done
    with mouse or arrows
** ['utranslate](far3examples/utranslate.py) - how to use Google translate for spellchecker and text translation
    F11 + "Python Translate" - display help dialog

## Testing

* ['CFFI callbacks test dialog](far3examples/t-dialog.py) - check CFFI generated bindings for dialog
* ['CFFI callbacks test settings](far3examples/t-settings.py) - check CFFI generated bindings for settings

## Implementation status

### Basic API

Export functions

- [ ] [ExitFARW](https://api.farmanager.com/ru/exported_functions/exitfarw.html)
- [x] [GetGlobalInfoW](https://api.farmanager.com/ru/exported_functions/getglobalinfow.html)
- [x] [GetPluginInfoW](https://api.farmanager.com/ru/exported_functions/getplugininfow.html)
- [x] [OpenW](https://api.farmanager.com/ru/exported_functions/openw.html)
- [x] [SetStartupInfoW](https://api.farmanager.com/ru/exported_functions/setstartupinfow.html)

Service functions

- [ ] [GetMsg](https://api.farmanager.com/ru/service_functions/getmsg.html)
- [ ] [InputBox](https://api.farmanager.com/ru/service_functions/inputbox.html)
- [ ] [Menu](https://api.farmanager.com/ru/service_functions/menu.html)
- [x] [Message](https://api.farmanager.com/ru/service_functions/message.html)
- [ ] [ShowHelp](https://api.farmanager.com/ru/service_functions/showhelp.html)

### Panel API

Export functions

- [ ] [AnalyseW](https://api.farmanager.com/ru/exported_functions/analysew.html)
- [ ] [CloseAnalyseW](https://api.farmanager.com/ru/exported_functions/closeanalysew.html)
- [ ] [ClosePanelW](https://api.farmanager.com/ru/exported_functions/closepanelw.html)
- [ ] [CompareW](https://api.farmanager.com/ru/exported_functions/comparew.html)
- [ ] [DeleteFilesW](https://api.farmanager.com/ru/exported_functions/deletefilesw.html)
- [ ] [FreeFindDataW](https://api.farmanager.com/ru/exported_functions/freefinddataw.html)
- [ ] [GetFilesW](https://api.farmanager.com/ru/exported_functions/getfilesw.html)
- [ ] [GetFindDataW](https://api.farmanager.com/ru/exported_functions/getfinddataw.html)
- [ ] [GetOpenPanelInfoW](https://api.farmanager.com/ru/exported_functions/getopenpanelinfow.html)
- [ ] [MakeDirectoryW](https://api.farmanager.com/ru/exported_functions/makedirectoryw.html)
- [ ] [ProcessPanelEventW](https://api.farmanager.com/ru/exported_functions/processpaneleventw.html)
- [ ] [ProcessHostFileW](https://api.farmanager.com/ru/exported_functions/processhostfilew.html)
- [ ] [ProcessPanelInputW](https://api.farmanager.com/ru/exported_functions/processpanelinputw.html)
- [ ] [PutFilesW](https://api.farmanager.com/ru/exported_functions/putfilesw.html)
- [ ] [SetDirectoryW](https://api.farmanager.com/ru/exported_functions/setdirectoryw.html)
- [ ] [SetFindListW](https://api.farmanager.com/ru/exported_functions/setfindlistw.html)

Service functions

- [ ] [PanelControl](https://api.farmanager.com/ru/service_functions/panelcontrol.html)
- [ ] [FileFilterControl](https://api.farmanager.com/ru/service_functions/filefiltercontrol.html)
- [ ] [FreeDirList](https://api.farmanager.com/ru/service_functions/freedirlist.html)
- [ ] [FreePluginDirList](https://api.farmanager.com/ru/service_functions/freeplugindirlist.html)
- [ ] [GetDirList](https://api.farmanager.com/ru/service_functions/getdirlist.html)
- [ ] [GetPluginDirList](https://api.farmanager.com/ru/service_functions/getplugindirlist.html)

### Editor API

Export functions

- [ ] [ProcessEditorInputW](https://api.farmanager.com/ru/exported_functions/processeditorinputw.html)
- [ ] [ProcessEditorEventW](https://api.farmanager.com/ru/exported_functions/processeditoreventw.html)

Service functions

- [ ] [Editor](https://api.farmanager.com/ru/service_functions/editor.html)
- [ ] [EditorControl](https://api.farmanager.com/ru/service_functions/editorcontrol.html)

### Viewer API

Export functions

- [ ] [ProcessViewerEventW](https://api.farmanager.com/ru/exported_functions/processviewereventw.html)

Service functions

- [ ] [Viewer](https://api.farmanager.com/ru/service_functions/viewer.html)
- [ ] [ViewerControl](https://api.farmanager.com/ru/service_functions/viewercontrol.html)

### Dialog API

Export functions

- [ ] [ProcessDialogEventW](https://api.farmanager.com/ru/exported_functions/processdialogeventw.html)

Service functions

- [x] [DefDlgProc](https://api.farmanager.com/ru/service_functions/defdlgproc.html)
- [x] [DialogFree](https://api.farmanager.com/ru/service_functions/dialogfree.html)
- [x] [DialogInit](https://api.farmanager.com/ru/service_functions/dialoginit.html)
- [x] [DialogRun](https://api.farmanager.com/ru/service_functions/dialogrun.html)
- [x] [SendDlgMessage](https://api.farmanager.com/ru/service_functions/senddlgmessage.html)

### Settings API

Export functions

- [x] [ConfigureW](https://api.farmanager.com/ru/exported_functions/configurew.html)

Service functions

- [ ] [SettingsControl](https://api.farmanager.com/ru/service_functions/settingscontrol.html)

### Plugin Manager API

Service functions

- [ ] [PluginsControl](https://api.farmanager.com/ru/service_functions/pluginscontrol.html)

### Miscellaneous API

Export functions

- [ ] [ProcessConsoleInputW](https://api.farmanager.com/ru/exported_functions/processconsoleinputw.html)
- [ ] [ProcessSynchroEventW](https://api.farmanager.com/ru/exported_functions/processsynchroeventw.html)

Service functions

- [ ] [AdvControl](https://api.farmanager.com/ru/service_functions/advcontrol.html)
- [ ] [ColorDialog](https://api.farmanager.com/ru/service_functions/colordialog.html)
- [ ] [RegExpControl](https://api.farmanager.com/ru/service_functions/regexpcontrol.html)
- [ ] [RestoreScreen](https://api.farmanager.com/ru/service_functions/restorescreen.html)
- [ ] [SaveScreen](https://api.farmanager.com/ru/service_functions/savescreen.html)
- [ ] [Text](https://api.farmanager.com/ru/service_functions/text.html)

### Macro API

Service functions

- [ ] [MacroControl](https://api.farmanager.com/ru/service_functions/macrocontrol.html)

## License
[license]: #license

This project is licensed under the terms of the MIT license.

See [LICENSE-MIT](LICENSE-MIT)
