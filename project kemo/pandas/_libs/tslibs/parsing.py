# encoding: utf-8
# module pandas._libs.tslibs.parsing
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\tslibs\parsing.cp314-win_amd64.pyd
# by generator 1.147
""" Parsing functions for datetime and datetime-like strings. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\re\__init__.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\warnings.py
import numpy as np # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.strptime import array_strptime

import datetime as __datetime
import decimal as __decimal


# functions

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def get_option(pat): # reliably restored by inspect
    """
    Retrieve the value of the specified option.
    
    This method allows users to query the current value of a given option
    in the pandas configuration system. Options control various display,
    performance, and behavior-related settings within pandas.
    
    Parameters
    ----------
    pat : str
        Regexp which should match a single option.
    
        .. warning::
    
            Partial matches are supported for convenience, but unless you use the
            full option name (e.g. x.y.z.option_name), your code may break in future
            versions if new options with similar names are introduced.
    
    Returns
    -------
    Any
        The value of the option.
    
    Raises
    ------
    OptionError : if no such option exists
    
    See Also
    --------
    set_option : Set the value of the specified option or options.
    reset_option : Reset one or more options to their default value.
    describe_option : Print the description for one or more registered options.
    
    Notes
    -----
    For all available options, please view the :ref:`User Guide <options.available>`
    or use ``pandas.describe_option()``.
    
    Examples
    --------
    >>> pd.get_option("display.max_columns")  # doctest: +SKIP
    4
    """
    pass

def get_rule_month(D): # real signature unknown; restored from __doc__
    """
    Return starting month of given freq, default is December.
    
        Parameters
        ----------
        source : str
            Derived from `freq.rule_code` or `freq.freqstr`.
    
        Returns
        -------
        rule_month: str
    
        Examples
        --------
        >>> get_rule_month('D')
        'DEC'
    
        >>> get_rule_month('A-JAN')
        'JAN'
    """
    pass

def guess_datetime_format(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Guess the datetime format of a given datetime string.
    
        This function attempts to deduce the format of a given datetime string. It is
        useful for situations where the datetime format is unknown and needs to be
        determined for proper parsing. The function is not guaranteed to return a format.
    
        Parameters
        ----------
        dt_str : str
            Datetime string to guess the format of.
        dayfirst : bool, default False
            If True parses dates with the day first, eg 20/01/2005
    
            .. warning::
                dayfirst=True is not strict, but will prefer to parse
                with day first (this is a known bug).
    
        Returns
        -------
        str or None : ret
            datetime format string (for `strftime` or `strptime`),
            or None if it can't be guessed.
    
        See Also
        --------
        to_datetime : Convert argument to datetime.
        Timestamp : Pandas replacement for python datetime.datetime object.
        DatetimeIndex : Immutable ndarray-like of datetime64 data.
    
        Examples
        --------
        >>> from pandas.tseries.api import guess_datetime_format
        >>> guess_datetime_format('09/13/2023')
        '%m/%d/%Y'
    
        >>> guess_datetime_format('2023|September|13')
    """
    pass

def parse_datetime_string_with_reso(*args, **kwargs): # real signature unknown
    """
    Try hard to parse datetime string, leveraging dateutil plus some extra
        goodies like quarter recognition.
    
        Parameters
        ----------
        date_string : str
        freq : str or None, default None
            Helps with interpreting time string if supplied
            Corresponds to `offset.rule_code`
        dayfirst : bool, default None
            If None uses default from print_config
        yearfirst : bool, default None
            If None uses default from print_config
    
        Returns
        -------
        datetime
        str
            Describing resolution of parsed string.
    
        Raises
        ------
        ValueError : preliminary check suggests string is not datetime
        DateParseError : error within dateutil
    """
    pass

def py_parse_datetime_string(*args, **kwargs): # real signature unknown
    pass

def quarter_to_myear(*args, **kwargs): # real signature unknown
    """
    A quarterly frequency defines a "year" which may not coincide with
        the calendar-year.  Find the calendar-year and calendar-month associated
        with the given year and quarter under the `freq`-derived calendar.
    
        Parameters
        ----------
        year : int
        quarter : int
        freq : str or None
    
        Returns
        -------
        year : int
        month : int
    
        See Also
        --------
        Period.qyear
    """
    pass

def try_parse_dates(*args, **kwargs): # real signature unknown
    pass

def _DATEUTIL_LEXER_SPLIT(*args, **kwargs): # real signature unknown
    pass

def _does_string_look_like_datetime(*args, **kwargs): # real signature unknown
    """
    Checks whether given string is a datetime: it has to start with '0' or
        be greater than 1000.
    
        Parameters
        ----------
        py_string: str
    
        Returns
        -------
        bool
            Whether given string is potentially a datetime.
    """
    pass

# classes

class DateParseError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class InvalidOperation(__decimal.DecimalException):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


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


