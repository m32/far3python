from ctypes import *
from ctypes.wintypes import _COORD
from ctypes.wintypes import *

RIGHT_ALT_PRESSED               =0x0001 #// the right alt key is pressed.
LEFT_ALT_PRESSED                =0x0002 #// the left alt key is pressed.
RIGHT_CTRL_PRESSED              =0x0004 #// the right ctrl key is pressed.
LEFT_CTRL_PRESSED               =0x0008 #// the left ctrl key is pressed.
SHIFT_PRESSED                   =0x0010 #// the shift key is pressed.
NUMLOCK_ON                      =0x0020 #// the numlock light is on.
SCROLLLOCK_ON                   =0x0040 #// the scrolllock light is on.
CAPSLOCK_ON                     =0x0080 #// the capslock light is on.
ENHANCED_KEY                    =0x0100 #// the key is enhanced.

FROM_LEFT_1ST_BUTTON_PRESSED    =0x0001
RIGHTMOST_BUTTON_PRESSED        =0x0002
FROM_LEFT_2ND_BUTTON_PRESSED    =0x0004
FROM_LEFT_3RD_BUTTON_PRESSED    =0x0008
FROM_LEFT_4TH_BUTTON_PRESSED    =0x0010

MOUSE_MOVED                     =0x0001
DOUBLE_CLICK                    =0x0002
MOUSE_WHEELED                   =0x0004
MOUSE_HWHEELED                  =0x0008

KEY_EVENT                       =0x0001 #// Event contains key event record
MOUSE_EVENT                     =0x0002 #// Event contains mouse event record
WINDOW_BUFFER_SIZE_EVENT        =0x0004 #// Event contains window change event record
MENU_EVENT                      =0x0008 #// Event contains menu event record
FOCUS_EVENT                     =0x0010 #// event contains focus change
BRACKETED_PASTE_EVENT           =0x0020 #// event contains bracketed paste state change
CALLBACK_EVENT                  =0x0040 #// callback to be invoked when its record dequeued, its translated into NOOP_EVENT when invoked
NOOP_EVENT                      =0x0080 #// nothing interesting, typically injected to kick events dispatcher

LONGLONG = c_longlong
ULONGLONG = c_ulonglong
SIZE_T = c_size_t

CCHAR = c_char
CSHORT = c_short
CLONG = c_long

PCCHAR = POINTER(CCHAR)
PCSHORT = POINTER(CSHORT)
PCLONG = POINTER(CLONG)

DWORD64 = c_longlong
PDWORD64 = POINTER(DWORD64)
INT64 = c_longlong
PINT64 = POINTER(INT64)
UINT64 = c_ulonglong
PUINT64 = POINTER(UINT64)
LONG64 = c_longlong
PLONG64 = POINTER(LONG64)
ULONG64 = c_ulonglong
PULONG64 = POINTER(ULONG64)


INT_PTR = INT64
UINT_PTR = UINT64
DWORD_PTR = DWORD64
LONG_PTR = LONG64
ULONG_PTR = ULONG64
PSTR = LPSTR

PWSTR = LPWSTR
COORD = _COORD



UCHAR = ctypes.c_ubyte
UBYTE = ctypes.c_uint8
PBYTE = POINTER(BYTE)
LPBYTE = POINTER(BYTE)


PLONGLONG = POINTER(LONGLONG)
PULONGLONG = POINTER(ULONGLONG)





#typedef struct _OVERLAPPED *LPOVERLAPPED;

ACCESS_MASK = DWORD
PACCESS_MASK = POINTER(ACCESS_MASK)
REGSAM = ACCESS_MASK

HRESULT = INT

class _FILETIME(Structure):
    _fields_ = [
        ('dwLowDateTime', DWORD),
        ('dwHighDateTime', DWORD),
    ]
FILETIME = _FILETIME
PFILETIME = LPFILETIME = POINTER(FILETIME)

class _SECURITY_ATTRIBUTES(Structure):
    _fields_ = [
    ]
LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)


class _SYSTEMTIME(Structure):
    _fields_ = [
        ('wYear', WORD),
        ('wMonth', WORD),
        ('wDayOfWeek', WORD),
        ('wDay', WORD),
        ('wHour', WORD),
        ('wMinute', WORD),
        ('wSecond', WORD),
        ('wMilliseconds', WORD),
    ]
SYSTEMTIME = _SYSTEMTIME
PSYSTEMTIME = LPSYSTEMTIME = POINTER(SYSTEMTIME)


class _WIN32_FIND_DATAA(Structure):
    _fields_ = [
        ('ftCreationTime', FILETIME),
        ('ftLastAccessTime', FILETIME),
        ('ftLastWriteTime', FILETIME),
        ('UnixOwner', c_uint32),
        ('UnixGroup', c_uint32),
        ('UnixDevice', DWORD64),
        ('UnixNode', DWORD64),
        ('nPhysicalSize', DWORD64),
        ('nFileSize', DWORD64),
        ('dwFileAttributes', DWORD),
        ('dwUnixMode', DWORD),
        ('nHardLinks', DWORD),
        ('cFileName', CHAR*255),
    ]
PWIN32_FIND_DATAA = LPWIN32_FIND_DATAA = POINTER(WIN32_FIND_DATAA)

class _WIN32_FIND_DATAW(Structure):
    _fields_ = [
        ('ftCreationTime', FILETIME),
        ('ftLastAccessTime', FILETIME),
        ('ftLastWriteTime', FILETIME),
        ('UnixOwner', c_uint32),
        ('UnixGroup', c_uint32),
        ('UnixDevice', DWORD64),
        ('UnixNode', DWORD64),
        ('nPhysicalSize', DWORD64),
        ('nFileSize', DWORD64),
        ('dwFileAttributes', DWORD),
        ('dwUnixMode', DWORD),
        ('nHardLinks', DWORD),
        ('nBlockSize', DWORD),
        ('cFileName', WCHAR*255),
    ]
PWIN32_FIND_DATAW = LPWIN32_FIND_DATAW = POINTER(_WIN32_FIND_DATAW)

WIN32_FIND_DATA = _WIN32_FIND_DATAW
PWIN32_FIND_DATA = LPWIN32_FIND_DATA = POINTER(WIN32_FIND_DATAW)

class _CONSOLE_FONT_INFO(Structure):
    _fields_ = [
        ('nFont', DWORD),
        ('dwFontSize', COORD),
    ]
CONSOLE_FONT_INFO = _CONSOLE_FONT_INFO
PCONSOLE_FONT_INFO = POINTER(CONSOLE_FONT_INFO)

class _CONSOLE_SCREEN_BUFFER_INFO(Structure):
    _fields_ = [
        ('dwSize', COORD),
        ('dwCursorPosition', COORD),
        ('wAttributes', DWORD64),
        ('srWindow', SMALL_RECT),
        ('dwMaximumWindowSize', COORD)
    ]
CONSOLE_SCREEN_BUFFER_INFO = _CONSOLE_SCREEN_BUFFER_INFO
PCONSOLE_SCREEN_BUFFER_INFO = POINTER(CONSOLE_SCREEN_BUFFER_INFO)

class _CONSOLE_CURSOR_INFO(Structure):
    _fields_ = [
        ('dwSize', DWORD),
        ('bVisible', BOOL),
    ]
CONSOLE_CURSOR_INFO = _CONSOLE_CURSOR_INFO
PCONSOLE_CURSOR_INFO = POINTER(CONSOLE_CURSOR_INFO)

COMP_CHAR = DWORD64

class _CHAR_INFO_Char(Union):
    _fields_ = [
        ('UnicodeChar', COMP_CHAR),
        ('AsciiChar', CHAR),
    ]
class _CHAR_INFO(Structure):
    _fields_ = [
        ('Char', _CHAR_INFO_Char),
        ('Attributes', DWORD64),
    ]
CHAR_INFO = _CHAR_INFO
PCHAR_INFO = POINTER(CHAR_INFO)

class _WINDOW_BUFFER_SIZE_RECORD(Structure):
    _fields_ = [
        ('dwSize', COORD),
    ]
WINDOW_BUFFER_SIZE_RECORD = _WINDOW_BUFFER_SIZE_RECORD
PWINDOW_BUFFER_SIZE_RECORD = POINTER(WINDOW_BUFFER_SIZE_RECORD)

class _MENU_EVENT_RECORD(Structure):
    _fields_ = [
        ('dwCommandId', UINT),
    ]
MENU_EVENT_RECORD = _MENU_EVENT_RECORD
PMENU_EVENT_RECORD = POINTER(MENU_EVENT_RECORD)

class _FOCUS_EVENT_RECORD(Structure):
    _fields_ = [
        ('bSetFocus', BOOL),
    ]
FOCUS_EVENT_RECORD = _FOCUS_EVENT_RECORD
PFOCUS_EVENT_RECORD = POINTER(FOCUS_EVENT_RECORD)

class _KEY_EVENT_RECORD_uChar(Union):
    _fields_ = [
        ('UnicodeChar', WCHAR),
        ('AsciiChar', CHAR),
    ]

class _KEY_EVENT_RECORD(Structure):
    _fields_ = [
        ('bKeyDown', BOOL),
        ('wRepeatCount', WORD),
        ('wVirtualKeyCode', WORD),
        ('wVirtualScanCode', WORD),
        ('uChar', _KEY_EVENT_RECORD_uChar),
        ('dwControlKeyState', DWORD),
    ]
KEY_EVENT_RECORD = _KEY_EVENT_RECORD
PKEY_EVENT_RECORD = POINTER(KEY_EVENT_RECORD)

_CALLBACK_EVENT_RECORD_Function = CFUNCTYPE(None, c_void_p)
class _CALLBACK_EVENT_RECORD(Structure):
    _fields_ = [
        ('Function', _CALLBACK_EVENT_RECORD_Function),
        ('Context', c_void_p),
    ]
CALLBACK_EVENT_RECORD = _CALLBACK_EVENT_RECORD
PCALLBACK_EVENT_RECORD = POINTER(CALLBACK_EVENT_RECORD)

class _MOUSE_EVENT_RECORD(Structure):
    _fields_ = [
        ('dwMousePosition', COORD),
        ('dwButtonState', DWORD),
        ('dwControlKeyState', DWORD),
        ('dwEventFlags', DWORD),
    ]
MOUSE_EVENT_RECORD = _MOUSE_EVENT_RECORD
PMOUSE_EVENT_RECORD = POINTER(MOUSE_EVENT_RECORD)

class _BRACKETED_PASTE(Structure):
    _fields_ = [
        ('bStartPaste', BOOL),
    ]
BRACKETED_PASTE = _BRACKETED_PASTE
PBRACKETED_PASTE = POINTER(BRACKETED_PASTE)

class _INPUT_RECORD_Event(Union):
    _fields_ = [
        ('KeyEvent', KEY_EVENT_RECORD),
        ('MouseEvent', MOUSE_EVENT_RECORD),
        ('WindowBufferSizeEvent', WINDOW_BUFFER_SIZE_RECORD),
        ('MenuEvent', MENU_EVENT_RECORD),
        ('FocusEvent', FOCUS_EVENT_RECORD),
        ('BracketedPaste', BRACKETED_PASTE),
        ('CallbackEvent', CALLBACK_EVENT_RECORD),
    ]

class _INPUT_RECORD(Structure):
    _fields_ = [
        ('EventType', WORD),
        ('Event', _INPUT_RECORD_Event),
    ]
INPUT_RECORD = _INPUT_RECORD
PINPUT_RECORD = POINTER(INPUT_RECORD)

class _UNICODE_STRING(Structure):
    _fields_ = [
        ('Length', USHORT),
        ('MaximumLength', USHORT),
        ('Buffer', PWSTR),
    ]
UNICODE_STRING = _UNICODE_STRING
PUNICODE_STRING = POINTER(UNICODE_STRING)




class _GUID(Structure):
    _fields_ = [
        ('Data1', c_uint32),
        ('Data2', c_uint16),
        ('Data3', c_uint16),
        ('Data4', c_uint8*8),
    ]
GUID = IID = _GUID

class _cpinfo(Structure):
    _fields_ = [
        ('MaxCharSize', UINT),
        ('DefaultChar', BYTE*4),
        ('LeadByte', BYTE*12),
    ]
CPINFO = _cpinfo
LPCPINFO = POINTER(CPINFO)

class _cpinfoex(Structure):
    _fields_ = [
        ('MaxCharSize', UINT),
        ('DefaultChar', BYTE*4),
        ('LeadByte', BYTE*12),
        ('UnicodeDefaultChar', WCHAR),
        ('CodePage', UINT),
        ('CodePageName', WCHAR*255),
    ]
CPINFOEX = _cpinfoex
LPCPINFOEX = POINTER(CPINFOEX)

CODEPAGE_ENUMPROCW = CFUNCTYPE(BOOL, LPWSTR)
NTSTATUS = LONG
class _nlsversioninfo(Structure):
    _fields_ = [
        ('dwNLSVersionInfoSize', DWORD),
        ('dwNLSVersion', DWORD),
        ('dwDefinedVersion', DWORD),
        ('dwEffectiveId', DWORD),
        ('guidCustomVersion', GUID),
    ]
NLSVERSIONINFO = _nlsversioninfo
LPNLSVERSIONINFO = POINTER(NLSVERSIONINFO)


LRESULT = LONG_PTR

WINPORT_THREAD_START_ROUTINE = CFUNCTYPE(DWORD, LPVOID)
WINPORT_HANDLER_ROUTINE = CFUNCTYPE(BOOL, DWORD)




PHANDLER_ROUTINE = WINPORT_HANDLER_ROUTINE
LPTHREAD_START_ROUTINE = PTHREAD_START_ROUTINE = WINPORT_THREAD_START_ROUTINE

PCONSOLE_SCROLL_CALLBACK = CFUNCTYPE(None, c_void_p, c_uint, POINTER(CHAR_INFO))

FarLangMsgID = c_int


#class FARMESSAGEFLAGS:
if 1:
	FMSG_WARNING             = 0x00000001
	FMSG_ERRORTYPE           = 0x00000002
	FMSG_KEEPBACKGROUND      = 0x00000004
	FMSG_LEFTALIGN           = 0x00000010

	FMSG_ALLINONE            = 0x00000020

	FMSG_COLOURS             = 0x00000040

	FMSG_DISPLAYNOTIFY       = 0x00000080

	FMSG_MB_OK               = 0x00010000
	FMSG_MB_OKCANCEL         = 0x00020000
	FMSG_MB_ABORTRETRYIGNORE = 0x00030000
	FMSG_MB_YESNO            = 0x00040000
	FMSG_MB_YESNOCANCEL      = 0x00050000
	FMSG_MB_RETRYCANCEL      = 0x00060000

FARAPIMESSAGE = CFUNCTYPE(c_int, INT_PTR, DWORD, POINTER(c_wchar), POINTER(c_wchar), c_int, c_int)


#class DialogItemTypes:
if 1:
	DI_TEXT        = 0
	DI_VTEXT       = 1
	DI_SINGLEBOX   = 2
	DI_DOUBLEBOX   = 3
	DI_EDIT        = 4
	DI_PSWEDIT     = 5
	DI_FIXEDIT     = 6
	DI_BUTTON      = 7
	DI_CHECKBOX    = 8
	DI_RADIOBUTTON = 9
	DI_COMBOBOX    = 10
	DI_LISTBOX     = 11
	DI_MEMOEDIT    = 12
	DI_USERCONTROL = 255

#class FarDialogItemFlags:
if 1:
	DIF_NONE                  = 0
	DIF_COLORMASK             = 0x000000ff
	DIF_SETCOLOR              = 0x00000100
	DIF_BOXCOLOR              = 0x00000200

	DIF_DEFAULT               = 0x00000200

	DIF_GROUP                 = 0x00000400
	DIF_LEFTTEXT              = 0x00000800

	DIF_FOCUS                 = 0x00000800

	DIF_MOVESELECT            = 0x00001000
	DIF_SHOWAMPERSAND         = 0x00002000
	DIF_CENTERGROUP           = 0x00004000
	DIF_NOBRACKETS            = 0x00008000
	DIF_MANUALADDHISTORY      = 0x00008000
	DIF_SEPARATOR             = 0x00010000
	DIF_SEPARATOR2            = 0x00020000
	DIF_EDITOR                = 0x00020000
	DIF_LISTNOAMPERSAND       = 0x00020000
	DIF_LISTNOBOX             = 0x00040000
	DIF_HISTORY               = 0x00040000
	DIF_BTNNOCLOSE            = 0x00040000
	DIF_CENTERTEXT            = 0x00040000

	DIF_SEPARATORUSER         = 0x00080000

	DIF_SETSHIELD             = 0x00080000
	DIF_EDITEXPAND            = 0x00080000
	DIF_DROPDOWNLIST          = 0x00100000
	DIF_USELASTHISTORY        = 0x00200000
	DIF_MASKEDIT              = 0x00400000
	DIF_SELECTONENTRY         = 0x00800000
	DIF_3STATE                = 0x00800000
	DIF_EDITPATH              = 0x01000000
	DIF_LISTWRAPMODE          = 0x01000000
	DIF_NOAUTOCOMPLETE        = 0x02000000
	DIF_LISTAUTOHIGHLIGHT     = 0x02000000
	DIF_LISTNOCLOSE           = 0x04000000

	DIF_AUTOMATION            = 0x08000000

	DIF_HIDDEN                = 0x10000000
	DIF_READONLY              = 0x20000000
	DIF_NOFOCUS               = 0x40000000
	DIF_DISABLE               = 0x80000000

