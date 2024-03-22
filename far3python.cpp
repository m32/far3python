#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <initguid.h>

#include <algorithm>
#include <string>

#include <Python.h>

#include <plugin.hpp->
#include <farcolor.hpp>

// {308868BA-5773-4C89-8142-DF877868E06A}
DEFINE_GUID(MainGuid, 0x308868ba, 0x5773, 0x4c89, 0x81, 0x42, 0xdf, 0x87, 0x78, 0x68, 0xe0, 0x6a);

static struct PluginStartupInfo		Info;
static struct FarStandardFunctions	FSF;

#define PYPLUGIN_DEBUGLOG "w:/temp/far3python.log"
//#undef PYPLUGIN_DEBUGLOG

static void python_log(const char *function, unsigned int line, const char *format, ...)
{
#ifdef PYPLUGIN_DEBUGLOG
    va_list args;
    char *xformat = (char *)alloca(strlen(format) + strlen(function) + 64);
    sprintf(xformat, "PYTHON: %s@%u%s%s",
        function, line, (*format != '\n') ? " - " : "", format);

    FILE *stream = nullptr;
    if (PYPLUGIN_DEBUGLOG[0]) {
        stream = fopen(PYPLUGIN_DEBUGLOG, "at");
    }
    if (!stream) {
        stream = stderr;
    }

    va_start(args, format);
    vfprintf(stream, xformat, args);
    va_end(args);

    if (stream != stderr) {
        fclose(stream);
    }
#endif
}

char pythonPluginInstallDir[512]="";

std::string ReplaceAll(std::string str, const std::string& from, const std::string& to) {
    size_t start_pos = 0;
    while((start_pos = str.find(from, start_pos)) != std::string::npos) {
        str.replace(start_pos, from.length(), to);
        start_pos += to.length(); // Handles case where 'to' is a substring of 'from'
    }
    return str;
}

static void InitGlobal(HINSTANCE hDll)
{
	size_t size = sizeof(pythonPluginInstallDir) / sizeof(pythonPluginInstallDir[0]);
	GetModuleFileNameA(hDll, pythonPluginInstallDir, (DWORD)size);
    strrchr(pythonPluginInstallDir, L'\\')[0] = 0;
}

static void DestroyGlobal()
{
}

BOOL WINAPI DllMain(HANDLE hDll, DWORD dwReason, LPVOID lpReserved)
{
	(void) lpReserved;

	if (DLL_PROCESS_ATTACH == dwReason){
		InitGlobal((HINSTANCE)hDll);
	} else if (DLL_PROCESS_DETACH == dwReason)
		DestroyGlobal();

	return TRUE;
}

class PythonHolder
{
    std::string pluginDir;
    void *soPythonInterpreter = nullptr;
    PyObject *pyPluginModule = nullptr;
    PyObject *pyPluginManager = nullptr;


public:
    PythonHolder(std::string pythonPluginInstallDir)
    {
        pluginDir = ReplaceAll(pythonPluginInstallDir, std::string("\\"), std::string("\\\\"));

        std::wstring progname = L"far3python";

        Py_SetProgramName((wchar_t *)progname.c_str());
        Py_Initialize();

        PyEval_InitThreads();

        std::string syspath = "import sys; ";
        syspath += "sys.path.insert(1, '" + pluginDir + "')";
        python_log(__FUNCTION__, __LINE__, "syspath=%s\n", syspath.c_str());

        PyRun_SimpleString(syspath.c_str());

        pyPluginModule = PyImport_ImportModule("far3");
        if (pyPluginModule == NULL) {
            PyErr_Print();
            python_log(__FUNCTION__, __LINE__, "Failed to load \"far3\"\n");
            return;
        }

        pyPluginManager = PyObject_GetAttrString(pyPluginModule, "pluginmanager");
        if (pyPluginManager == NULL) {
            python_log(__FUNCTION__, __LINE__, "Failed to load \"far3.pluginmanager\"\n");
            Py_DECREF(pyPluginModule);
            pyPluginModule = NULL;
        } else {
            vcall("PySetup", 1, pluginDir.c_str());
        }

        python_log(__FUNCTION__, __LINE__, "complete\n");
    }

    virtual ~PythonHolder()
    {
        if (pyPluginManager) {
            Py_XDECREF(pyPluginManager);
            pyPluginManager = nullptr;
        }

        if (pyPluginModule) {
            Py_XDECREF(pyPluginModule);
            pyPluginModule = nullptr;
        }

        Py_Finalize();
    }

    PyObject *pycall(const char *func, int n, va_list args)
    {
        PyObject *result = NULL;
        PyObject *pFunc = PyObject_GetAttrString(pyPluginManager, func);

        if (pFunc == NULL)
            return NULL;

        if (PyCallable_Check(pFunc)) {
            PyObject *pArgs = PyTuple_New(n);

            for (int i = 0; i < n; ++i) {
                PyObject *pValue = PyLong_FromSize_t((size_t)va_arg(args, void *));
                PyTuple_SetItem(pArgs, i, pValue);
            }

            result = PyObject_CallObject(pFunc, pArgs);
            Py_DECREF(pArgs);
        }

        Py_XDECREF(pFunc);
        return result;
    }

