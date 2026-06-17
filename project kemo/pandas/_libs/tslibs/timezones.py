# encoding: utf-8
# module pandas._libs.tslibs.timezones
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\tslibs\timezones.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import zoneinfo as zoneinfo # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\zoneinfo\__init__.py
import numpy as np # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\numpy\__init__.py
import datetime as __datetime
import dateutil.tz._common as __dateutil_tz__common


# Variables with simple values

pytz = None

# functions

def dateutil_gettz(*args, **kwargs): # real signature unknown
    """
    Retrieve a time zone object from a string representation
    
    This function is intended to retrieve the :py:class:`tzinfo` subclass
    that best represents the time zone that would be used if a POSIX
    `TZ variable`_ were set to the same value.
    
    If no argument or an empty string is passed to ``gettz``, local time
    is returned:
    
    .. code-block:: python3
    
        >>> gettz()
        tzfile('/etc/localtime')
    
    This function is also the preferred way to map IANA tz database keys
    to :class:`tzfile` objects:
    
    .. code-block:: python3
    
        >>> gettz('Pacific/Kiritimati')
        tzfile('/usr/share/zoneinfo/Pacific/Kiritimati')
    
    On Windows, the standard is extended to include the Windows-specific
    zone names provided by the operating system:
    
    .. code-block:: python3
    
        >>> gettz('Egypt Standard Time')
        tzwin('Egypt Standard Time')
    
    Passing a GNU ``TZ`` style string time zone specification returns a
    :class:`tzstr` object:
    
    .. code-block:: python3
    
        >>> gettz('AEST-10AEDT-11,M10.1.0/2,M4.1.0/3')
        tzstr('AEST-10AEDT-11,M10.1.0/2,M4.1.0/3')
    
    :param name:
        A time zone name (IANA, or, on Windows, Windows keys), location of
        a ``tzfile(5)`` zoneinfo file or ``TZ`` variable style time zone
        specifier. An empty string, no argument or ``None`` is interpreted
        as local time.
    
    :return:
        Returns an instance of one of ``dateutil``'s :py:class:`tzinfo`
        subclasses.
    
    .. versionchanged:: 2.7.0
    
        After version 2.7.0, any two calls to ``gettz`` using the same
        input strings will return the same object:
    
        .. code-block:: python3
    
            >>> tz.gettz('America/Chicago') is tz.gettz('America/Chicago')
            True
    
        In addition to improving performance, this ensures that
        `"same zone" semantics`_ are used for datetimes in the same zone.
    
    
    .. _`TZ variable`:
        https://www.gnu.org/software/libc/manual/html_node/TZ-Variable.html
    
    .. _`"same zone" semantics`:
        https://blog.ganssle.io/articles/2018/02/aware-datetime-arithmetic.html
    """
    pass

def get_timezone(*args, **kwargs): # real signature unknown
    """
    We need to do several things here:
        1) Distinguish between pytz and dateutil timezones
        2) Not be over-specific (e.g. US/Eastern with/without DST is same *zone*
           but a different tz object)
        3) Provide something to serialize when we're storing a datetime object
           in pytables.
    
        We return a string prefaced with dateutil if it's a dateutil tz, else just
        the tz name. It needs to be a string so that we can serialize it with
        UJSON/pytables. maybe_get_tz (below) is the inverse of this process.
    """
    pass

def import_optional_dependency(name, extra=None, min_version=None, *, errors=None): # reliably restored by inspect
    """
    Import an optional dependency.
    
    By default, if a dependency is missing an ImportError with a nice
    message will be raised. If a dependency is present, but too old,
    we raise.
    
    Parameters
    ----------
    name : str
        The module name.
    extra : str
        Additional text to include in the ImportError message.
    errors : str {'raise', 'warn', 'ignore'}
        What to do when a dependency is not found or its version is too old.
    
        * raise : Raise an ImportError
        * warn : Only applicable when a module's version is to old.
          Warns that the version is too old and returns None
        * ignore: If the module is not installed, return None, otherwise,
          return the module, even if the version is too old.
          It's expected that users validate the version locally when
          using ``errors="ignore"`` (see. ``io/html.py``)
    min_version : str, default None
        Specify a minimum version that is different from the global pandas
        minimum version required.
    Returns
    -------
    maybe_module : Optional[ModuleType]
        The imported module, when found and the version is correct.
        None is returned when the package is not found and `errors`
        is False, or when the package's version is too old and `errors`
        is ``'warn'`` or ``'ignore'``.
    """
    pass