#class FarMessagesProc:
if 1:
	DM_FIRST                   = 0
	DM_CLOSE                   = 1
	DM_ENABLE                  = 2
	DM_ENABLEREDRAW            = 3
	DM_GETDLGDATA              = 4
	DM_GETDLGITEM              = 5
	DM_GETDLGRECT              = 6
	DM_GETTEXT                 = 7
	DM_GETTEXTLENGTH           = 8
	DM_KEY                     = 9
	DM_MOVEDIALOG              = 10
	DM_SETDLGDATA              = 11
	DM_SETDLGITEM              = 12
	DM_SETFOCUS                = 13
	DM_REDRAW                  = 14
	DM_SETREDRAW               =DM_REDRAW
	DM_SETTEXT                 = 15
	DM_SETMAXTEXTLENGTH        = 16
	DM_SETTEXTLENGTH           = DM_SETMAXTEXTLENGTH,
	DM_SHOWDIALOG              = 17
	DM_GETFOCUS                = 18
	DM_GETCURSORPOS            = 19
	DM_SETCURSORPOS            = 20
	DM_GETTEXTPTR              = 21
	DM_SETTEXTPTR              = 22
	DM_SHOWITEM                = 23
	DM_ADDHISTORY              = 24

	DM_GETCHECK                = 25
	DM_SETCHECK                = 26
	DM_SET3STATE               = 27

	DM_LISTSORT                = 28
	DM_LISTGETITEM             = 29
	DM_LISTGETCURPOS           = 30
	DM_LISTSETCURPOS           = 31
	DM_LISTDELETE              = 32
	DM_LISTADD                 = 33
	DM_LISTADDSTR              = 34
	DM_LISTUPDATE              = 35
	DM_LISTINSERT              = 36
	DM_LISTFINDSTRING          = 37
	DM_LISTINFO                = 38
	DM_LISTGETDATA             = 39
	DM_LISTSETDATA             = 40
	DM_LISTSETTITLES           = 41
	DM_LISTGETTITLES           = 42

	DM_RESIZEDIALOG            = 43
	DM_SETITEMPOSITION         = 44

	DM_GETDROPDOWNOPENED       = 45
	DM_SETDROPDOWNOPENED       = 46

	DM_SETHISTORY              = 47

	DM_GETITEMPOSITION         = 48
	DM_SETMOUSEEVENTNOTIFY     = 49

	DM_EDITUNCHANGEDFLAG       = 50

	DM_GETITEMDATA             = 51
	DM_SETITEMDATA             = 52

	DM_LISTSET                 = 53
	DM_LISTSETMOUSEREACTION    = 54

	DM_GETCURSORSIZE           = 55
	DM_SETCURSORSIZE           = 56

	DM_LISTGETDATASIZE         = 57

	DM_GETSELECTION            = 58
	DM_SETSELECTION            = 59

	DM_GETEDITPOSITION         = 60
	DM_SETEDITPOSITION         = 61

	DM_SETCOMBOBOXEVENT        = 62
	DM_GETCOMBOBOXEVENT        = 63

	DM_GETCONSTTEXTPTR         = 64
	DM_GETDLGITEMSHORT         = 65
	DM_SETDLGITEMSHORT         = 66

	DM_GETDIALOGINFO           = 67

	DM_GETCOLOR                = 68
	DM_SETCOLOR                = 69

	DM_SETREADONLY             = 70

	DM_GETTRUECOLOR            = 71
	DM_SETTRUECOLOR            = 72


	DN_FIRST                   = 0x1000
	DN_BTNCLICK                = 0x1001
	DN_CTLCOLORDIALOG          = 0x1002
	DN_CTLCOLORDLGITEM         = 0x1003
	DN_CTLCOLORDLGLIST         = 0x1004
	DN_DRAWDIALOG              = 0x1005
	DN_DRAWDLGITEM             = 0x1006
	DN_EDITCHANGE              = 0x1007
	DN_ENTERIDLE               = 0x1008
	DN_GOTFOCUS                = 0x1009
	DN_HELP                    = 0x100a
	DN_HOTKEY                  = 0x100b
	DN_INITDIALOG              = 0x100c
	DN_KILLFOCUS               = 0x100d
	DN_LISTCHANGE              = 0x100e
	DN_MOUSECLICK              = 0x100f
	DN_DRAGGED                 = 0x1010
	DN_RESIZECONSOLE           = 0x1011
	DN_MOUSEEVENT              = 0x1012
	DN_DRAWDIALOGDONE          = 0x1013
	DN_LISTHOTKEY              = 0x1014

	DN_GETDIALOGINFO           = DM_GETDIALOGINFO

	DN_CLOSE                   = DM_CLOSE
	DN_KEY                     = DM_KEY


	DM_USER                    = 0x4000


	DM_KILLSAVESCREEN          = DN_FIRST-1
	DM_ALLKEYMODE              = DN_FIRST-2
	DN_ACTIVATEAPP             = DM_USER-1

#class FARCHECKEDSTATE:
if 1:
	BSTATE_UNCHECKED = 0
	BSTATE_CHECKED   = 1
	BSTATE_3STATE    = 2
	BSTATE_TOGGLE    = 3

#class FARLISTMOUSEREACTIONTYPE:
if 1:
	LMRT_ONLYFOCUS   = 0
	LMRT_ALWAYS      = 1
	LMRT_NEVER       = 2

#class FARCOMBOBOXEVENTTYPE:
	CBET_KEY         = 0x00000001
	CBET_MOUSE       = 0x00000002

#class LISTITEMFLAGS:
	LIF_SELECTED           = 0x00010000
	LIF_CHECKED            = 0x00020000
	LIF_SEPARATOR          = 0x00040000
	LIF_DISABLE            = 0x00080000
	LIF_GRAYED             = 0x00100000
	LIF_HIDDEN             = 0x00200000
	LIF_DELETEUSERDATA     = 0x80000000


class FarListItem(Structure):
    _fields_ = [
	   ('Flags', DWORD),
	   ('Text', POINTER(c_wchar)),
	   ('Reserved', DWORD *3),
    ]

class FarListUpdate(Structure):
    _fields_ = [
	   ('Index', c_int),
	   ('Item', FarListItem),
    ]

class FarListInsert(Structure):
    _fields_ = [
	   ('Index', c_int),
	   ('Item', FarListItem),
    ]

class FarListGetItem(Structure):
    _fields_ = [
	   ('Index', c_int),
	   ('Item', FarListItem),
    ]

class FarListPos(Structure):
    _fields_ = [
	   ('SelectPos', c_int),
	   ('TopPos', c_int),
    ]

#class FARLISTFINDFLAGS:
if 1:
	LIFIND_EXACTMATCH = 0x00000001

class FarListFind(Structure):
    _fields_ = [
	   ('StartIndex', c_int),
	   ('Pattern', POINTER(c_wchar)),
	   ('Flags', DWORD),
	   ('Reserved', DWORD),
    ]

class FarListDelete(Structure):
    _fields_ = [
	   ('StartIndex', c_int),
	   ('Count', c_int),
    ]

#class FARLISTINFOFLAGS:
if 1:
	LINFO_SHOWNOBOX             = 0x00000400
	LINFO_AUTOHIGHLIGHT         = 0x00000800
	LINFO_REVERSEHIGHLIGHT      = 0x00001000
	LINFO_WRAPMODE              = 0x00008000
	LINFO_SHOWAMPERSAND         = 0x00010000

class FarListInfo(Structure):
    _fields_ = [
	   ('Flags', DWORD),
	   ('ItemsNumber', c_int),
	   ('SelectPos', c_int),
	   ('TopPos', c_int),
	   ('MaxHeight', c_int),
	   ('MaxLength', c_int),
	   ('Reserved', DWORD*6),
    ]

class FarListItemData(Structure):
    _fields_ = [
        ('Index', c_int),
        ('DataSize', c_int),
        ('Data', c_void_p),
	    ('Reserved', DWORD),
    ]