class tzoffset(__datetime.tzinfo):
    """
    A simple class for representing a fixed offset from UTC.
    
    :param name:
        The timezone name, to be returned when ``tzname()`` is called.
    :param offset:
        The time zone offset in seconds, or (since version 2.6.0, represented
        as a :py:class:`datetime.timedelta` object).
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        # no doc
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
        zone.
        
        :param dt:
            A :py:class:`datetime.datetime`, naive or time zone aware.
        :return:
            Returns ``True`` if ambiguous, ``False`` otherwise.
        
        .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, name, offset): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _cache_lock = None # (!) real value is '<unlocked _thread.lock object at 0x00000190BF265850>'
    _TzOffsetFactory__instances = None # (!) real value is '<WeakValueDictionary at 0x190bf557ce0>'
    _TzOffsetFactory__strong_cache = OrderedDict()
    _TzOffsetFactory__strong_cache_size = 8
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'dateutil.tz.tz', '__firstlineno__': 132, '__doc__': '\\nA simple class for representing a fixed offset from UTC.\\n\\n:param name:\\n    The timezone name, to be returned when ``tzname()`` is called.\\n:param offset:\\n    The time zone offset in seconds, or (since version 2.6.0, represented\\n    as a :py:class:`datetime.timedelta` object).\\n', '__init__': <function tzoffset.__init__ at 0x00000190BF65E400>, 'utcoffset': <function tzoffset.utcoffset at 0x00000190BF65E4B0>, 'dst': <function tzoffset.dst at 0x00000190BF65E560>, 'tzname': <function tzoffset.tzname at 0x00000190BF65E610>, 'fromutc': <function tzoffset.fromutc at 0x00000190BF65E770>, 'is_ambiguous': <function tzoffset.is_ambiguous at 0x00000190BF65E820>, '__eq__': <function tzoffset.__eq__ at 0x00000190BF65E8D0>, '__hash__': None, '__ne__': <function tzoffset.__ne__ at 0x00000190BF65E980>, '__repr__': <function tzoffset.__repr__ at 0x00000190BF65EA30>, '__reduce__': <method '__reduce__' of 'object' objects>, '__static_attributes__': ('_name', '_offset'), '__dict__': <attribute '__dict__' of 'tzoffset' objects>, '__weakref__': <attribute '__weakref__' of 'tzoffset' objects>, '_TzOffsetFactory__instances': <WeakValueDictionary at 0x190bf557ce0>, '_TzOffsetFactory__strong_cache': OrderedDict(), '_TzOffsetFactory__strong_cache_size': 8, '_cache_lock': <unlocked _thread.lock object at 0x00000190BF265850>})"
    __firstlineno__ = 132
    __hash__ = None
    __static_attributes__ = (
        '_name',
        '_offset',
    )


class _dateutil_tzutc(__datetime.tzinfo):
    """
    This is a tzinfo object that represents the UTC time zone.
    
    **Examples:**
    
    .. doctest::
    
        >>> from datetime import *
        >>> from dateutil.tz import *
    
        >>> datetime.now()
        datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)
    
        >>> datetime.now(tzutc())
        datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())
    
        >>> datetime.now(tzutc()).tzname()
        'UTC'
    
    .. versionchanged:: 2.7.0
        ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will
        always return the same object.
    
        .. doctest::
    
            >>> from dateutil.tz import tzutc, UTC
            >>> tzutc() is tzutc()
            True
            >>> tzutc() is UTC
            True
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """
        Fast track version of fromutc() returns the original ``dt`` object for
        any valid :py:class:`datetime.datetime` object.
        """
        pass

    def is_ambiguous(self, dt): # reliably restored by inspect
        """
        Whether or not the "wall time" of a given datetime is ambiguous in this
        zone.
        
        :param dt:
            A :py:class:`datetime.datetime`, naive or time zone aware.
        
        
        :return:
            Returns ``True`` if ambiguous, ``False`` otherwise.
        
        .. versionadded:: 2.6.0
        """
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Helper for pickle. """
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _TzSingleton__instance = tzutc()
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'dateutil.tz.tz\', \'__firstlineno__\': 41, \'__doc__\': "\\nThis is a tzinfo object that represents the UTC time zone.\\n\\n**Examples:**\\n\\n.. doctest::\\n\\n    >>> from datetime import *\\n    >>> from dateutil.tz import *\\n\\n    >>> datetime.now()\\n    datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)\\n\\n    >>> datetime.now(tzutc())\\n    datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())\\n\\n    >>> datetime.now(tzutc()).tzname()\\n    \'UTC\'\\n\\n.. versionchanged:: 2.7.0\\n    ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will\\n    always return the same object.\\n\\n    .. doctest::\\n\\n        >>> from dateutil.tz import tzutc, UTC\\n        >>> tzutc() is tzutc()\\n        True\\n        >>> tzutc() is UTC\\n        True\\n", \'utcoffset\': <function tzutc.utcoffset at 0x00000190BF65DDD0>, \'dst\': <function tzutc.dst at 0x00000190BF65DE80>, \'tzname\': <function tzutc.tzname at 0x00000190BF65DF30>, \'is_ambiguous\': <function tzutc.is_ambiguous at 0x00000190BF65DFE0>, \'fromutc\': <function tzutc.fromutc at 0x00000190BF65E140>, \'__eq__\': <function tzutc.__eq__ at 0x00000190BF65E1F0>, \'__hash__\': None, \'__ne__\': <function tzutc.__ne__ at 0x00000190BF65E2A0>, \'__repr__\': <function tzutc.__repr__ at 0x00000190BF65E350>, \'__reduce__\': <method \'__reduce__\' of \'object\' objects>, \'__static_attributes__\': (), \'__dict__\': <attribute \'__dict__\' of \'tzutc\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'tzutc\' objects>, \'_TzSingleton__instance\': tzutc()})'
    __firstlineno__ = 41
    __hash__ = None
    __static_attributes__ = ()


class _timelex(object):
    # no doc
    def get_tokens(self, *args, **kwargs): # real signature unknown
        """
        This function breaks the time string into lexical units (tokens), which
                can be parsed by the parser. Lexical units are demarcated by changes in
                the character set, so any continuous string of letters is considered
                one unit, any continuous string of numbers is considered one unit.
                The main complication arises from the fact that dots ('.') can be used
                both as separators (e.g. "Sep.20.2009") or decimal points (e.g.
                "4:30:21.447"). As such, it is necessary to read the full context of
                any dot-separated strings before breaking it into tokens; as such, this
                function maintains a "token stack", for when the ambiguous context
                demands that multiple tokens be parsed at once.
        """
        pass

    @classmethod
    def split(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'pandas._libs.tslibs.parsing', '__init__': <cyfunction _timelex.__init__ at 0x00000190BF602B70>, 'get_tokens': <cyfunction _timelex.get_tokens at 0x00000190BF602C60>, 'split': <classmethod(<cyfunction _timelex.split at 0x00000190BF602D50>)>, '__dict__': <attribute '__dict__' of '_timelex' objects>, '__weakref__': <attribute '__weakref__' of '_timelex' objects>, '__doc__': None})"


# variables with complex values

DEFAULTPARSER = None # (!) real value is '<dateutil.parser._parser.parser object at 0x00000190BF665D30>'

_DEFAULT_DATETIME = None # (!) real value is 'datetime.datetime(1, 1, 1, 0, 0)'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000190BF64DB50>'

__pyx_capi__ = {
    'get_rule_month': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch)" at 0x00000190BF553330>'
    'parse_datetime_string': None, # (!) real value is '<capsule object "PyDateTime_DateTime *(PyObject *, int, int, NPY_DATETIMEUNIT *, __pyx_t_5numpy_int64_t *)" at 0x00000190BF553560>'
    'quarter_to_myear': None, # (!) real value is '<capsule object "PyObject *(int, int, PyObject *, int __pyx_skip_dispatch)" at 0x00000190BF5532E0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.parsing', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000190BF64DB50>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\parsing.cp314-win_amd64.pyd')"

__test__ = {
    'get_rule_month (line 1099)': "\n    Return starting month of given freq, default is December.\n\n    Parameters\n    ----------\n    source : str\n        Derived from `freq.rule_code` or `freq.freqstr`.\n\n    Returns\n    -------\n    rule_month: str\n\n    Examples\n    --------\n    >>> get_rule_month('D')\n    'DEC'\n\n    >>> get_rule_month('A-JAN')\n    'JAN'\n    ",
    'guess_datetime_format (line 859)': "\n    Guess the datetime format of a given datetime string.\n\n    This function attempts to deduce the format of a given datetime string. It is\n    useful for situations where the datetime format is unknown and needs to be\n    determined for proper parsing. The function is not guaranteed to return a format.\n\n    Parameters\n    ----------\n    dt_str : str\n        Datetime string to guess the format of.\n    dayfirst : bool, default False\n        If True parses dates with the day first, eg 20/01/2005\n\n        .. warning::\n            dayfirst=True is not strict, but will prefer to parse\n            with day first (this is a known bug).\n\n    Returns\n    -------\n    str or None : ret\n        datetime format string (for `strftime` or `strptime`),\n        or None if it can't be guessed.\n\n    See Also\n    --------\n    to_datetime : Convert argument to datetime.\n    Timestamp : Pandas replacement for python datetime.datetime object.\n    DatetimeIndex : Immutable ndarray-like of datetime64 data.\n\n    Examples\n    --------\n    >>> from pandas.tseries.api import guess_datetime_format\n    >>> guess_datetime_format('09/13/2023')\n    '%m/%d/%Y'\n\n    >>> guess_datetime_format('2023|September|13')\n    ",
}