    void vcall(const char *func, int n, ...)
    {
#ifdef PYPLUGIN_THREADED
        WaitThread();
#endif
        if (pyPluginManager == NULL)
            return;

        // Acquire the GIL
        PyGILState_STATE gstate = PyGILState_Ensure();

        va_list args;
        va_start(args, n);
        PyObject *pyresult = this->pycall(func, n, args);
        va_end(args);
        if (pyresult == NULL || PyErr_Occurred()) {
            PyErr_Print();
            python_log(__FUNCTION__, __LINE__, "Failed to call \"%s\"\n", func);
        }
        Py_DECREF(pyresult);

        // Release the GIL. No Python API allowed beyond this point.
        PyGILState_Release(gstate);
    }

    intptr_t icall(intptr_t defresult, const char *func, int n, ...)
    {
#ifdef PYPLUGIN_THREADED
        WaitThread();
#endif
        if (pyPluginManager == NULL)
            return defresult;

        // Acquire the GIL
        PyGILState_STATE gstate = PyGILState_Ensure();

        intptr_t result = defresult;
        va_list args;
        va_start(args, n);
        PyObject *pyresult = this->pycall(func, n, args);
        va_end(args);
        if( pyresult != NULL && PyLong_Check(pyresult) )
            result = (intptr_t)PyLong_AsSize_t(pyresult);
        if (pyresult == NULL || PyErr_Occurred()) {
            PyErr_Print();
            python_log(__FUNCTION__, __LINE__, "Failed to call \"%s\"\n", func);
            result = defresult;
        }
        Py_DECREF(pyresult);

        // Release the GIL. No Python API allowed beyond this point.
        PyGILState_Release(gstate);
        return result;
    }

    HANDLE hcall(HANDLE defresult, const char *func, int n, ...)
    {
#ifdef PYPLUGIN_THREADED
        WaitThread();
#endif
        if (pyPluginManager == NULL)
            return defresult;

        // Acquire the GIL
        PyGILState_STATE gstate = PyGILState_Ensure();

        HANDLE result = defresult;
        va_list args;
        va_start(args, n);
        PyObject *pyresult = this->pycall(func, n, args);
        va_end(args);
        if( pyresult != NULL && PyLong_Check(pyresult) )
            result = (HANDLE)PyLong_AsSize_t(pyresult);
        if (pyresult == NULL || PyErr_Occurred()) {
            PyErr_Print();
            python_log(__FUNCTION__, __LINE__, "Failed to call \"%s\"\n", func);
            result = defresult;
        }
        Py_DECREF(pyresult);

        // Release the GIL. No Python API allowed beyond this point.
        PyGILState_Release(gstate);
        return result;
    }
} *g_python_holder = nullptr;


HANDLE WINAPI AnalyseW(const struct AnalyseInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "AnalyseW\n", Info);
    return g_python_holder->hcall(INVALID_HANDLE_VALUE, "AnalyseW", 1, Info);
}

void WINAPI CloseAnalyseW(const struct CloseAnalyseInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "CloseAnalyseW(%p)\n", Info);
    g_python_holder->vcall("CloseAnalyseW", 1, Info);
}

void WINAPI ClosePanelW(const struct ClosePanelInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ClosePanelW(%p)\n", Info);
    g_python_holder->vcall("ClosePanelW", 1, Info);
}

intptr_t WINAPI CompareW(const struct CompareInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "CompareW(%p)\n", Info);
    return g_python_holder->icall(NULL, "CompareW", 1, Info);
}

intptr_t WINAPI ConfigureW(const struct ConfigureInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ConfigureW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ConfigureW", 1, Info);
}

intptr_t WINAPI DeleteFilesW(const struct DeleteFilesInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "DeleteFilesW(%p)\n", Info);
    return g_python_holder->icall(NULL, "DeleteFilesW", 1, Info);
}

void WINAPI ExitFARW(const struct ExitInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ExitFARW(%p)\n", Info);
    g_python_holder->vcall("ExitFARW", 1, Info);
}

void WINAPI FreeFindDataW(const struct FreeFindDataInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "FreeFindDataW\n", Info);
    g_python_holder->vcall("FreeFindDataW", 1, Info);
}

intptr_t WINAPI GetFilesW(struct GetFilesInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "GetFilesW(%p)\n", Info);
    return g_python_holder->icall(NULL, "GetFilesW", 1, Info);
}

intptr_t WINAPI GetFindDataW(struct GetFindDataInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "GetFindDataW(%p)\n", Info);
    return g_python_holder->icall(NULL, "GetFindDataW", 1, Info);
}

