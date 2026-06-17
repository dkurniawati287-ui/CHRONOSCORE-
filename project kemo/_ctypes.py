# encoding: utf-8
# module _ctypes
# from C:\Users\T14\AppData\Local\Programs\Python\Python314\DLLs\_ctypes.pyd
# by generator 1.147
""" Create and manipulate C compatible data types in Python. """
# no imports

# Variables with simple values

CTYPES_MAX_ARGCOUNT = 1024

FUNCFLAG_CDECL = 1
FUNCFLAG_HRESULT = 2
FUNCFLAG_PYTHONAPI = 4
FUNCFLAG_STDCALL = 0

FUNCFLAG_USE_ERRNO = 8
FUNCFLAG_USE_LASTERROR = 16

RTLD_GLOBAL = 0
RTLD_LOCAL = 0

SIZEOF_TIME_T = 8

_cast_addr = 140705756345772

_memmove_addr = 140705761858544

_memoryview_at_addr = 140705756347140

_memset_addr = 140705761860240

_string_at_addr = 140705756347284

_wstring_at_addr = 140705756347376

__version__ = '1.1.0'

# functions

def addressof(*args, **kwargs): # real signature unknown
    """ Return the address of the C instance internal buffer """
    pass

def alignment(C_type): # real signature unknown; restored from __doc__
    """
    alignment(C type) -> integer
    alignment(C instance) -> integer
    Return the alignment requirements of a C instance
    """
    return 0

def buffer_info(*args, **kwargs): # real signature unknown
    """ Return buffer interface information """
    pass

def byref(*args, **kwargs): # real signature unknown
    """ Return a pointer lookalike to a C instance, only usable as function argument. """
    pass

def call_cdeclfunction(*args, **kwargs): # real signature unknown
    pass

def call_function(*args, **kwargs): # real signature unknown
    pass

def CopyComPointer(src, dst): # real signature unknown; restored from __doc__
    """ CopyComPointer(src, dst) -> HRESULT value """
    pass

def FormatError(integer=None): # real signature unknown; restored from __doc__
    """
    FormatError([integer]) -> string
    
    Convert a win32 error code into a string. If the error code is not
    given, the return value of a call to GetLastError() is used.
    """
    return ""

def FreeLibrary(handle): # real signature unknown; restored from __doc__
    """
    FreeLibrary(handle) -> void
    
    Free the handle of an executable previously loaded by LoadLibrary.
    """
    pass

def get_errno(*args, **kwargs): # real signature unknown
    pass

def get_last_error(*args, **kwargs): # real signature unknown
    pass

def LoadLibrary(name, load_flags): # real signature unknown; restored from __doc__
    """
    LoadLibrary(name, load_flags) -> handle
    
    Load an executable (usually a DLL), and return a handle to it.
    The handle may be used to locate exported functions in this
    module. load_flags are as defined for LoadLibraryEx in the
    Windows API.
    """
    pass

def PyObj_FromPtr(*args, **kwargs): # real signature unknown
    pass

def Py_DECREF(*args, **kwargs): # real signature unknown
    pass

def Py_INCREF(*args, **kwargs): # real signature unknown
    pass

def resize(*args, **kwargs): # real signature unknown
    pass

def set_errno(*args, **kwargs): # real signature unknown
    pass

def set_last_error(*args, **kwargs): # real signature unknown
    pass

def sizeof(*args, **kwargs): # real signature unknown
    """ Return the size in bytes of a C instance. """
    pass

def _check_HRESULT(*args, **kwargs): # real signature unknown
    pass

def _unpickle(*args, **kwargs): # real signature unknown
    pass

# classes

class ArgumentError(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class Array(_CData):
    """
    Abstract base class for arrays.
    
    The recommended way to create concrete array types is by multiplying any
    ctypes data type with a non-negative integer. Alternatively, you can subclass
    this type and define _length_ and _type_ class variables. Array elements can
    be read and written using standard subscript and slice accesses for slice
    reads, the resulting object is not itself an Array.
    """
    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass


class CField(object):
    """ Structure/Union member """
    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass

    bit_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """additional offset in bits (relative to byte_offset); zero for non-bitfields"""

    bit_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """size of this field in bits"""

    byte_offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """offset in bytes of this field. For bitfields: excludes bit_offset."""

    byte_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """size of this field in bytes"""

    is_anonymous = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if this field is anonymous"""

    is_bitfield = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """true if this is a bitfield"""

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name of this field"""

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """offset in bytes of this field (same as byte_offset)"""

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """size in bytes of this field. For bitfields, this is a legacy packed value; use byte_size instead"""

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """type of this field"""



class CFuncPtr(_CData):
    """ Function Pointer """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    argtypes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """specify the argument types"""

    errcheck = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """a function to check for errors"""

    restype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """specify the result type"""



class COMError(Exception):
    """ Raised when a COM method call failed. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


class Structure(_CData):
    """ Structure base class """
    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Union(_CData):
    """ Union base class """
    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class _Pointer(_CData):
    """ XXX to be provided """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the object this pointer points to (read-write)"""



class _SimpleCData(_CData):
    """ XXX to be provided """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __ctypes_from_outparam__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D632408050>'

__spec__ = None # (!) real value is "ModuleSpec(name='_ctypes', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D632408050>, origin='C:\\\\Users\\\\T14\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python314\\\\DLLs\\\\_ctypes.pyd')"

