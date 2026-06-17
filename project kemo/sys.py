# encoding: utf-8
# module sys
# from (built-in)
# by generator 1.147
"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_exc - the last uncaught exception
  Only available in an interactive session after a
  traceback has been printed.
last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are the (deprecated) legacy representation of last_exc.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
dllhandle -- [Windows only] integer handle of the Python DLL
winver -- [Windows only] version number of the Python DLL
_enablelegacywindowsfsencoding -- [Windows only]
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exception() -- return the current thread's active exception
exc_info() -- return information about the current thread's active exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
"""

# imports
import sys.monitoring as monitoring # <module 'sys.monitoring'>
import sys._jit as _jit # <module 'sys._jit'>
from _io import __stderr__, __stdin__, __stdout__, stderr, stdin, stdout


# Variables with simple values

api_version = 1013

base_exec_prefix = 'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314'

base_prefix = 'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314'

byteorder = 'little'

copyright = 'Copyright (c) 2001 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

dllhandle = 140703563120640

dont_write_bytecode = True

executable = 'C:\\Users\\T14\\PyCharmMiscProject\\.venv\\Scripts\\python.exe'

exec_prefix = 'C:\\Users\\T14\\PyCharmMiscProject\\.venv'

float_repr_style = 'short'

hexversion = 51249392

maxsize = 9223372036854775807
maxunicode = 1114111

platform = 'win32'
platlibdir = 'DLLs'

prefix = 'C:\\Users\\T14\\PyCharmMiscProject\\.venv'

pycache_prefix = None

version = '3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]'

winver = '3.14'

_base_executable = 'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'

_framework = ''

_home = 'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314'

_stdlib_dir = 'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314\\Lib'

_vpath = '..\\..'

# functions

def activate_stack_trampoline(*args, **kwargs): # real signature unknown
    """ Activate stack profiler trampoline *backend*. """
    pass

def addaudithook(*args, **kwargs): # real signature unknown
    """ Adds a new audit hook callback. """
    pass

def audit(*args, **kwargs): # real signature unknown
    """ Passes the event to any audit hooks that are attached. """
    pass

def breakpointhook(*args, **kwargs): # real signature unknown
    """ This hook function is called by built-in breakpoint(). """
    pass

def call_tracing(*args, **kwargs): # real signature unknown
    """
    Call func(*args), while tracing is enabled.
    
    The tracing state is saved, and restored afterwards.  This is intended
    to be called from a debugger from a checkpoint, to recursively debug
    some other code.
    """
    pass

def deactivate_stack_trampoline(*args, **kwargs): # real signature unknown
    """
    Deactivate the current stack profiler trampoline backend.
    
    If no stack profiler is activated, this function has no effect.
    """
    pass

def displayhook(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def excepthook(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def exception(*args, **kwargs): # real signature unknown
    """
    Return the current exception.
    
    Return the most recent exception caught by an except clause
    in the current stack frame or in an older stack frame, or None
    if no such exception exists.
    """
    pass

def exc_info(*args, **kwargs): # real signature unknown
    """
    Return current exception information: (type, value, traceback).
    
    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.
    """
    pass

def exit(*args, **kwargs): # real signature unknown
    """
    Exit the interpreter by raising SystemExit(status).
    
    If the status is omitted or None, it defaults to zero (i.e., success).
    If the status is an integer, it will be used as the system exit status.
    If it is another kind of object, it will be printed and the system
    exit status will be one (i.e., failure).
    """
    pass

def getallocatedblocks(*args, **kwargs): # real signature unknown
    """ Return the number of memory blocks currently allocated. """
    pass

def getdefaultencoding(*args, **kwargs): # real signature unknown
    """ Return the current default encoding used by the Unicode implementation. """
    pass

def getfilesystemencodeerrors(*args, **kwargs): # real signature unknown
    """ Return the error mode used Unicode to OS filename conversion. """
    pass

def getfilesystemencoding(*args, **kwargs): # real signature unknown
    """ Return the encoding used to convert Unicode filenames to OS filenames. """
    pass

def getprofile(*args, **kwargs): # real signature unknown
    """
    Return the profiling function set with sys.setprofile.
    
    See the profiler chapter in the library manual.
    """
    pass

def getrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Return the current value of the recursion limit.
    
    The recursion limit is the maximum depth of the Python interpreter
    stack.  This limit prevents infinite recursion from causing an overflow
    of the C stack and crashing Python.
    """
    pass