'''
struct FarList
{
	int ItemsNumber;
	struct FarListItem *Items;
};

struct FarListTitles
{
	int   TitleLen;
	const wchar_t *Title;
	int   BottomLen;
	const wchar_t *Bottom;
};

struct FarListColors
{
	DWORD  Flags;
	DWORD  Reserved;
	int    ColorCount;
	LPBYTE Colors;
};


struct FarDialogItem
{
	int Type;
	int X1,Y1,X2,Y2;
	int Focus;
	union
	{
		DWORD_PTR Reserved;
		int Selected;
		const wchar_t *History;
		const wchar_t *Mask;
		struct FarList *ListItems;
		int  ListPos;
		CHAR_INFO *VBuf;
	}

	Param

	;
	DWORD Flags;
	int DefaultButton;

	const wchar_t *PtrData;
	size_t MaxLen;
};

struct FarDialogItemData
{
	size_t  PtrLength;
	wchar_t *PtrData;
};

struct FarDialogEvent
{
	HANDLE hDlg;
	int Msg;
	int Param1;
	LONG_PTR Param2;
	LONG_PTR Result;
};

struct OpenDlgPluginData
{
	int ItemNumber;
	HANDLE hDlg;
};

struct DialogInfo
{
	int StructSize;
	GUID Id;
};
//#line 611 "../../far2l/far2sdk/farplug-wide.h"
enum FARDIALOGFLAGS
{
	FDLG_WARNING             = 0x00000001,
	FDLG_SMALLDIALOG         = 0x00000002,
	FDLG_NODRAWSHADOW        = 0x00000004,
	FDLG_NODRAWPANEL         = 0x00000008,

	FDLG_NONMODAL            = 0x00000010,

	FDLG_KEEPCONSOLETITLE    = 0x00000020,
	FDLG_REGULARIDLE         = 0x00000040
};

typedef LONG_PTR( *FARWINDOWPROC)(
	HANDLE   hDlg,
	int      Msg,
	int      Param1,
	LONG_PTR Param2
);

typedef LONG_PTR( *FARAPISENDDLGMESSAGE)(
	HANDLE   hDlg,
	int      Msg,
	int      Param1,
	LONG_PTR Param2
);

typedef LONG_PTR( *FARAPIDEFDLGPROC)(
	HANDLE   hDlg,
	int      Msg,
	int      Param1,
	LONG_PTR Param2
);

typedef HANDLE( *FARAPIDIALOGINIT)(
	INT_PTR               PluginNumber,
	int                   X1,
	int                   Y1,
	int                   X2,
	int                   Y2,
	const wchar_t        *HelpTopic,
	struct FarDialogItem *Item,
	unsigned int          ItemsNumber,
	DWORD                 Reserved,
	DWORD                 Flags,
	FARWINDOWPROC         DlgProc,
	LONG_PTR              Param
);

typedef int ( *FARAPIDIALOGRUN)(
	HANDLE hDlg
);

typedef void ( *FARAPIDIALOGFREE)(
	HANDLE hDlg
);

struct FarMenuItem
{
	const wchar_t *Text;
	int  Selected;
	int  Checked;
	int  Separator;
};

enum MENUITEMFLAGS
{
	MIF_NONE   = 0,
	MIF_SELECTED   = 0x00010000
	MIF_CHECKED    = 0x00020000
	MIF_SEPARATOR  = 0x00040000
	MIF_DISABLE    = 0x00080000
	MIF_GRAYED     = 0x00100000
	MIF_HIDDEN     = 0x00200000

	MIF_SUBMENU    = 0x00400000

};

struct FarMenuItemEx
{
	DWORD Flags;
	const wchar_t *Text;
	DWORD AccelKey;
	DWORD Reserved;
	DWORD_PTR UserData;
};

enum FARMENUFLAGS
{
	FMENU_SHOWAMPERSAND        = 0x00000001,
	FMENU_WRAPMODE             = 0x00000002,
	FMENU_AUTOHIGHLIGHT        = 0x00000004,
	FMENU_REVERSEAUTOHIGHLIGHT = 0x00000008,

	FMENU_SHOWNOBOX            = 0x00000010,

	FMENU_USEEXT               = 0x00000020,
	FMENU_CHANGECONSOLETITLE   = 0x00000040,
};

typedef int ( *FARAPIMENU)(
	INT_PTR             PluginNumber,
	int                 X,
	int                 Y,
	int                 MaxHeight,
	DWORD               Flags,
	const wchar_t      *Title,
	const wchar_t      *Bottom,
	const wchar_t      *HelpTopic,
	const int          *BreakKeys,
	int                *BreakCode,
	const struct FarMenuItem *Item,
	int                 ItemsNumber
);


enum PLUGINPANELITEMFLAGS
{
	PPIF_PROCESSDESCR           = 0x80000000,
	PPIF_SELECTED               = 0x40000000,
	PPIF_USERDATA               = 0x20000000,
};

struct FAR_FIND_DATA
{
	FILETIME ftCreationTime;
	FILETIME ftLastAccessTime;
	FILETIME ftLastWriteTime;
	uint64_t nPhysicalSize;
	uint64_t nFileSize;
	DWORD    dwFileAttributes;
	DWORD    dwUnixMode;

	wchar_t *lpwszFileName;



};

struct PluginPanelItem
{
	struct FAR_FIND_DATA FindData;
	DWORD_PTR     UserData;
	DWORD         Flags;
	DWORD         NumberOfLinks;
	const wchar_t *Description;
	const wchar_t *Owner;
	const wchar_t *Group;
	const wchar_t * const *CustomColumnData;
	int           CustomColumnNumber;
	DWORD         CRC32;
	DWORD_PTR     Reserved[2];
};

enum PANELINFOFLAGS
{
	PFLAGS_SHOWHIDDEN         = 0x00000001,
	PFLAGS_HIGHLIGHT          = 0x00000002,
	PFLAGS_REVERSESORTORDER   = 0x00000004,
	PFLAGS_USESORTGROUPS      = 0x00000008,
	PFLAGS_SELECTEDFIRST      = 0x00000010,
	PFLAGS_REALNAMES          = 0x00000020,
	PFLAGS_NUMERICSORT        = 0x00000040,
	PFLAGS_PANELLEFT          = 0x00000080,
	PFLAGS_DIRECTORIESFIRST   = 0x00000100,
	PFLAGS_USECRC32           = 0x00000200,
	PFLAGS_CASESENSITIVESORT  = 0x00000400,
};

enum PANELINFOTYPE
{
	PTYPE_FILEPANEL,
	PTYPE_TREEPANEL,
	PTYPE_QVIEWPANEL,
	PTYPE_INFOPANEL
};

struct PanelInfo
{
	int PanelType;
	int Plugin;
	RECT PanelRect;
	int ItemsNumber;
	int SelectedItemsNumber;
	int CurrentItem;
	int TopPanelItem;
	int Visible;
	int Focus;
	int ViewMode;
	int SortMode;
	DWORD Flags;
	DWORD Reserved;
};


struct PanelRedrawInfo
{
	int CurrentItem;
	int TopPanelItem;
};

struct CmdLineSelect
{
	int SelStart;
	int SelEnd;
};

struct FarPanelLocation
{
	const wchar_t *PluginName;
	const wchar_t *HostFile;
	LONG_PTR Item;
	const wchar_t *Path;
};





enum FILE_CONTROL_COMMANDS
{
	FCTL_CLOSEPLUGIN,
	FCTL_GETPANELINFO,
	FCTL_UPDATEPANEL,
	FCTL_REDRAWPANEL,
	FCTL_GETCMDLINE,
	FCTL_SETCMDLINE,
	FCTL_SETSELECTION,
	FCTL_SETVIEWMODE,
	FCTL_INSERTCMDLINE,
	FCTL_SETUSERSCREEN,
	FCTL_SETPANELDIR,
	FCTL_SETCMDLINEPOS,
	FCTL_GETCMDLINEPOS,
	FCTL_SETSORTMODE,
	FCTL_SETSORTORDER,
	FCTL_GETCMDLINESELECTEDTEXT,
	FCTL_SETCMDLINESELECTION,
	FCTL_GETCMDLINESELECTION,
	FCTL_CHECKPANELSEXIST,
	FCTL_SETNUMERICSORT,
	FCTL_GETUSERSCREEN,
	FCTL_ISACTIVEPANEL,
	FCTL_GETPANELITEM,
	FCTL_GETSELECTEDPANELITEM,
	FCTL_GETCURRENTPANELITEM,
	FCTL_GETPANELDIR,
	FCTL_GETCOLUMNTYPES,
	FCTL_GETCOLUMNWIDTHS,
	FCTL_BEGINSELECTION,
	FCTL_ENDSELECTION,
	FCTL_CLEARSELECTION,
	FCTL_SETDIRECTORIESFIRST,
	FCTL_GETPANELFORMAT,
	FCTL_GETPANELHOSTFILE,
	FCTL_SETCASESENSITIVESORT,
	FCTL_GETPANELPLUGINHANDLE,
	FCTL_SETPANELLOCATION,
};

typedef int ( *FARAPICONTROL)(
	HANDLE hPlugin,
	int Command,
	int Param1,
	LONG_PTR Param2
);

typedef void ( *FARAPITEXT)(
	int X,
	int Y,
	int Color,
	const wchar_t *Str
);

typedef HANDLE( *FARAPISAVESCREEN)(int X1, int Y1, int X2, int Y2);

typedef void ( *FARAPIRESTORESCREEN)(HANDLE hScreen);


typedef int ( *FARAPIGETDIRLIST)(
	const wchar_t *Dir,
	struct FAR_FIND_DATA **pPanelItem,
	int *pItemsNumber
);

typedef int ( *FARAPIGETPLUGINDIRLIST)(
	INT_PTR PluginNumber,
	HANDLE hPlugin,
	const wchar_t *Dir,
	struct PluginPanelItem **pPanelItem,
	int *pItemsNumber
);

typedef void ( *FARAPIFREEDIRLIST)(struct FAR_FIND_DATA *PanelItem, int nItemsNumber);
typedef void ( *FARAPIFREEPLUGINDIRLIST)(struct PluginPanelItem *PanelItem, int nItemsNumber);

enum VIEWER_FLAGS
{
	VF_NONMODAL              = 0x00000001,
	VF_DELETEONCLOSE         = 0x00000002,
	VF_ENABLE_F6             = 0x00000004,
	VF_DISABLEHISTORY        = 0x00000008,
	VF_IMMEDIATERETURN       = 0x00000100,
	VF_DELETEONLYFILEONCLOSE = 0x00000200,
};

typedef int ( *FARAPIVIEWER)(
	const wchar_t *FileName,
	const wchar_t *Title,
	int X1,
	int Y1,
	int X2,
	int Y2,
	DWORD Flags,
	UINT CodePage
);

enum EDITOR_FLAGS
{
	EF_NONMODAL              = 0x00000001,
	EF_CREATENEW             = 0x00000002,
	EF_ENABLE_F6             = 0x00000004,
	EF_DISABLEHISTORY        = 0x00000008,
	EF_DELETEONCLOSE         = 0x00000010,
	EF_IMMEDIATERETURN       = 0x00000100,
	EF_DELETEONLYFILEONCLOSE = 0x00000200,

	EF_LOCKED                = 0x00000400,

	EF_OPENMODE_MASK         = 0xF0000000,
	EF_OPENMODE_NEWIFOPEN    = 0x10000000,
	EF_OPENMODE_USEEXISTING  = 0x20000000,
	EF_OPENMODE_BREAKIFOPEN  = 0x30000000,
	EF_OPENMODE_RELOADIFOPEN = 0x40000000,


	EF_SERVICEREGION         = 0x00001000,

};

enum EDITOR_EXITCODE
{
	EEC_OPEN_ERROR          = 0,
	EEC_MODIFIED            = 1,
	EEC_NOT_MODIFIED        = 2,
	EEC_LOADING_INTERRUPTED = 3,

	EEC_OPENED_EXISTING     = 4,
	EEC_ALREADY_EXISTS      = 5,
	EEC_OPEN_NEWINSTANCE    = 6,
	EEC_RELOAD              = 7,

};

typedef int ( *FARAPIEDITOR)(
	const wchar_t *FileName,
	const wchar_t *Title,
	int X1,
	int Y1,
	int X2,
	int Y2,
	DWORD Flags,
	int StartLine,
	int StartChar,
	UINT CodePage
);

typedef int ( *FARAPICMPNAME)(
	const wchar_t *Pattern,
	const wchar_t *String,
	int SkipPath
);


typedef const wchar_t*( *FARAPIGETMSG)(
	INT_PTR PluginNumber,
	FarLangMsgID MsgId
);


enum FarHelpFlags
{
	FHELP_NOSHOWERROR = 0x80000000,
	FHELP_SELFHELP    = 0x00000000,
	FHELP_FARHELP     = 0x00000001,
	FHELP_CUSTOMFILE  = 0x00000002,
	FHELP_CUSTOMPATH  = 0x00000004,
	FHELP_USECONTENTS = 0x40000000,
};

typedef BOOL ( *FARAPISHOWHELP)(
	const wchar_t *ModuleName,
	const wchar_t *Topic,
	DWORD Flags
);

enum ADVANCED_CONTROL_COMMANDS
{
	ACTL_GETFARVERSION        = 0,



	ACTL_GETSYSWORDDIV        = 2,
	ACTL_WAITKEY              = 3,
	ACTL_GETCOLOR             = 4,
	ACTL_GETARRAYCOLOR        = 5,
	ACTL_EJECTMEDIA           = 6,
	ACTL_KEYMACRO             = 7,
	ACTL_POSTKEYSEQUENCE      = 8,
	ACTL_GETWINDOWINFO        = 9,
	ACTL_GETWINDOWCOUNT       = 10,
	ACTL_SETCURRENTWINDOW     = 11,
	ACTL_COMMIT               = 12,
	ACTL_GETFARHWND           = 13,
	ACTL_GETSYSTEMSETTINGS    = 14,
	ACTL_GETPANELSETTINGS     = 15,
	ACTL_GETINTERFACESETTINGS = 16,
	ACTL_GETCONFIRMATIONS     = 17,
	ACTL_GETDESCSETTINGS      = 18,
	ACTL_SETARRAYCOLOR        = 19,



	ACTL_GETPLUGINMAXREADDATA = 21,
	ACTL_GETDIALOGSETTINGS    = 22,
	ACTL_GETSHORTWINDOWINFO   = 23,

	ACTL_REMOVEMEDIA          = 24,
	ACTL_GETMEDIATYPE         = 25,
	ACTL_GETPOLICIES          = 26,

	ACTL_REDRAWALL            = 27,
	ACTL_SYNCHRO              = 28,
	ACTL_SETPROGRESSSTATE     = 29,
	ACTL_SETPROGRESSVALUE     = 30,
	ACTL_QUIT                 = 31,
	ACTL_GETFARRECT           = 32,
	ACTL_GETCURSORPOS         = 33,
	ACTL_SETCURSORPOS         = 34,
	ACTL_PROGRESSNOTIFY       = 35,
};


enum FarPoliciesFlags
{
	FFPOL_MAINMENUSYSTEM        = 0x00000001,
	FFPOL_MAINMENUPANEL         = 0x00000002,
	FFPOL_MAINMENUINTERFACE     = 0x00000004,
	FFPOL_MAINMENULANGUAGE      = 0x00000008,
	FFPOL_MAINMENUPLUGINS       = 0x00000010,
	FFPOL_MAINMENUDIALOGS       = 0x00000020,
	FFPOL_MAINMENUCONFIRMATIONS = 0x00000040,
	FFPOL_MAINMENUPANELMODE     = 0x00000080,
	FFPOL_MAINMENUFILEDESCR     = 0x00000100,
	FFPOL_MAINMENUFOLDERDESCR   = 0x00000200,
	FFPOL_MAINMENUVIEWER        = 0x00000800,
	FFPOL_MAINMENUEDITOR        = 0x00001000,
	FFPOL_MAINMENUCOLORS        = 0x00004000,
	FFPOL_MAINMENUHILIGHT       = 0x00008000,
	FFPOL_MAINMENUSAVEPARAMS    = 0x00020000,

	FFPOL_CREATEMACRO           = 0x00040000,
	FFPOL_USEPSWITCH            = 0x00080000,
	FFPOL_PERSONALPATH          = 0x00100000,
	FFPOL_KILLTASK              = 0x00200000,
	FFPOL_SHOWHIDDENDRIVES      = 0x80000000,
};



enum FarSystemSettings
{
	FSS_DELETETORECYCLEBIN             = 0x00000002,
	FSS_WRITETHROUGH                   = 0x00000004,
	FSS_RESERVED                       = 0x00000008,
	FSS_SAVECOMMANDSHISTORY            = 0x00000020,
	FSS_SAVEFOLDERSHISTORY             = 0x00000040,
	FSS_SAVEVIEWANDEDITHISTORY         = 0x00000080,
	FSS_USEWINDOWSREGISTEREDTYPES      = 0x00000100,
	FSS_AUTOSAVESETUP                  = 0x00000200,
	FSS_SCANSYMLINK                    = 0x00000400,
};

enum FarPanelSettings
{
	FPS_SHOWHIDDENANDSYSTEMFILES       = 0x00000001,
	FPS_HIGHLIGHTFILES                 = 0x00000002,
	FPS_AUTOCHANGEFOLDER               = 0x00000004,
	FPS_SELECTFOLDERS                  = 0x00000008,
	FPS_ALLOWREVERSESORTMODES          = 0x00000010,
	FPS_SHOWCOLUMNTITLES               = 0x00000020,
	FPS_SHOWSTATUSLINE                 = 0x00000040,
	FPS_SHOWFILESTOTALINFORMATION      = 0x00000080,
	FPS_SHOWFREESIZE                   = 0x00000100,
	FPS_SHOWSCROLLBAR                  = 0x00000200,
	FPS_SHOWBACKGROUNDSCREENSNUMBER    = 0x00000400,
	FPS_SHOWSORTMODELETTER             = 0x00000800,
};

enum FarDialogSettings
{
	FDIS_HISTORYINDIALOGEDITCONTROLS    = 0x00000001,
	FDIS_PERSISTENTBLOCKSINEDITCONTROLS = 0x00000002,
	FDIS_AUTOCOMPLETEININPUTLINES       = 0x00000004,
	FDIS_BSDELETEUNCHANGEDTEXT          = 0x00000008,
	FDIS_DELREMOVESBLOCKS               = 0x00000010,
	FDIS_MOUSECLICKOUTSIDECLOSESDIALOG  = 0x00000020,
};

enum FarInterfaceSettings
{
	FIS_CLOCKINPANELS                  = 0x00000001,
	FIS_CLOCKINVIEWERANDEDITOR         = 0x00000002,
	FIS_MOUSE                          = 0x00000004,
	FIS_SHOWKEYBAR                     = 0x00000008,
	FIS_ALWAYSSHOWMENUBAR              = 0x00000010,
	FIS_SHOWTOTALCOPYPROGRESSINDICATOR = 0x00000100,
	FIS_SHOWCOPYINGTIMEINFO            = 0x00000200,
	FIS_USECTRLPGUPTOCHANGEDRIVE       = 0x00000800,
	FIS_SHOWTOTALDELPROGRESSINDICATOR  = 0x00001000,
};

enum FarConfirmationsSettings
{
	FCS_COPYOVERWRITE                  = 0x00000001,
	FCS_MOVEOVERWRITE                  = 0x00000002,
	FCS_DRAGANDDROP                    = 0x00000004,
	FCS_DELETE                         = 0x00000008,
	FCS_DELETENONEMPTYFOLDERS          = 0x00000010,
	FCS_INTERRUPTOPERATION             = 0x00000020,
	FCS_DISCONNECTNETWORKDRIVE         = 0x00000040,
	FCS_RELOADEDITEDFILE               = 0x00000080,
	FCS_CLEARHISTORYLIST               = 0x00000100,
	FCS_EXIT                           = 0x00000200,
	FCS_OVERWRITEDELETEROFILES         = 0x00000400,
};

enum FarDescriptionSettings
{
	FDS_UPDATEALWAYS                   = 0x00000001,
	FDS_UPDATEIFDISPLAYED              = 0x00000002,
	FDS_SETHIDDEN                      = 0x00000004,
	FDS_UPDATEREADONLY                 = 0x00000008,
};

enum FAREJECTMEDIAFLAGS
{
	EJECT_NO_MESSAGE                    = 0x00000001,
	EJECT_LOAD_MEDIA                    = 0x00000002,

	EJECT_NOTIFY_AFTERREMOVE            = 0x00000004,
	EJECT_READY                         = 0x80000000,

};

struct ActlEjectMedia
{
	DWORD Letter;
	DWORD Flags;
};


enum FARMEDIATYPE
{
	FMT_DRIVE_ERROR                =  -1,
	FMT_DRIVE_UNKNOWN              =  0,
	FMT_DRIVE_NO_ROOT_DIR          =  1,
	FMT_DRIVE_REMOVABLE            =  2,
	FMT_DRIVE_FIXED                =  3,
	FMT_DRIVE_REMOTE               =  4,
	FMT_DRIVE_CDROM                =  5,
	FMT_DRIVE_RAMDISK              =  6,
	FMT_DRIVE_SUBSTITUTE           =  15,
	FMT_DRIVE_REMOTE_NOT_CONNECTED =  16,
	FMT_DRIVE_CD_RW                =  18,
	FMT_DRIVE_CD_RWDVD             =  19,
	FMT_DRIVE_DVD_ROM              =  20,
	FMT_DRIVE_DVD_RW               =  21,
	FMT_DRIVE_DVD_RAM              =  22,
	FMT_DRIVE_USBDRIVE             =  40,
	FMT_DRIVE_NOT_INIT             = 255,
};

enum FARMEDIATYPEFLAGS
{
	MEDIATYPE_NODETECTCDROM             = 0x80000000,
};

struct ActlMediaType
{
	DWORD Letter;
	DWORD Flags;
	DWORD Reserved[2];
};


enum FARKEYSEQUENCEFLAGS
{
	KSFLAGS_DISABLEOUTPUT       = 0x00000001,
	KSFLAGS_NOSENDKEYSTOPLUGINS = 0x00000002,
	KSFLAGS_SILENTCHECK         = 0x00000001,
};

struct KeySequence
{
	DWORD Flags;
	int Count;
	const DWORD *Sequence;
};

enum FARMACROCOMMAND
{
	MCMD_LOADALL           = 0,
	MCMD_SAVEALL           = 1,
	MCMD_POSTMACROSTRING   = 2,

	MCMD_COMPILEMACRO      = 3,

	MCMD_CHECKMACRO        = 4,
	MCMD_GETSTATE          = 5,
	MCMD_GETAREA           = 6,

	MCMD_RUNMACROSTRING    = 7,

};

enum FARMACROAREA
{
	MACROAREA_OTHER             = 0,
	MACROAREA_SHELL             = 1,
	MACROAREA_VIEWER            = 2,
	MACROAREA_EDITOR            = 3,
	MACROAREA_DIALOG            = 4,
	MACROAREA_SEARCH            = 5,
	MACROAREA_DISKS             = 6,
	MACROAREA_MAINMENU          = 7,
	MACROAREA_MENU              = 8,
	MACROAREA_HELP              = 9,
	MACROAREA_INFOPANEL         =10,
	MACROAREA_QVIEWPANEL        =11,
	MACROAREA_TREEPANEL         =12,
	MACROAREA_FINDFOLDER        =13,
	MACROAREA_USERMENU          =14,
	MACROAREA_AUTOCOMPLETION    =15,
};

enum FARMACROSTATE
{
	MACROSTATE_NOMACRO          = 0,
	MACROSTATE_EXECUTING        = 1,
	MACROSTATE_EXECUTING_COMMON = 2,
	MACROSTATE_RECORDING        = 3,
	MACROSTATE_RECORDING_COMMON = 4,
};

enum FARMACROPARSEERRORCODE
{
	MPEC_SUCCESS                = 0,
	MPEC_UNRECOGNIZED_KEYWORD   = 1,
	MPEC_UNRECOGNIZED_FUNCTION  = 2,
	MPEC_FUNC_PARAM             = 3,
	MPEC_NOT_EXPECTED_ELSE      = 4,
	MPEC_NOT_EXPECTED_END       = 5,
	MPEC_UNEXPECTED_EOS         = 6,
	MPEC_EXPECTED_TOKEN         = 7,
	MPEC_BAD_HEX_CONTROL_CHAR   = 8,
	MPEC_BAD_CONTROL_CHAR       = 9,
	MPEC_VAR_EXPECTED           =10,
	MPEC_EXPR_EXPECTED          =11,
	MPEC_ZEROLENGTHMACRO        =12,
	MPEC_INTPARSERERROR         =13,
	MPEC_CONTINUE_OTL           =14,
};

struct MacroParseResult
{
	DWORD ErrCode;
	COORD ErrPos;
	const wchar_t *ErrSrc;
};

struct ActlKeyMacro
{
	int Command;
	union
	{
		struct
		{
			const wchar_t *SequenceText;
			DWORD Flags;
			DWORD AKey;
		} PlainText;

		struct KeySequence Compile;

		struct MacroParseResult MacroResult;
		DWORD_PTR Reserved[3];
	} Param;
};



enum FARMACROVARTYPE
{
	FMVT_INTEGER                = 0,
	FMVT_STRING                 = 1,
	FMVT_DOUBLE                 = 2,
};

struct FarMacroValue
{
	enum FARMACROVARTYPE type;
	union
	{
		int64_t  i;
		double   d;
		const wchar_t *s;
	} v;
};

struct FarMacroFunction
{
	DWORD Flags;
	const wchar_t *Name;
	int nParam;
	int oParam;
	const wchar_t *Syntax;
	const wchar_t *Description;
};



enum FARCOLORFLAGS
{
	FCLR_REDRAW                 = 0x00000001,
};

struct FarSetColors
{
	DWORD Flags;
	int StartIndex;
	int ColorCount;
	LPBYTE Colors;
};

struct FarTrueColor
{
	unsigned char R;
	unsigned char G;
	unsigned char B;
	unsigned char Flags;
};

struct FarTrueColorForeAndBack
{
	struct FarTrueColor Fore;
	struct FarTrueColor Back;
};

struct DialogItemTrueColors
{
	struct FarTrueColorForeAndBack Normal;
	struct FarTrueColorForeAndBack Hilighted;
	struct FarTrueColorForeAndBack Frame;
	struct FarTrueColorForeAndBack Reserved;
};

enum WINDOWINFO_TYPE
{

	WTYPE_VIRTUAL,




	WTYPE_PANELS=1,
	WTYPE_VIEWER,
	WTYPE_EDITOR,
	WTYPE_DIALOG,
	WTYPE_VMENU,
	WTYPE_HELP,

	WTYPE_COMBOBOX,
	WTYPE_FINDFOLDER,
	WTYPE_USER,

};

struct WindowInfo
{
	int  Pos;
	int  Type;
	int  Modified;
	int  Current;
	wchar_t *TypeName;
	int TypeNameSize;
	wchar_t *Name;
	int NameSize;
};

enum PROGRESSTATE
{
	PGS_NOPROGRESS   =0x0,
	PGS_INDETERMINATE=0x1,
	PGS_NORMAL       =0x2,
	PGS_ERROR        =0x4,
	PGS_PAUSED       =0x8,
};

struct PROGRESSVALUE
{
	uint64_t Completed;
	uint64_t Total;
};

typedef INT_PTR( *FARAPIADVCONTROL)(
	INT_PTR ModuleNumber,
	int Command,
	void *Param
);


enum VIEWER_CONTROL_COMMANDS
{
	VCTL_GETINFO,
	VCTL_QUIT,
	VCTL_REDRAW,
	VCTL_SETKEYBAR,
	VCTL_SETPOSITION,
	VCTL_SELECT,
	VCTL_SETMODE,
};

enum VIEWER_OPTIONS
{
	VOPT_SAVEFILEPOSITION=1,
	VOPT_AUTODETECTCODEPAGE=2,
};

enum VIEWER_SETMODE_TYPES
{
	VSMT_HEX,
	VSMT_WRAP,
	VSMT_WORDWRAP,
};

enum VIEWER_SETMODEFLAGS_TYPES
{
	VSMFL_REDRAW    = 0x00000001,
};

struct ViewerSetMode
{
	int Type;
	union
	{
		int iParam;
		wchar_t *wszParam;
	} Param;
	DWORD Flags;
	DWORD Reserved;
};

struct ViewerSelect
{
	int64_t BlockStartPos;
	int     BlockLen;
};

enum VIEWER_SETPOS_FLAGS
{
	VSP_NOREDRAW    = 0x0001,
	VSP_PERCENT     = 0x0002,
	VSP_RELATIVE    = 0x0004,
	VSP_NORETNEWPOS = 0x0008,
};

struct ViewerSetPosition
{
	DWORD Flags;
	int64_t StartPos;
	int64_t LeftPos;
};

struct ViewerMode
{
	UINT CodePage;
	int Wrap;
	int WordWrap;
	int Hex;
	int Processed;
	DWORD Reserved[3];
};

struct ViewerInfo
{
	int    StructSize;
	int    ViewerID;
	const wchar_t *FileName;
	int64_t FileSize;
	int64_t FilePos;
	int    WindowSizeX;
	int    WindowSizeY;
	DWORD  Options;
	int    TabSize;
	struct ViewerMode CurMode;
	int64_t LeftPos;
};

typedef int ( *FARAPIVIEWERCONTROL)(
	int Command,
	void *Param
);

enum VIEWER_EVENTS
{
	VE_READ       =0,
	VE_CLOSE      =1,

	VE_GOTFOCUS   =6,
	VE_KILLFOCUS  =7,
};


enum EDITOR_EVENTS
{
	EE_READ       =0,
	EE_SAVE       =1,
	EE_REDRAW     =2,
	EE_CLOSE      =3,

	EE_GOTFOCUS   =6,
	EE_KILLFOCUS  =7,
};

enum DIALOG_EVENTS
{
	DE_DLGPROCINIT    =0,
	DE_DEFDLGPROCINIT =1,
	DE_DLGPROCEND     =2,
};

enum SYNCHRO_EVENTS
{
	SE_COMMONSYNCHRO  =0,
};





enum EDITOR_CONTROL_COMMANDS
{
	ECTL_GETSTRING,
	ECTL_SETSTRING,
	ECTL_INSERTSTRING,
	ECTL_DELETESTRING,
	ECTL_DELETECHAR,
	ECTL_INSERTTEXT,
	ECTL_GETINFO,
	ECTL_SETPOSITION,
	ECTL_SELECT,
	ECTL_REDRAW,
	ECTL_TABTOREAL,
	ECTL_REALTOTAB,
	ECTL_EXPANDTABS,
	ECTL_SETTITLE,
	ECTL_READINPUT,
	ECTL_PROCESSINPUT,
	ECTL_ADDCOLOR,
	ECTL_GETCOLOR,
	ECTL_SAVEFILE,
	ECTL_QUIT,
	ECTL_SETKEYBAR,
	ECTL_PROCESSKEY,
	ECTL_SETPARAM,
	ECTL_GETBOOKMARKS,
	ECTL_TURNOFFMARKINGBLOCK,
	ECTL_DELETEBLOCK,
	ECTL_ADDSTACKBOOKMARK,
	ECTL_PREVSTACKBOOKMARK,
	ECTL_NEXTSTACKBOOKMARK,
	ECTL_CLEARSTACKBOOKMARKS,
	ECTL_DELETESTACKBOOKMARK,
	ECTL_GETSTACKBOOKMARKS,
	ECTL_UNDOREDO,
	ECTL_GETFILENAME,
	ECTL_ADDTRUECOLOR,
	ECTL_GETTRUECOLOR,
};
//#line 1606 "../../far2l/far2sdk/farplug-wide.h"
enum EDITOR_SETPARAMETER_TYPES
{
	ESPT_TABSIZE,
	ESPT_EXPANDTABS,
	ESPT_AUTOINDENT,
	ESPT_CURSORBEYONDEOL,
	ESPT_CHARCODEBASE,
	ESPT_CODEPAGE,
	ESPT_SAVEFILEPOSITION,
	ESPT_LOCKMODE,
	ESPT_SETWORDDIV,
	ESPT_GETWORDDIV,
	ESPT_SHOWWHITESPACE,
	ESPT_SETBOM,
};


struct EditorServiceRegion
{
	int Command;
	DWORD Flags;
};



struct EditorSetParameter
{
	int Type;
	union
	{
		int iParam;
		wchar_t *wszParam;
		DWORD Reserved1;
	} Param;
	DWORD Flags;
	DWORD Size;
};


enum EDITOR_UNDOREDO_COMMANDS
{
	EUR_BEGIN,
	EUR_END,
	EUR_UNDO,
	EUR_REDO
};


struct EditorUndoRedo
{
	int Command;
	DWORD_PTR Reserved[3];
};

struct EditorGetString
{
	int StringNumber;

	wchar_t *StringText;
	wchar_t *StringEOL;




	int StringLength;
	int SelStart;
	int SelEnd;
};


struct EditorSetString
{
	int StringNumber;
	const wchar_t *StringText;
	const wchar_t *StringEOL;
	int StringLength;
};

enum EXPAND_TABS
{
	EXPAND_NOTABS,
	EXPAND_ALLTABS,
	EXPAND_NEWTABS
};


enum EDITOR_OPTIONS
{
	EOPT_EXPANDALLTABS     = 0x00000001,
	EOPT_PERSISTENTBLOCKS  = 0x00000002,
	EOPT_DELREMOVESBLOCKS  = 0x00000004,
	EOPT_AUTOINDENT        = 0x00000008,
	EOPT_SAVEFILEPOSITION  = 0x00000010,
	EOPT_AUTODETECTCODEPAGE= 0x00000020,
	EOPT_CURSORBEYONDEOL   = 0x00000040,
	EOPT_EXPANDONLYNEWTABS = 0x00000080,
	EOPT_SHOWWHITESPACE    = 0x00000100,
	EOPT_BOM               = 0x00000200,
};


enum EDITOR_BLOCK_TYPES
{
	BTYPE_NONE,
	BTYPE_STREAM,
	BTYPE_COLUMN
};

enum EDITOR_CURRENTSTATE
{
	ECSTATE_MODIFIED       = 0x00000001,
	ECSTATE_SAVED          = 0x00000002,
	ECSTATE_LOCKED         = 0x00000004,
};


struct EditorInfo
{
	int EditorID;
	int WindowSizeX;
	int WindowSizeY;
	int TotalLines;
	int CurLine;
	int CurPos;
	int CurTabPos;
	int TopScreenLine;
	int LeftPos;
	int Overtype;
	int BlockType;
	int BlockStartLine;
	DWORD Options;
	int TabSize;
	int BookMarkCount;
	DWORD CurState;
	UINT CodePage;
	DWORD Reserved[5];
};

struct EditorBookMarks
{
	long *Line;
	long *Cursor;
	long *ScreenLine;
	long *LeftPos;
	DWORD Reserved[4];
};

struct EditorSetPosition
{
	int CurLine;
	int CurPos;
	int CurTabPos;
	int TopScreenLine;
	int LeftPos;
	int Overtype;
};


struct EditorSelect
{
	int BlockType;
	int BlockStartLine;
	int BlockStartPos;
	int BlockWidth;
	int BlockHeight;
};


struct EditorConvertPos
{
	int StringNumber;
	int SrcPos;
	int DestPos;
};


enum EDITORCOLORFLAGS
{
	ECF_TAB1 = 0x10000,
};

struct EditorColor
{
	int StringNumber;
	int ColorItem;
	int StartPos;
	int EndPos;
	int Color;
};

struct EditorTrueColor
{
	struct EditorColor Base;
	struct FarTrueColorForeAndBack TrueColor;
};

struct EditorSaveFile
{
	const wchar_t *FileName;
	const wchar_t *FileEOL;
	UINT CodePage;
};

typedef int ( *FARAPIEDITORCONTROL)(
	int Command,
	void *Param
);

enum INPUTBOXFLAGS
{
	FIB_ENABLEEMPTY      = 0x00000001,
	FIB_PASSWORD         = 0x00000002,
	FIB_EXPANDENV        = 0x00000004,
	FIB_NOUSELASTHISTORY = 0x00000008,
	FIB_BUTTONS          = 0x00000010,
	FIB_NOAMPERSAND      = 0x00000020,

	FIB_CHECKBOX         = 0x00010000,

	FIB_EDITPATH         = 0x01000000,
};

typedef int ( *FARAPIINPUTBOX)(
	const wchar_t *Title,
	const wchar_t *SubTitle,
	const wchar_t *HistoryName,
	const wchar_t *SrcText,
	wchar_t *DestText,
	int   DestLength,
	const wchar_t *HelpTopic,
	DWORD Flags
);

typedef int ( *FARAPIPLUGINSCONTROL)(
	HANDLE hHandle,
	int Command,
	int Param1,
	LONG_PTR Param2
);

typedef int ( *FARAPIFILEFILTERCONTROL)(
	HANDLE hHandle,
	int Command,
	int Param1,
	LONG_PTR Param2
);

typedef int ( *FARAPIREGEXPCONTROL)(
	HANDLE hHandle,
	int Command,
	LONG_PTR Param
);


typedef int ( *FARSTDSNPRINTF)(wchar_t *Buffer,size_t Sizebuf,const wchar_t *Format,...);
typedef int ( *FARSTDSSCANF)(const wchar_t *Buffer, const wchar_t *Format,...);

typedef void ( *FARSTDQSORT)(void *base, size_t nelem, size_t width, int ( *fcmp)(const void *, const void *));
typedef void ( *FARSTDQSORTEX)(void *base, size_t nelem, size_t width, int ( *fcmp)(const void *, const void *,void *userparam),void *userparam);
typedef void   *( *FARSTDBSEARCH)(const void *key, const void *base, size_t nelem, size_t width, int ( *fcmp)(const void *, const void *));
typedef int ( *FARSTDGETFILEOWNER)(const wchar_t *Computer,const wchar_t *Name,wchar_t *Owner,int Size);
typedef int ( *FARSTDGETNUMBEROFLINKS)(const wchar_t *Name);
typedef int ( *FARSTDATOI)(const wchar_t *s);
typedef int64_t ( *FARSTDATOI64)(const wchar_t *s);
typedef wchar_t   *( *FARSTDITOA64)(int64_t value, wchar_t *string, int radix);
typedef wchar_t   *( *FARSTDITOA)(int value, wchar_t *string, int radix);
typedef wchar_t   *( *FARSTDLTRIM)(wchar_t *Str);
typedef wchar_t   *( *FARSTDRTRIM)(wchar_t *Str);
typedef wchar_t   *( *FARSTDTRIM)(wchar_t *Str);

typedef wchar_t   *( *FARSTDTRUNCSTR)(wchar_t *Str,int MaxCells);
typedef wchar_t   *( *FARSTDTRUNCPATHSTR)(wchar_t *Str,int MaxCells);
typedef wchar_t   *( *FARSTDQUOTESPACEONLY)(wchar_t *Str);
typedef const wchar_t*( *FARSTDPOINTTONAME)(const wchar_t *Path);
typedef int ( *FARSTDGETPATHROOT)(const wchar_t *Path,wchar_t *Root, int DestSize);
typedef BOOL ( *FARSTDADDENDSLASH)(wchar_t *Path);
typedef int ( *FARSTDCOPYTOCLIPBOARD)(const wchar_t *Data);
typedef wchar_t *( *FARSTDPASTEFROMCLIPBOARD)(void);
typedef int ( *FARSTDINPUTRECORDTOKEY)(const INPUT_RECORD *r);
typedef int ( *FARSTDLOCALISLOWER)(wchar_t Ch);
typedef int ( *FARSTDLOCALISUPPER)(wchar_t Ch);
typedef int ( *FARSTDLOCALISALPHA)(wchar_t Ch);
typedef int ( *FARSTDLOCALISALPHANUM)(wchar_t Ch);
typedef wchar_t ( *FARSTDLOCALUPPER)(wchar_t LowerChar);
typedef wchar_t ( *FARSTDLOCALLOWER)(wchar_t UpperChar);
typedef void ( *FARSTDLOCALUPPERBUF)(wchar_t *Buf,int Length);
typedef void ( *FARSTDLOCALLOWERBUF)(wchar_t *Buf,int Length);
typedef void ( *FARSTDLOCALSTRUPR)(wchar_t *s1);
typedef void ( *FARSTDLOCALSTRLWR)(wchar_t *s1);
typedef int ( *FARSTDLOCALSTRICMP)(const wchar_t *s1,const wchar_t *s2);
typedef int ( *FARSTDLOCALSTRNICMP)(const wchar_t *s1,const wchar_t *s2,int n);

enum PROCESSNAME_FLAGS
{
	PN_CMPNAME      = 0x00000000
	PN_CMPNAMELIST  = 0x00010000
	PN_GENERATENAME = 0x00020000
	PN_SKIPPATH     = 0x01000000
};

typedef int ( *FARSTDPROCESSNAME)(const wchar_t *param1, wchar_t *param2, DWORD size, DWORD flags);

typedef void ( *FARSTDUNQUOTE)(wchar_t *Str);

enum XLATMODE
{
	XLAT_SWITCHKEYBLAYOUT  = 0x00000001
	XLAT_SWITCHKEYBBEEP    = 0x00000002
	XLAT_USEKEYBLAYOUTNAME = 0x00000004
	XLAT_CONVERTALLCMDLINE = 0x00010000
};

typedef size_t ( *FARSTDKEYTOKEYNAME)(int Key,wchar_t *KeyText,size_t Size);

typedef wchar_t*( *FARSTDXLAT)(wchar_t *Line,int StartPos,int EndPos,DWORD Flags);

typedef int ( *FARSTDKEYNAMETOKEY)(const wchar_t *Name);

typedef int ( *FRSUSERFUNC)(
	const struct FAR_FIND_DATA *FData,
	const wchar_t *FullName,
	void *Param
);

enum FRSMODE
{
	FRS_RETUPDIR             = 0x01,
	FRS_RECUR                = 0x02,
	FRS_SCANSYMLINK          = 0x04,
};

typedef void ( *FARSTDRECURSIVESEARCH)(const wchar_t *InitDir,const wchar_t *Mask,FRSUSERFUNC Func,DWORD Flags,void *Param);
typedef int ( *FARSTDMKTEMP)(wchar_t *Dest, DWORD size, const wchar_t *Prefix);
typedef void ( *FARSTDDELETEBUFFER)(void *Buffer);

enum MKLINKOP
{
	FLINK_HARDLINK         = 1,
	FLINK_JUNCTION         = 2,
	FLINK_VOLMOUNT         = 3,
	FLINK_SYMLINKFILE      = 4,
	FLINK_SYMLINKDIR       = 5,
	FLINK_SYMLINK          = 6,

	FLINK_SHOWERRMSG       = 0x10000,
	FLINK_DONOTUPDATEPANEL = 0x20000,
};
typedef int ( *FARSTDMKLINK)(const wchar_t *Src,const wchar_t *Dest,DWORD Flags);
typedef int ( *FARGETREPARSEPOINTINFO)(const wchar_t *Src, wchar_t *Dest,int DestSize);

enum CONVERTPATHMODES
{
	CPM_FULL,
	CPM_REAL,
	CPM_NATIVE,
};

typedef int ( *FARCONVERTPATH)(enum CONVERTPATHMODES Mode, const wchar_t *Src, wchar_t *Dest, int DestSize);

typedef DWORD ( *FARGETCURRENTDIRECTORY)(DWORD Size,wchar_t* Buffer);


enum EXECUTEFLAGS
{
	EF_HIDEOUT = 0x01,
	EF_NOWAIT = 0x02,
	EF_SUDO = 0x04,
	EF_NOTIFY = 0x08,
	EF_NOCMDPRINT = 0x10,
	EF_OPEN = 0x20
};

typedef int ( *FAREXECUTE)(const wchar_t *CmdStr, unsigned int ExecFlags);
typedef int ( *FAREXECUTE_LIBRARY)(const wchar_t *Library, const wchar_t *Symbol, const wchar_t *CmdStr, unsigned int ExecFlags);
typedef void ( *FARDISPLAYNOTIFICATION)(const wchar_t *action, const wchar_t *object);
typedef int ( *FARDISPATCHNTRTHRDCALLS)();



typedef void ( *FARBACKGROUNDTASK)(const wchar_t *Info, BOOL Started);

typedef size_t ( *FARSTRCELLSCOUNT)(const wchar_t *Str, size_t CharsCount);
//#line 1996 "../../far2l/far2sdk/farplug-wide.h"
typedef size_t ( *FARSTRSIZEOFCELLS)(const wchar_t *Str, size_t CharsCount, size_t *CellsCount, BOOL RoundUp);

enum BOX_DEF_SYMBOLS
{
	BS_X_B0,
	BS_X_B1,
	BS_X_B2,
	BS_V1,
	BS_R_H1V1,
	BS_R_H2V1,
	BS_R_H1V2,
	BS_RT_H1V2,
	BS_RT_H2V1,
	BS_R_H2V2,
	BS_V2,
	BS_RT_H2V2,
	BS_RB_H2V2,
	BS_RB_H1V2,
	BS_RB_H2V1,
	BS_RT_H1V1,
	BS_LB_H1V1,
	BS_B_H1V1,
	BS_T_H1V1,
	BS_L_H1V1,
	BS_H1,
	BS_C_H1V1,
	BS_L_H2V1,
	BS_L_H1V2,
	BS_LB_H2V2,
	BS_LT_H2V2,
	BS_B_H2V2,
	BS_T_H2V2,
	BS_L_H2V2,
	BS_H2,
	BS_C_H2V2,
	BS_B_H2V1,
	BS_B_H1V2,
	BS_T_H2V1,
	BS_T_H1V2,
	BS_LB_H1V2,
	BS_LB_H2V1,
	BS_LT_H2V1,
	BS_LT_H1V2,
	BS_C_H1V2,
	BS_C_H2V1,
	BS_RB_H1V1,
	BS_LT_H1V1,
	BS_X_DB,
	BS_X_DC,
	BS_X_DD,
	BS_X_DE,
	BS_X_DF,
};


typedef struct FarStandardFunctions
{
	int StructSize;

	FARSTDATOI                 atoi;
	FARSTDATOI64               atoi64;
	FARSTDITOA                 itoa;
	FARSTDITOA64               itoa64;

	FARSTDSSCANF               sscanf;

	FARSTDQSORT                qsort;
	FARSTDBSEARCH              bsearch;
	FARSTDQSORTEX              qsortex;

	FARSTDSNPRINTF             snprintf;


	DWORD_PTR                  Reserved[7];
	const WCHAR *              BoxSymbols;

	FARSTDLOCALISLOWER         LIsLower;
	FARSTDLOCALISUPPER         LIsUpper;
	FARSTDLOCALISALPHA         LIsAlpha;
	FARSTDLOCALISALPHANUM      LIsAlphanum;
	FARSTDLOCALUPPER           LUpper;
	FARSTDLOCALLOWER           LLower;
	FARSTDLOCALUPPERBUF        LUpperBuf;
	FARSTDLOCALLOWERBUF        LLowerBuf;
	FARSTDLOCALSTRUPR          LStrupr;
	FARSTDLOCALSTRLWR          LStrlwr;
	FARSTDLOCALSTRICMP         LStricmp;
	FARSTDLOCALSTRNICMP        LStrnicmp;

	FARSTDUNQUOTE              Unquote;
	FARSTDLTRIM                LTrim;
	FARSTDRTRIM                RTrim;
	FARSTDTRIM                 Trim;
	FARSTDTRUNCSTR             TruncStr;
	FARSTDTRUNCPATHSTR         TruncPathStr;
	FARSTDQUOTESPACEONLY       QuoteSpaceOnly;
	FARSTDPOINTTONAME          PointToName;
	FARSTDGETPATHROOT          GetPathRoot;
	FARSTDADDENDSLASH          AddEndSlash;
	FARSTDCOPYTOCLIPBOARD      CopyToClipboard;
	FARSTDPASTEFROMCLIPBOARD   PasteFromClipboard;
	FARSTDKEYTOKEYNAME         FarKeyToName;
	FARSTDKEYNAMETOKEY         FarNameToKey;
	FARSTDINPUTRECORDTOKEY     FarInputRecordToKey;
	FARSTDXLAT                 XLat;
	FARSTDGETFILEOWNER         GetFileOwner;
	FARSTDGETNUMBEROFLINKS     GetNumberOfLinks;
	FARSTDRECURSIVESEARCH      FarRecursiveSearch;
	FARSTDMKTEMP               MkTemp;
	FARSTDDELETEBUFFER         DeleteBuffer;
	FARSTDPROCESSNAME          ProcessName;
	FARSTDMKLINK               MkLink;
	FARCONVERTPATH             ConvertPath;
	FARGETREPARSEPOINTINFO     GetReparsePointInfo;
	FARGETCURRENTDIRECTORY     GetCurrentDirectory;
	FAREXECUTE                 Execute;
	FAREXECUTE_LIBRARY         ExecuteLibrary;
	FARDISPLAYNOTIFICATION     DisplayNotification;
	FARDISPATCHNTRTHRDCALLS    DispatchInterThreadCalls;
	FARBACKGROUNDTASK          BackgroundTask;
	FARSTRCELLSCOUNT           StrCellsCount;
	FARSTRSIZEOFCELLS          StrSizeOfCells;
} FARSTANDARDFUNCTIONS;

struct PluginStartupInfo
{
	int StructSize;
	const wchar_t *ModuleName;
	INT_PTR ModuleNumber;
	const wchar_t *RootKey;
	FARAPIMENU             Menu;
	FARAPIMESSAGE          Message;
	FARAPIGETMSG           GetMsg;
	FARAPICONTROL          Control;
	FARAPISAVESCREEN       SaveScreen;
	FARAPIRESTORESCREEN    RestoreScreen;
	FARAPIGETDIRLIST       GetDirList;
	FARAPIGETPLUGINDIRLIST GetPluginDirList;
	FARAPIFREEDIRLIST      FreeDirList;
	FARAPIFREEPLUGINDIRLIST FreePluginDirList;
	FARAPIVIEWER           Viewer;
	FARAPIEDITOR           Editor;
	FARAPICMPNAME          CmpName;
	FARAPITEXT             Text;
	FARAPIEDITORCONTROL    EditorControl;

	FARSTANDARDFUNCTIONS  *FSF;

	FARAPISHOWHELP         ShowHelp;
	FARAPIADVCONTROL       AdvControl;
	FARAPIINPUTBOX         InputBox;
	FARAPIDIALOGINIT       DialogInit;
	FARAPIDIALOGRUN        DialogRun;
	FARAPIDIALOGFREE       DialogFree;

	FARAPISENDDLGMESSAGE   SendDlgMessage;
	FARAPIDEFDLGPROC       DefDlgProc;
	DWORD_PTR              Reserved;
	FARAPIVIEWERCONTROL    ViewerControl;
	FARAPIPLUGINSCONTROL   PluginsControl;
	FARAPIFILEFILTERCONTROL FileFilterControl;
	FARAPIREGEXPCONTROL    RegExpControl;
};


enum PLUGIN_FLAGS
{
	PF_PRELOAD        = 0x0001,
	PF_DISABLEPANELS  = 0x0002,
	PF_EDITOR         = 0x0004,
	PF_VIEWER         = 0x0008,
	PF_FULLCMDLINE    = 0x0010,
	PF_DIALOG         = 0x0020,
	PF_PREOPEN        = 0x8000
};

struct PluginInfo
{
	int StructSize;
	DWORD Flags;
	const wchar_t * const *DiskMenuStrings;
	int *Reserved0;
	int DiskMenuStringsNumber;
	const wchar_t * const *PluginMenuStrings;
	int PluginMenuStringsNumber;
	const wchar_t * const *PluginConfigStrings;
	int PluginConfigStringsNumber;
	const wchar_t *CommandPrefix;

	DWORD SysID;





	int MacroFunctionNumber;
	const struct FarMacroFunction *MacroFunctions;


};



struct InfoPanelLine
{
	const wchar_t *Text;
	const wchar_t *Data;
	int  Separator;
};

struct PanelMode
{
	const wchar_t *ColumnTypes;
	const wchar_t *ColumnWidths;
	const wchar_t * const *ColumnTitles;
	int    FullScreen;
	int    DetailedStatus;
	int    AlignExtensions;
	int    CaseConversion;
	const wchar_t *StatusColumnTypes;
	const wchar_t *StatusColumnWidths;
	DWORD  Reserved[2];
};


enum OPENPLUGININFO_FLAGS
{
	OPIF_USEFILTER               = 0x00000001,
	OPIF_USESORTGROUPS           = 0x00000002,
	OPIF_USEHIGHLIGHTING         = 0x00000004,
	OPIF_ADDDOTS                 = 0x00000008,
	OPIF_RAWSELECTION            = 0x00000010,
	OPIF_REALNAMES               = 0x00000020,
	OPIF_SHOWNAMESONLY           = 0x00000040,
	OPIF_SHOWRIGHTALIGNNAMES     = 0x00000080,
	OPIF_SHOWPRESERVECASE        = 0x00000100,


	OPIF_COMPAREFATTIME          = 0x00000400,
	OPIF_EXTERNALGET             = 0x00000800,
	OPIF_EXTERNALPUT             = 0x00001000,
	OPIF_EXTERNALDELETE          = 0x00002000,
	OPIF_EXTERNALMKDIR           = 0x00004000,
	OPIF_USEATTRHIGHLIGHTING     = 0x00008000,
	OPIF_USECRC32                = 0x00010000,
};


enum OPENPLUGININFO_SORTMODES
{
	SM_DEFAULT,
	SM_UNSORTED,
	SM_NAME,
	SM_EXT,
	SM_MTIME,
	SM_CTIME,
	SM_ATIME,
	SM_SIZE,
	SM_DESCR,
	SM_OWNER,
	SM_COMPRESSEDSIZE,
	SM_NUMLINKS,
	SM_FULLNAME,
	SM_CHTIME,
};


struct KeyBarTitles
{
	wchar_t *Titles[12];
	wchar_t *CtrlTitles[12];
	wchar_t *AltTitles[12];
	wchar_t *ShiftTitles[12];

	wchar_t *CtrlShiftTitles[12];
	wchar_t *AltShiftTitles[12];
	wchar_t *CtrlAltTitles[12];
};


enum OPERATION_MODES
{
	OPM_SILENT     =0x0001,
	OPM_FIND       =0x0002,
	OPM_VIEW       =0x0004,
	OPM_EDIT       =0x0008,
	OPM_TOPLEVEL   =0x0010,
	OPM_DESCR      =0x0020,
	OPM_QUICKVIEW  =0x0040,
	OPM_PGDN       =0x0080,
	OPM_COMMANDS   =0x0100,
};

struct OpenPluginInfo
{
	int                   StructSize;
	DWORD                 Flags;
	const wchar_t           *HostFile;
	const wchar_t           *CurDir;
	const wchar_t           *Format;
	const wchar_t           *PanelTitle;
	const struct InfoPanelLine *InfoLines;
	int                   InfoLinesNumber;
	const wchar_t * const   *DescrFiles;
	int                   DescrFilesNumber;
	const struct PanelMode *PanelModesArray;
	int                   PanelModesNumber;
	int                   StartPanelMode;
	int                   StartSortMode;
	int                   StartSortOrder;
	const struct KeyBarTitles *KeyBar;
	const wchar_t           *ShortcutData;
	long                  Reserved;
};

enum OPENPLUGIN_OPENFROM
{
	OPEN_FROM_MASK          = 0x000000FF,

	OPEN_DISKMENU           = 0,
	OPEN_PLUGINSMENU        = 1,
	OPEN_FINDLIST           = 2,
	OPEN_SHORTCUT           = 3,
	OPEN_COMMANDLINE        = 4,
	OPEN_EDITOR             = 5,
	OPEN_VIEWER             = 6,
	OPEN_FILEPANEL          = 7,
	OPEN_DIALOG             = 8,
	OPEN_ANALYSE            = 9,

	OPEN_FROMMACRO_MASK     = 0x000F0000,

	OPEN_FROMMACRO          = 0x00010000,
	OPEN_FROMMACROSTRING    = 0x00020000,
};

enum FAR_PKF_FLAGS
{
	PKF_CONTROL     = 0x00000001,
	PKF_ALT         = 0x00000002,
	PKF_SHIFT       = 0x00000004,
	PKF_PREPROCESS  = 0x00080000,
};

enum FAR_EVENTS
{
	FE_CHANGEVIEWMODE =0,
	FE_REDRAW         =1,
	FE_IDLE           =2,
	FE_CLOSE          =3,
	FE_BREAK          =4,
	FE_COMMAND        =5,

	FE_GOTFOCUS       =6,
	FE_KILLFOCUS      =7,
};

enum FAR_PLUGINS_CONTROL_COMMANDS
{
	PCTL_LOADPLUGIN         = 0,
	PCTL_UNLOADPLUGIN       = 1,
	PCTL_FORCEDLOADPLUGIN   = 2,

	PCTL_CACHEFORGET		= 3
};

enum FAR_PLUGIN_LOAD_TYPE
{
	PLT_PATH = 0,
};

enum FAR_FILE_FILTER_CONTROL_COMMANDS
{
	FFCTL_CREATEFILEFILTER = 0,
	FFCTL_FREEFILEFILTER,
	FFCTL_OPENFILTERSMENU,
	FFCTL_STARTINGTOFILTER,
	FFCTL_ISFILEINFILTER,
};

enum FAR_FILE_FILTER_TYPE
{
	FFT_PANEL = 0,
	FFT_FINDFILE,
	FFT_COPY,
	FFT_SELECT,
	FFT_CUSTOM,
};

enum FAR_REGEXP_CONTROL_COMMANDS
{
	RECTL_CREATE=0,
	RECTL_FREE,
	RECTL_COMPILE,
	RECTL_OPTIMIZE,
	RECTL_MATCHEX,
	RECTL_SEARCHEX,
	RECTL_BRACKETSCOUNT
};

struct RegExpMatch
{
	int start,end;
};

struct RegExpSearch
{
	const wchar_t* Text;
	int Position;
	int Length;
	struct RegExpMatch* Match;
	int Count;
	void* Reserved;
};
//#line 2418 "../../far2l/far2sdk/farplug-wide.h"
	void PluginModuleOpen(const char *path);
	void ClosePluginW(HANDLE hPlugin);
	int CompareW(HANDLE hPlugin,const struct PluginPanelItem *Item1,const struct PluginPanelItem *Item2,unsigned int Mode);
	int ConfigureW(int ItemNumber);
	int DeleteFilesW(HANDLE hPlugin,struct PluginPanelItem *PanelItem,int ItemsNumber,int OpMode);
	void ExitFARW(void);
	int MayExitFARW(void);
	void FreeFindDataW(HANDLE hPlugin,struct PluginPanelItem *PanelItem,int ItemsNumber);
	void FreeVirtualFindDataW(HANDLE hPlugin,struct PluginPanelItem *PanelItem,int ItemsNumber);
	int GetFilesW(HANDLE hPlugin,struct PluginPanelItem *PanelItem,int ItemsNumber,int Move,const wchar_t **DestPath,int OpMode);
	int GetFindDataW(HANDLE hPlugin,struct PluginPanelItem **pPanelItem,int *pItemsNumber,int OpMode);
	int GetMinFarVersionW(void);
	void GetOpenPluginInfoW(HANDLE hPlugin,struct OpenPluginInfo *Info);
	void GetPluginInfoW(struct PluginInfo *Info);
	int GetVirtualFindDataW(HANDLE hPlugin,struct PluginPanelItem **pPanelItem,int *pItemsNumber,const wchar_t *Path);
	int MakeDirectoryW(HANDLE hPlugin,const wchar_t **Name,int OpMode);
	HANDLE OpenFilePluginW(const wchar_t *Name,const unsigned char *Data,int DataSize,int OpMode);
	HANDLE OpenPluginW(int OpenFrom,INT_PTR Item);
	int ProcessDialogEventW(int Event,void *Param);
	int ProcessEditorEventW(int Event,void *Param);
	int ProcessEditorInputW(const INPUT_RECORD *Rec);
	int ProcessEventW(HANDLE hPlugin,int Event,void *Param);
	int ProcessHostFileW(HANDLE hPlugin,struct PluginPanelItem *PanelItem,int ItemsNumber,int OpMode);
	int ProcessKeyW(HANDLE hPlugin,int Key,unsigned int ControlState);


	int ProcessMacroFuncW(const wchar_t *Name, const struct FarMacroValue *Params, int nParams, struct FarMacroValue **Results, int *nResults);


	int ProcessSynchroEventW(int Event,void *Param);
	int ProcessViewerEventW(int Event,void *Param);
	int PutFilesW(HANDLE hPlugin,struct PluginPanelItem *PanelItem,int ItemsNumber,int Move,const wchar_t *SrcPath,int OpMode);
	int SetDirectoryW(HANDLE hPlugin,const wchar_t *Dir,int OpMode);
	int SetFindListW(HANDLE hPlugin,const struct PluginPanelItem *PanelItem,int ItemsNumber);
	void SetStartupInfoW(const struct PluginStartupInfo *Info);
//#line 2463 "../../far2l/far2sdk/farplug-wide.h"
//#pragma pack()
//#line 44 "../../far2l/far2sdk/farcolor.h"
enum PaletteColors
{
	COL_MENUTEXT,
	COL_MENUSELECTEDTEXT,
	COL_MENUHIGHLIGHT,
	COL_MENUSELECTEDHIGHLIGHT,
	COL_MENUBOX,
	COL_MENUTITLE,

	COL_HMENUTEXT,
	COL_HMENUSELECTEDTEXT,
	COL_HMENUHIGHLIGHT,
	COL_HMENUSELECTEDHIGHLIGHT,

	COL_PANELTEXT,
	COL_PANELSELECTEDTEXT,
	COL_PANELHIGHLIGHTTEXT,
	COL_PANELINFOTEXT,
	COL_PANELCURSOR,
	COL_PANELSELECTEDCURSOR,
	COL_PANELTITLE,
	COL_PANELSELECTEDTITLE,
	COL_PANELCOLUMNTITLE,
	COL_PANELTOTALINFO,
	COL_PANELSELECTEDINFO,

	COL_DIALOGTEXT,
	COL_DIALOGHIGHLIGHTTEXT,
	COL_DIALOGBOX,
	COL_DIALOGBOXTITLE,
	COL_DIALOGHIGHLIGHTBOXTITLE,
	COL_DIALOGEDIT,
	COL_DIALOGBUTTON,
	COL_DIALOGSELECTEDBUTTON,
	COL_DIALOGHIGHLIGHTBUTTON,
	COL_DIALOGHIGHLIGHTSELECTEDBUTTON,

	COL_DIALOGLISTTEXT,
	COL_DIALOGLISTSELECTEDTEXT,
	COL_DIALOGLISTHIGHLIGHT,
	COL_DIALOGLISTSELECTEDHIGHLIGHT,

	COL_WARNDIALOGTEXT,
	COL_WARNDIALOGHIGHLIGHTTEXT,
	COL_WARNDIALOGBOX,
	COL_WARNDIALOGBOXTITLE,
	COL_WARNDIALOGHIGHLIGHTBOXTITLE,
	COL_WARNDIALOGEDIT,
	COL_WARNDIALOGBUTTON,
	COL_WARNDIALOGSELECTEDBUTTON,
	COL_WARNDIALOGHIGHLIGHTBUTTON,
	COL_WARNDIALOGHIGHLIGHTSELECTEDBUTTON,

	COL_KEYBARNUM,
	COL_KEYBARTEXT,
	COL_KEYBARBACKGROUND,

	COL_COMMANDLINE,

	COL_CLOCK,

	COL_VIEWERTEXT,
	COL_VIEWERSELECTEDTEXT,
	COL_VIEWERSTATUS,

	COL_EDITORTEXT,
	COL_EDITORSELECTEDTEXT,
	COL_EDITORSTATUS,

	COL_HELPTEXT,
	COL_HELPHIGHLIGHTTEXT,
	COL_HELPTOPIC,
	COL_HELPSELECTEDTOPIC,
	COL_HELPBOX,
	COL_HELPBOXTITLE,

	COL_PANELDRAGTEXT,
	COL_DIALOGEDITUNCHANGED,
	COL_PANELSCROLLBAR,
	COL_HELPSCROLLBAR,
	COL_PANELBOX,
	COL_PANELSCREENSNUMBER,
	COL_DIALOGEDITSELECTED,
	COL_COMMANDLINESELECTED,
	COL_VIEWERARROWS,

	COL_RESERVED0,

	COL_DIALOGLISTSCROLLBAR,
	COL_MENUSCROLLBAR,
	COL_VIEWERSCROLLBAR,
	COL_COMMANDLINEPREFIX,
	COL_DIALOGDISABLED,
	COL_DIALOGEDITDISABLED,
	COL_DIALOGLISTDISABLED,
	COL_WARNDIALOGDISABLED,
	COL_WARNDIALOGEDITDISABLED,
	COL_WARNDIALOGLISTDISABLED,

	COL_MENUDISABLEDTEXT,

	COL_EDITORCLOCK,
	COL_VIEWERCLOCK,

	COL_DIALOGLISTTITLE,
	COL_DIALOGLISTBOX,

	COL_WARNDIALOGEDITSELECTED,
	COL_WARNDIALOGEDITUNCHANGED,

	COL_DIALOGCOMBOTEXT,
	COL_DIALOGCOMBOSELECTEDTEXT,
	COL_DIALOGCOMBOHIGHLIGHT,
	COL_DIALOGCOMBOSELECTEDHIGHLIGHT,
	COL_DIALOGCOMBOBOX,
	COL_DIALOGCOMBOTITLE,
	COL_DIALOGCOMBODISABLED,
	COL_DIALOGCOMBOSCROLLBAR,

	COL_WARNDIALOGLISTTEXT,
	COL_WARNDIALOGLISTSELECTEDTEXT,
	COL_WARNDIALOGLISTHIGHLIGHT,
	COL_WARNDIALOGLISTSELECTEDHIGHLIGHT,
	COL_WARNDIALOGLISTBOX,
	COL_WARNDIALOGLISTTITLE,
	COL_WARNDIALOGLISTSCROLLBAR,

	COL_WARNDIALOGCOMBOTEXT,
	COL_WARNDIALOGCOMBOSELECTEDTEXT,
	COL_WARNDIALOGCOMBOHIGHLIGHT,
	COL_WARNDIALOGCOMBOSELECTEDHIGHLIGHT,
	COL_WARNDIALOGCOMBOBOX,
	COL_WARNDIALOGCOMBOTITLE,
	COL_WARNDIALOGCOMBODISABLED,
	COL_WARNDIALOGCOMBOSCROLLBAR,

	COL_DIALOGLISTARROWS,
	COL_DIALOGLISTARROWSDISABLED,
	COL_DIALOGLISTARROWSSELECTED,
	COL_DIALOGCOMBOARROWS,
	COL_DIALOGCOMBOARROWSDISABLED,
	COL_DIALOGCOMBOARROWSSELECTED,
	COL_WARNDIALOGLISTARROWS,
	COL_WARNDIALOGLISTARROWSDISABLED,
	COL_WARNDIALOGLISTARROWSSELECTED,
	COL_WARNDIALOGCOMBOARROWS,
	COL_WARNDIALOGCOMBOARROWSDISABLED,
	COL_WARNDIALOGCOMBOARROWSSELECTED,
	COL_MENUARROWS,
	COL_MENUARROWSDISABLED,
	COL_MENUARROWSSELECTED,
	COL_COMMANDLINEUSERSCREEN,
	COL_EDITORSCROLLBAR,

	COL_MENUGRAYTEXT,
	COL_MENUSELECTEDGRAYTEXT,
	COL_DIALOGCOMBOGRAY,
	COL_DIALOGCOMBOSELECTEDGRAYTEXT,
	COL_DIALOGLISTGRAY,
	COL_DIALOGLISTSELECTEDGRAYTEXT,
	COL_WARNDIALOGCOMBOGRAY,
	COL_WARNDIALOGCOMBOSELECTEDGRAYTEXT,
	COL_WARNDIALOGLISTGRAY,
	COL_WARNDIALOGLISTSELECTEDGRAYTEXT,

	COL_DIALOGDEFAULTBUTTON,
	COL_DIALOGSELECTEDDEFAULTBUTTON,
	COL_DIALOGHIGHLIGHTDEFAULTBUTTON,
	COL_DIALOGHIGHLIGHTSELECTEDDEFAULTBUTTON,
	COL_WARNDIALOGDEFAULTBUTTON,
	COL_WARNDIALOGSELECTEDDEFAULTBUTTON,
	COL_WARNDIALOGHIGHLIGHTDEFAULTBUTTON,
	COL_WARNDIALOGHIGHLIGHTSELECTEDDEFAULTBUTTON,

	COL_LASTPALETTECOLOR
};
//#line 46 "../../far2l/far2sdk/farkeys.h"
enum BaseDefKeyboard
{
	KEY_CTRLMASK             =0xFFF00000,
	KEY_CTRL                 =0x01000000,
	KEY_ALT                  =0x02000000,
	KEY_SHIFT                =0x04000000,

	KEY_RCTRL                =0x10000000,
	KEY_RALT                 =0x20000000,

	KEY_BRACKET              =91,
	KEY_BACKBRACKET          =93,
	KEY_COMMA                =44,
	KEY_QUOTE                =34,
	KEY_DOT                  =46,
	KEY_SLASH                =47,
	KEY_COLON                =58,
	KEY_SEMICOLON            =59,
	KEY_BACKSLASH            =92,

	KEY_BS                   =0x00000008,
	KEY_TAB                  =0x00000009,
	KEY_ENTER                =0x0000000D,
	KEY_ESC                  =0x0000001B,
	KEY_SPACE                =0x00000020,

	KEY_MASKF                =0x0001FFFF,

	KEY_FKEY_BEGIN           =0x00010000,

	KEY_BREAK                =0x00010000+0x03,

	KEY_PAUSE                =0x00010000+0x13,
	KEY_CAPSLOCK             =0x00010000+0x14,

	KEY_PGUP                 =0x00010000+0x21,
	KEY_PGDN                 =0x00010000+0x22,
	KEY_END                  =0x00010000+0x23,
	KEY_HOME                 =0x00010000+0x24,
	KEY_LEFT                 =0x00010000+0x25,
	KEY_UP                   =0x00010000+0x26,
	KEY_RIGHT                =0x00010000+0x27,
	KEY_DOWN                 =0x00010000+0x28,
	KEY_PRNTSCRN             =0x00010000+0x2C,
	KEY_INS                  =0x00010000+0x2D,
	KEY_DEL                  =0x00010000+0x2E,

	KEY_LWIN                 =0x00010000+0x5B,
	KEY_RWIN                 =0x00010000+0x5C,
	KEY_APPS                 =0x00010000+0x5D,
	KEY_STANDBY              =0x00010000+0x5F,

	KEY_NUMPAD0              =0x00010000+0x60,
	KEY_NUMPAD1              =0x00010000+0x61,
	KEY_NUMPAD2              =0x00010000+0x62,
	KEY_NUMPAD3              =0x00010000+0x63,
	KEY_NUMPAD4              =0x00010000+0x64,
	KEY_NUMPAD5              =0x00010000+0x65,
	KEY_CLEAR                =KEY_NUMPAD5,
	KEY_NUMPAD6              =0x00010000+0x66,
	KEY_NUMPAD7              =0x00010000+0x67,
	KEY_NUMPAD8              =0x00010000+0x68,
	KEY_NUMPAD9              =0x00010000+0x69,

	KEY_MULTIPLY             =0x00010000+0x6A,
	KEY_ADD                  =0x00010000+0x6B,
	KEY_SUBTRACT             =0x00010000+0x6D,
	KEY_DECIMAL              =0x00010000+0x6E,
	KEY_DIVIDE               =0x00010000+0x6F,

	KEY_F1                   =0x00010000+0x70,
	KEY_F2                   =0x00010000+0x71,
	KEY_F3                   =0x00010000+0x72,
	KEY_F4                   =0x00010000+0x73,
	KEY_F5                   =0x00010000+0x74,
	KEY_F6                   =0x00010000+0x75,
	KEY_F7                   =0x00010000+0x76,
	KEY_F8                   =0x00010000+0x77,
	KEY_F9                   =0x00010000+0x78,
	KEY_F10                  =0x00010000+0x79,
	KEY_F11                  =0x00010000+0x7A,
	KEY_F12                  =0x00010000+0x7B,

	KEY_F13                  =0x00010000+0x7C,
	KEY_F14                  =0x00010000+0x7D,
	KEY_F15                  =0x00010000+0x7E,
	KEY_F16                  =0x00010000+0x7F,
	KEY_F17                  =0x00010000+0x80,
	KEY_F18                  =0x00010000+0x81,
	KEY_F19                  =0x00010000+0x82,
	KEY_F20                  =0x00010000+0x83,
	KEY_F21                  =0x00010000+0x84,
	KEY_F22                  =0x00010000+0x85,
	KEY_F23                  =0x00010000+0x86,
	KEY_F24                  =0x00010000+0x87,

	KEY_NUMLOCK              =0x00010000+0x90,
	KEY_SCROLLLOCK           =0x00010000+0x91,
//#line 166 "../../far2l/far2sdk/farkeys.h"
	KEY_CTRLALTSHIFTPRESS    =0x00020000+1,
	KEY_CTRLALTSHIFTRELEASE  =0x00020000+2,

	KEY_MSWHEEL_UP           =0x00020000+3,
	KEY_MSWHEEL_DOWN         =0x00020000+4,
	KEY_NUMDEL               =0x00020000+9,
	KEY_NUMENTER             =0x00020000+0xB,

	KEY_MSWHEEL_LEFT         =0x00020000+0xC,
	KEY_MSWHEEL_RIGHT        =0x00020000+0xD,

	KEY_MSLCLICK             =0x00020000+0xF,
	KEY_MSRCLICK             =0x00020000+0x10,

	KEY_MSM1CLICK            =0x00020000+0x11,
	KEY_MSM2CLICK            =0x00020000+0x12,
	KEY_MSM3CLICK            =0x00020000+0x13,



	KEY_VK_0xFF_BEGIN        =0x00010000+0x00000100,
	KEY_VK_0xFF_END          =0x00010000+0x000001FF,

	KEY_END_FKEY             =0x0001FFFF,

	KEY_NONE                 =0x00030000+1,
	KEY_IDLE                 =0x00030000+2,

	KEY_KILLFOCUS            =0x00030000+6,
	KEY_GOTFOCUS             =0x00030000+7,
	KEY_CONSOLE_BUFFER_RESIZE=0x00030000+8,


	KEY_END_SKEY             =0x0003FFFF,
	KEY_LAST_BASE            =KEY_END_SKEY,

};

enum AddDefKeyboard
{
	KEY_CTRLSHIFT            =KEY_CTRL|KEY_SHIFT,
	KEY_ALTSHIFT             =KEY_ALT|KEY_SHIFT,
	KEY_CTRLALT              =KEY_CTRL|KEY_ALT,

	KEY_CTRL0                =KEY_CTRL+48,
	KEY_CTRL1                =KEY_CTRL+49,
	KEY_CTRL2                =KEY_CTRL+50,
	KEY_CTRL3                =KEY_CTRL+51,
	KEY_CTRL4                =KEY_CTRL+52,
	KEY_CTRL5                =KEY_CTRL+53,
	KEY_CTRL6                =KEY_CTRL+54,
	KEY_CTRL7                =KEY_CTRL+55,
	KEY_CTRL8                =KEY_CTRL+56,
	KEY_CTRL9                =KEY_CTRL+57,

	KEY_RCTRL0               =KEY_RCTRL+48,
	KEY_RCTRL1               =KEY_RCTRL+49,
	KEY_RCTRL2               =KEY_RCTRL+50,
	KEY_RCTRL3               =KEY_RCTRL+51,
	KEY_RCTRL4               =KEY_RCTRL+52,
	KEY_RCTRL5               =KEY_RCTRL+53,
	KEY_RCTRL6               =KEY_RCTRL+54,
	KEY_RCTRL7               =KEY_RCTRL+55,
	KEY_RCTRL8               =KEY_RCTRL+56,
	KEY_RCTRL9               =KEY_RCTRL+57,

	KEY_CTRLA                =KEY_CTRL+65,
	KEY_CTRLB                =KEY_CTRL+66,
	KEY_CTRLC                =KEY_CTRL+67,
	KEY_CTRLD                =KEY_CTRL+68,
	KEY_CTRLE                =KEY_CTRL+69,
	KEY_CTRLF                =KEY_CTRL+70,
	KEY_CTRLG                =KEY_CTRL+71,
	KEY_CTRLH                =KEY_CTRL+72,
	KEY_CTRLI                =KEY_CTRL+73,
	KEY_CTRLJ                =KEY_CTRL+74,
	KEY_CTRLK                =KEY_CTRL+75,
	KEY_CTRLL                =KEY_CTRL+76,
	KEY_CTRLM                =KEY_CTRL+77,
	KEY_CTRLN                =KEY_CTRL+78,
	KEY_CTRLO                =KEY_CTRL+79,
	KEY_CTRLP                =KEY_CTRL+80,
	KEY_CTRLQ                =KEY_CTRL+81,
	KEY_CTRLR                =KEY_CTRL+82,
	KEY_CTRLS                =KEY_CTRL+83,
	KEY_CTRLT                =KEY_CTRL+84,
	KEY_CTRLU                =KEY_CTRL+85,
	KEY_CTRLV                =KEY_CTRL+86,
	KEY_CTRLW                =KEY_CTRL+87,
	KEY_CTRLX                =KEY_CTRL+88,
	KEY_CTRLY                =KEY_CTRL+89,
	KEY_CTRLZ                =KEY_CTRL+90,

	KEY_CTRLBRACKET          =KEY_CTRL|KEY_BRACKET,
	KEY_CTRLBACKBRACKET      =KEY_CTRL|KEY_BACKBRACKET,
	KEY_CTRLCOMMA            =KEY_CTRL|KEY_COMMA,
	KEY_CTRLQUOTE            =KEY_CTRL|KEY_QUOTE,
	KEY_CTRLDOT              =KEY_CTRL|KEY_DOT,

	KEY_ALT0                 =KEY_ALT+48,
	KEY_ALT1                 =KEY_ALT+49,
	KEY_ALT2                 =KEY_ALT+50,
	KEY_ALT3                 =KEY_ALT+51,
	KEY_ALT4                 =KEY_ALT+52,
	KEY_ALT5                 =KEY_ALT+53,
	KEY_ALT6                 =KEY_ALT+54,
	KEY_ALT7                 =KEY_ALT+55,
	KEY_ALT8                 =KEY_ALT+56,
	KEY_ALT9                 =KEY_ALT+57,

	KEY_ALTADD               =KEY_ALT|KEY_ADD,
	KEY_ALTDOT               =KEY_ALT|KEY_DOT,
	KEY_ALTCOMMA             =KEY_ALT|KEY_COMMA,
	KEY_ALTMULTIPLY          =KEY_ALT|KEY_MULTIPLY,

	KEY_ALTA                 =KEY_ALT+65,
	KEY_ALTB                 =KEY_ALT+66,
	KEY_ALTC                 =KEY_ALT+67,
	KEY_ALTD                 =KEY_ALT+68,
	KEY_ALTE                 =KEY_ALT+69,
	KEY_ALTF                 =KEY_ALT+70,
	KEY_ALTG                 =KEY_ALT+71,
	KEY_ALTH                 =KEY_ALT+72,
	KEY_ALTI                 =KEY_ALT+73,
	KEY_ALTJ                 =KEY_ALT+74,
	KEY_ALTK                 =KEY_ALT+75,
	KEY_ALTL                 =KEY_ALT+76,
	KEY_ALTM                 =KEY_ALT+77,
	KEY_ALTN                 =KEY_ALT+78,
	KEY_ALTO                 =KEY_ALT+79,
	KEY_ALTP                 =KEY_ALT+80,
	KEY_ALTQ                 =KEY_ALT+81,
	KEY_ALTR                 =KEY_ALT+82,
	KEY_ALTS                 =KEY_ALT+83,
	KEY_ALTT                 =KEY_ALT+84,
	KEY_ALTU                 =KEY_ALT+85,
	KEY_ALTV                 =KEY_ALT+86,
	KEY_ALTW                 =KEY_ALT+87,
	KEY_ALTX                 =KEY_ALT+88,
	KEY_ALTY                 =KEY_ALT+89,
	KEY_ALTZ                 =KEY_ALT+90,

	KEY_CTRLSHIFTADD         =KEY_CTRL|KEY_SHIFT|KEY_ADD,
	KEY_CTRLSHIFTSUBTRACT    =KEY_CTRL|KEY_SHIFT|KEY_SUBTRACT,
	KEY_CTRLSHIFTDOT         =KEY_CTRL|KEY_SHIFT|KEY_DOT,
	KEY_CTRLSHIFTSLASH       =KEY_CTRL|KEY_SHIFT|KEY_SLASH,

	KEY_CTRLSHIFT0           =(KEY_CTRL|KEY_SHIFT)+48,
	KEY_CTRLSHIFT1           =(KEY_CTRL|KEY_SHIFT)+49,
	KEY_CTRLSHIFT2           =(KEY_CTRL|KEY_SHIFT)+50,
	KEY_CTRLSHIFT3           =(KEY_CTRL|KEY_SHIFT)+51,
	KEY_CTRLSHIFT4           =(KEY_CTRL|KEY_SHIFT)+52,
	KEY_CTRLSHIFT5           =(KEY_CTRL|KEY_SHIFT)+53,
	KEY_CTRLSHIFT6           =(KEY_CTRL|KEY_SHIFT)+54,
	KEY_CTRLSHIFT7           =(KEY_CTRL|KEY_SHIFT)+55,
	KEY_CTRLSHIFT8           =(KEY_CTRL|KEY_SHIFT)+56,
	KEY_CTRLSHIFT9           =(KEY_CTRL|KEY_SHIFT)+57,

	KEY_RCTRLSHIFT0          =KEY_RCTRL+KEY_SHIFT+48,
	KEY_RCTRLSHIFT1          =KEY_RCTRL+KEY_SHIFT+49,
	KEY_RCTRLSHIFT2          =KEY_RCTRL+KEY_SHIFT+50,
	KEY_RCTRLSHIFT3          =KEY_RCTRL+KEY_SHIFT+51,
	KEY_RCTRLSHIFT4          =KEY_RCTRL+KEY_SHIFT+52,
	KEY_RCTRLSHIFT5          =KEY_RCTRL+KEY_SHIFT+53,
	KEY_RCTRLSHIFT6          =KEY_RCTRL+KEY_SHIFT+54,
	KEY_RCTRLSHIFT7          =KEY_RCTRL+KEY_SHIFT+55,
	KEY_RCTRLSHIFT8          =KEY_RCTRL+KEY_SHIFT+56,
	KEY_RCTRLSHIFT9          =KEY_RCTRL+KEY_SHIFT+57,

	KEY_CTRLSHIFTA           =(KEY_CTRL|KEY_SHIFT)+65,
	KEY_CTRLSHIFTB           =(KEY_CTRL|KEY_SHIFT)+66,
	KEY_CTRLSHIFTC           =(KEY_CTRL|KEY_SHIFT)+67,
	KEY_CTRLSHIFTD           =(KEY_CTRL|KEY_SHIFT)+68,
	KEY_CTRLSHIFTE           =(KEY_CTRL|KEY_SHIFT)+69,
	KEY_CTRLSHIFTF           =(KEY_CTRL|KEY_SHIFT)+70,
	KEY_CTRLSHIFTG           =(KEY_CTRL|KEY_SHIFT)+71,
	KEY_CTRLSHIFTH           =(KEY_CTRL|KEY_SHIFT)+72,
	KEY_CTRLSHIFTI           =(KEY_CTRL|KEY_SHIFT)+73,
	KEY_CTRLSHIFTJ           =(KEY_CTRL|KEY_SHIFT)+74,
	KEY_CTRLSHIFTK           =(KEY_CTRL|KEY_SHIFT)+75,
	KEY_CTRLSHIFTL           =(KEY_CTRL|KEY_SHIFT)+76,
	KEY_CTRLSHIFTM           =(KEY_CTRL|KEY_SHIFT)+77,
	KEY_CTRLSHIFTN           =(KEY_CTRL|KEY_SHIFT)+78,
	KEY_CTRLSHIFTO           =(KEY_CTRL|KEY_SHIFT)+79,
	KEY_CTRLSHIFTP           =(KEY_CTRL|KEY_SHIFT)+80,
	KEY_CTRLSHIFTQ           =(KEY_CTRL|KEY_SHIFT)+81,
	KEY_CTRLSHIFTR           =(KEY_CTRL|KEY_SHIFT)+82,
	KEY_CTRLSHIFTS           =(KEY_CTRL|KEY_SHIFT)+83,
	KEY_CTRLSHIFTT           =(KEY_CTRL|KEY_SHIFT)+84,
	KEY_CTRLSHIFTU           =(KEY_CTRL|KEY_SHIFT)+85,
	KEY_CTRLSHIFTV           =(KEY_CTRL|KEY_SHIFT)+86,
	KEY_CTRLSHIFTW           =(KEY_CTRL|KEY_SHIFT)+87,
	KEY_CTRLSHIFTX           =(KEY_CTRL|KEY_SHIFT)+88,
	KEY_CTRLSHIFTY           =(KEY_CTRL|KEY_SHIFT)+89,
	KEY_CTRLSHIFTZ           =(KEY_CTRL|KEY_SHIFT)+90,

	KEY_CTRLSHIFTBRACKET     =KEY_CTRL|KEY_SHIFT|KEY_BRACKET,
	KEY_CTRLSHIFTBACKSLASH   =KEY_CTRL|KEY_SHIFT|KEY_BACKSLASH,
	KEY_CTRLSHIFTBACKBRACKET =KEY_CTRL|KEY_SHIFT|KEY_BACKBRACKET,

	KEY_ALTSHIFT0            =(KEY_ALT|KEY_SHIFT)+48,
	KEY_ALTSHIFT1            =(KEY_ALT|KEY_SHIFT)+49,
	KEY_ALTSHIFT2            =(KEY_ALT|KEY_SHIFT)+50,
	KEY_ALTSHIFT3            =(KEY_ALT|KEY_SHIFT)+51,
	KEY_ALTSHIFT4            =(KEY_ALT|KEY_SHIFT)+52,
	KEY_ALTSHIFT5            =(KEY_ALT|KEY_SHIFT)+53,
	KEY_ALTSHIFT6            =(KEY_ALT|KEY_SHIFT)+54,
	KEY_ALTSHIFT7            =(KEY_ALT|KEY_SHIFT)+55,
	KEY_ALTSHIFT8            =(KEY_ALT|KEY_SHIFT)+56,
	KEY_ALTSHIFT9            =(KEY_ALT|KEY_SHIFT)+57,

	KEY_ALTSHIFTA            =(KEY_ALT|KEY_SHIFT)+65,
	KEY_ALTSHIFTB            =(KEY_ALT|KEY_SHIFT)+66,
	KEY_ALTSHIFTC            =(KEY_ALT|KEY_SHIFT)+67,
	KEY_ALTSHIFTD            =(KEY_ALT|KEY_SHIFT)+68,
	KEY_ALTSHIFTE            =(KEY_ALT|KEY_SHIFT)+69,
	KEY_ALTSHIFTF            =(KEY_ALT|KEY_SHIFT)+70,
	KEY_ALTSHIFTG            =(KEY_ALT|KEY_SHIFT)+71,
	KEY_ALTSHIFTH            =(KEY_ALT|KEY_SHIFT)+72,
	KEY_ALTSHIFTI            =(KEY_ALT|KEY_SHIFT)+73,
	KEY_ALTSHIFTJ            =(KEY_ALT|KEY_SHIFT)+74,
	KEY_ALTSHIFTK            =(KEY_ALT|KEY_SHIFT)+75,
	KEY_ALTSHIFTL            =(KEY_ALT|KEY_SHIFT)+76,
	KEY_ALTSHIFTM            =(KEY_ALT|KEY_SHIFT)+77,
	KEY_ALTSHIFTN            =(KEY_ALT|KEY_SHIFT)+78,
	KEY_ALTSHIFTO            =(KEY_ALT|KEY_SHIFT)+79,
	KEY_ALTSHIFTP            =(KEY_ALT|KEY_SHIFT)+80,
	KEY_ALTSHIFTQ            =(KEY_ALT|KEY_SHIFT)+81,
	KEY_ALTSHIFTR            =(KEY_ALT|KEY_SHIFT)+82,
	KEY_ALTSHIFTS            =(KEY_ALT|KEY_SHIFT)+83,
	KEY_ALTSHIFTT            =(KEY_ALT|KEY_SHIFT)+84,
	KEY_ALTSHIFTU            =(KEY_ALT|KEY_SHIFT)+85,
	KEY_ALTSHIFTV            =(KEY_ALT|KEY_SHIFT)+86,
	KEY_ALTSHIFTW            =(KEY_ALT|KEY_SHIFT)+87,
	KEY_ALTSHIFTX            =(KEY_ALT|KEY_SHIFT)+88,
	KEY_ALTSHIFTY            =(KEY_ALT|KEY_SHIFT)+89,
	KEY_ALTSHIFTZ            =(KEY_ALT|KEY_SHIFT)+90,

	KEY_ALTSHIFTBRACKET      =KEY_ALT|KEY_SHIFT|KEY_BRACKET,
	KEY_ALTSHIFTBACKBRACKET  =KEY_ALT|KEY_SHIFT|KEY_BACKBRACKET,

	KEY_CTRLALT0             =(KEY_CTRL|KEY_ALT)+48,
	KEY_CTRLALT1             =(KEY_CTRL|KEY_ALT)+49,
	KEY_CTRLALT2             =(KEY_CTRL|KEY_ALT)+50,
	KEY_CTRLALT3             =(KEY_CTRL|KEY_ALT)+51,
	KEY_CTRLALT4             =(KEY_CTRL|KEY_ALT)+52,
	KEY_CTRLALT5             =(KEY_CTRL|KEY_ALT)+53,
	KEY_CTRLALT6             =(KEY_CTRL|KEY_ALT)+54,
	KEY_CTRLALT7             =(KEY_CTRL|KEY_ALT)+55,
	KEY_CTRLALT8             =(KEY_CTRL|KEY_ALT)+56,
	KEY_CTRLALT9             =(KEY_CTRL|KEY_ALT)+57,

	KEY_CTRLALTA             =(KEY_CTRL|KEY_ALT)+65,
	KEY_CTRLALTB             =(KEY_CTRL|KEY_ALT)+66,
	KEY_CTRLALTC             =(KEY_CTRL|KEY_ALT)+67,
	KEY_CTRLALTD             =(KEY_CTRL|KEY_ALT)+68,
	KEY_CTRLALTE             =(KEY_CTRL|KEY_ALT)+69,
	KEY_CTRLALTF             =(KEY_CTRL|KEY_ALT)+70,
	KEY_CTRLALTG             =(KEY_CTRL|KEY_ALT)+71,
	KEY_CTRLALTH             =(KEY_CTRL|KEY_ALT)+72,
	KEY_CTRLALTI             =(KEY_CTRL|KEY_ALT)+73,
	KEY_CTRLALTJ             =(KEY_CTRL|KEY_ALT)+74,
	KEY_CTRLALTK             =(KEY_CTRL|KEY_ALT)+75,
	KEY_CTRLALTL             =(KEY_CTRL|KEY_ALT)+76,
	KEY_CTRLALTM             =(KEY_CTRL|KEY_ALT)+77,
	KEY_CTRLALTN             =(KEY_CTRL|KEY_ALT)+78,
	KEY_CTRLALTO             =(KEY_CTRL|KEY_ALT)+79,
	KEY_CTRLALTP             =(KEY_CTRL|KEY_ALT)+80,
	KEY_CTRLALTQ             =(KEY_CTRL|KEY_ALT)+81,
	KEY_CTRLALTR             =(KEY_CTRL|KEY_ALT)+82,
	KEY_CTRLALTS             =(KEY_CTRL|KEY_ALT)+83,
	KEY_CTRLALTT             =(KEY_CTRL|KEY_ALT)+84,
	KEY_CTRLALTU             =(KEY_CTRL|KEY_ALT)+85,
	KEY_CTRLALTV             =(KEY_CTRL|KEY_ALT)+86,
	KEY_CTRLALTW             =(KEY_CTRL|KEY_ALT)+87,
	KEY_CTRLALTX             =(KEY_CTRL|KEY_ALT)+88,
	KEY_CTRLALTY             =(KEY_CTRL|KEY_ALT)+89,
	KEY_CTRLALTZ             =(KEY_CTRL|KEY_ALT)+90,

	KEY_CTRLALTBRACKET       =KEY_CTRL|KEY_ALT|KEY_BRACKET,
	KEY_CTRLALTBACKBRACKET   =KEY_CTRL|KEY_ALT|KEY_BACKBRACKET,

	KEY_CTRLF1               =KEY_CTRL|KEY_F1,
	KEY_CTRLF2               =KEY_CTRL|KEY_F2,
	KEY_CTRLF3               =KEY_CTRL|KEY_F3,
	KEY_CTRLF4               =KEY_CTRL|KEY_F4,
	KEY_CTRLF5               =KEY_CTRL|KEY_F5,
	KEY_CTRLF6               =KEY_CTRL|KEY_F6,
	KEY_CTRLF7               =KEY_CTRL|KEY_F7,
	KEY_CTRLF8               =KEY_CTRL|KEY_F8,
	KEY_CTRLF9               =KEY_CTRL|KEY_F9,
	KEY_CTRLF10              =KEY_CTRL|KEY_F10,
	KEY_CTRLF11              =KEY_CTRL|KEY_F11,
	KEY_CTRLF12              =KEY_CTRL|KEY_F12,

	KEY_SHIFTF1              =KEY_SHIFT|KEY_F1,
	KEY_SHIFTF2              =KEY_SHIFT|KEY_F2,
	KEY_SHIFTF3              =KEY_SHIFT|KEY_F3,
	KEY_SHIFTF4              =KEY_SHIFT|KEY_F4,
	KEY_SHIFTF5              =KEY_SHIFT|KEY_F5,
	KEY_SHIFTF6              =KEY_SHIFT|KEY_F6,
	KEY_SHIFTF7              =KEY_SHIFT|KEY_F7,
	KEY_SHIFTF8              =KEY_SHIFT|KEY_F8,
	KEY_SHIFTF9              =KEY_SHIFT|KEY_F9,
	KEY_SHIFTF10             =KEY_SHIFT|KEY_F10,
	KEY_SHIFTF11             =KEY_SHIFT|KEY_F11,
	KEY_SHIFTF12             =KEY_SHIFT|KEY_F12,

	KEY_ALTF1                =KEY_ALT|KEY_F1,
	KEY_ALTF2                =KEY_ALT|KEY_F2,
	KEY_ALTF3                =KEY_ALT|KEY_F3,
	KEY_ALTF4                =KEY_ALT|KEY_F4,
	KEY_ALTF5                =KEY_ALT|KEY_F5,
	KEY_ALTF6                =KEY_ALT|KEY_F6,
	KEY_ALTF7                =KEY_ALT|KEY_F7,
	KEY_ALTF8                =KEY_ALT|KEY_F8,
	KEY_ALTF9                =KEY_ALT|KEY_F9,
	KEY_ALTF10               =KEY_ALT|KEY_F10,
	KEY_ALTF11               =KEY_ALT|KEY_F11,
	KEY_ALTF12               =KEY_ALT|KEY_F12,

	KEY_CTRLSHIFTF1          =KEY_CTRL|KEY_SHIFT|KEY_F1,
	KEY_CTRLSHIFTF2          =KEY_CTRL|KEY_SHIFT|KEY_F2,
	KEY_CTRLSHIFTF3          =KEY_CTRL|KEY_SHIFT|KEY_F3,
	KEY_CTRLSHIFTF4          =KEY_CTRL|KEY_SHIFT|KEY_F4,
	KEY_CTRLSHIFTF5          =KEY_CTRL|KEY_SHIFT|KEY_F5,
	KEY_CTRLSHIFTF6          =KEY_CTRL|KEY_SHIFT|KEY_F6,
	KEY_CTRLSHIFTF7          =KEY_CTRL|KEY_SHIFT|KEY_F7,
	KEY_CTRLSHIFTF8          =KEY_CTRL|KEY_SHIFT|KEY_F8,
	KEY_CTRLSHIFTF9          =KEY_CTRL|KEY_SHIFT|KEY_F9,
	KEY_CTRLSHIFTF10         =KEY_CTRL|KEY_SHIFT|KEY_F10,
	KEY_CTRLSHIFTF11         =KEY_CTRL|KEY_SHIFT|KEY_F11,
	KEY_CTRLSHIFTF12         =KEY_CTRL|KEY_SHIFT|KEY_F12,

	KEY_ALTSHIFTF1           =KEY_ALT|KEY_SHIFT|KEY_F1,
	KEY_ALTSHIFTF2           =KEY_ALT|KEY_SHIFT|KEY_F2,
	KEY_ALTSHIFTF3           =KEY_ALT|KEY_SHIFT|KEY_F3,
	KEY_ALTSHIFTF4           =KEY_ALT|KEY_SHIFT|KEY_F4,
	KEY_ALTSHIFTF5           =KEY_ALT|KEY_SHIFT|KEY_F5,
	KEY_ALTSHIFTF6           =KEY_ALT|KEY_SHIFT|KEY_F6,
	KEY_ALTSHIFTF7           =KEY_ALT|KEY_SHIFT|KEY_F7,
	KEY_ALTSHIFTF8           =KEY_ALT|KEY_SHIFT|KEY_F8,
	KEY_ALTSHIFTF9           =KEY_ALT|KEY_SHIFT|KEY_F9,
	KEY_ALTSHIFTF10          =KEY_ALT|KEY_SHIFT|KEY_F10,
	KEY_ALTSHIFTF11          =KEY_ALT|KEY_SHIFT|KEY_F11,
	KEY_ALTSHIFTF12          =KEY_ALT|KEY_SHIFT|KEY_F12,

	KEY_CTRLALTF1            =KEY_CTRL|KEY_ALT|KEY_F1,
	KEY_CTRLALTF2            =KEY_CTRL|KEY_ALT|KEY_F2,
	KEY_CTRLALTF3            =KEY_CTRL|KEY_ALT|KEY_F3,
	KEY_CTRLALTF4            =KEY_CTRL|KEY_ALT|KEY_F4,
	KEY_CTRLALTF5            =KEY_CTRL|KEY_ALT|KEY_F5,
	KEY_CTRLALTF6            =KEY_CTRL|KEY_ALT|KEY_F6,
	KEY_CTRLALTF7            =KEY_CTRL|KEY_ALT|KEY_F7,
	KEY_CTRLALTF8            =KEY_CTRL|KEY_ALT|KEY_F8,
	KEY_CTRLALTF9            =KEY_CTRL|KEY_ALT|KEY_F9,
	KEY_CTRLALTF10           =KEY_CTRL|KEY_ALT|KEY_F10,
	KEY_CTRLALTF11           =KEY_CTRL|KEY_ALT|KEY_F11,
	KEY_CTRLALTF12           =KEY_CTRL|KEY_ALT|KEY_F12,

	KEY_CTRLHOME             =KEY_CTRL|KEY_HOME,
	KEY_CTRLUP               =KEY_CTRL|KEY_UP,
	KEY_CTRLPGUP             =KEY_CTRL|KEY_PGUP,
	KEY_CTRLLEFT             =KEY_CTRL|KEY_LEFT,
	KEY_CTRLRIGHT            =KEY_CTRL|KEY_RIGHT,
	KEY_CTRLEND              =KEY_CTRL|KEY_END,
	KEY_CTRLDOWN             =KEY_CTRL|KEY_DOWN,
	KEY_CTRLPGDN             =KEY_CTRL|KEY_PGDN,
	KEY_CTRLINS              =KEY_CTRL|KEY_INS,
	KEY_CTRLDEL              =KEY_CTRL|KEY_DEL,
	KEY_CTRLNUMDEL           =KEY_CTRL|KEY_NUMDEL,
	KEY_CTRLDECIMAL          =KEY_CTRL|KEY_DECIMAL,

	KEY_SHIFTHOME            =KEY_SHIFT|KEY_HOME,
	KEY_SHIFTUP              =KEY_SHIFT|KEY_UP,
	KEY_SHIFTPGUP            =KEY_SHIFT|KEY_PGUP,
	KEY_SHIFTLEFT            =KEY_SHIFT|KEY_LEFT,
	KEY_SHIFTRIGHT           =KEY_SHIFT|KEY_RIGHT,
	KEY_SHIFTEND             =KEY_SHIFT|KEY_END,
	KEY_SHIFTDOWN            =KEY_SHIFT|KEY_DOWN,
	KEY_SHIFTPGDN            =KEY_SHIFT|KEY_PGDN,
	KEY_SHIFTINS             =KEY_SHIFT|KEY_INS,
	KEY_SHIFTDEL             =KEY_SHIFT|KEY_DEL,
	KEY_SHIFTNUMDEL          =KEY_SHIFT|KEY_NUMDEL,
	KEY_SHIFTDECIMAL         =KEY_SHIFT|KEY_DECIMAL,

	KEY_ALTHOME              =KEY_ALT|KEY_HOME,
	KEY_ALTUP                =KEY_ALT|KEY_UP,
	KEY_ALTPGUP              =KEY_ALT|KEY_PGUP,
	KEY_ALTLEFT              =KEY_ALT|KEY_LEFT,
	KEY_ALTRIGHT             =KEY_ALT|KEY_RIGHT,
	KEY_ALTEND               =KEY_ALT|KEY_END,
	KEY_ALTDOWN              =KEY_ALT|KEY_DOWN,
	KEY_ALTPGDN              =KEY_ALT|KEY_PGDN,
	KEY_ALTINS               =KEY_ALT|KEY_INS,
	KEY_ALTDEL               =KEY_ALT|KEY_DEL,
	KEY_ALTNUMDEL            =KEY_ALT|KEY_NUMDEL,
	KEY_ALTDECIMAL           =KEY_ALT|KEY_DECIMAL,

	KEY_CTRLSHIFTHOME        =KEY_CTRL|KEY_SHIFT|KEY_HOME,
	KEY_CTRLSHIFTUP          =KEY_CTRL|KEY_SHIFT|KEY_UP,
	KEY_CTRLSHIFTPGUP        =KEY_CTRL|KEY_SHIFT|KEY_PGUP,
	KEY_CTRLSHIFTLEFT        =KEY_CTRL|KEY_SHIFT|KEY_LEFT,
	KEY_CTRLSHIFTRIGHT       =KEY_CTRL|KEY_SHIFT|KEY_RIGHT,
	KEY_CTRLSHIFTEND         =KEY_CTRL|KEY_SHIFT|KEY_END,
	KEY_CTRLSHIFTDOWN        =KEY_CTRL|KEY_SHIFT|KEY_DOWN,
	KEY_CTRLSHIFTPGDN        =KEY_CTRL|KEY_SHIFT|KEY_PGDN,
	KEY_CTRLSHIFTINS         =KEY_CTRL|KEY_SHIFT|KEY_INS,
	KEY_CTRLSHIFTDEL         =KEY_CTRL|KEY_SHIFT|KEY_DEL,
	KEY_CTRLSHIFTNUMDEL      =KEY_CTRL|KEY_SHIFT|KEY_NUMDEL,
	KEY_CTRLSHIFTDECIMAL     =KEY_CTRL|KEY_SHIFT|KEY_DECIMAL,

	KEY_ALTSHIFTHOME         =KEY_ALT|KEY_SHIFT|KEY_HOME,
	KEY_ALTSHIFTUP           =KEY_ALT|KEY_SHIFT|KEY_UP,
	KEY_ALTSHIFTPGUP         =KEY_ALT|KEY_SHIFT|KEY_PGUP,
	KEY_ALTSHIFTLEFT         =KEY_ALT|KEY_SHIFT|KEY_LEFT,
	KEY_ALTSHIFTRIGHT        =KEY_ALT|KEY_SHIFT|KEY_RIGHT,
	KEY_ALTSHIFTEND          =KEY_ALT|KEY_SHIFT|KEY_END,
	KEY_ALTSHIFTDOWN         =KEY_ALT|KEY_SHIFT|KEY_DOWN,
	KEY_ALTSHIFTPGDN         =KEY_ALT|KEY_SHIFT|KEY_PGDN,
	KEY_ALTSHIFTINS          =KEY_ALT|KEY_SHIFT|KEY_INS,
	KEY_ALTSHIFTDEL          =KEY_ALT|KEY_SHIFT|KEY_DEL,
	KEY_ALTSHIFTNUMDEL       =KEY_ALT|KEY_SHIFT|KEY_NUMDEL,
	KEY_ALTSHIFTDECIMAL      =KEY_ALT|KEY_SHIFT|KEY_DECIMAL,

	KEY_CTRLALTHOME          =KEY_CTRL|KEY_ALT|KEY_HOME,
	KEY_CTRLALTUP            =KEY_CTRL|KEY_ALT|KEY_UP,
	KEY_CTRLALTPGUP          =KEY_CTRL|KEY_ALT|KEY_PGUP,
	KEY_CTRLALTLEFT          =KEY_CTRL|KEY_ALT|KEY_LEFT,
	KEY_CTRLALTRIGHT         =KEY_CTRL|KEY_ALT|KEY_RIGHT,
	KEY_CTRLALTEND           =KEY_CTRL|KEY_ALT|KEY_END,
	KEY_CTRLALTDOWN          =KEY_CTRL|KEY_ALT|KEY_DOWN,
	KEY_CTRLALTPGDN          =KEY_CTRL|KEY_ALT|KEY_PGDN,
	KEY_CTRLALTINS           =KEY_CTRL|KEY_ALT|KEY_INS,

	KEY_CTRLNUMPAD0          =KEY_CTRL|KEY_NUMPAD0,
	KEY_CTRLNUMPAD1          =KEY_CTRL|KEY_NUMPAD1,
	KEY_CTRLNUMPAD2          =KEY_CTRL|KEY_NUMPAD2,
	KEY_CTRLNUMPAD3          =KEY_CTRL|KEY_NUMPAD3,
	KEY_CTRLNUMPAD4          =KEY_CTRL|KEY_NUMPAD4,
	KEY_CTRLNUMPAD5          =KEY_CTRL|KEY_NUMPAD5,
	KEY_CTRLNUMPAD6          =KEY_CTRL|KEY_NUMPAD6,
	KEY_CTRLNUMPAD7          =KEY_CTRL|KEY_NUMPAD7,
	KEY_CTRLNUMPAD8          =KEY_CTRL|KEY_NUMPAD8,
	KEY_CTRLNUMPAD9          =KEY_CTRL|KEY_NUMPAD9,

	KEY_SHIFTNUMPAD0         =KEY_SHIFT|KEY_NUMPAD0,
	KEY_SHIFTNUMPAD1         =KEY_SHIFT|KEY_NUMPAD1,
	KEY_SHIFTNUMPAD2         =KEY_SHIFT|KEY_NUMPAD2,
	KEY_SHIFTNUMPAD3         =KEY_SHIFT|KEY_NUMPAD3,
	KEY_SHIFTNUMPAD4         =KEY_SHIFT|KEY_NUMPAD4,
	KEY_SHIFTNUMPAD5         =KEY_SHIFT|KEY_NUMPAD5,
	KEY_SHIFTNUMPAD6         =KEY_SHIFT|KEY_NUMPAD6,
	KEY_SHIFTNUMPAD7         =KEY_SHIFT|KEY_NUMPAD7,
	KEY_SHIFTNUMPAD8         =KEY_SHIFT|KEY_NUMPAD8,
	KEY_SHIFTNUMPAD9         =KEY_SHIFT|KEY_NUMPAD9,

	KEY_CTRLSHIFTNUMPAD0     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD0,
	KEY_CTRLSHIFTNUMPAD1     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD1,
	KEY_CTRLSHIFTNUMPAD2     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD2,
	KEY_CTRLSHIFTNUMPAD3     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD3,
	KEY_CTRLSHIFTNUMPAD4     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD4,
	KEY_CTRLSHIFTNUMPAD5     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD5,
	KEY_CTRLSHIFTNUMPAD6     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD6,
	KEY_CTRLSHIFTNUMPAD7     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD7,
	KEY_CTRLSHIFTNUMPAD8     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD8,
	KEY_CTRLSHIFTNUMPAD9     =KEY_CTRL|KEY_SHIFT|KEY_NUMPAD9,

	KEY_CTRLALTNUMPAD0       =KEY_CTRL|KEY_ALT|KEY_NUMPAD0,
	KEY_CTRLALTNUMPAD1       =KEY_CTRL|KEY_ALT|KEY_NUMPAD1,
	KEY_CTRLALTNUMPAD2       =KEY_CTRL|KEY_ALT|KEY_NUMPAD2,
	KEY_CTRLALTNUMPAD3       =KEY_CTRL|KEY_ALT|KEY_NUMPAD3,
	KEY_CTRLALTNUMPAD4       =KEY_CTRL|KEY_ALT|KEY_NUMPAD4,
	KEY_CTRLALTNUMPAD5       =KEY_CTRL|KEY_ALT|KEY_NUMPAD5,
	KEY_CTRLALTNUMPAD6       =KEY_CTRL|KEY_ALT|KEY_NUMPAD6,
	KEY_CTRLALTNUMPAD7       =KEY_CTRL|KEY_ALT|KEY_NUMPAD7,
	KEY_CTRLALTNUMPAD8       =KEY_CTRL|KEY_ALT|KEY_NUMPAD8,
	KEY_CTRLALTNUMPAD9       =KEY_CTRL|KEY_ALT|KEY_NUMPAD9,

	KEY_ALTSHIFTNUMPAD0      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD0,
	KEY_ALTSHIFTNUMPAD1      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD1,
	KEY_ALTSHIFTNUMPAD2      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD2,
	KEY_ALTSHIFTNUMPAD3      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD3,
	KEY_ALTSHIFTNUMPAD4      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD4,
	KEY_ALTSHIFTNUMPAD5      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD5,
	KEY_ALTSHIFTNUMPAD6      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD6,
	KEY_ALTSHIFTNUMPAD7      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD7,
	KEY_ALTSHIFTNUMPAD8      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD8,
	KEY_ALTSHIFTNUMPAD9      =KEY_ALT|KEY_SHIFT|KEY_NUMPAD9,

	KEY_CTRLSLASH            =KEY_CTRL|KEY_SLASH,
	KEY_CTRLBACKSLASH        =KEY_CTRL|KEY_BACKSLASH,
	KEY_CTRLCLEAR            =KEY_CTRL|KEY_CLEAR,
	KEY_CTRLSHIFTCLEAR       =KEY_CTRL|KEY_SHIFT|KEY_CLEAR,
	KEY_CTRLALTCLEAR         =KEY_CTRL|KEY_ALT|KEY_CLEAR,
	KEY_CTRLADD              =KEY_CTRL|KEY_ADD,
	KEY_SHIFTADD             =KEY_SHIFT|KEY_ADD,

	KEY_CTRLSUBTRACT         =KEY_CTRL|KEY_SUBTRACT,
	KEY_ALTSUBTRACT          =KEY_ALT|KEY_SUBTRACT,
	KEY_SHIFTSUBTRACT        =KEY_SHIFT|KEY_SUBTRACT,
	KEY_CTRLMULTIPLY         =KEY_CTRL|KEY_MULTIPLY,

	KEY_CTRLBS               =KEY_CTRL|KEY_BS,
	KEY_ALTBS                =KEY_ALT|KEY_BS,
	KEY_CTRLSHIFTBS          =KEY_CTRL|KEY_SHIFT|KEY_BS,
	KEY_SHIFTBS              =KEY_SHIFT|KEY_BS,

	KEY_CTRLSHIFTTAB         =KEY_CTRL|KEY_SHIFT|KEY_TAB,
	KEY_CTRLTAB              =KEY_CTRL|KEY_TAB,
	KEY_SHIFTTAB             =KEY_SHIFT|KEY_TAB,

	KEY_CTRLENTER            =KEY_CTRL|KEY_ENTER,
	KEY_SHIFTENTER           =KEY_SHIFT|KEY_ENTER,
	KEY_ALTSHIFTENTER        =KEY_ALT|KEY_SHIFT|KEY_ENTER,
	KEY_CTRLALTENTER         =KEY_CTRL|KEY_ALT|KEY_ENTER,
	KEY_CTRLSHIFTENTER       =KEY_CTRL|KEY_SHIFT|KEY_ENTER,

	KEY_CTRLNUMENTER         =KEY_CTRL|KEY_NUMENTER,
	KEY_SHIFTNUMENTER        =KEY_SHIFT|KEY_NUMENTER,
	KEY_ALTSHIFTNUMENTER     =KEY_ALT|KEY_SHIFT|KEY_NUMENTER,
	KEY_CTRLALTNUMENTER      =KEY_CTRL|KEY_ALT|KEY_NUMENTER,
	KEY_CTRLSHIFTNUMENTER    =KEY_CTRL|KEY_SHIFT|KEY_NUMENTER,

	KEY_CTRLAPPS             =KEY_CTRL|KEY_APPS,
	KEY_ALTAPPS              =KEY_ALT|KEY_APPS,
	KEY_SHIFTAPPS            =KEY_SHIFT|KEY_APPS,
	KEY_CTRLSHIFTAPPS        =KEY_CTRL|KEY_SHIFT|KEY_APPS,
	KEY_ALTSHIFTAPPS         =KEY_ALT|KEY_SHIFT|KEY_APPS,
	KEY_CTRLALTAPPS          =KEY_CTRL|KEY_ALT|KEY_APPS,

	KEY_CTRLSPACE            =KEY_CTRL|KEY_SPACE,
	KEY_SHIFTSPACE           =KEY_SHIFT|KEY_SPACE,
	KEY_CTRLSHIFTSPACE       =KEY_CTRL|KEY_SHIFT|KEY_SPACE,

	KEY_ALT_BASE             =KEY_ALT,
	KEY_ALTSHIFT_BASE        =KEY_ALTSHIFT,
};
'''