void WINAPI GetGlobalInfoW(struct GlobalInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "GetGlobalInfoW\n", Info);
	Info->StructSize = sizeof(GlobalInfo);
	//Info->MinFarVersion = MAKEFARVERSION(FARMANAGERVERSION_MAJOR, FARMANAGERVERSION_MINOR, FARMANAGERVERSION_REVISION, FARMANAGERVERSION_BUILD, FARMANAGERVERSION_STAGE);
	Info->MinFarVersion = MAKEFARVERSION(FARMANAGERVERSION_MAJOR, 0, 0, 0, VS_RELEASE);
	Info->Version = MAKEFARVERSION(1, 0, 0, 0, VS_ALPHA);
	Info->Guid = MainGuid;
	Info->Title = L"Python interpreter";
	Info->Description = L"Python interpreter";
	Info->Author = L"Grzegorz Makarewicz <mak@trisoft.com.pl>";
}

void WINAPI GetOpenPanelInfoW(struct OpenPanelInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "GetOpenPanelInfoW(%p)\n", Info);
    g_python_holder->vcall("GetOpenPanelInfoW", 1, Info);
}

void WINAPI GetPluginInfoW(struct PluginInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "GetPluginInfoW(%p)\n", Info);
    Info->StructSize = sizeof(*Info);
    Info->Flags = PF_DISABLEPANELS;
    if( g_python_holder == nullptr )
        return;
    g_python_holder->vcall("GetPluginInfoW", 1, Info);
}

intptr_t WINAPI MakeDirectoryW(struct MakeDirectoryInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "MakeDirectoryW(%p)\n", Info);
    return g_python_holder->icall(NULL, "MakeDirectoryW", 1, Info);
}

HANDLE WINAPI OpenW(const struct OpenInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "OpenW(%p)\n", Info);
    return g_python_holder->hcall(INVALID_HANDLE_VALUE, "OpenW", 1, Info);
}

intptr_t WINAPI ProcessDialogEventW(const struct ProcessDialogEventInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessDialogEventW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessDialogEventW", 1, Info);
}

intptr_t WINAPI ProcessEditorEventW(const struct ProcessEditorEventInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessEditorEventW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessEditorEventW", 1, Info);
}

intptr_t WINAPI ProcessEditorInputW(const struct ProcessEditorInputInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessEditorInputW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessEditorInputW", 1, Info);
}

intptr_t WINAPI ProcessPanelEventW(const struct ProcessPanelEventInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessPanelEventW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessPanelEventW", 1, Info);
}

intptr_t WINAPI ProcessHostFileW(const struct ProcessHostFileInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessHostFileW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessHostFileW", 1, Info);
}

intptr_t WINAPI ProcessPanelInputW(const struct ProcessPanelInputInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessPanelInputW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessPanelInputW", 1, Info);
}

intptr_t WINAPI ProcessConsoleInputW(struct ProcessConsoleInputInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessConsoleInputW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessConsoleInputW", 1, Info);
}

intptr_t WINAPI ProcessSynchroEventW(const struct ProcessSynchroEventInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessSynchroEventW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessSynchroEventW", 1, Info);
}

intptr_t WINAPI ProcessViewerEventW(const struct ProcessViewerEventInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "ProcessViewerEventW(%p)\n", Info);
    return g_python_holder->icall(NULL, "ProcessViewerEventW", 1, Info);
}

intptr_t WINAPI PutFilesW(const struct PutFilesInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "PutFilesW(%p)\n", Info);
    return g_python_holder->icall(NULL, "PutFilesW", 1, Info);
}

intptr_t WINAPI SetDirectoryW(const struct SetDirectoryInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "SetDirectoryW(%p)\n", Info);
    return g_python_holder->icall(NULL, "SetDirectoryW", 1, Info);
}

intptr_t WINAPI SetFindListW(const struct SetFindListInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "SetFindListW(%p)\n", Info);
    return g_python_holder->icall(NULL, "SetFindListW", 1, Info);
}

void WINAPI SetStartupInfoW(const struct PluginStartupInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "SetStartupInfoW(%p)\n", Info);

	::Info = *Info;
	::FSF = *Info->FSF;
	::Info.FSF = &FSF;

    std::string splugindir(pythonPluginInstallDir);
    g_python_holder = new PythonHolder(splugindir);
    g_python_holder->vcall("SetStartupInfoW", 2, &::Info, &::FSF);
}

intptr_t WINAPI GetContentFieldsW(const struct GetContentFieldsInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "GetContentFieldsW(%p)\n", Info);
    return g_python_holder->icall(NULL, "GetContentFieldsW", 1, Info);
}

intptr_t WINAPI GetContentDataW(struct GetContentDataInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "GetContentDataW(%p)\n", Info);
    return g_python_holder->icall(NULL, "GetContentDataW", 1, Info);
}

void WINAPI FreeContentDataW(const struct GetContentDataInfo *Info)
{
    python_log(__FUNCTION__, __LINE__, "FreeContentDataW(%p)\n", Info);
    g_python_holder->vcall("FreeContentDataW", 1, Info);
}