def getrefcount(): # real signature unknown; restored from __doc__
    """
    Return the reference count of object.
    
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().
    """
    pass

def getsizeof(p_object, default=None): # real signature unknown; restored from __doc__
    """
    getsizeof(object [, default]) -> int
    
    Return the size of object in bytes.
    """
    return 0

def getswitchinterval(*args, **kwargs): # real signature unknown
    """ Return the current thread switch interval; see sys.setswitchinterval(). """
    pass

def gettrace(*args, **kwargs): # real signature unknown
    """
    Return the global debug tracing function set with sys.settrace.
    
    See the debugger chapter in the library manual.
    """
    pass

def getunicodeinternedsize(*args, **kwargs): # real signature unknown
    """ Return the number of elements of the unicode interned dictionary """
    pass

def getwindowsversion(*args, **kwargs): # real signature unknown
    """
    Return info about the running version of Windows as a named tuple.
    
    The members are named: major, minor, build, platform, service_pack,
    service_pack_major, service_pack_minor, suite_mask, product_type and
    platform_version. For backward compatibility, only the first 5 items
    are available by indexing. All elements are numbers, except
    service_pack and platform_type which are strings, and platform_version
    which is a 3-tuple. Platform is always 2. Product_type may be 1 for a
    workstation, 2 for a domain controller, 3 for a server.
    Platform_version is a 3-tuple containing a version number that is
    intended for identifying the OS rather than feature detection.
    """
    pass

def get_asyncgen_hooks(*args, **kwargs): # real signature unknown
    """
    Return the installed asynchronous generators hooks.
    
    This returns a namedtuple of the form (firstiter, finalizer).
    """
    pass

def get_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """ Check status of origin tracking for coroutine objects in this thread. """
    pass

def get_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Return the maximum string digits limit for non-binary int<->str conversions. """
    pass

def intern(*args, **kwargs): # real signature unknown
    """
    ``Intern'' the given string.
    
    This enters the string in the (global) table of interned strings whose
    purpose is to speed up dictionary lookups. Return the string itself or
    the previously interned string object with the same value.
    """
    pass

def is_finalizing(*args, **kwargs): # real signature unknown
    """ Return True if Python is exiting. """
    pass

def is_remote_debug_enabled(*args, **kwargs): # real signature unknown
    """ Return True if remote debugging is enabled, False otherwise. """
    pass

def is_stack_trampoline_active(*args, **kwargs): # real signature unknown
    """ Return *True* if a stack profiler trampoline is active. """
    pass

def remote_exec(*args, **kwargs): # real signature unknown
    """
    Executes a file containing Python code in a given remote Python process.
    
    This function returns immediately, and the code will be executed by the
    target process's main thread at the next available opportunity, similarly
    to how signals are handled. There is no interface to determine when the
    code has been executed. The caller is responsible for making sure that
    the file still exists whenever the remote process tries to read it and that
    it hasn't been overwritten.
    
    The remote process must be running a CPython interpreter of the same major
    and minor version as the local process. If either the local or remote
    interpreter is pre-release (alpha, beta, or release candidate) then the
    local and remote interpreters must be the same exact version.
    
    Args:
         pid (int): The process ID of the target Python process.
         script (str|bytes): The path to a file containing
             the Python code to be executed.
    """
    pass

def setprofile(*args, **kwargs): # real signature unknown
    """
    Set the profiling function.
    
    It will be called on each function call and return.  See the profiler
    chapter in the library manual.
    """
    pass

def setrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Set the maximum depth of the Python interpreter stack to n.
    
    This limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python.  The highest possible limit is platform-
    dependent.
    """
    pass

def setswitchinterval(*args, **kwargs): # real signature unknown
    """
    Set the ideal thread switching delay inside the Python interpreter.
    
    The actual frequency of switching threads can be lower if the
    interpreter executes long sequences of uninterruptible code
    (this is implementation-specific and workload-dependent).
    
    The parameter must represent the desired switching delay in seconds
    A typical value is 0.005 (5 milliseconds).
    """
    pass

def settrace(*args, **kwargs): # real signature unknown
    """
    Set the global debug tracing function.
    
    It will be called on each function call.  See the debugger chapter
    in the library manual.
    """
    pass