def infer_tzinfo(*args, **kwargs): # real signature unknown
    pass

def is_fixed_offset(*args, **kwargs): # real signature unknown
    pass

def is_utc(*args, **kwargs): # real signature unknown
    pass

def maybe_get_tz(*args, **kwargs): # real signature unknown
    """
    (Maybe) Construct a timezone object from a string. If tz is a string, use
        it to construct a timezone object. Otherwise, just return tz.
    """
    pass

def tz_compare(*args, **kwargs): # real signature unknown
    """
    Compare string representations of timezones
    
        The same timezone can be represented as different instances of
        timezones. For example
        `<DstTzInfo 'Europe/Paris' LMT+0:09:00 STD>` and
        `<DstTzInfo 'Europe/Paris' CET+1:00:00 STD>` are essentially same
        timezones but aren't evaluated such, but the string representation
        for both of these is `'Europe/Paris'`.
    
        This exists only to add a notion of equality to pytz-style zones
        that is compatible with the notion of equality expected of tzinfo
        subclasses.
    
        Parameters
        ----------
        start : tzinfo
        end : tzinfo
    
        Returns:
        -------
        bool
    """
    pass

def tz_standardize(tz): # real signature unknown; restored from __doc__
    """
    If the passed tz is a pytz timezone object, "normalize" it to the a
        consistent version
    
        Parameters
        ----------
        tz : tzinfo
    
        Returns
        -------
        tzinfo
    
        Examples
        --------
        >>> from datetime import datetime
        >>> from pytz import timezone
        >>> tz = timezone('US/Pacific').normalize(
        ...     datetime(2014, 1, 1, tzinfo=pytz.utc)
        ... ).tzinfo
        >>> tz
        <DstTzInfo 'US/Pacific' PST-1 day, 16:00:00 STD>
        >>> tz_standardize(tz)
        <DstTzInfo 'US/Pacific' LMT-1 day, 16:07:00 STD>
    
        >>> tz = timezone('US/Pacific')
        >>> tz
        <DstTzInfo 'US/Pacific' LMT-1 day, 16:07:00 STD>
        >>> tz_standardize(tz)
        <DstTzInfo 'US/Pacific' LMT-1 day, 16:07:00 STD>
    """
    pass

def _p_tz_cache_key(*args, **kwargs): # real signature unknown
    """ Python interface for cache function to facilitate testing. """
    pass

# classes

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


