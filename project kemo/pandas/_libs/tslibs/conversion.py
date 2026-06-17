# encoding: utf-8
# module pandas._libs.tslibs.conversion
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\tslibs\conversion.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\numpy\__init__.py
import datetime as __datetime


# functions

def cast_from_unit_vectorized(*args, **kwargs): # real signature unknown
    """ Vectorized analogue to cast_from_unit. """
    pass

def localize_pydatetime(*args, **kwargs): # real signature unknown
    """
    Take a datetime/Timestamp in UTC and localizes to timezone tz.
    
        Parameters
        ----------
        dt : datetime or Timestamp
        tz : tzinfo or None
    
        Returns
        -------
        localized : datetime or Timestamp
    """
    pass

def __reduce_cython__(*args, **kwargs): # real signature unknown
    pass

def __setstate_cython__(*args, **kwargs): # real signature unknown
    pass

# classes

class OutOfBoundsDatetime(ValueError):
    """
    Raised when the datetime is outside the range that can be represented.
    
        This error occurs when attempting to convert or parse a datetime value
        that exceeds the bounds supported by pandas' internal datetime
        representation.
    
        See Also
        --------
        to_datetime : Convert argument to datetime.
        Timestamp : Pandas replacement for python ``datetime.datetime`` object.
    
        Examples
        --------
        >>> pd.to_datetime("08335394550")
        Traceback (most recent call last):
        OutOfBoundsDatetime: Parsing "08335394550" to datetime overflows,
        at position 0
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class timezone(__datetime.tzinfo):
    """ Fixed offset from UTC implementation of tzinfo. """
    def dst(self, *args, **kwargs): # real signature unknown
        """ Return None. """
        pass

    def fromutc(self, *args, **kwargs): # real signature unknown
        """ datetime in UTC -> datetime in local time. """
        pass

    def tzname(self, *args, **kwargs): # real signature unknown
        """ If name is specified when timezone is created, returns the name.  Otherwise returns offset as 'UTC(+|-)HH:MM'. """
        pass

    def utcoffset(self, *args, **kwargs): # real signature unknown
        """ Return fixed offset. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getinitargs__(self, *args, **kwargs): # real signature unknown
        """ pickle support """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    max = datetime.timezone(datetime.timedelta(seconds=86340))
    min = datetime.timezone(datetime.timedelta(days=-1, seconds=60))
    utc = datetime.timezone.utc


class _TSObject(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    creso = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x0000018506050220>'


# variables with complex values

DT64NS_DTYPE = None # (!) real value is "dtype('<M8[ns]')"

TD64NS_DTYPE = None # (!) real value is "dtype('<m8[ns]')"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001857FD2A930>'

__pyx_capi__ = {
    'cast_from_unit': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, PyObject *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_cast_from_unit *__pyx_optional_args)" at 0x00000185060306D0>'
    'convert_datetime_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyDateTime_DateTime *, PyDateTime_TZInfo *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_datetime_to_tsobject *__pyx_optional_args)" at 0x0000018506033C90>'
    'convert_str_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyObject *, PyDateTime_TZInfo *, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_str_to_tsobject *__pyx_optional_args)" at 0x0000018506050090>'
    'convert_to_tsobject': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *(PyObject *, PyDateTime_TZInfo *, PyObject *, int, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10conversion_convert_to_tsobject *__pyx_optional_args)" at 0x0000018506050040>'
    'get_datetime64_nanos': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyObject *, NPY_DATETIMEUNIT)" at 0x00000185060339C0>'
    'localize_pydatetime': None, # (!) real value is '<capsule object "PyDateTime_DateTime *(PyDateTime_DateTime *, PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x0000018506033AB0>'
    'maybe_localize_tso': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_obj_6pandas_5_libs_6tslibs_10conversion__TSObject *, PyDateTime_TZInfo *, NPY_DATETIMEUNIT)" at 0x0000018506033A60>'
    'parse_pydatetime': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (PyDateTime_DateTime *, npy_datetimestruct *, NPY_DATETIMEUNIT)" at 0x0000018506033A10>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.conversion', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001857FD2A930>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\conversion.cp314-win_amd64.pyd')"

__test__ = {}