def set_asyncgen_hooks(firstiter=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_asyncgen_hooks([firstiter] [, finalizer])
    
    Set a finalizer for async generators objects.
    """
    pass

def set_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """
    Enable or disable origin tracking for coroutine objects in this thread.
    
    Coroutine objects will track 'depth' frames of traceback information
    about where they came from, available in their cr_origin attribute.
    
    Set a depth of 0 to disable.
    """
    pass

def set_int_max_str_digits(*args, **kwargs): # real signature unknown
    """ Set the maximum string digits limit for non-binary int<->str conversions. """
    pass

def unraisablehook(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

def _baserepl(*args, **kwargs): # real signature unknown
    """ Private function for getting the base REPL """
    pass

def _clear_internal_caches(*args, **kwargs): # real signature unknown
    """ Clear all internal performance-related caches. """
    pass

def _clear_type_cache(*args, **kwargs): # real signature unknown
    """ Clear the internal type lookup cache. """
    pass

def _clear_type_descriptors(*args, **kwargs): # real signature unknown
    """
    Private function for clearing certain descriptors from a type's dictionary.
    
    See gh-135228 for context.
    """
    pass

def _current_exceptions(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's identifier to its current raised exception.
    
    This function should be used for specialized purposes only.
    """
    pass

def _current_frames(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's thread id to its current stack frame.
    
    This function should be used for specialized purposes only.
    """
    pass

def _debugmallocstats(*args, **kwargs): # real signature unknown
    """
    Print summary info to stderr about the state of pymalloc's structures.
    
    In Py_DEBUG mode, also perform some expensive internal consistency
    checks.
    """
    pass

def _dump_tracelets(*args, **kwargs): # real signature unknown
    """ Dump the graph of tracelets in graphviz format """
    pass

def _enablelegacywindowsfsencoding(*args, **kwargs): # real signature unknown
    """
    Changes the default filesystem encoding to mbcs:replace.
    
    This is done for consistency with earlier versions of Python. See PEP
    529 for more information.
    
    This is equivalent to defining the PYTHONLEGACYWINDOWSFSENCODING
    environment variable before launching Python.
    """
    pass

def _getframe(*args, **kwargs): # real signature unknown
    """
    Return a frame object from the call stack.
    
    If optional integer depth is given, return the frame object that many
    calls below the top of the stack.  If that is deeper than the call
    stack, ValueError is raised.  The default for depth is zero, returning
    the frame at the top of the call stack.
    
    This function should be used for internal and specialized purposes
    only.
    """
    pass

def _getframemodulename(*args, **kwargs): # real signature unknown
    """
    Return the name of the module for a calling frame.
    
    The default depth returns the module containing the call to this API.
    A more typical use in a library will pass a depth of 1 to get the user's
    module rather than the library module.
    
    If no frame, module, or name can be found, returns None.
    """
    pass

def _get_cpu_count_config(*args, **kwargs): # real signature unknown
    """ Private function for getting PyConfig.cpu_count """
    pass

def _is_gil_enabled(*args, **kwargs): # real signature unknown
    """ Return True if the GIL is currently enabled and False otherwise. """
    pass

def _is_immortal(*args, **kwargs): # real signature unknown
    """
    Return True if the given object is "immortal" per PEP 683.
    
    This function should be used for specialized purposes only.
    """
    pass

def _is_interned(*args, **kwargs): # real signature unknown
    """ Return True if the given string is "interned". """
    pass

def _setprofileallthreads(*args, **kwargs): # real signature unknown
    """
    Set the profiling function in all running threads belonging to the current interpreter.
    
    It will be called on each function call and return.  See the profiler
    chapter in the library manual.
    """
    pass

def _settraceallthreads(*args, **kwargs): # real signature unknown
    """
    Set the global debug tracing function in all running threads belonging to the current interpreter.
    
    It will be called on each function call. See the debugger chapter
    in the library manual.
    """
    pass

def __breakpointhook__(*args, **kwargs): # real signature unknown
    """ This hook function is called by built-in breakpoint(). """
    pass

def __displayhook__(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def __excepthook__(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def __interactivehook__(): # reliably restored by inspect
    """
    Configure readline completion on interactive prompts.
    
    If the readline module can be imported, the hook will set the Tab key
    as completion key and register ~/.python_history as history file.
    This can be overridden in the sitecustomize or usercustomize module,
    or in a PYTHONSTARTUP file.
    """
    pass

def __unraisablehook__(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
    All methods are either class or static methods to avoid the need to
    instantiate the class.
    """
    @staticmethod
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    @staticmethod
    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
        This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 974, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x0000021212B6AB90>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x0000021212B6AC40>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x0000021212B6ACF0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x0000021212B6AE50>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x0000021212B6AFB0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x0000021212B6B110>)>, 'load_module': <classmethod(<function _load_module_shim at 0x0000021212B69DD0>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 974
    __static_attributes__ = ()


# variables with complex values

argv = [] # real value of type <class 'list'> skipped

builtin_module_names = () # real value of type <class 'tuple'> skipped

flags = (
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    False,
    0,
    0,
    False,
    4300,
)

float_info = (
    1.7976931348623157e+308,
    1024,
    308,
    2.2250738585072014e-308,
    -1021,
    -307,
    15,
    53,
    2.220446049250313e-16,
    2,
    1,
)

hash_info = (
    64,
    2305843009213693951,
    314159,
    0,
    1000003,
    'siphash13',
    64,
    128,
    0,
)

implementation = None # (!) real value is "namespace(name='cpython', cache_tag='cpython-314', version=sys.version_info(major=3, minor=14, micro=0, releaselevel='final', serial=0), hexversion=51249392, supports_isolated_interpreters=True)"

int_info = (
    30,
    4,
    4300,
    640,
)

meta_path = [
    None, # (!) real value is '<_virtualenv._Finder object at 0x0000021212E44AD0>'
    __loader__,
    None, # (!) real value is "<class '_frozen_importlib.FrozenImporter'>"
    None, # (!) real value is "<class '_frozen_importlib_external.PathFinder'>"
    None, # (!) real value is '<six._SixMetaPathImporter object at 0x000002121392AA50>'
]

modules = {} # real value of type <class 'dict'> skipped

orig_argv = [
    'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314\\python.exe',
    '-B',
    '-c',
    'from multiprocessing.spawn import spawn_main; spawn_main(parent_pid=4116, pipe_handle=592)',
    '--multiprocessing-fork',
]

path = [
    'C:\\Program Files\\JetBrains\\PyCharm 2026.1.2\\plugins\\python-ce\\helpers',
    'C:\\Program Files\\JetBrains\\PyCharm 2026.1.2\\plugins\\python-ce\\helpers\\generator3',
    'C:\\Program Files\\JetBrains\\PyCharm 2026.1.2\\plugins\\python-ce\\helpers',
    'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314\\python314.zip',
    'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314\\DLLs',
    'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314\\Lib',
    'C:\\Users\\T14\\AppData\\Local\\Programs\\Python\\Python314',
    'C:\\Users\\T14\\PyCharmMiscProject\\.venv',
    'C:\\Users\\T14\\PyCharmMiscProject\\.venv\\Lib\\site-packages',
    'C:/Users/T14/AppData/Local/Programs/Python/Python314/DLLs',
    'C:/Users/T14/AppData/Local/Programs/Python/Python314/Lib',
    'C:/Users/T14/AppData/Local/Programs/Python/Python314',
    'C:/Users/T14/PyCharmMiscProject/.venv',
    'C:/Users/T14/PyCharmMiscProject/.venv/Lib/site-packages',
]

path_hooks = [
    None, # (!) real value is "<class 'zipimport.zipimporter'>"
    None, # (!) real value is '<function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x0000021212B68300>'
]

path_importer_cache = {} # real value of type <class 'dict'> skipped

stdlib_module_names = None # (!) real value is "frozenset({'rlcompleter', '_ssl', 'symtable', '_multiprocessing', 'tarfile', '_typing', 'configparser', 'profile', '_hashlib', '_overlapped', 'sqlite3', 'gzip', '_codecs_tw', '_bz2', '_sqlite3', 'colorsys', 'weakref', 'winreg', 'argparse', 'netrc', 'posixpath', 'turtle', 'graphlib', '_apple_support', 'asyncio', 'posix', 'copy', 'heapq', '_codecs_cn', 'importlib', 'json', 'grp', '_locale', 'difflib', 'typing', 'encodings', 'statistics', '_datetime', '_pydatetime', 'bisect', 'unicodedata', 'reprlib', 'pdb', '_opcode', 'compileall', 'struct', '_aix_support', '_struct', 'dbm', 'ssl', 'doctest', 'hashlib', 'webbrowser', 'operator', 'random', 'optparse', 'marshal', 'bz2', 'cProfile', 'decimal', 'mmap', 'turtledemo', 'csv', '_frozen_importlib_external', '_pylong', 'builtins', 'plistlib', 'site', '_opcode_metadata', '_posixsubprocess', '_tracemalloc', '_weakref', 'pprint', '_ast', 'xml', 'hmac', 'zlib', 'array', '_sre', 'modulefinder', 'pathlib', 'time', 'base64', '_asyncio', 'tty', 'unittest', '_interpchannels', '_functools', '_pyio', 'select', 'ntpath', 'readline', '_statistics', 'wsgiref', 'gettext', 'secrets', '_string', 'fileinput', 'wave', 'code', 'pickletools', 'cmath', '_suggestions', 'faulthandler', '__future__', '_posixshmem', '_pyrepl', '_sysconfig', 'sysconfig', 'contextlib', 'atexit', 'pyclbr', 'resource', 'curses', 'annotationlib', 'getpass', '_codecs', '_osx_support', 'sre_constants', '_remote_debugging', 'msvcrt', '_strptime', 'queue', '_md5', 'email', 're', 'ftplib', '_interpreters', 'shelve', '_tkinter', '_symtable', 'fcntl', 'uuid', 'ast', 'pty', 'tkinter', 'platform', '_ctypes', 'zipimport', '_gdbm', '_hmac', '_curses_panel', '_weakrefset', '_socket', 'enum', 'quopri', 'selectors', 'calendar', 'locale', 'collections', 'dis', 'functools', 'math', 'idlelib', '_csv', '_lzma', '_frozen_importlib', '_ios_support', 'multiprocessing', 'binascii', '_scproxy', 'nturl2path', 'cmd', 'pyexpat', 'nt', '_multibytecodec', '_heapq', 'stat', 'zipapp', 'shlex', 'traceback', 'gc', 'pydoc', 'itertools', 'concurrent', '_codecs_jp', '_collections_abc', 'zipfile', 'threading', 'runpy', 'mimetypes', 'os', '_pickle', 'tracemalloc', '_wmi', '_sha2', 'http', 'sre_compile', 'zoneinfo', 'types', '_py_abc', 'io', '_interpqueues', 'keyword', '_markupbase', 'glob', 'sched', '_py_warnings', 'imaplib', 'codeop', 'copyreg', '_operator', 'pickle', 'pstats', 'sys', 'antigravity', 'termios', 'html', 'shutil', 'sre_parse', 'winsound', 'tempfile', 'compression', 'pwd', 'lzma', 'abc', '_contextvars', 'smtplib', '_sha1', 'linecache', 'tokenize', '_collections', '_queue', '_winapi', 'errno', '_types', '_codecs_kr', '_compat_pickle', '_curses', '_stat', '_tokenize', '_elementtree', 'opcode', 'tabnanny', '_android_support', 'genericpath', '_json', 'inspect', 'py_compile', '_dbm', 'contextvars', '_abc', 'logging', '_imp', '_zoneinfo', '_sitebuiltins', 'syslog', 'timeit', '_codecs_hk', '_signal', 'datetime', 'fnmatch', 'fractions', 'subprocess', 'stringprep', 'codecs', '_bisect', 'socketserver', 'signal', 'getopt', 'xmlrpc', 'filecmp', 'textwrap', 'trace', 'ipaddress', '_pydecimal', 'this', 'urllib', '_ast_unparse', 'ctypes', '_warnings', 'ensurepip', 'numbers', 'string', 'warnings', 'socket', 'bdb', '_blake2', '_thread', 'mailbox', '_decimal', '_threading_local', '_zstd', '_lsprof', 'pydoc_data', 'poplib', '_sha3', 'token', '_codecs_iso2022', '_colorize', '_random', '_uuid', 'pkgutil', 'tomllib', 'venv', 'dataclasses', '_io'})"

thread_info = (
    'nt',
    None,
    None,
)

version_info = (
    3,
    14,
    0,
    'final',
    0,
)

warnoptions = []

_git = (
    'CPython',
    'tags/v3.14.0',
    'ebf955d',
)

_xoptions = {}

__spec__ = None # (!) real value is "ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

# intermittent names
exc_value = Exception()
exc_traceback=None