class _dateutil_tzfile(__dateutil_tz__common._tzinfo):
    """
    This is a ``tzinfo`` subclass that allows one to use the ``tzfile(5)``
    format timezone files to extract current and historical zone information.
    
    :param fileobj:
        This can be an opened file stream or a file name that the time zone
        information can be read from.
    
    :param filename:
        This is an optional parameter specifying the source of the time zone
        information in the event that ``fileobj`` is a file object. If omitted
        and ``fileobj`` is a file stream, this parameter will be set either to
        ``fileobj``'s ``name`` attribute or to ``repr(fileobj)``.
    
    See `Sources for Time Zone and Daylight Saving Time Data
    <https://data.iana.org/time-zones/tz-link.html>`_ for more information.
    Time zone files can be compiled from the `IANA Time Zone database files
    <https://www.iana.org/time-zones>`_ with the `zic time zone compiler
    <https://www.freebsd.org/cgi/man.cgi?query=zic&sektion=8>`_
    
    .. note::
    
        Only construct a ``tzfile`` directly if you have a specific timezone
        file on disk that you want to read into a Python ``tzinfo`` object.
        If you want to get a ``tzfile`` representing a specific IANA zone,
        (e.g. ``'America/New_York'``), you should call
        :func:`dateutil.tz.gettz` with the zone identifier.
    
    
    **Examples:**
    
    Using the US Eastern time zone as an example, we can see that a ``tzfile``
    provides time zone information for the standard Daylight Saving offsets:
    
    .. testsetup:: tzfile
    
        from dateutil.tz import gettz
        from datetime import datetime
    
    .. doctest:: tzfile
    
        >>> NYC = gettz('America/New_York')
        >>> NYC
        tzfile('/usr/share/zoneinfo/America/New_York')
    
        >>> print(datetime(2016, 1, 3, tzinfo=NYC))     # EST
        2016-01-03 00:00:00-05:00
    
        >>> print(datetime(2016, 7, 7, tzinfo=NYC))     # EDT
        2016-07-07 00:00:00-04:00
    
    
    The ``tzfile`` structure contains a fully history of the time zone,
    so historical dates will also have the right offsets. For example, before
    the adoption of the UTC standards, New York used local solar  mean time:
    
    .. doctest:: tzfile
    
       >>> print(datetime(1901, 4, 12, tzinfo=NYC))    # LMT
       1901-04-12 00:00:00-04:56
    
    And during World War II, New York was on "Eastern War Time", which was a
    state of permanent daylight saving time:
    
    .. doctest:: tzfile
    
        >>> print(datetime(1944, 2, 7, tzinfo=NYC))    # EWT
        1944-02-07 00:00:00-04:00
    """
    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """
        The ``tzfile`` implementation of :py:func:`datetime.tzinfo.fromutc`.
        
        :param dt:
            A :py:class:`datetime.datetime` object.
        
        :raises TypeError:
            Raised if ``dt`` is not a :py:class:`datetime.datetime` object.
        
        :raises ValueError:
            Raised if this is called with a ``dt`` which does not have this
            ``tzinfo`` attached.
        
        :return:
            Returns a :py:class:`datetime.datetime` object representing the
            wall time in ``self``'s time zone.
        """
        pass

    def is_ambiguous(self, dt, idx=None): # reliably restored by inspect
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

    def _find_last_transition(self, dt, in_utc=False): # reliably restored by inspect
        # no doc
        pass

    def _find_ttinfo(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _get_ttinfo(self, idx): # reliably restored by inspect
        # no doc
        pass

    def _read_tzfile(self, fileobj): # reliably restored by inspect
        # no doc
        pass

    def _resolve_ambiguous_time(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _set_tzdata(self, tzobj): # reliably restored by inspect
        """ Set the time zone data of this object from a _tzfile object """
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, fileobj, filename=None): # reliably restored by inspect
        # no doc
        pass

    def __ne__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __reduce_ex__(self, protocol): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    __firstlineno__ = 386
    __hash__ = None
    __static_attributes__ = (
        '_filename',
    )


class _dateutil_tzlocal(__dateutil_tz__common._tzinfo):
    """ A :class:`tzinfo` subclass built around the ``time`` timezone functions. """
    def dst(self, dt): # reliably restored by inspect
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

    def _isdst(self, dt, fold_naive=True): # reliably restored by inspect
        # no doc
        pass

    def _naive_is_dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def __eq__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self): # reliably restored by inspect
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

    __firstlineno__ = 201
    __hash__ = None
    __static_attributes__ = (
        '_dst_offset',
        '_dst_saved',
        '_hasdst',
        '_std_offset',
        '_tznames',
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
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'dateutil.tz.tz\', \'__firstlineno__\': 41, \'__doc__\': "\\nThis is a tzinfo object that represents the UTC time zone.\\n\\n**Examples:**\\n\\n.. doctest::\\n\\n    >>> from datetime import *\\n    >>> from dateutil.tz import *\\n\\n    >>> datetime.now()\\n    datetime.datetime(2003, 9, 27, 9, 40, 1, 521290)\\n\\n    >>> datetime.now(tzutc())\\n    datetime.datetime(2003, 9, 27, 12, 40, 12, 156379, tzinfo=tzutc())\\n\\n    >>> datetime.now(tzutc()).tzname()\\n    \'UTC\'\\n\\n.. versionchanged:: 2.7.0\\n    ``tzutc()`` is now a singleton, so the result of ``tzutc()`` will\\n    always return the same object.\\n\\n    .. doctest::\\n\\n        >>> from dateutil.tz import tzutc, UTC\\n        >>> tzutc() is tzutc()\\n        True\\n        >>> tzutc() is UTC\\n        True\\n", \'utcoffset\': <function tzutc.utcoffset at 0x000001A76219DD20>, \'dst\': <function tzutc.dst at 0x000001A76219DDD0>, \'tzname\': <function tzutc.tzname at 0x000001A76219DE80>, \'is_ambiguous\': <function tzutc.is_ambiguous at 0x000001A76219DF30>, \'fromutc\': <function tzutc.fromutc at 0x000001A76219E090>, \'__eq__\': <function tzutc.__eq__ at 0x000001A76219E140>, \'__hash__\': None, \'__ne__\': <function tzutc.__ne__ at 0x000001A76219E1F0>, \'__repr__\': <function tzutc.__repr__ at 0x000001A76219E2A0>, \'__reduce__\': <method \'__reduce__\' of \'object\' objects>, \'__static_attributes__\': (), \'__dict__\': <attribute \'__dict__\' of \'tzutc\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'tzutc\' objects>, \'_TzSingleton__instance\': tzutc()})'
    __firstlineno__ = 41
    __hash__ = None
    __static_attributes__ = ()


class _ZoneInfo(__datetime.tzinfo):
    # no doc
    @classmethod
    def clear_cache(cls, *args, **kwargs): # real signature unknown
        pass

    def dst(self, dt): # reliably restored by inspect
        # no doc
        pass

    def fromutc(self, dt): # reliably restored by inspect
        """ Convert from datetime in UTC to datetime in local time """
        pass

    @classmethod
    def from_file(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def no_cache(cls, *args, **kwargs): # real signature unknown
        pass

    def tzname(self, dt): # reliably restored by inspect
        # no doc
        pass

    def utcoffset(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _file_reduce(self): # reliably restored by inspect
        # no doc
        pass

    def _find_trans(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _find_tzfile(self, key): # reliably restored by inspect
        # no doc
        pass

    def _get_local_timestamp(self, dt): # reliably restored by inspect
        # no doc
        pass

    def _load_file(self, fobj): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def _new_instance(cls, *args, **kwargs): # real signature unknown
        pass

    @staticmethod
    def _ts_to_local(trans_idx, trans_list_utc, utcoffsets): # reliably restored by inspect
        """
        Generate number of seconds since 1970 *in the local time*.
        
        This is necessary to easily find the transition times in local time
        """
        pass

    @classmethod
    def _unpickle(cls, *args, **kwargs): # real signature unknown
        pass

    @staticmethod
    def _utcoff_to_dstoff(trans_idx, utcoffsets, isdsts): # reliably restored by inspect
        # no doc
        pass

    @classmethod
    def __init_subclass__(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, key): # reliably restored by inspect
        # no doc
        pass

    def __reduce__(self): # reliably restored by inspect
        # no doc
        pass

    def __repr__(self): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    key = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _strong_cache = OrderedDict()
    _strong_cache_size = 8
    _weak_cache = None # (!) real value is '<WeakValueDictionary at 0x1a7620363f0>'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': 'zoneinfo', '__firstlineno__': 30, '_strong_cache_size': 8, '_strong_cache': OrderedDict(), '_weak_cache': <WeakValueDictionary at 0x1a7620363f0>, '__init_subclass__': <classmethod(<function ZoneInfo.__init_subclass__ at 0x000001A76207E560>)>, '__new__': <staticmethod(<function ZoneInfo.__new__ at 0x000001A76207E610>)>, 'no_cache': <classmethod(<function ZoneInfo.no_cache at 0x000001A76207E6C0>)>, '_new_instance': <classmethod(<function ZoneInfo._new_instance at 0x000001A76207E770>)>, 'from_file': <classmethod(<function ZoneInfo.from_file at 0x000001A76207E820>)>, 'clear_cache': <classmethod(<function ZoneInfo.clear_cache at 0x000001A76207E8D0>)>, 'key': <property object at 0x000001A76205E110>, 'utcoffset': <function ZoneInfo.utcoffset at 0x000001A76207EA30>, 'dst': <function ZoneInfo.dst at 0x000001A76207EAE0>, 'tzname': <function ZoneInfo.tzname at 0x000001A76207EB90>, 'fromutc': <function ZoneInfo.fromutc at 0x000001A76207EC40>, '_find_trans': <function ZoneInfo._find_trans at 0x000001A76207ECF0>, '_get_local_timestamp': <function ZoneInfo._get_local_timestamp at 0x000001A76207EDA0>, '__str__': <function ZoneInfo.__str__ at 0x000001A76207EE50>, '__repr__': <function ZoneInfo.__repr__ at 0x000001A76207EF00>, '__reduce__': <function ZoneInfo.__reduce__ at 0x000001A76207EFB0>, '_file_reduce': <function ZoneInfo._file_reduce at 0x000001A76207F060>, '_unpickle': <classmethod(<function ZoneInfo._unpickle at 0x000001A76207F110>)>, '_find_tzfile': <function ZoneInfo._find_tzfile at 0x000001A76207F1C0>, '_load_file': <function ZoneInfo._load_file at 0x000001A76207F270>, '_utcoff_to_dstoff': <staticmethod(<function ZoneInfo._utcoff_to_dstoff at 0x000001A76207F320>)>, '_ts_to_local': <staticmethod(<function ZoneInfo._ts_to_local at 0x000001A76207F3D0>)>, '__static_attributes__': ('_fixed_offset', '_trans_local', '_trans_utc', '_tti_before', '_ttinfos', '_tz_after'), '__dict__': <attribute '__dict__' of 'ZoneInfo' objects>, '__weakref__': <attribute '__weakref__' of 'ZoneInfo' objects>, '__doc__': None})"
    __firstlineno__ = 30
    __static_attributes__ = (
        '_fixed_offset',
        '_trans_local',
        '_trans_utc',
        '_tti_before',
        '_ttinfos',
        '_tz_after',
    )


# variables with complex values

dst_cache = {}

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A76201F3B0>'

__pyx_capi__ = {
    'get_dst_info': None, # (!) real value is '<capsule object "PyObject *(PyDateTime_TZInfo *)" at 0x000001A76205C0E0>'
    'get_timezone': None, # (!) real value is '<capsule object "PyObject *(PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x000001A76205C130>'
    'get_utcoffset': None, # (!) real value is '<capsule object "PyDateTime_Delta *(PyDateTime_TZInfo *, PyDateTime_DateTime *)" at 0x000001A76205C040>'
    'is_fixed_offset': None, # (!) real value is '<capsule object "int (PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x000001A76205C2C0>'
    'is_tzlocal': None, # (!) real value is '<capsule object "int (PyDateTime_TZInfo *)" at 0x000001A76205C180>'
    'is_utc': None, # (!) real value is '<capsule object "int (PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x000001A76205C310>'
    'is_zoneinfo': None, # (!) real value is '<capsule object "int (PyDateTime_TZInfo *)" at 0x000001A76205C1D0>'
    'maybe_get_tz': None, # (!) real value is '<capsule object "PyDateTime_TZInfo *(PyObject *, int __pyx_skip_dispatch)" at 0x000001A76205C090>'
    'treat_tz_as_pytz': None, # (!) real value is '<capsule object "int (PyDateTime_TZInfo *)" at 0x000001A76205C220>'
    'tz_compare': None, # (!) real value is '<capsule object "int (PyDateTime_TZInfo *, PyDateTime_TZInfo *, int __pyx_skip_dispatch)" at 0x000001A76205C270>'
    'utc_stdlib': None, # (!) real value is '<capsule object "PyDateTime_TZInfo *" at 0x000001A76204BFB0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.timezones', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A76201F3B0>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\timezones.cp314-win_amd64.pyd')"

__test__ = {
    'tz_standardize (line 512)': '\n    If the passed tz is a pytz timezone object, "normalize" it to the a\n    consistent version\n\n    Parameters\n    ----------\n    tz : tzinfo\n\n    Returns\n    -------\n    tzinfo\n\n    Examples\n    --------\n    >>> from datetime import datetime\n    >>> from pytz import timezone\n    >>> tz = timezone(\'US/Pacific\').normalize(\n    ...     datetime(2014, 1, 1, tzinfo=pytz.utc)\n    ... ).tzinfo\n    >>> tz\n    <DstTzInfo \'US/Pacific\' PST-1 day, 16:00:00 STD>\n    >>> tz_standardize(tz)\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n\n    >>> tz = timezone(\'US/Pacific\')\n    >>> tz\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n    >>> tz_standardize(tz)\n    <DstTzInfo \'US/Pacific\' LMT-1 day, 16:07:00 STD>\n    ',
}

