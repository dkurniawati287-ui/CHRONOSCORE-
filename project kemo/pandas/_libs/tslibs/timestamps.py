# encoding: utf-8
# module pandas._libs.tslibs.timestamps
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\tslibs\timestamps.cp314-win_amd64.pyd
# by generator 1.147
"""
_Timestamp is a c-defined subclass of datetime.datetime

_Timestamp is PITA. Because we inherit from datetime, which has very specific
construction requirements, we need to do object instantiation in python
(see Timestamp class below). This will serve as a C extension type that
shadows the python class, where we do any heavy lifting.
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\warnings.py
import numpy as np # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\numpy\__init__.py
import datetime as dt # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\datetime.py
from pandas._libs.tslibs.fields import (RoundTo, get_date_name_field, 
    get_start_end_field, round_nsint64)

import pandas._libs.tslibs.base as __pandas__libs_tslibs_base
import pandas._libs.tslibs.timedeltas as __pandas__libs_tslibs_timedeltas


# functions

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def integer_op_not_supported(*args, **kwargs): # real signature unknown
    pass

def set_module(module): # reliably restored by inspect
    """
    Private decorator for overriding __module__ on a function or class.
    
    Example usage::
    
        @set_module("pandas")
        def example():
            pass
    
    
        assert example.__module__ == "pandas"
    """
    pass

def _unpickle_timestamp(*args, **kwargs): # real signature unknown
    pass

# classes

class MinMaxReso(object):
    """
    We need to define min/max/resolution on both the Timestamp _instance_
        and Timestamp class.  On an instance, these depend on the object's _reso.
        On the class, we default to the values we would get with nanosecond _reso.
    
        See also: timedeltas.MinMaxReso
    """
    def __get__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.timestamps\', \'__doc__\': "\\n    We need to define min/max/resolution on both the Timestamp _instance_\\n    and Timestamp class.  On an instance, these depend on the object\'s _reso.\\n    On the class, we default to the values we would get with nanosecond _reso.\\n\\n    See also: timedeltas.MinMaxReso\\n    ", \'__init__\': <cyfunction MinMaxReso.__init__ at 0x000001D45F614B90>, \'__get__\': <cyfunction MinMaxReso.__get__ at 0x000001D45F614C80>, \'__set__\': <cyfunction MinMaxReso.__set__ at 0x000001D45F614D70>, \'__dict__\': <attribute \'__dict__\' of \'MinMaxReso\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'MinMaxReso\' objects>})'


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



class OutOfBoundsTimedelta(ValueError):
    """
    Raised when encountering a timedelta value that cannot be represented.
    
        Representation should be within a timedelta64[ns].
    
        See Also
        --------
        date_range : Return a fixed frequency DatetimeIndex.
    
        Examples
        --------
        >>> pd.date_range(start="1/1/1700", freq="B", periods=100000, unit="ns")
        Traceback (most recent call last):
        OutOfBoundsTimedelta: Cannot cast 139999 days 00:00:00
        to unit='ns' without overflow.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class Timedelta(__pandas__libs_tslibs_timedeltas._Timedelta):
    """
    Represents a duration, the difference between two dates or times.
    
        Timedelta is the pandas equivalent of python's ``datetime.timedelta``
        and is interchangeable with it in most cases.
    
        Parameters
        ----------
        value : Timedelta, timedelta, np.timedelta64, str, int or float
            Input value.
        unit : str, default 'ns'
            If input is an integer, denote the unit of the input.
            If input is a float, denote the unit of the integer parts.
            The decimal parts with resolution lower than 1 nanosecond are ignored.
    
            Possible values:
    
            * 'W', or 'D'
            * 'days', or 'day'
            * 'hours', 'hour', 'hr', or 'h'
            * 'minutes', 'minute', 'min', or 'm'
            * 'seconds', 'second', 'sec', or 's'
            * 'milliseconds', 'millisecond', 'millis', 'milli', or 'ms'
            * 'microseconds', 'microsecond', 'micros', 'micro', or 'us'
            * 'nanoseconds', 'nanosecond', 'nanos', 'nano', or 'ns'.
    
            .. deprecated:: 3.0.0
    
                Allowing the values `w`, `d`, `MIN`, `MS`, `US` and `NS` to denote units
                are deprecated in favour of the values `W`, `D`, `min`, `ms`, `us` and `ns`.
    
        **kwargs
            Available kwargs: {days, seconds, microseconds,
            milliseconds, minutes, hours, weeks}.
            Values for construction in compat with datetime.timedelta.
            Numpy ints and floats will be coerced to python ints and floats.
    
        See Also
        --------
        Timestamp : Represents a single timestamp in time.
        TimedeltaIndex : Immutable Index of timedelta64 data.
        DateOffset : Standard kind of date increment used for a date range.
        to_timedelta : Convert argument to timedelta.
        datetime.timedelta : Represents a duration in the datetime module.
        numpy.timedelta64 : Represents a duration compatible with NumPy.
    
        Notes
        -----
        The constructor may take in either both values of value and unit or
        kwargs as above. Either one of them must be used during initialization
    
        The ``.value`` attribute is always in ns.
    
        If the precision is higher than nanoseconds, the precision of the duration is
        truncated to nanoseconds.
    
        Examples
        --------
        Here we initialize Timedelta object with both value and unit
    
        >>> td = pd.Timedelta(1, "D")
        >>> td
        Timedelta('1 days 00:00:00')
    
        Here we initialize the Timedelta object with kwargs
    
        >>> td2 = pd.Timedelta(days=1)
        >>> td2
        Timedelta('1 days 00:00:00')
    
        We see that either way we get the same result
    """
    def ceil(self, s): # real signature unknown; restored from __doc__
        """
        Return a new Timedelta ceiled to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the ceiling resolution. Must be a fixed
                    frequency like 's' (second) not 'ME' (month end). See
                    :ref:`frequency aliases <timeseries.offset_aliases>` for
                    a list of possible `freq` values.
        
                Returns
                -------
                Timedelta
                    A new Timedelta object ceiled to the specified resolution.
        
                See Also
                --------
                    Timedelta.floor : Floor the Timedelta to the specified resolution.
                    Timedelta.round : Round the Timedelta to the nearest specified resolution.
        
                Examples
                --------
                >>> td = pd.Timedelta('1001ms')
                >>> td
                Timedelta('0 days 00:00:01.001000')
                >>> td.ceil('s')
                Timedelta('0 days 00:00:02')
        """
        pass

    def floor(self, s): # real signature unknown; restored from __doc__
        """
        Return a new Timedelta floored to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the flooring resolution.
                    It uses the same units as class constructor :class:`~pandas.Timedelta`.
        
                Returns
                -------
                Timedelta
                    A new Timedelta object floored to the specified resolution.
        
                See Also
                --------
                    Timestamp.ceil : Round the Timestamp up to the nearest specified resolution.
                    Timestamp.round : Round the Timestamp to the nearest specified resolution.
        
                Examples
                --------
                >>> td = pd.Timedelta('1001ms')
                >>> td
                Timedelta('0 days 00:00:01.001000')
                >>> td.floor('s')
                Timedelta('0 days 00:00:01')
        """
        pass

    def round(self, s): # real signature unknown; restored from __doc__
        """
        Round the Timedelta to the specified resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the rounding resolution.
                    It uses the same units as class constructor :class:`~pandas.Timedelta`.
        
                Returns
                -------
                a new Timedelta rounded to the given resolution of `freq`
        
                Raises
                ------
                ValueError if the freq cannot be converted
        
                See Also
                --------
                    Timedelta.floor : Floor the Timedelta to the specified resolution.
                    Timedelta.round : Round the Timedelta to the nearest specified resolution.
                    Timestamp.ceil : Similar method for Timestamp objects.
        
                Examples
                --------
                >>> td = pd.Timedelta('1001ms')
                >>> td
                Timedelta('0 days 00:00:01.001000')
                >>> td.round('s')
                Timedelta('0 days 00:00:01')
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _module_source = 'pandas._libs.tslibs.timedeltas'
    _req_any_kwargs_new = None # (!) real value is "{'days', 'milliseconds', 'minutes', 'microseconds', 'seconds', 'hours', 'weeks', 'nanoseconds'}"
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas\', \'__doc__\': \'\\n    Represents a duration, the difference between two dates or times.\\n\\n    Timedelta is the pandas equivalent of python\\\'s ``datetime.timedelta``\\n    and is interchangeable with it in most cases.\\n\\n    Parameters\\n    ----------\\n    value : Timedelta, timedelta, np.timedelta64, str, int or float\\n        Input value.\\n    unit : str, default \\\'ns\\\'\\n        If input is an integer, denote the unit of the input.\\n        If input is a float, denote the unit of the integer parts.\\n        The decimal parts with resolution lower than 1 nanosecond are ignored.\\n\\n        Possible values:\\n\\n        * \\\'W\\\', or \\\'D\\\'\\n        * \\\'days\\\', or \\\'day\\\'\\n        * \\\'hours\\\', \\\'hour\\\', \\\'hr\\\', or \\\'h\\\'\\n        * \\\'minutes\\\', \\\'minute\\\', \\\'min\\\', or \\\'m\\\'\\n        * \\\'seconds\\\', \\\'second\\\', \\\'sec\\\', or \\\'s\\\'\\n        * \\\'milliseconds\\\', \\\'millisecond\\\', \\\'millis\\\', \\\'milli\\\', or \\\'ms\\\'\\n        * \\\'microseconds\\\', \\\'microsecond\\\', \\\'micros\\\', \\\'micro\\\', or \\\'us\\\'\\n        * \\\'nanoseconds\\\', \\\'nanosecond\\\', \\\'nanos\\\', \\\'nano\\\', or \\\'ns\\\'.\\n\\n        .. deprecated:: 3.0.0\\n\\n            Allowing the values `w`, `d`, `MIN`, `MS`, `US` and `NS` to denote units\\n            are deprecated in favour of the values `W`, `D`, `min`, `ms`, `us` and `ns`.\\n\\n    **kwargs\\n        Available kwargs: {days, seconds, microseconds,\\n        milliseconds, minutes, hours, weeks}.\\n        Values for construction in compat with datetime.timedelta.\\n        Numpy ints and floats will be coerced to python ints and floats.\\n\\n    See Also\\n    --------\\n    Timestamp : Represents a single timestamp in time.\\n    TimedeltaIndex : Immutable Index of timedelta64 data.\\n    DateOffset : Standard kind of date increment used for a date range.\\n    to_timedelta : Convert argument to timedelta.\\n    datetime.timedelta : Represents a duration in the datetime module.\\n    numpy.timedelta64 : Represents a duration compatible with NumPy.\\n\\n    Notes\\n    -----\\n    The constructor may take in either both values of value and unit or\\n    kwargs as above. Either one of them must be used during initialization\\n\\n    The ``.value`` attribute is always in ns.\\n\\n    If the precision is higher than nanoseconds, the precision of the duration is\\n    truncated to nanoseconds.\\n\\n    Examples\\n    --------\\n    Here we initialize Timedelta object with both value and unit\\n\\n    >>> td = pd.Timedelta(1, "D")\\n    >>> td\\n    Timedelta(\\\'1 days 00:00:00\\\')\\n\\n    Here we initialize the Timedelta object with kwargs\\n\\n    >>> td2 = pd.Timedelta(days=1)\\n    >>> td2\\n    Timedelta(\\\'1 days 00:00:00\\\')\\n\\n    We see that either way we get the same result\\n    \', \'_req_any_kwargs_new\': {\'days\', \'milliseconds\', \'minutes\', \'microseconds\', \'seconds\', \'hours\', \'weeks\', \'nanoseconds\'}, \'__new__\': <staticmethod(<cyfunction Timedelta.__new__ at 0x000001D45F61A3F0>)>, \'__setstate__\': <cyfunction Timedelta.__setstate__ at 0x000001D45F61A4E0>, \'__reduce__\': <cyfunction Timedelta.__reduce__ at 0x000001D45F61A5D0>, \'_round\': <cyfunction Timedelta._round at 0x000001D45F61A6C0>, \'round\': <cyfunction Timedelta.round at 0x000001D45F61A7B0>, \'floor\': <cyfunction Timedelta.floor at 0x000001D45F61A8A0>, \'ceil\': <cyfunction Timedelta.ceil at 0x000001D45F61A990>, \'__neg__\': <cyfunction _op_unary_method.<locals>.f at 0x000001D45F61AB70>, \'__pos__\': <cyfunction _op_unary_method.<locals>.f at 0x000001D45F61AD50>, \'__abs__\': <cyfunction _op_unary_method.<locals>.f at 0x000001D45F61AF30>, \'__add__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001D45F61B110>, \'__radd__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001D45F61B2F0>, \'__sub__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001D45F61B4D0>, \'__rsub__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001D45F61B6B0>, \'__mul__\': <cyfunction Timedelta.__mul__ at 0x000001D45F61B7A0>, \'__rmul__\': <cyfunction Timedelta.__mul__ at 0x000001D45F61B7A0>, \'__truediv__\': <cyfunction Timedelta.__truediv__ at 0x000001D45F61B890>, \'__rtruediv__\': <cyfunction Timedelta.__rtruediv__ at 0x000001D45F61B980>, \'__floordiv__\': <cyfunction Timedelta.__floordiv__ at 0x000001D45F61BA70>, \'__rfloordiv__\': <cyfunction Timedelta.__rfloordiv__ at 0x000001D45F61BB60>, \'__mod__\': <cyfunction Timedelta.__mod__ at 0x000001D45F61BC50>, \'__rmod__\': <cyfunction Timedelta.__rmod__ at 0x000001D45F61BD40>, \'__divmod__\': <cyfunction Timedelta.__divmod__ at 0x000001D45F61BE30>, \'__rdivmod__\': <cyfunction Timedelta.__rdivmod__ at 0x000001D45F61BF20>, \'__dict__\': <attribute \'__dict__\' of \'Timedelta\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timedelta\' objects>, \'_module_source\': \'pandas._libs.tslibs.timedeltas\'})'


class _Timestamp(__pandas__libs_tslibs_base.ABCTimestamp):
    # no doc
    def as_unit(self, s): # real signature unknown; restored from __doc__
        """
        Convert the underlying int64 representation to the given unit.
        
                Parameters
                ----------
                unit : {"ns", "us", "ms", "s"}
                round_ok : bool, default True
                    If False and the conversion requires rounding, raise.
        
                Returns
                -------
                Timestamp
        
                See Also
                --------
                Timestamp.asm8 : Return numpy datetime64 format with same precision.
                Timestamp.to_pydatetime : Convert Timestamp object to a native
                    Python datetime object.
                to_timedelta : Convert argument into timedelta object,
                    which can represent differences in times.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 00:00:00.01')
                >>> ts
                Timestamp('2023-01-01 00:00:00.010000')
                >>> ts.unit
                'ms'
                >>> ts = ts.as_unit('s')
                >>> ts
                Timestamp('2023-01-01 00:00:00')
                >>> ts.unit
                's'
        """
        pass

    def day_name(self): # real signature unknown; restored from __doc__
        """
        Return the day name of the Timestamp with specified locale.
        
                Parameters
                ----------
                locale : str, default None (English locale)
                    Locale determining the language in which to return the day name.
        
                Returns
                -------
                str
        
                See Also
                --------
                Timestamp.day_of_week : Return day of the week.
                Timestamp.day_of_year : Return day of the year.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.day_name()
                'Saturday'
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.day_name()
                nan
        """
        pass

    def isoformat(self): # real signature unknown; restored from __doc__
        """
        Return the time formatted according to ISO 8601.
        
                The full format looks like 'YYYY-MM-DD HH:MM:SS.mmmmmmnnn'.
                By default, the fractional part is omitted if self.microsecond == 0
                and self._nanosecond == 0.
        
                If self.tzinfo is not None, the UTC offset is also attached,
                giving a full format of 'YYYY-MM-DD HH:MM:SS.mmmmmmnnn+HH:MM'.
        
                Parameters
                ----------
                sep : str, default 'T'
                    String used as the separator between the date and time.
        
                timespec : str, default 'auto'
                    Specifies the number of additional terms of the time to include.
                    The valid values are 'auto', 'hours', 'minutes', 'seconds',
                    'milliseconds', 'microseconds', and 'nanoseconds'.
        
                Returns
                -------
                str
        
                See Also
                --------
                Timestamp.strftime : Return a formatted string.
                Timestamp.isocalendar : Return a tuple containing ISO year, week number and
                    weekday.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.isoformat()
                '2020-03-14T15:32:52.192548651'
                >>> ts.isoformat(timespec='microseconds')
                '2020-03-14T15:32:52.192548'
        """
        pass

    def month_name(self): # real signature unknown; restored from __doc__
        """
        Return the month name of the Timestamp with specified locale.
        
                This method returns the full name of the month corresponding to the
                `Timestamp`, such as 'January', 'February', etc. The month name can
                be returned in a specified locale if provided; otherwise, it defaults
                to the English locale.
        
                Parameters
                ----------
                locale : str, default None (English locale)
                    Locale determining the language in which to return the month name.
        
                Returns
                -------
                str
                    The full month name as a string.
        
                See Also
                --------
                Timestamp.day_name : Returns the name of the day of the week.
                Timestamp.strftime : Returns a formatted string of the Timestamp.
                datetime.datetime.strftime : Returns a string representing the date and time.
        
                Examples
                --------
                Get the month name in English (default):
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.month_name()
                'March'
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.month_name()
                nan
        """
        pass

    def normalize(self): # real signature unknown; restored from __doc__
        """
        Normalize Timestamp to midnight, preserving tz information.
        
                This method sets the time component of the `Timestamp` to midnight (00:00:00),
                while preserving the date and time zone information. It is useful when you
                need to standardize the time across different `Timestamp` objects without
                altering the time zone or the date.
        
                Returns
                -------
                Timestamp
        
                See Also
                --------
                Timestamp.floor : Rounds `Timestamp` down to the nearest frequency.
                Timestamp.ceil : Rounds `Timestamp` up to the nearest frequency.
                Timestamp.round : Rounds `Timestamp` to the nearest frequency.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2020, 3, 14, 15, 30)
                >>> ts.normalize()
                Timestamp('2020-03-14 00:00:00')
        """
        pass

    def timestamp(self): # real signature unknown; restored from __doc__
        """
        Return POSIX timestamp as float.
        
                This method converts the `Timestamp` object to a POSIX timestamp, which is
                the number of seconds since the Unix epoch (January 1, 1970). The returned
                value is a floating-point number, where the integer part represents the
                seconds, and the fractional part represents the microseconds.
        
                Returns
                -------
                float
                    The POSIX timestamp representation of the `Timestamp` object.
        
                See Also
                --------
                Timestamp.fromtimestamp : Construct a `Timestamp` from a POSIX timestamp.
                datetime.datetime.timestamp : Equivalent method from the `datetime` module.
                Timestamp.to_pydatetime : Convert the `Timestamp` to a `datetime` object.
                Timestamp.to_datetime64 : Converts `Timestamp` to `numpy.datetime64`.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')
                >>> ts.timestamp()
                1584199972.192548
        """
        pass

    def to_datetime64(self): # real signature unknown; restored from __doc__
        """
        Return a NumPy datetime64 object with same precision.
        
                This method returns a numpy.datetime64 object with the same
                date and time information and precision as the pd.Timestamp object.
        
                See Also
                --------
                numpy.datetime64 : Class to represent dates and times with high precision.
                Timestamp.to_numpy : Alias for this method.
                Timestamp.asm8 : Alias for this method.
                pd.to_datetime : Convert argument to datetime.
        
                Examples
                --------
                >>> ts = pd.Timestamp(year=2023, month=1, day=1,
                ...                   hour=10, second=15)
                >>> ts
                Timestamp('2023-01-01 10:00:15')
                >>> ts.to_datetime64()
                numpy.datetime64('2023-01-01T10:00:15.000000')
        """
        pass

    def to_numpy(self): # real signature unknown; restored from __doc__
        """
        Convert the Timestamp to a NumPy datetime64.
        
                This is an alias method for `Timestamp.to_datetime64()`. The dtype and
                copy parameters are available here only for compatibility. Their values
                will not affect the return value.
        
                Parameters
                ----------
                dtype : dtype, optional
                    Data type of the output, ignored in this method as the return type
                    is always `numpy.datetime64`.
                copy : bool, default False
                    Whether to ensure that the returned value is a new object. This
                    parameter is also ignored as the method does not support copying.
        
                Returns
                -------
                numpy.datetime64
        
                See Also
                --------
                DatetimeIndex.to_numpy : Similar method for DatetimeIndex.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.to_numpy()
                numpy.datetime64('2020-03-14T15:32:52.192548651')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.to_numpy()
                numpy.datetime64('NaT', 'ns')
        """
        pass

    def to_period(self, freq='Y'): # real signature unknown; restored from __doc__
        """
        Return a period of which this timestamp is an observation.
        
                This method converts the given Timestamp to a Period object,
                which represents a span of time,such as a year, month, etc.,
                based on the specified frequency.
        
                Parameters
                ----------
                freq : str, optional
                    Frequency string for the period (e.g., 'Y', 'M', 'W'). Defaults to `None`.
        
                See Also
                --------
                Timestamp : Represents a specific timestamp.
                Period : Represents a span of time.
                to_period : Converts an object to a Period.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> # Year end frequency
                >>> ts.to_period(freq='Y')
                Period('2020', 'Y-DEC')
        
                >>> # Month end frequency
                >>> ts.to_period(freq='M')
                Period('2020-03', 'M')
        
                >>> # Weekly frequency
                >>> ts.to_period(freq='W')
                Period('2020-03-09/2020-03-15', 'W-SUN')
        
                >>> # Quarter end frequency
                >>> ts.to_period(freq='Q')
                Period('2020Q1', 'Q-DEC')
        """
        pass

    def to_pydatetime(self): # real signature unknown; restored from __doc__
        """
        Convert a Timestamp object to a native Python datetime object.
        
                This method is useful for when you need to utilize a pandas Timestamp
                object in contexts where native Python datetime objects are expected
                or required. The conversion discards the nanoseconds component, and a
                warning can be issued in such cases if desired.
        
                Parameters
                ----------
                warn : bool, default True
                    If True, issues a warning when the timestamp includes nonzero
                    nanoseconds, as these will be discarded during the conversion.
        
                Returns
                -------
                datetime.datetime or NaT
                    Returns a datetime.datetime object representing the timestamp,
                    with year, month, day, hour, minute, second, and microsecond components.
                    If the timestamp is NaT (Not a Time), returns NaT.
        
                See Also
                --------
                datetime.datetime : The standard Python datetime class that this method
                    returns.
                Timestamp.timestamp : Convert a Timestamp object to POSIX timestamp.
                Timestamp.to_datetime64 : Convert a Timestamp object to numpy.datetime64.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')
                >>> ts.to_pydatetime()
                datetime.datetime(2020, 3, 14, 15, 32, 52, 192548)
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.to_pydatetime()
                NaT
        """
        pass

    @classmethod
    def _from_dt64(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_value_and_reso(cls, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
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

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return numpy datetime64 format with same precision.

        See Also
        --------
        numpy.datetime64 : Numpy datatype for dates and times with high precision.
        Timestamp.to_numpy : Convert the Timestamp to a NumPy datetime64.
        to_datetime : Convert argument to datetime.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14, 15)
        >>> ts.asm8
        numpy.datetime64('2020-03-14T15:00:00.000000')
        """

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the Timestamp.

        Returns
        -------
        int
            The day of the Timestamp.

        See Also
        --------
        Timestamp.week : Return the week number of the year.
        Timestamp.weekday : Return the day of the week.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30")
        >>> ts.day
        31
        """

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return day of the week.

        Returns
        -------
        int

        See Also
        --------
        Timestamp.isoweekday : Return the ISO day of the week represented by the date.
        Timestamp.weekday : Return the day of the week represented by the date.
        Timestamp.day_of_year : Return day of the year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.day_of_week
        5
        """

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the year.

        Returns
        -------
        int

        See Also
        --------
        Timestamp.day_of_week : Return day of the week.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.day_of_year
        74
        """

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of days in the month.

        Returns
        -------
        int

        See Also
        --------
        Timestamp.month_name : Return the month name of the Timestamp with
            specified locale.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.days_in_month
        31
        """

    day_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return day of the week.

        Returns
        -------
        int

        See Also
        --------
        Timestamp.isoweekday : Return the ISO day of the week represented by the date.
        Timestamp.weekday : Return the day of the week represented by the date.
        Timestamp.day_of_year : Return day of the year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.day_of_week
        5
        """

    day_of_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the year.

        Returns
        -------
        int

        See Also
        --------
        Timestamp.day_of_week : Return day of the week.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.day_of_year
        74
        """

    fold = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the fold value of the Timestamp.

        Returns
        -------
        int
            The fold value of the Timestamp, where 0 indicates the first occurrence
            of the ambiguous time, and 1 indicates the second.

        See Also
        --------
        Timestamp.dst : Return the daylight saving time (DST) adjustment.
        Timestamp.tzinfo : Return the timezone information associated.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-11-03 01:30:00")
        >>> ts.fold
        0
        """

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the hour of the Timestamp.

        Returns
        -------
        int
            The hour of the Timestamp.

        See Also
        --------
        Timestamp.minute : Return the minute of the Timestamp.
        Timestamp.second : Return the second of the Timestamp.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30")
        >>> ts.hour
        16
        """

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if year is a leap year.

        A leap year is a year, which has 366 days (instead of 365) including 29th of
        February as an intercalary day. Leap years are years which are multiples of
        four with the exception of years divisible by 100 but not by 400.

        Returns
        -------
        bool
            True if year is a leap year, else False

        See Also
        --------
        Period.is_leap_year : Return True if the period’s year is in a leap year.
        DatetimeIndex.is_leap_year : Boolean indicator if the date belongs to a
            leap year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_leap_year
        True
        """

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the date is the last day of the month.

        Returns
        -------
        bool
            True if the date is the last day of the month.

        See Also
        --------
        Timestamp.is_month_start : Similar property indicating month start.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_month_end
        False

        >>> ts = pd.Timestamp(2020, 12, 31)
        >>> ts.is_month_end
        True
        """

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the date is the first day of the month.

        Returns
        -------
        bool
            True if the date is the first day of the month.

        See Also
        --------
        Timestamp.is_month_end : Similar property indicating the last day of the month.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_month_start
        False

        >>> ts = pd.Timestamp(2020, 1, 1)
        >>> ts.is_month_start
        True
        """

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if date is last day of the quarter.

        Returns
        -------
        bool
            True if date is last day of the quarter.

        See Also
        --------
        Timestamp.is_quarter_start : Similar property indicating the quarter start.
        Timestamp.quarter : Return the quarter of the date.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_quarter_end
        False

        >>> ts = pd.Timestamp(2020, 3, 31)
        >>> ts.is_quarter_end
        True
        """

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Check if the date is the first day of the quarter.

        Returns
        -------
        bool
            True if date is first day of the quarter.

        See Also
        --------
        Timestamp.is_quarter_end : Similar property indicating the quarter end.
        Timestamp.quarter : Return the quarter of the date.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_quarter_start
        False

        >>> ts = pd.Timestamp(2020, 4, 1)
        >>> ts.is_quarter_start
        True
        """

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is last day of the year.

        Returns
        -------
        bool

        See Also
        --------
        Timestamp.is_year_start : Similar property indicating the start of the year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_year_end
        False

        >>> ts = pd.Timestamp(2020, 12, 31)
        >>> ts.is_year_end
        True
        """

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if date is first day of the year.

        Returns
        -------
        bool

        See Also
        --------
        Timestamp.is_year_end : Similar property indicating the end of the year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.is_year_start
        False

        >>> ts = pd.Timestamp(2020, 1, 1)
        >>> ts.is_year_start
        True
        """

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the microsecond of the Timestamp.

        Returns
        -------
        int
            The microsecond of the Timestamp.

        See Also
        --------
        Timestamp.second : Return the second of the Timestamp.
        Timestamp.minute : Return the minute of the Timestamp.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30.2304")
        >>> ts.microsecond
        230400
        """

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the minute of the Timestamp.

        Returns
        -------
        int
            The minute of the Timestamp.

        See Also
        --------
        Timestamp.hour : Return the hour of the Timestamp.
        Timestamp.second : Return the second of the Timestamp.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30")
        >>> ts.minute
        16
        """

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the month of the Timestamp.

        Returns
        -------
        int
            The month of the Timestamp.

        See Also
        --------
        Timestamp.day : Return the day of the Timestamp.
        Timestamp.year : Return the year of the Timestamp.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30")
        >>> ts.month
        8
        """

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the nanosecond of the Timestamp.

        Returns
        -------
        int
            The nanosecond of the Timestamp.

        See Also
        --------
        Timestamp.second : Return the second of the Timestamp.
        Timestamp.microsecond : Return the microsecond of the Timestamp.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30.230400015")
        >>> ts.nanosecond
        15
        """

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the quarter of the year for the `Timestamp`.

        This property returns an integer representing the quarter of the year in
        which the `Timestamp` falls. The quarters are defined as follows:
        - Q1: January 1 to March 31
        - Q2: April 1 to June 30
        - Q3: July 1 to September 30
        - Q4: October 1 to December 31

        Returns
        -------
        int
            The quarter of the year (1 through 4).

        See Also
        --------
        Timestamp.month : Returns the month of the `Timestamp`.
        Timestamp.year : Returns the year of the `Timestamp`.

        Examples
        --------
        Get the quarter for a `Timestamp`:

        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.quarter
        1

        For a `Timestamp` in the fourth quarter:

        >>> ts = pd.Timestamp(2020, 10, 14)
        >>> ts.quarter
        4
        """

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the second of the Timestamp.

        Returns
        -------
        int
            The second of the Timestamp.

        See Also
        --------
        Timestamp.microsecond : Return the microsecond of the Timestamp.
        Timestamp.minute : Return the minute of the Timestamp.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30")
        >>> ts.second
        30
        """

    unit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        The abbreviation associated with self._creso.

        This property returns a string representing the time unit of the Timestamp's
        resolution. It corresponds to the smallest time unit that can be represented
        by this Timestamp object. The possible values are:
        - 's' (second)
        - 'ms' (millisecond)
        - 'us' (microsecond)
        - 'ns' (nanosecond)

        Returns
        -------
        str
            A string abbreviation of the Timestamp's resolution unit:
            - 's' for second
            - 'ms' for millisecond
            - 'us' for microsecond
            - 'ns' for nanosecond

        See Also
        --------
        Timestamp.resolution : Return resolution of the Timestamp.
        Timedelta : A duration expressing the difference between two dates or times.

        Examples
        --------
        >>> pd.Timestamp("2020-01-01 12:34:56").unit
        's'

        >>> pd.Timestamp("2020-01-01 12:34:56.123").unit
        'ms'

        >>> pd.Timestamp("2020-01-01 12:34:56.123456").unit
        'us'

        >>> pd.Timestamp("2020-01-01 12:34:56.123456789").unit
        'ns'
        """

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the value of the Timestamp.

        Returns
        -------
        int
            The integer representation of the Timestamp object in nanoseconds
            since the Unix epoch (1970-01-01 00:00:00 UTC).

        See Also
        --------
        Timestamp.second : Return the second of the Timestamp.
        Timestamp.minute : Return the minute of the Timestamp.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30")
        >>> ts.value
        1725120990000000000
        """

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the week number of the year.

        Returns
        -------
        int

        See Also
        --------
        Timestamp.weekday : Return the day of the week.
        Timestamp.quarter : Return the quarter of the year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.week
        11
        """

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the year of the Timestamp.

        Returns
        -------
        int
            The year of the Timestamp.

        See Also
        --------
        Timestamp.month : Return the month of the Timestamp.
        Timestamp.day : Return the day of the Timestamp.

        Examples
        --------
        >>> ts = pd.Timestamp("2024-08-31 16:16:30")
        >>> ts.year
        2024
        """

    _creso = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _date_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _repr_base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _time_repr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    max = Timestamp('2262-04-11 23:47:16.854775807')
    min = Timestamp('1677-09-21 00:12:43.145224193')
    resolution = Timedelta('0 days 00:00:00.000000001')
    _docstring_max = "\n    Returns the maximum bound possible for Timestamp.\n\n    This property provides access to the largest possible value that\n    can be represented by a Timestamp object.\n\n    Returns\n    -------\n    Timestamp\n\n    See Also\n    --------\n    Timestamp.min: Returns the minimum bound possible for Timestamp.\n    Timestamp.resolution: Returns the smallest possible difference between\n        non-equal Timestamp objects.\n\n    Examples\n    --------\n    >>> pd.Timestamp.max\n    Timestamp('2262-04-11 23:47:16.854775807')\n    "
    _docstring_min = "\n    Returns the minimum bound possible for Timestamp.\n\n    This property provides access to the smallest possible value that\n    can be represented by a Timestamp object.\n\n    Returns\n    -------\n    Timestamp\n\n    See Also\n    --------\n    Timestamp.max: Returns the maximum bound possible for Timestamp.\n    Timestamp.resolution: Returns the smallest possible difference between\n        non-equal Timestamp objects.\n\n    Examples\n    --------\n    >>> pd.Timestamp.min\n    Timestamp('1677-09-21 00:12:43.145224193')\n    "
    _docstring_reso = "\n    Returns the smallest possible difference between non-equal Timestamp objects.\n\n    The resolution value is determined by the underlying representation of time\n    units and is equivalent to Timedelta(nanoseconds=1).\n\n    Returns\n    -------\n    Timedelta\n\n    See Also\n    --------\n    Timestamp.max: Returns the maximum bound possible for Timestamp.\n    Timestamp.min: Returns the minimum bound possible for Timestamp.\n\n    Examples\n    --------\n    >>> pd.Timestamp.resolution\n    Timedelta('0 days 00:00:00.000000001')\n    "
    __array_priority__ = 100
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001D45F4A3970>'


class Timestamp(_Timestamp):
    """
    Pandas replacement for python datetime.datetime object.
    
        Timestamp is the pandas equivalent of python's Datetime
        and is interchangeable with it in most cases. It's the type used
        for the entries that make up a DatetimeIndex, and other timeseries
        oriented data structures in pandas.
    
        Parameters
        ----------
        ts_input : datetime-like, str, int, float
            Value to be converted to Timestamp.
        year : int
            Value of year.
        month : int
            Value of month.
        day : int
            Value of day.
        hour : int, optional, default 0
            Value of hour.
        minute : int, optional, default 0
            Value of minute.
        second : int, optional, default 0
            Value of second.
        microsecond : int, optional, default 0
            Value of microsecond.
        tzinfo : datetime.tzinfo, optional, default None
            Timezone info.
        nanosecond : int, optional, default 0
            Value of nanosecond.
        tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None
            Time zone for time which Timestamp will have.
        unit : str
            Unit used for conversion if ts_input is of type int or float. The
            valid values are 'W', 'D', 'h', 'm', 's', 'ms', 'us', and 'ns'. For
            example, 's' means seconds and 'ms' means milliseconds.
    
            For float inputs, the result will be stored in nanoseconds, and
            the unit attribute will be set as ``'ns'``.
        fold : {0, 1}, default None, keyword-only
            Due to daylight saving time, one wall clock time can occur twice
            when shifting from summer to winter time; fold describes whether the
            datetime-like corresponds  to the first (0) or the second time (1)
            the wall clock hits the ambiguous time.
    
        See Also
        --------
        Timedelta : Represents a duration, the difference between two dates or times.
        datetime.datetime : Python datetime.datetime object.
    
        Notes
        -----
        There are essentially three calling conventions for the constructor. The
        primary form accepts four parameters. They can be passed by position or
        keyword.
    
        The other two forms mimic the parameters from ``datetime.datetime``. They
        can be passed by either position or keyword, but not both mixed together.
    
        Examples
        --------
        Using the primary calling convention:
    
        This converts a datetime-like string
    
        >>> pd.Timestamp('2017-01-01T12')
        Timestamp('2017-01-01 12:00:00')
    
        This converts a float representing a Unix epoch in units of seconds
    
        >>> pd.Timestamp(1513393355.5, unit='s')
        Timestamp('2017-12-16 03:02:35.500000')
    
        This converts an int representing a Unix-epoch in units of weeks
    
        >>> pd.Timestamp(1535, unit='W')
        Timestamp('1999-06-03 00:00:00')
    
        This converts an int representing a Unix-epoch in units of seconds
        and for a particular timezone
    
        >>> pd.Timestamp(1513393355, unit='s', tz='US/Pacific')
        Timestamp('2017-12-15 19:02:35-0800', tz='US/Pacific')
    
        Using the other two forms that mimic the API for ``datetime.datetime``:
    
        >>> pd.Timestamp(2017, 1, 1, 12)
        Timestamp('2017-01-01 12:00:00')
    
        >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)
        Timestamp('2017-01-01 12:00:00')
    """
    def astimezone(self, tz=None): # real signature unknown; restored from __doc__
        """
        Convert timezone-aware Timestamp to another time zone.
        
                This method is used to convert a timezone-aware Timestamp object to a
                different time zone. The original UTC time remains the same; only the
                time zone information is changed. If the Timestamp is timezone-naive, a
                TypeError is raised.
        
                Parameters
                ----------
                tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        
                See Also
                --------
                Timestamp.tz_localize : Localize the Timestamp to a timezone.
                DatetimeIndex.tz_convert : Convert a DatetimeIndex to another time zone.
                DatetimeIndex.tz_localize : Localize a DatetimeIndex to a specific time zone.
                datetime.datetime.astimezone : Convert a datetime object to another time zone.
        
                Examples
                --------
                Create a timestamp object with UTC timezone:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Change to Tokyo timezone:
        
                >>> ts.tz_convert(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Can also use ``astimezone``:
        
                >>> ts.astimezone(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_convert(tz='Asia/Tokyo')
                NaT
        """
        pass

    def ceil(self, freq='h'): # real signature unknown; restored from __doc__
        """
        Return a new Timestamp ceiled to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the ceiling resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise a ValueError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward', 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise a ValueError if there are
                      nonexistent times.
        
                Raises
                ------
                ValueError if the freq cannot be converted.
        
                See Also
                --------
                Timestamp.floor : Round down a Timestamp to the specified resolution.
                Timestamp.round : Round a Timestamp to the specified resolution.
                Series.dt.ceil : Ceil the datetime values in a Series.
        
                Notes
                -----
                If the Timestamp has a timezone, ceiling will take place relative to the
                local ("wall") time and re-localized to the same timezone. When ceiling
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be ceiled using multiple frequency units:
        
                >>> ts.ceil(freq='h')  # hour
                Timestamp('2020-03-14 16:00:00')
        
                >>> ts.ceil(freq='min')  # minute
                Timestamp('2020-03-14 15:33:00')
        
                >>> ts.ceil(freq='s')  # seconds
                Timestamp('2020-03-14 15:32:53')
        
                >>> ts.ceil(freq='us')  # microseconds
                Timestamp('2020-03-14 15:32:52.192549')
        
                ``freq`` can also be a multiple of a single unit, like '5min' (i.e.  5 minutes):
        
                >>> ts.ceil(freq='5min')
                Timestamp('2020-03-14 15:35:00')
        
                or a combination of multiple units, like '1h30min' (i.e. 1 hour and 30 minutes):
        
                >>> ts.ceil(freq='1h30min')
                Timestamp('2020-03-14 16:30:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.ceil()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.ceil("h", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.ceil("h", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    @classmethod
    def combine(cls, date, time): # real signature unknown; restored from __doc__
        """
        Timestamp.combine(date, time)
        
                Combine a date and time into a single Timestamp object.
        
                This method takes a `date` object and a `time` object
                and combines them into a single `Timestamp`
                that has the same date and time fields.
        
                Parameters
                ----------
                date : datetime.date
                    The date part of the Timestamp.
                time : datetime.time
                    The time part of the Timestamp.
        
                Returns
                -------
                Timestamp
                    A new `Timestamp` object representing the combined date and time.
        
                See Also
                --------
                Timestamp : Represents a single timestamp, similar to `datetime`.
                to_datetime : Converts various types of data to datetime.
        
                Examples
                --------
                >>> from datetime import date, time
                >>> pd.Timestamp.combine(date(2020, 3, 14), time(15, 30, 15))
                Timestamp('2020-03-14 15:30:15')
        """
        pass

    def ctime(self): # real signature unknown; restored from __doc__
        """
        Return a ctime() style string representing the Timestamp.
        
                This method returns a string representing the date and time
                in the format returned by the standard library's `time.ctime()`
                function, which is typically in the form 'Day Mon DD HH:MM:SS YYYY'.
        
                If the `Timestamp` is outside the range supported by Python's
                standard library, a `NotImplementedError` is raised.
        
                Returns
                -------
                str
                    A string representing the Timestamp in ctime format.
        
                See Also
                --------
                time.ctime : Return a string representing time in ctime format.
                Timestamp : Represents a single timestamp, similar to `datetime`.
                datetime.datetime.ctime : Return a ctime style string from a datetime object.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00.00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.ctime()
                'Sun Jan  1 10:00:00 2023'
        """
        pass

    def date(self): # real signature unknown; restored from __doc__
        """
        Returns `datetime.date` with the same year, month, and day.
        
                This method extracts the date component from the `Timestamp` and returns
                it as a `datetime.date` object, discarding the time information.
        
                Returns
                -------
                datetime.date
                    The date part of the `Timestamp`.
        
                See Also
                --------
                Timestamp : Represents a single timestamp, similar to `datetime`.
                datetime.datetime.date : Extract the date component from a `datetime` object.
        
                Examples
                --------
                Extract the date from a Timestamp:
        
                >>> ts = pd.Timestamp('2023-01-01 10:00:00.00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.date()
                datetime.date(2023, 1, 1)
        """
        pass

    def dst(self): # real signature unknown; restored from __doc__
        """
        Return the daylight saving time (DST) adjustment.
        
                This method returns the DST adjustment as a `datetime.timedelta` object
                if the Timestamp is timezone-aware and DST is applicable.
        
                See Also
                --------
                Timestamp.tz_localize : Localize the Timestamp to a timezone.
                Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2000-06-01 00:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2000-06-01 00:00:00+0200', tz='Europe/Brussels')
                >>> ts.dst()
                datetime.timedelta(seconds=3600)
        """
        pass

    def floor(self, freq='h'): # real signature unknown; restored from __doc__
        """
        Return a new Timestamp floored to this resolution.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the flooring resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise a ValueError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward', 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise a ValueError if there are
                      nonexistent times.
        
                Raises
                ------
                ValueError if the freq cannot be converted.
        
                See Also
                --------
                Timestamp.ceil : Round up a Timestamp to the specified resolution.
                Timestamp.round : Round a Timestamp to the specified resolution.
                Series.dt.floor : Round down the datetime values in a Series.
        
                Notes
                -----
                If the Timestamp has a timezone, flooring will take place relative to the
                local ("wall") time and re-localized to the same timezone. When flooring
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be floored using multiple frequency units:
        
                >>> ts.floor(freq='h')  # hour
                Timestamp('2020-03-14 15:00:00')
        
                >>> ts.floor(freq='min')  # minute
                Timestamp('2020-03-14 15:32:00')
        
                >>> ts.floor(freq='s')  # seconds
                Timestamp('2020-03-14 15:32:52')
        
                >>> ts.floor(freq='ns')  # nanoseconds
                Timestamp('2020-03-14 15:32:52.192548651')
        
                ``freq`` can also be a multiple of a single unit, like '5min' (i.e.  5 minutes):
        
                >>> ts.floor(freq='5min')
                Timestamp('2020-03-14 15:30:00')
        
                or a combination of multiple units, like '1h30min' (i.e. 1 hour and 30 minutes):
        
                >>> ts.floor(freq='1h30min')
                Timestamp('2020-03-14 15:00:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.floor()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 03:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.floor("2h", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.floor("2h", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    @classmethod
    def fromordinal(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Construct a timestamp from a proleptic Gregorian ordinal.
        
                This method creates a `Timestamp` object corresponding to the given
                proleptic Gregorian ordinal, which is a count of days from January 1,
                0001 (using the proleptic Gregorian calendar). The time part of the
                `Timestamp` is set to midnight (00:00:00) by default.
        
                Parameters
                ----------
                ordinal : int
                    Date corresponding to a proleptic Gregorian ordinal.
                tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for the Timestamp.
        
                Returns
                -------
                Timestamp
                    A `Timestamp` object representing the specified ordinal date.
        
                See Also
                --------
                Timestamp : Represents a single timestamp, similar to `datetime`.
                to_datetime : Converts various types of data to datetime.
        
                Notes
                -----
                By definition there cannot be any tz info on the ordinal itself.
        
                Examples
                --------
                Convert an ordinal to a `Timestamp`:
        
                >>> pd.Timestamp.fromordinal(737425)
                Timestamp('2020-01-01 00:00:00')
        
                Create a `Timestamp` from an ordinal with timezone information:
        
                >>> pd.Timestamp.fromordinal(737425, tz='UTC')
                Timestamp('2020-01-01 00:00:00+0000', tz='UTC')
        """
        pass

    @classmethod
    def fromtimestamp(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Create a `Timestamp` object from a POSIX timestamp.
        
                This method converts a POSIX timestamp (the number of seconds since
                January 1, 1970, 00:00:00 UTC) into a `Timestamp` object. The resulting
                `Timestamp` can be localized to a specific time zone if provided.
        
                Parameters
                ----------
                ts : float
                    The POSIX timestamp to convert, representing seconds since
                    the epoch (1970-01-01 00:00:00 UTC).
                tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile, optional
                    Time zone for the `Timestamp`. If not provided, the `Timestamp` will
                    be timezone-naive (i.e., without time zone information).
        
                Returns
                -------
                Timestamp
                    A `Timestamp` object representing the given POSIX timestamp.
        
                See Also
                --------
                Timestamp : Represents a single timestamp, similar to `datetime`.
                to_datetime : Converts various types of data to datetime.
                datetime.datetime.fromtimestamp : Returns a datetime from a POSIX timestamp.
        
                Examples
                --------
                Convert a POSIX timestamp to a `Timestamp`:
        
                >>> pd.Timestamp.fromtimestamp(1584199972)  # doctest: +SKIP
                Timestamp('2020-03-14 15:32:52')
        
                Note that the output may change depending on your local time and time zone:
        
                >>> pd.Timestamp.fromtimestamp(1584199972, tz='UTC')  # doctest: +SKIP
                Timestamp('2020-03-14 15:32:52+0000', tz='UTC')
        """
        pass

    def isocalendar(self): # real signature unknown; restored from __doc__
        """
        Return a named tuple containing ISO year, week number, and weekday.
        
                See Also
                --------
                DatetimeIndex.isocalendar : Return a 3-tuple containing ISO year,
                    week number, and weekday for the given DatetimeIndex object.
                datetime.date.isocalendar : The equivalent method for `datetime.date` objects.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.isocalendar()
                datetime.IsoCalendarDate(year=2022, week=52, weekday=7)
        """
        pass

    def isoweekday(self): # real signature unknown; restored from __doc__
        """
        Return the day of the week represented by the date.
        
                Monday == 1 ... Sunday == 7.
        
                See Also
                --------
                Timestamp.weekday : Return the day of the week with Monday=0, Sunday=6.
                Timestamp.isocalendar : Return a tuple containing ISO year, week number
                    and weekday.
                datetime.date.isoweekday : Equivalent method in datetime module.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.isoweekday()
                7
        """
        pass

    @classmethod
    def now(cls): # real signature unknown; restored from __doc__
        """
        Return new Timestamp object representing current time local to tz.
        
                This method returns a new `Timestamp` object that represents the current time.
                If a timezone is provided, either through a timezone object or an IANA
                standard timezone identifier, the current time will be localized to that
                timezone.
                Otherwise, it returns the current local time.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to.
        
                See Also
                --------
                to_datetime : Convert argument to datetime.
                Timestamp.utcnow : Return a new Timestamp representing UTC day and time.
                Timestamp.today : Return the current time in the local timezone.
        
                Examples
                --------
                >>> pd.Timestamp.now()  # doctest: +SKIP
                Timestamp('2020-11-16 22:06:16.378782')
        
                If you want a specific timezone, in this case 'Brazil/East':
        
                >>> pd.Timestamp.now('Brazil/East')  # doctest: +SKIP
                Timestamp('2025-11-11 22:17:59.609943-03:00)
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.now()
                NaT
        """
        pass

    def replace(self, year=1999, hour=10): # real signature unknown; restored from __doc__
        """
        Implements datetime.replace, handles nanoseconds.
        
                This method creates a new `Timestamp` object by replacing the specified
                fields with new values. The new `Timestamp` retains the original fields
                that are not explicitly replaced. This method handles nanoseconds, and
                the `tzinfo` parameter allows for timezone replacement without conversion.
        
                Parameters
                ----------
                year : int, optional
                    The year to replace. If `None`, the year is not changed.
                month : int, optional
                    The month to replace. If `None`, the month is not changed.
                day : int, optional
                    The day to replace. If `None`, the day is not changed.
                hour : int, optional
                    The hour to replace. If `None`, the hour is not changed.
                minute : int, optional
                    The minute to replace. If `None`, the minute is not changed.
                second : int, optional
                    The second to replace. If `None`, the second is not changed.
                microsecond : int, optional
                    The microsecond to replace. If `None`, the microsecond is not changed.
                nanosecond : int, optional
                    The nanosecond to replace. If `None`, the nanosecond is not changed.
                tzinfo : tz-convertible, optional
                    The timezone information to replace. If `None`, the timezone is not changed.
                fold : int, optional
                    The fold information to replace. If `None`, the fold is not changed.
        
                Returns
                -------
                Timestamp
                    A new `Timestamp` object with the specified fields replaced.
        
                See Also
                --------
                Timestamp : Represents a single timestamp, similar to `datetime`.
                to_datetime : Converts various types of data to datetime.
        
                Notes
                -----
                The `replace` method does not perform timezone conversions. If you need
                to convert the timezone, use the `tz_convert` method instead.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Replace year and the hour:
        
                >>> ts.replace(year=1999, hour=10)
                Timestamp('1999-03-14 10:32:52.192548651+0000', tz='UTC')
        
                Replace timezone (not a conversion):
        
                >>> import zoneinfo
                >>> ts.replace(tzinfo=zoneinfo.ZoneInfo('US/Pacific'))
                Timestamp('2020-03-14 15:32:52.192548651-0700', tz='US/Pacific')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.replace(tzinfo=zoneinfo.ZoneInfo('US/Pacific'))
                NaT
        """
        pass

    def round(self, freq='h'): # real signature unknown; restored from __doc__
        """
        Round the Timestamp to the specified resolution.
        
                This method rounds the given Timestamp down to a specified frequency
                level. It is particularly useful in data analysis to normalize timestamps
                to regular frequency intervals. For instance, rounding to the nearest
                minute, hour, or day can help in time series comparisons or resampling
                operations.
        
                Parameters
                ----------
                freq : str
                    Frequency string indicating the rounding resolution.
                ambiguous : bool or {'raise', 'NaT'}, default 'raise'
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise a ValueError for an ambiguous time.
        
                nonexistent : {'raise', 'shift_forward', 'shift_backward', 'NaT', timedelta}, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise a ValueError if there are
                      nonexistent times.
        
                Returns
                -------
                a new Timestamp rounded to the given resolution of `freq`
        
                Raises
                ------
                ValueError if the freq cannot be converted
        
                See Also
                --------
                datetime.round : Similar behavior in native Python datetime module.
                Timestamp.floor : Round the Timestamp downward to the nearest multiple
                    of the specified frequency.
                Timestamp.ceil : Round the Timestamp upward to the nearest multiple of
                    the specified frequency.
        
                Notes
                -----
                If the Timestamp has a timezone, rounding will take place relative to the
                local ("wall") time and re-localized to the same timezone. When rounding
                near daylight savings time, use ``nonexistent`` and ``ambiguous`` to
                control the re-localization behavior.
        
                Examples
                --------
                Create a timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
        
                A timestamp can be rounded using multiple frequency units:
        
                >>> ts.round(freq='h')  # hour
                Timestamp('2020-03-14 16:00:00')
        
                >>> ts.round(freq='min')  # minute
                Timestamp('2020-03-14 15:33:00')
        
                >>> ts.round(freq='s')  # seconds
                Timestamp('2020-03-14 15:32:52')
        
                >>> ts.round(freq='ms')  # milliseconds
                Timestamp('2020-03-14 15:32:52.193000')
        
                ``freq`` can also be a multiple of a single unit, like '5min' (i.e.  5 minutes):
        
                >>> ts.round(freq='5min')
                Timestamp('2020-03-14 15:35:00')
        
                or a combination of multiple units, like '1h30min' (i.e. 1 hour and 30 minutes):
        
                >>> ts.round(freq='1h30min')
                Timestamp('2020-03-14 15:00:00')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.round()
                NaT
        
                When rounding near a daylight savings time transition, use ``ambiguous`` or
                ``nonexistent`` to control how the timestamp should be re-localized.
        
                >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")
        
                >>> ts_tz.round("h", ambiguous=False)
                Timestamp('2021-10-31 02:00:00+0100', tz='Europe/Amsterdam')
        
                >>> ts_tz.round("h", ambiguous=True)
                Timestamp('2021-10-31 02:00:00+0200', tz='Europe/Amsterdam')
        """
        pass

    def strftime(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Return a formatted string of the Timestamp.
        
                Parameters
                ----------
                format : str
                    Format string to convert Timestamp to string.
                    See strftime documentation for more information on the format string:
                    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.
        
                See Also
                --------
                Timestamp.isoformat : Return the time formatted according to ISO 8601.
                pd.to_datetime : Convert argument to datetime.
                Period.strftime : Format a single Period.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts.strftime('%Y-%m-%d %X')
                '2020-03-14 15:32:52'
        """
        pass

    @classmethod
    def strptime(cls, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Convert string argument to datetime.
        
                This method is not implemented; calling it will raise NotImplementedError.
                Use pd.to_datetime() instead.
        
                Parameters
                ----------
                date_string : str
                    String to convert to a datetime.
                format : str, default None
                    The format string to parse time, e.g. "%d/%m/%Y".
        
                See Also
                --------
                pd.to_datetime : Convert argument to datetime.
                datetime.datetime.strptime : Return a datetime corresponding to a string
                    representing a date and time, parsed according to a separate
                    format string.
                datetime.datetime.strftime : Return a string representing the date and
                    time, controlled by an explicit format string.
                Timestamp.isoformat : Return the time formatted according to ISO 8601.
        
                Examples
                --------
                >>> pd.Timestamp.strptime("2023-01-01", "%d/%m/%y")
                Traceback (most recent call last):
                NotImplementedError
        """
        pass

    def time(self, hours, minutes, seconds, and_microseconds): # real signature unknown; restored from __doc__
        """
        Return time object with same time but with tzinfo=None.
        
                This method extracts the time part of the `Timestamp` object, excluding any
                timezone information. It returns a `datetime.time` object which only represents
                the time (hours, minutes, seconds, and microseconds).
        
                See Also
                --------
                Timestamp.date : Return date object with same year, month and day.
                Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.
                Timestamp.tz_localize : Localize the Timestamp to a timezone.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.time()
                datetime.time(10, 0)
        """
        pass

    def timetuple(self): # real signature unknown; restored from __doc__
        """
        Return time tuple, compatible with time.localtime().
        
                This method converts the `Timestamp` into a time tuple, which is compatible
                with functions like `time.localtime()`. The time tuple is a named tuple with
                attributes such as year, month, day, hour, minute, second, weekday,
                day of the year, and daylight savings indicator.
        
                See Also
                --------
                time.localtime : Converts a POSIX timestamp into a time tuple.
                Timestamp : The `Timestamp` that represents a specific point in time.
                datetime.datetime.timetuple : Equivalent method in the `datetime` module.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00')
                >>> ts
                Timestamp('2023-01-01 10:00:00')
                >>> ts.timetuple()
                time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1,
                tm_hour=10, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=-1)
        """
        pass

    def timetz(self): # real signature unknown; restored from __doc__
        """
        Return time object with same time and tzinfo.
        
                This method returns a datetime.time object with
                the time and tzinfo corresponding to the pd.Timestamp
                object, ignoring any information about the day/date.
        
                See Also
                --------
                datetime.datetime.timetz : Return datetime.time object with the
                    same time attributes as the datetime object.
                datetime.time : Class to represent the time of day, independent
                    of any particular day.
                datetime.datetime.tzinfo : Attribute of datetime.datetime objects
                    representing the timezone of the datetime object.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
                >>> ts.timetz()
                datetime.time(10, 0, tzinfo=<DstTzInfo 'Europe/Brussels' CET+1:00:00 STD>)
        """
        pass

    @classmethod
    def today(cls): # real signature unknown; restored from __doc__
        """
        Return the current time in the local timezone.
        
                This differs from datetime.today() in that it can be localized to a
                passed timezone.
        
                Parameters
                ----------
                tz : str or timezone object, default None
                    Timezone to localize to.
        
                See Also
                --------
                datetime.datetime.today : Returns the current local date.
                Timestamp.now : Returns current time with optional timezone.
                Timestamp : A class representing a specific timestamp.
        
                Examples
                --------
                >>> pd.Timestamp.today()    # doctest: +SKIP
                Timestamp('2020-11-16 22:37:39.969883')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.today()
                NaT
        """
        pass

    def toordinal(self): # real signature unknown; restored from __doc__
        """
        Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.
        
                The proleptic Gregorian ordinal is a continuous count of days since
                January 1 of year 1, which is considered day 1. This method converts
                the `Timestamp` to its equivalent ordinal number, useful for date arithmetic
                and comparison operations.
        
                See Also
                --------
                datetime.datetime.toordinal : Equivalent method in the `datetime` module.
                Timestamp : The `Timestamp` that represents a specific point in time.
                Timestamp.fromordinal : Create a `Timestamp` from an ordinal.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:50')
                >>> ts
                Timestamp('2023-01-01 10:00:50')
                >>> ts.toordinal()
                738521
        """
        pass

    def to_julian_date(self): # real signature unknown; restored from __doc__
        """
        Convert TimeStamp to a Julian Date.
        
                This method returns the number of days as a float since
                0 Julian date, which is noon January 1, 4713 BC.
        
                See Also
                --------
                Timestamp.toordinal : Return proleptic Gregorian ordinal.
                Timestamp.timestamp : Return POSIX timestamp as float.
                Timestamp : Represents a single timestamp.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2020-03-14T15:32:52')
                >>> ts.to_julian_date()
                2458923.147824074
        """
        pass

    def tzname(self): # real signature unknown; restored from __doc__
        """
        Return time zone name.
        
                This method returns the name of the Timestamp's time zone as a string.
        
                See Also
                --------
                Timestamp.tzinfo : Returns the timezone information of the Timestamp.
                Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
                >>> ts.tzname()
                'CET'
        """
        pass

    def tz_convert(self, tz=None): # real signature unknown; restored from __doc__
        """
        Convert timezone-aware Timestamp to another time zone.
        
                This method is used to convert a timezone-aware Timestamp object to a
                different time zone. The original UTC time remains the same; only the
                time zone information is changed. If the Timestamp is timezone-naive, a
                TypeError is raised.
        
                Parameters
                ----------
                tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding UTC time.
        
                Returns
                -------
                converted : Timestamp
        
                Raises
                ------
                TypeError
                    If Timestamp is tz-naive.
        
                See Also
                --------
                Timestamp.tz_localize : Localize the Timestamp to a timezone.
                DatetimeIndex.tz_convert : Convert a DatetimeIndex to another time zone.
                DatetimeIndex.tz_localize : Localize a DatetimeIndex to a specific time zone.
                datetime.datetime.astimezone : Convert a datetime object to another time zone.
        
                Examples
                --------
                Create a timestamp object with UTC timezone:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
        
                Change to Tokyo timezone:
        
                >>> ts.tz_convert(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Can also use ``astimezone``:
        
                >>> ts.astimezone(tz='Asia/Tokyo')
                Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_convert(tz='Asia/Tokyo')
                NaT
        """
        pass

    def tz_localize(self, tz=None): # real signature unknown; restored from __doc__
        """
        Localize the Timestamp to a timezone.
        
                Convert naive Timestamp to local time zone or remove
                timezone from timezone-aware Timestamp.
        
                Parameters
                ----------
                tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None
                    Time zone for time which Timestamp will be converted to.
                    None will remove timezone holding local time.
        
                ambiguous : bool, 'NaT', default 'raise'
                    When clocks moved backward due to DST, ambiguous times may arise.
                    For example in Central European Time (UTC+01), when going from
                    03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at
                    00:30:00 UTC and at 01:30:00 UTC. In such a situation, the
                    `ambiguous` parameter dictates how ambiguous times should be
                    handled.
        
                    The behavior is as follows:
        
                    * bool contains flags to determine if time is dst or not (note
                      that this flag is only applicable for ambiguous fall dst dates).
                    * 'NaT' will return NaT for an ambiguous time.
                    * 'raise' will raise a ValueError for an ambiguous time.
        
                nonexistent : 'shift_forward', 'shift_backward', 'NaT', timedelta, default 'raise'
                    A nonexistent time does not exist in a particular timezone
                    where clocks moved forward due to DST.
        
                    The behavior is as follows:
        
                    * 'shift_forward' will shift the nonexistent time forward to the
                      closest existing time.
                    * 'shift_backward' will shift the nonexistent time backward to the
                      closest existing time.
                    * 'NaT' will return NaT where there are nonexistent times.
                    * timedelta objects will shift nonexistent times by the timedelta.
                    * 'raise' will raise a ValueError if there are
                      nonexistent times.
        
                Returns
                -------
                localized : Timestamp
        
                Raises
                ------
                TypeError
                    If the Timestamp is tz-aware and tz is not None.
        
                See Also
                --------
                Timestamp.tzinfo : Returns the timezone information of the Timestamp.
                Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.
                DatetimeIndex.tz_localize : Localize a DatetimeIndex to a specific time zone.
                datetime.datetime.astimezone : Convert a datetime object to another time zone.
        
                Examples
                --------
                Create a naive timestamp object:
        
                >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')
                >>> ts
                Timestamp('2020-03-14 15:32:52.192548651')
        
                Add 'Europe/Stockholm' as timezone:
        
                >>> ts.tz_localize(tz='Europe/Stockholm')
                Timestamp('2020-03-14 15:32:52.192548651+0100', tz='Europe/Stockholm')
        
                Analogous for ``pd.NaT``:
        
                >>> pd.NaT.tz_localize()
                NaT
        """
        pass

    @classmethod
    def utcfromtimestamp(cls, ts): # real signature unknown; restored from __doc__
        """
        Timestamp.utcfromtimestamp(ts)
        
                Construct a timezone-aware UTC datetime from a POSIX timestamp.
        
                This method creates a datetime object from a POSIX timestamp, keeping the
                Timestamp object's timezone.
        
                Parameters
                ----------
                ts : float
                    POSIX timestamp.
        
                See Also
                --------
                Timezone.tzname : Return time zone name.
                Timestamp.utcnow : Return a new Timestamp representing UTC day and time.
                Timestamp.fromtimestamp : Transform timestamp[, tz] to tz's local
                    time from POSIX timestamp.
        
                Notes
                -----
                Timestamp.utcfromtimestamp behavior differs from datetime.utcfromtimestamp
                in returning a timezone-aware object.
        
                Examples
                --------
                >>> pd.Timestamp.utcfromtimestamp(1584199972)
                Timestamp('2020-03-14 15:32:52+0000', tz='UTC')
        """
        pass

    @classmethod
    def utcnow(cls): # real signature unknown; restored from __doc__
        """
        Timestamp.utcnow()
        
                Return a new Timestamp representing UTC day and time.
        
                See Also
                --------
                Timestamp : Constructs an arbitrary datetime.
                Timestamp.now : Return the current local date and time, which
                    can be timezone-aware.
                Timestamp.today : Return the current local date and time with
                    timezone information set to None.
                to_datetime : Convert argument to datetime.
                date_range : Return a fixed frequency DatetimeIndex.
                Timestamp.utctimetuple : Return UTC time tuple, compatible with
                    time.localtime().
        
                Examples
                --------
                >>> pd.Timestamp.utcnow()   # doctest: +SKIP
                Timestamp('2020-11-16 22:50:18.092888+0000', tz='UTC')
        """
        pass

    def utcoffset(self): # real signature unknown; restored from __doc__
        """
        Return utc offset.
        
                This method returns the difference between UTC and the local time
                as a `timedelta` object. It is useful for understanding the time
                difference between the current timezone and UTC.
        
                Returns
                -------
                timedelta
                    The difference between UTC and the local time as a `timedelta` object.
        
                See Also
                --------
                datetime.datetime.utcoffset :
                    Standard library method to get the UTC offset of a datetime object.
                Timestamp.tzname : Return the name of the timezone.
                Timestamp.dst : Return the daylight saving time (DST) adjustment.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
                >>> ts.utcoffset()
                datetime.timedelta(seconds=3600)
        """
        pass

    def utctimetuple(self): # real signature unknown; restored from __doc__
        """
        Return UTC time tuple, compatible with `time.localtime()`.
        
                This method converts the Timestamp to UTC and returns a time tuple
                containing 9 components: year, month, day, hour, minute, second,
                weekday, day of year, and DST flag. This is particularly useful for
                converting a Timestamp to a format compatible with time module functions.
        
                Returns
                -------
                time.struct_time
                    A time.struct_time object representing the UTC time.
        
                See Also
                --------
                datetime.datetime.utctimetuple :
                    Return UTC time tuple, compatible with time.localtime().
                Timestamp.timetuple : Return time tuple of local time.
                time.struct_time : Time tuple structure used by time functions.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')
                >>> ts
                Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')
                >>> ts.utctimetuple()
                time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1, tm_hour=9,
                tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=0)
        """
        pass

    def weekday(self): # real signature unknown; restored from __doc__
        """
        Return the day of the week represented by the date.
        
                Monday == 0 ... Sunday == 6.
        
                See Also
                --------
                Timestamp.dayofweek : Return the day of the week with Monday=0, Sunday=6.
                Timestamp.isoweekday : Return the day of the week with Monday=1, Sunday=7.
                datetime.date.weekday : Equivalent method in datetime module.
        
                Examples
                --------
                >>> ts = pd.Timestamp('2023-01-01')
                >>> ts
                Timestamp('2023-01-01  00:00:00')
                >>> ts.weekday()
                6
        """
        pass

    def _round(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the number of days in the month.

        Returns
        -------
        int

        See Also
        --------
        Timestamp.month_name : Return the month name of the Timestamp with
            specified locale.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.days_in_month
        31
        """

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Alias for tzinfo.

        The `tz` property provides a simple and direct way to retrieve the timezone
        information of a `Timestamp` object. It is particularly useful when working
        with time series data that includes timezone information, allowing for easy
        access and manipulation of the timezone context.

        See Also
        --------
        Timestamp.tzinfo : Returns the timezone information of the Timestamp.
        Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.
        Timestamp.tz_localize : Localize the Timestamp to a timezone.

        Examples
        --------
        >>> ts = pd.Timestamp(1584226800, unit='s', tz='Europe/Stockholm')
        >>> ts.tz
        zoneinfo.ZoneInfo(key='Europe/Stockholm')
        """

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns the timezone info of the Timestamp.

        This property returns a `datetime.tzinfo` object if the Timestamp
        is timezone-aware. If the Timestamp has no timezone, it returns `None`.
        If the Timestamp is in UTC or a fixed-offset timezone,
        it returns `datetime.timezone`. If the Timestamp uses an
        IANA timezone (e.g., "America/New_York"), it returns `zoneinfo.ZoneInfo`.

        See Also
        --------
        Timestamp.tz : Alias for `tzinfo`, may return a `zoneinfo.ZoneInfo` object.
        Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.
        Timestamp.tz_localize : Localize the Timestamp to a specific timezone.

        Examples
        --------
        >>> ts = pd.Timestamp("2023-01-01 12:00:00", tz="UTC")
        >>> ts.tzinfo
        datetime.timezone.utc

        >>> ts_naive = pd.Timestamp("2023-01-01 12:00:00")
        >>> ts_naive.tzinfo
        """

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the week number of the year.

        Returns
        -------
        int

        See Also
        --------
        Timestamp.weekday : Return the day of the week.
        Timestamp.quarter : Return the quarter of the year.

        Examples
        --------
        >>> ts = pd.Timestamp(2020, 3, 14)
        >>> ts.week
        11
        """

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _module_source = 'pandas._libs.tslibs.timestamps'
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas\', \'__doc__\': "\\n    Pandas replacement for python datetime.datetime object.\\n\\n    Timestamp is the pandas equivalent of python\'s Datetime\\n    and is interchangeable with it in most cases. It\'s the type used\\n    for the entries that make up a DatetimeIndex, and other timeseries\\n    oriented data structures in pandas.\\n\\n    Parameters\\n    ----------\\n    ts_input : datetime-like, str, int, float\\n        Value to be converted to Timestamp.\\n    year : int\\n        Value of year.\\n    month : int\\n        Value of month.\\n    day : int\\n        Value of day.\\n    hour : int, optional, default 0\\n        Value of hour.\\n    minute : int, optional, default 0\\n        Value of minute.\\n    second : int, optional, default 0\\n        Value of second.\\n    microsecond : int, optional, default 0\\n        Value of microsecond.\\n    tzinfo : datetime.tzinfo, optional, default None\\n        Timezone info.\\n    nanosecond : int, optional, default 0\\n        Value of nanosecond.\\n    tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None\\n        Time zone for time which Timestamp will have.\\n    unit : str\\n        Unit used for conversion if ts_input is of type int or float. The\\n        valid values are \'W\', \'D\', \'h\', \'m\', \'s\', \'ms\', \'us\', and \'ns\'. For\\n        example, \'s\' means seconds and \'ms\' means milliseconds.\\n\\n        For float inputs, the result will be stored in nanoseconds, and\\n        the unit attribute will be set as ``\'ns\'``.\\n    fold : {0, 1}, default None, keyword-only\\n        Due to daylight saving time, one wall clock time can occur twice\\n        when shifting from summer to winter time; fold describes whether the\\n        datetime-like corresponds  to the first (0) or the second time (1)\\n        the wall clock hits the ambiguous time.\\n\\n    See Also\\n    --------\\n    Timedelta : Represents a duration, the difference between two dates or times.\\n    datetime.datetime : Python datetime.datetime object.\\n\\n    Notes\\n    -----\\n    There are essentially three calling conventions for the constructor. The\\n    primary form accepts four parameters. They can be passed by position or\\n    keyword.\\n\\n    The other two forms mimic the parameters from ``datetime.datetime``. They\\n    can be passed by either position or keyword, but not both mixed together.\\n\\n    Examples\\n    --------\\n    Using the primary calling convention:\\n\\n    This converts a datetime-like string\\n\\n    >>> pd.Timestamp(\'2017-01-01T12\')\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    This converts a float representing a Unix epoch in units of seconds\\n\\n    >>> pd.Timestamp(1513393355.5, unit=\'s\')\\n    Timestamp(\'2017-12-16 03:02:35.500000\')\\n\\n    This converts an int representing a Unix-epoch in units of weeks\\n\\n    >>> pd.Timestamp(1535, unit=\'W\')\\n    Timestamp(\'1999-06-03 00:00:00\')\\n\\n    This converts an int representing a Unix-epoch in units of seconds\\n    and for a particular timezone\\n\\n    >>> pd.Timestamp(1513393355, unit=\'s\', tz=\'US/Pacific\')\\n    Timestamp(\'2017-12-15 19:02:35-0800\', tz=\'US/Pacific\')\\n\\n    Using the other two forms that mimic the API for ``datetime.datetime``:\\n\\n    >>> pd.Timestamp(2017, 1, 1, 12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n    ", \'fromordinal\': <classmethod(<cyfunction Timestamp.fromordinal at 0x000001D45F615C70>)>, \'now\': <classmethod(<cyfunction Timestamp.now at 0x000001D45F615D60>)>, \'today\': <classmethod(<cyfunction Timestamp.today at 0x000001D45F615E50>)>, \'utcnow\': <classmethod(<cyfunction Timestamp.utcnow at 0x000001D45F615F40>)>, \'utcfromtimestamp\': <classmethod(<cyfunction Timestamp.utcfromtimestamp at 0x000001D45F616030>)>, \'fromtimestamp\': <classmethod(<cyfunction Timestamp.fromtimestamp at 0x000001D45F616120>)>, \'strftime\': <cyfunction Timestamp.strftime at 0x000001D45F616210>, \'ctime\': <cyfunction Timestamp.ctime at 0x000001D45F616300>, \'date\': <cyfunction Timestamp.date at 0x000001D45F6163F0>, \'dst\': <cyfunction Timestamp.dst at 0x000001D45F6164E0>, \'isocalendar\': <cyfunction Timestamp.isocalendar at 0x000001D45F6165D0>, \'tzname\': <cyfunction Timestamp.tzname at 0x000001D45F6166C0>, \'tzinfo\': <property object at 0x000001D45F4A3880>, \'utcoffset\': <cyfunction Timestamp.utcoffset at 0x000001D45F6168A0>, \'utctimetuple\': <cyfunction Timestamp.utctimetuple at 0x000001D45F616990>, \'time\': <cyfunction Timestamp.time at 0x000001D45F616A80>, \'timetuple\': <cyfunction Timestamp.timetuple at 0x000001D45F616B70>, \'timetz\': <cyfunction Timestamp.timetz at 0x000001D45F616C60>, \'toordinal\': <cyfunction Timestamp.toordinal at 0x000001D45F616D50>, \'strptime\': <classmethod(<cyfunction Timestamp.strptime at 0x000001D45F616E40>)>, \'combine\': <classmethod(<cyfunction Timestamp.combine at 0x000001D45F616F30>)>, \'__new__\': <staticmethod(<cyfunction Timestamp.__new__ at 0x000001D45F617020>)>, \'_round\': <cyfunction Timestamp._round at 0x000001D45F617110>, \'round\': <cyfunction Timestamp.round at 0x000001D45F617200>, \'floor\': <cyfunction Timestamp.floor at 0x000001D45F6172F0>, \'ceil\': <cyfunction Timestamp.ceil at 0x000001D45F6173E0>, \'tz\': <property object at 0x000001D45F4A3790>, \'tz_localize\': <cyfunction Timestamp.tz_localize at 0x000001D45F6176B0>, \'tz_convert\': <cyfunction Timestamp.tz_convert at 0x000001D45F6177A0>, \'astimezone\': <cyfunction Timestamp.tz_convert at 0x000001D45F6177A0>, \'replace\': <cyfunction Timestamp.replace at 0x000001D45F617890>, \'to_julian_date\': <cyfunction Timestamp.to_julian_date at 0x000001D45F617980>, \'isoweekday\': <cyfunction Timestamp.isoweekday at 0x000001D45F617A70>, \'weekday\': <cyfunction Timestamp.weekday at 0x000001D45F617B60>, \'__dict__\': <attribute \'__dict__\' of \'Timestamp\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timestamp\' objects>, \'_module_source\': \'pandas._libs.tslibs.timestamps\', \'weekofyear\': <attribute \'week\' of \'pandas._libs.tslibs.timestamps._Timestamp\' objects>, \'daysinmonth\': <attribute \'days_in_month\' of \'pandas._libs.tslibs.timestamps._Timestamp\' objects>})'


# variables with complex values

_no_input = None # (!) real value is '<object object at 0x000001D43E0A2F10>'

_zero_time = None # (!) real value is 'datetime.time(0, 0)'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D45F47DA30>'

__pyx_capi__ = {
    'create_timestamp_from_ts': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_10timestamps__Timestamp *(__pyx_t_5numpy_int64_t, npy_datetimestruct, PyDateTime_TZInfo *, int, struct __pyx_opt_args_6pandas_5_libs_6tslibs_10timestamps_create_timestamp_from_ts *__pyx_optional_args)" at 0x000001D45F4A3060>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.timestamps', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D45F47DA30>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\timestamps.cp314-win_amd64.pyd')"

__test__ = {
    'Timestamp.ceil (line 2989)': '\n        Return a new Timestamp ceiled to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the ceiling resolution.\n        ambiguous : bool or {\'raise\', \'NaT\'}, default \'raise\'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * \'NaT\' will return NaT for an ambiguous time.\n            * \'raise\' will raise a ValueError for an ambiguous time.\n\n        nonexistent : {\'raise\', \'shift_forward\', \'shift_backward\', \'NaT\', timedelta}, default \'raise\'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * \'shift_forward\' will shift the nonexistent time forward to the\n              closest existing time.\n            * \'shift_backward\' will shift the nonexistent time backward to the\n              closest existing time.\n            * \'NaT\' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * \'raise\' will raise a ValueError if there are\n              nonexistent times.\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n\n        See Also\n        --------\n        Timestamp.floor : Round down a Timestamp to the specified resolution.\n        Timestamp.round : Round a Timestamp to the specified resolution.\n        Series.dt.ceil : Ceil the datetime values in a Series.\n\n        Notes\n        -----\n        If the Timestamp has a timezone, ceiling will take place relative to the\n        local ("wall") time and re-localized to the same timezone. When ceiling\n        near daylight savings time, use ``nonexistent`` and ``ambiguous`` to\n        control the re-localization behavior.\n\n        Examples\n        --------\n        Create a timestamp object:\n\n        >>> ts = pd.Timestamp(\'2020-03-14T15:32:52.192548651\')\n\n        A timestamp can be ceiled using multiple frequency units:\n\n        >>> ts.ceil(freq=\'h\')  # hour\n        Timestamp(\'2020-03-14 16:00:00\')\n\n        >>> ts.ceil(freq=\'min\')  # minute\n        Timestamp(\'2020-03-14 15:33:00\')\n\n        >>> ts.ceil(freq=\'s\')  # seconds\n        Timestamp(\'2020-03-14 15:32:53\')\n\n        >>> ts.ceil(freq=\'us\')  # microseconds\n        Timestamp(\'2020-03-14 15:32:52.192549\')\n\n        ``freq`` can also be a multiple of a single unit, like \'5min\' (i.e.  5 minutes):\n\n        >>> ts.ceil(freq=\'5min\')\n        Timestamp(\'2020-03-14 15:35:00\')\n\n        or a combination of multiple units, like \'1h30min\' (i.e. 1 hour and 30 minutes):\n\n        >>> ts.ceil(freq=\'1h30min\')\n        Timestamp(\'2020-03-14 16:30:00\')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.ceil()\n        NaT\n\n        When rounding near a daylight savings time transition, use ``ambiguous`` or\n        ``nonexistent`` to control how the timestamp should be re-localized.\n\n        >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")\n\n        >>> ts_tz.ceil("h", ambiguous=False)\n        Timestamp(\'2021-10-31 02:00:00+0100\', tz=\'Europe/Amsterdam\')\n\n        >>> ts_tz.ceil("h", ambiguous=True)\n        Timestamp(\'2021-10-31 02:00:00+0200\', tz=\'Europe/Amsterdam\')\n        ',
    'Timestamp.combine (line 2545)': "\n        Timestamp.combine(date, time)\n\n        Combine a date and time into a single Timestamp object.\n\n        This method takes a `date` object and a `time` object\n        and combines them into a single `Timestamp`\n        that has the same date and time fields.\n\n        Parameters\n        ----------\n        date : datetime.date\n            The date part of the Timestamp.\n        time : datetime.time\n            The time part of the Timestamp.\n\n        Returns\n        -------\n        Timestamp\n            A new `Timestamp` object representing the combined date and time.\n\n        See Also\n        --------\n        Timestamp : Represents a single timestamp, similar to `datetime`.\n        to_datetime : Converts various types of data to datetime.\n\n        Examples\n        --------\n        >>> from datetime import date, time\n        >>> pd.Timestamp.combine(date(2020, 3, 14), time(15, 30, 15))\n        Timestamp('2020-03-14 15:30:15')\n        ",
    'Timestamp.ctime (line 2147)': "\n        Return a ctime() style string representing the Timestamp.\n\n        This method returns a string representing the date and time\n        in the format returned by the standard library's `time.ctime()`\n        function, which is typically in the form 'Day Mon DD HH:MM:SS YYYY'.\n\n        If the `Timestamp` is outside the range supported by Python's\n        standard library, a `NotImplementedError` is raised.\n\n        Returns\n        -------\n        str\n            A string representing the Timestamp in ctime format.\n\n        See Also\n        --------\n        time.ctime : Return a string representing time in ctime format.\n        Timestamp : Represents a single timestamp, similar to `datetime`.\n        datetime.datetime.ctime : Return a ctime style string from a datetime object.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00.00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.ctime()\n        'Sun Jan  1 10:00:00 2023'\n        ",
    'Timestamp.date (line 2190)': "\n        Returns `datetime.date` with the same year, month, and day.\n\n        This method extracts the date component from the `Timestamp` and returns\n        it as a `datetime.date` object, discarding the time information.\n\n        Returns\n        -------\n        datetime.date\n            The date part of the `Timestamp`.\n\n        See Also\n        --------\n        Timestamp : Represents a single timestamp, similar to `datetime`.\n        datetime.datetime.date : Extract the date component from a `datetime` object.\n\n        Examples\n        --------\n        Extract the date from a Timestamp:\n\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00.00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.date()\n        datetime.date(2023, 1, 1)\n        ",
    'Timestamp.dst (line 2226)': "\n        Return the daylight saving time (DST) adjustment.\n\n        This method returns the DST adjustment as a `datetime.timedelta` object\n        if the Timestamp is timezone-aware and DST is applicable.\n\n        See Also\n        --------\n        Timestamp.tz_localize : Localize the Timestamp to a timezone.\n        Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2000-06-01 00:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2000-06-01 00:00:00+0200', tz='Europe/Brussels')\n        >>> ts.dst()\n        datetime.timedelta(seconds=3600)\n        ",
    'Timestamp.floor (line 2894)': '\n        Return a new Timestamp floored to this resolution.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the flooring resolution.\n        ambiguous : bool or {\'raise\', \'NaT\'}, default \'raise\'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * \'NaT\' will return NaT for an ambiguous time.\n            * \'raise\' will raise a ValueError for an ambiguous time.\n\n        nonexistent : {\'raise\', \'shift_forward\', \'shift_backward\', \'NaT\', timedelta}, default \'raise\'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * \'shift_forward\' will shift the nonexistent time forward to the\n              closest existing time.\n            * \'shift_backward\' will shift the nonexistent time backward to the\n              closest existing time.\n            * \'NaT\' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * \'raise\' will raise a ValueError if there are\n              nonexistent times.\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted.\n\n        See Also\n        --------\n        Timestamp.ceil : Round up a Timestamp to the specified resolution.\n        Timestamp.round : Round a Timestamp to the specified resolution.\n        Series.dt.floor : Round down the datetime values in a Series.\n\n        Notes\n        -----\n        If the Timestamp has a timezone, flooring will take place relative to the\n        local ("wall") time and re-localized to the same timezone. When flooring\n        near daylight savings time, use ``nonexistent`` and ``ambiguous`` to\n        control the re-localization behavior.\n\n        Examples\n        --------\n        Create a timestamp object:\n\n        >>> ts = pd.Timestamp(\'2020-03-14T15:32:52.192548651\')\n\n        A timestamp can be floored using multiple frequency units:\n\n        >>> ts.floor(freq=\'h\')  # hour\n        Timestamp(\'2020-03-14 15:00:00\')\n\n        >>> ts.floor(freq=\'min\')  # minute\n        Timestamp(\'2020-03-14 15:32:00\')\n\n        >>> ts.floor(freq=\'s\')  # seconds\n        Timestamp(\'2020-03-14 15:32:52\')\n\n        >>> ts.floor(freq=\'ns\')  # nanoseconds\n        Timestamp(\'2020-03-14 15:32:52.192548651\')\n\n        ``freq`` can also be a multiple of a single unit, like \'5min\' (i.e.  5 minutes):\n\n        >>> ts.floor(freq=\'5min\')\n        Timestamp(\'2020-03-14 15:30:00\')\n\n        or a combination of multiple units, like \'1h30min\' (i.e. 1 hour and 30 minutes):\n\n        >>> ts.floor(freq=\'1h30min\')\n        Timestamp(\'2020-03-14 15:00:00\')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.floor()\n        NaT\n\n        When rounding near a daylight savings time transition, use ``ambiguous`` or\n        ``nonexistent`` to control how the timestamp should be re-localized.\n\n        >>> ts_tz = pd.Timestamp("2021-10-31 03:30:00").tz_localize("Europe/Amsterdam")\n\n        >>> ts_tz.floor("2h", ambiguous=False)\n        Timestamp(\'2021-10-31 02:00:00+0100\', tz=\'Europe/Amsterdam\')\n\n        >>> ts_tz.floor("2h", ambiguous=True)\n        Timestamp(\'2021-10-31 02:00:00+0200\', tz=\'Europe/Amsterdam\')\n        ',
    'Timestamp.fromordinal (line 1869)': "\n        Construct a timestamp from a proleptic Gregorian ordinal.\n\n        This method creates a `Timestamp` object corresponding to the given\n        proleptic Gregorian ordinal, which is a count of days from January 1,\n        0001 (using the proleptic Gregorian calendar). The time part of the\n        `Timestamp` is set to midnight (00:00:00) by default.\n\n        Parameters\n        ----------\n        ordinal : int\n            Date corresponding to a proleptic Gregorian ordinal.\n        tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for the Timestamp.\n\n        Returns\n        -------\n        Timestamp\n            A `Timestamp` object representing the specified ordinal date.\n\n        See Also\n        --------\n        Timestamp : Represents a single timestamp, similar to `datetime`.\n        to_datetime : Converts various types of data to datetime.\n\n        Notes\n        -----\n        By definition there cannot be any tz info on the ordinal itself.\n\n        Examples\n        --------\n        Convert an ordinal to a `Timestamp`:\n\n        >>> pd.Timestamp.fromordinal(737425)\n        Timestamp('2020-01-01 00:00:00')\n\n        Create a `Timestamp` from an ordinal with timezone information:\n\n        >>> pd.Timestamp.fromordinal(737425, tz='UTC')\n        Timestamp('2020-01-01 00:00:00+0000', tz='UTC')\n        ",
    'Timestamp.fromtimestamp (line 2067)': "\n        Create a `Timestamp` object from a POSIX timestamp.\n\n        This method converts a POSIX timestamp (the number of seconds since\n        January 1, 1970, 00:00:00 UTC) into a `Timestamp` object. The resulting\n        `Timestamp` can be localized to a specific time zone if provided.\n\n        Parameters\n        ----------\n        ts : float\n            The POSIX timestamp to convert, representing seconds since\n            the epoch (1970-01-01 00:00:00 UTC).\n        tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile, optional\n            Time zone for the `Timestamp`. If not provided, the `Timestamp` will\n            be timezone-naive (i.e., without time zone information).\n\n        Returns\n        -------\n        Timestamp\n            A `Timestamp` object representing the given POSIX timestamp.\n\n        See Also\n        --------\n        Timestamp : Represents a single timestamp, similar to `datetime`.\n        to_datetime : Converts various types of data to datetime.\n        datetime.datetime.fromtimestamp : Returns a datetime from a POSIX timestamp.\n\n        Examples\n        --------\n        Convert a POSIX timestamp to a `Timestamp`:\n\n        >>> pd.Timestamp.fromtimestamp(1584199972)  # doctest: +SKIP\n        Timestamp('2020-03-14 15:32:52')\n\n        Note that the output may change depending on your local time and time zone:\n\n        >>> pd.Timestamp.fromtimestamp(1584199972, tz='UTC')  # doctest: +SKIP\n        Timestamp('2020-03-14 15:32:52+0000', tz='UTC')\n        ",
    'Timestamp.isocalendar (line 2248)': "\n        Return a named tuple containing ISO year, week number, and weekday.\n\n        See Also\n        --------\n        DatetimeIndex.isocalendar : Return a 3-tuple containing ISO year,\n            week number, and weekday for the given DatetimeIndex object.\n        datetime.date.isocalendar : The equivalent method for `datetime.date` objects.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.isocalendar()\n        datetime.IsoCalendarDate(year=2022, week=52, weekday=7)\n        ",
    'Timestamp.isoweekday (line 3515)': "\n        Return the day of the week represented by the date.\n\n        Monday == 1 ... Sunday == 7.\n\n        See Also\n        --------\n        Timestamp.weekday : Return the day of the week with Monday=0, Sunday=6.\n        Timestamp.isocalendar : Return a tuple containing ISO year, week number\n            and weekday.\n        datetime.date.isoweekday : Equivalent method in datetime module.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.isoweekday()\n        7\n        ",
    'Timestamp.now (line 1914)': "\n        Return new Timestamp object representing current time local to tz.\n\n        This method returns a new `Timestamp` object that represents the current time.\n        If a timezone is provided, either through a timezone object or an IANA\n        standard timezone identifier, the current time will be localized to that\n        timezone.\n        Otherwise, it returns the current local time.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n\n        See Also\n        --------\n        to_datetime : Convert argument to datetime.\n        Timestamp.utcnow : Return a new Timestamp representing UTC day and time.\n        Timestamp.today : Return the current time in the local timezone.\n\n        Examples\n        --------\n        >>> pd.Timestamp.now()  # doctest: +SKIP\n        Timestamp('2020-11-16 22:06:16.378782')\n\n        If you want a specific timezone, in this case 'Brazil/East':\n\n        >>> pd.Timestamp.now('Brazil/East')  # doctest: +SKIP\n        Timestamp('2025-11-11 22:17:59.609943-03:00)\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.now()\n        NaT\n        ",
    'Timestamp.replace (line 3295)': "\n        Implements datetime.replace, handles nanoseconds.\n\n        This method creates a new `Timestamp` object by replacing the specified\n        fields with new values. The new `Timestamp` retains the original fields\n        that are not explicitly replaced. This method handles nanoseconds, and\n        the `tzinfo` parameter allows for timezone replacement without conversion.\n\n        Parameters\n        ----------\n        year : int, optional\n            The year to replace. If `None`, the year is not changed.\n        month : int, optional\n            The month to replace. If `None`, the month is not changed.\n        day : int, optional\n            The day to replace. If `None`, the day is not changed.\n        hour : int, optional\n            The hour to replace. If `None`, the hour is not changed.\n        minute : int, optional\n            The minute to replace. If `None`, the minute is not changed.\n        second : int, optional\n            The second to replace. If `None`, the second is not changed.\n        microsecond : int, optional\n            The microsecond to replace. If `None`, the microsecond is not changed.\n        nanosecond : int, optional\n            The nanosecond to replace. If `None`, the nanosecond is not changed.\n        tzinfo : tz-convertible, optional\n            The timezone information to replace. If `None`, the timezone is not changed.\n        fold : int, optional\n            The fold information to replace. If `None`, the fold is not changed.\n\n        Returns\n        -------\n        Timestamp\n            A new `Timestamp` object with the specified fields replaced.\n\n        See Also\n        --------\n        Timestamp : Represents a single timestamp, similar to `datetime`.\n        to_datetime : Converts various types of data to datetime.\n\n        Notes\n        -----\n        The `replace` method does not perform timezone conversions. If you need\n        to convert the timezone, use the `tz_convert` method instead.\n\n        Examples\n        --------\n        Create a timestamp object:\n\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')\n        >>> ts\n        Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')\n\n        Replace year and the hour:\n\n        >>> ts.replace(year=1999, hour=10)\n        Timestamp('1999-03-14 10:32:52.192548651+0000', tz='UTC')\n\n        Replace timezone (not a conversion):\n\n        >>> import zoneinfo\n        >>> ts.replace(tzinfo=zoneinfo.ZoneInfo('US/Pacific'))\n        Timestamp('2020-03-14 15:32:52.192548651-0700', tz='US/Pacific')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.replace(tzinfo=zoneinfo.ZoneInfo('US/Pacific'))\n        NaT\n        ",
    'Timestamp.round (line 2785)': '\n        Round the Timestamp to the specified resolution.\n\n        This method rounds the given Timestamp down to a specified frequency\n        level. It is particularly useful in data analysis to normalize timestamps\n        to regular frequency intervals. For instance, rounding to the nearest\n        minute, hour, or day can help in time series comparisons or resampling\n        operations.\n\n        Parameters\n        ----------\n        freq : str\n            Frequency string indicating the rounding resolution.\n        ambiguous : bool or {\'raise\', \'NaT\'}, default \'raise\'\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * \'NaT\' will return NaT for an ambiguous time.\n            * \'raise\' will raise a ValueError for an ambiguous time.\n\n        nonexistent : {\'raise\', \'shift_forward\', \'shift_backward\', \'NaT\', timedelta}, default \'raise\'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            * \'shift_forward\' will shift the nonexistent time forward to the\n              closest existing time.\n            * \'shift_backward\' will shift the nonexistent time backward to the\n              closest existing time.\n            * \'NaT\' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * \'raise\' will raise a ValueError if there are\n              nonexistent times.\n\n        Returns\n        -------\n        a new Timestamp rounded to the given resolution of `freq`\n\n        Raises\n        ------\n        ValueError if the freq cannot be converted\n\n        See Also\n        --------\n        datetime.round : Similar behavior in native Python datetime module.\n        Timestamp.floor : Round the Timestamp downward to the nearest multiple\n            of the specified frequency.\n        Timestamp.ceil : Round the Timestamp upward to the nearest multiple of\n            the specified frequency.\n\n        Notes\n        -----\n        If the Timestamp has a timezone, rounding will take place relative to the\n        local ("wall") time and re-localized to the same timezone. When rounding\n        near daylight savings time, use ``nonexistent`` and ``ambiguous`` to\n        control the re-localization behavior.\n\n        Examples\n        --------\n        Create a timestamp object:\n\n        >>> ts = pd.Timestamp(\'2020-03-14T15:32:52.192548651\')\n\n        A timestamp can be rounded using multiple frequency units:\n\n        >>> ts.round(freq=\'h\')  # hour\n        Timestamp(\'2020-03-14 16:00:00\')\n\n        >>> ts.round(freq=\'min\')  # minute\n        Timestamp(\'2020-03-14 15:33:00\')\n\n        >>> ts.round(freq=\'s\')  # seconds\n        Timestamp(\'2020-03-14 15:32:52\')\n\n        >>> ts.round(freq=\'ms\')  # milliseconds\n        Timestamp(\'2020-03-14 15:32:52.193000\')\n\n        ``freq`` can also be a multiple of a single unit, like \'5min\' (i.e.  5 minutes):\n\n        >>> ts.round(freq=\'5min\')\n        Timestamp(\'2020-03-14 15:35:00\')\n\n        or a combination of multiple units, like \'1h30min\' (i.e. 1 hour and 30 minutes):\n\n        >>> ts.round(freq=\'1h30min\')\n        Timestamp(\'2020-03-14 15:00:00\')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.round()\n        NaT\n\n        When rounding near a daylight savings time transition, use ``ambiguous`` or\n        ``nonexistent`` to control how the timestamp should be re-localized.\n\n        >>> ts_tz = pd.Timestamp("2021-10-31 01:30:00").tz_localize("Europe/Amsterdam")\n\n        >>> ts_tz.round("h", ambiguous=False)\n        Timestamp(\'2021-10-31 02:00:00+0100\', tz=\'Europe/Amsterdam\')\n\n        >>> ts_tz.round("h", ambiguous=True)\n        Timestamp(\'2021-10-31 02:00:00+0200\', tz=\'Europe/Amsterdam\')\n        ',
    'Timestamp.strftime (line 2111)': "\n        Return a formatted string of the Timestamp.\n\n        Parameters\n        ----------\n        format : str\n            Format string to convert Timestamp to string.\n            See strftime documentation for more information on the format string:\n            https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior.\n\n        See Also\n        --------\n        Timestamp.isoformat : Return the time formatted according to ISO 8601.\n        pd.to_datetime : Convert argument to datetime.\n        Period.strftime : Format a single Period.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.strftime('%Y-%m-%d %X')\n        '2020-03-14 15:32:52'\n        ",
    'Timestamp.strptime (line 2509)': '\n        Convert string argument to datetime.\n\n        This method is not implemented; calling it will raise NotImplementedError.\n        Use pd.to_datetime() instead.\n\n        Parameters\n        ----------\n        date_string : str\n            String to convert to a datetime.\n        format : str, default None\n            The format string to parse time, e.g. "%d/%m/%Y".\n\n        See Also\n        --------\n        pd.to_datetime : Convert argument to datetime.\n        datetime.datetime.strptime : Return a datetime corresponding to a string\n            representing a date and time, parsed according to a separate\n            format string.\n        datetime.datetime.strftime : Return a string representing the date and\n            time, controlled by an explicit format string.\n        Timestamp.isoformat : Return the time formatted according to ISO 8601.\n\n        Examples\n        --------\n        >>> pd.Timestamp.strptime("2023-01-01", "%d/%m/%y")\n        Traceback (most recent call last):\n        NotImplementedError\n        ',
    'Timestamp.time (line 2388)': "\n        Return time object with same time but with tzinfo=None.\n\n        This method extracts the time part of the `Timestamp` object, excluding any\n        timezone information. It returns a `datetime.time` object which only represents\n        the time (hours, minutes, seconds, and microseconds).\n\n        See Also\n        --------\n        Timestamp.date : Return date object with same year, month and day.\n        Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.\n        Timestamp.tz_localize : Localize the Timestamp to a timezone.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.time()\n        datetime.time(10, 0)\n        ",
    'Timestamp.timetuple (line 2412)': "\n        Return time tuple, compatible with time.localtime().\n\n        This method converts the `Timestamp` into a time tuple, which is compatible\n        with functions like `time.localtime()`. The time tuple is a named tuple with\n        attributes such as year, month, day, hour, minute, second, weekday,\n        day of the year, and daylight savings indicator.\n\n        See Also\n        --------\n        time.localtime : Converts a POSIX timestamp into a time tuple.\n        Timestamp : The `Timestamp` that represents a specific point in time.\n        datetime.datetime.timetuple : Equivalent method in the `datetime` module.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00')\n        >>> ts.timetuple()\n        time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1,\n        tm_hour=10, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=-1)\n        ",
    'Timestamp.timetz (line 2447)': "\n        Return time object with same time and tzinfo.\n\n        This method returns a datetime.time object with\n        the time and tzinfo corresponding to the pd.Timestamp\n        object, ignoring any information about the day/date.\n\n        See Also\n        --------\n        datetime.datetime.timetz : Return datetime.time object with the\n            same time attributes as the datetime object.\n        datetime.time : Class to represent the time of day, independent\n            of any particular day.\n        datetime.datetime.tzinfo : Attribute of datetime.datetime objects\n            representing the timezone of the datetime object.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')\n        >>> ts.timetz()\n        datetime.time(10, 0, tzinfo=<DstTzInfo 'Europe/Brussels' CET+1:00:00 STD>)\n        ",
    'Timestamp.to_julian_date (line 3476)': "\n        Convert TimeStamp to a Julian Date.\n\n        This method returns the number of days as a float since\n        0 Julian date, which is noon January 1, 4713 BC.\n\n        See Also\n        --------\n        Timestamp.toordinal : Return proleptic Gregorian ordinal.\n        Timestamp.timestamp : Return POSIX timestamp as float.\n        Timestamp : Represents a single timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52')\n        >>> ts.to_julian_date()\n        2458923.147824074\n        ",
    'Timestamp.today (line 1955)': "\n        Return the current time in the local timezone.\n\n        This differs from datetime.today() in that it can be localized to a\n        passed timezone.\n\n        Parameters\n        ----------\n        tz : str or timezone object, default None\n            Timezone to localize to.\n\n        See Also\n        --------\n        datetime.datetime.today : Returns the current local date.\n        Timestamp.now : Returns current time with optional timezone.\n        Timestamp : A class representing a specific timestamp.\n\n        Examples\n        --------\n        >>> pd.Timestamp.today()    # doctest: +SKIP\n        Timestamp('2020-11-16 22:37:39.969883')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.today()\n        NaT\n        ",
    'Timestamp.toordinal (line 2474)': "\n        Return proleptic Gregorian ordinal. January 1 of year 1 is day 1.\n\n        The proleptic Gregorian ordinal is a continuous count of days since\n        January 1 of year 1, which is considered day 1. This method converts\n        the `Timestamp` to its equivalent ordinal number, useful for date arithmetic\n        and comparison operations.\n\n        See Also\n        --------\n        datetime.datetime.toordinal : Equivalent method in the `datetime` module.\n        Timestamp : The `Timestamp` that represents a specific point in time.\n        Timestamp.fromordinal : Create a `Timestamp` from an ordinal.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:50')\n        >>> ts\n        Timestamp('2023-01-01 10:00:50')\n        >>> ts.toordinal()\n        738521\n        ",
    'Timestamp.tz (line 3084)': "\n        Alias for tzinfo.\n\n        The `tz` property provides a simple and direct way to retrieve the timezone\n        information of a `Timestamp` object. It is particularly useful when working\n        with time series data that includes timezone information, allowing for easy\n        access and manipulation of the timezone context.\n\n        See Also\n        --------\n        Timestamp.tzinfo : Returns the timezone information of the Timestamp.\n        Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.\n        Timestamp.tz_localize : Localize the Timestamp to a timezone.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(1584226800, unit='s', tz='Europe/Stockholm')\n        >>> ts.tz\n        zoneinfo.ZoneInfo(key='Europe/Stockholm')\n        ",
    'Timestamp.tz_convert (line 3228)': "\n        Convert timezone-aware Timestamp to another time zone.\n\n        This method is used to convert a timezone-aware Timestamp object to a\n        different time zone. The original UTC time remains the same; only the\n        time zone information is changed. If the Timestamp is timezone-naive, a\n        TypeError is raised.\n\n        Parameters\n        ----------\n        tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding UTC time.\n\n        Returns\n        -------\n        converted : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If Timestamp is tz-naive.\n\n        See Also\n        --------\n        Timestamp.tz_localize : Localize the Timestamp to a timezone.\n        DatetimeIndex.tz_convert : Convert a DatetimeIndex to another time zone.\n        DatetimeIndex.tz_localize : Localize a DatetimeIndex to a specific time zone.\n        datetime.datetime.astimezone : Convert a datetime object to another time zone.\n\n        Examples\n        --------\n        Create a timestamp object with UTC timezone:\n\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')\n        >>> ts\n        Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')\n\n        Change to Tokyo timezone:\n\n        >>> ts.tz_convert(tz='Asia/Tokyo')\n        Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')\n\n        Can also use ``astimezone``:\n\n        >>> ts.astimezone(tz='Asia/Tokyo')\n        Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.tz_convert(tz='Asia/Tokyo')\n        NaT\n        ",
    'Timestamp.tz_localize (line 3116)': "\n        Localize the Timestamp to a timezone.\n\n        Convert naive Timestamp to local time zone or remove\n        timezone from timezone-aware Timestamp.\n\n        Parameters\n        ----------\n        tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None\n            Time zone for time which Timestamp will be converted to.\n            None will remove timezone holding local time.\n\n        ambiguous : bool, 'NaT', default 'raise'\n            When clocks moved backward due to DST, ambiguous times may arise.\n            For example in Central European Time (UTC+01), when going from\n            03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at\n            00:30:00 UTC and at 01:30:00 UTC. In such a situation, the\n            `ambiguous` parameter dictates how ambiguous times should be\n            handled.\n\n            The behavior is as follows:\n\n            * bool contains flags to determine if time is dst or not (note\n              that this flag is only applicable for ambiguous fall dst dates).\n            * 'NaT' will return NaT for an ambiguous time.\n            * 'raise' will raise a ValueError for an ambiguous time.\n\n        nonexistent : 'shift_forward', 'shift_backward', 'NaT', timedelta, default 'raise'\n            A nonexistent time does not exist in a particular timezone\n            where clocks moved forward due to DST.\n\n            The behavior is as follows:\n\n            * 'shift_forward' will shift the nonexistent time forward to the\n              closest existing time.\n            * 'shift_backward' will shift the nonexistent time backward to the\n              closest existing time.\n            * 'NaT' will return NaT where there are nonexistent times.\n            * timedelta objects will shift nonexistent times by the timedelta.\n            * 'raise' will raise a ValueError if there are\n              nonexistent times.\n\n        Returns\n        -------\n        localized : Timestamp\n\n        Raises\n        ------\n        TypeError\n            If the Timestamp is tz-aware and tz is not None.\n\n        See Also\n        --------\n        Timestamp.tzinfo : Returns the timezone information of the Timestamp.\n        Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.\n        DatetimeIndex.tz_localize : Localize a DatetimeIndex to a specific time zone.\n        datetime.datetime.astimezone : Convert a datetime object to another time zone.\n\n        Examples\n        --------\n        Create a naive timestamp object:\n\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts\n        Timestamp('2020-03-14 15:32:52.192548651')\n\n        Add 'Europe/Stockholm' as timezone:\n\n        >>> ts.tz_localize(tz='Europe/Stockholm')\n        Timestamp('2020-03-14 15:32:52.192548651+0100', tz='Europe/Stockholm')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.tz_localize()\n        NaT\n        ",
    'Timestamp.tzinfo (line 2298)': '\n        Returns the timezone info of the Timestamp.\n\n        This property returns a `datetime.tzinfo` object if the Timestamp\n        is timezone-aware. If the Timestamp has no timezone, it returns `None`.\n        If the Timestamp is in UTC or a fixed-offset timezone,\n        it returns `datetime.timezone`. If the Timestamp uses an\n        IANA timezone (e.g., "America/New_York"), it returns `zoneinfo.ZoneInfo`.\n\n        See Also\n        --------\n        Timestamp.tz : Alias for `tzinfo`, may return a `zoneinfo.ZoneInfo` object.\n        Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.\n        Timestamp.tz_localize : Localize the Timestamp to a specific timezone.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2023-01-01 12:00:00", tz="UTC")\n        >>> ts.tzinfo\n        datetime.timezone.utc\n\n        >>> ts_naive = pd.Timestamp("2023-01-01 12:00:00")\n        >>> ts_naive.tzinfo\n        ',
    'Timestamp.tzname (line 2277)': "\n        Return time zone name.\n\n        This method returns the name of the Timestamp's time zone as a string.\n\n        See Also\n        --------\n        Timestamp.tzinfo : Returns the timezone information of the Timestamp.\n        Timestamp.tz_convert : Convert timezone-aware Timestamp to another time zone.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')\n        >>> ts.tzname()\n        'CET'\n        ",
    'Timestamp.utcfromtimestamp (line 2022)': "\n        Timestamp.utcfromtimestamp(ts)\n\n        Construct a timezone-aware UTC datetime from a POSIX timestamp.\n\n        This method creates a datetime object from a POSIX timestamp, keeping the\n        Timestamp object's timezone.\n\n        Parameters\n        ----------\n        ts : float\n            POSIX timestamp.\n\n        See Also\n        --------\n        Timezone.tzname : Return time zone name.\n        Timestamp.utcnow : Return a new Timestamp representing UTC day and time.\n        Timestamp.fromtimestamp : Transform timestamp[, tz] to tz's local\n            time from POSIX timestamp.\n\n        Notes\n        -----\n        Timestamp.utcfromtimestamp behavior differs from datetime.utcfromtimestamp\n        in returning a timezone-aware object.\n\n        Examples\n        --------\n        >>> pd.Timestamp.utcfromtimestamp(1584199972)\n        Timestamp('2020-03-14 15:32:52+0000', tz='UTC')\n        ",
    'Timestamp.utcnow (line 1986)': "\n        Timestamp.utcnow()\n\n        Return a new Timestamp representing UTC day and time.\n\n        See Also\n        --------\n        Timestamp : Constructs an arbitrary datetime.\n        Timestamp.now : Return the current local date and time, which\n            can be timezone-aware.\n        Timestamp.today : Return the current local date and time with\n            timezone information set to None.\n        to_datetime : Convert argument to datetime.\n        date_range : Return a fixed frequency DatetimeIndex.\n        Timestamp.utctimetuple : Return UTC time tuple, compatible with\n            time.localtime().\n\n        Examples\n        --------\n        >>> pd.Timestamp.utcnow()   # doctest: +SKIP\n        Timestamp('2020-11-16 22:50:18.092888+0000', tz='UTC')\n        ",
    'Timestamp.utcoffset (line 2326)': "\n        Return utc offset.\n\n        This method returns the difference between UTC and the local time\n        as a `timedelta` object. It is useful for understanding the time\n        difference between the current timezone and UTC.\n\n        Returns\n        -------\n        timedelta\n            The difference between UTC and the local time as a `timedelta` object.\n\n        See Also\n        --------\n        datetime.datetime.utcoffset :\n            Standard library method to get the UTC offset of a datetime object.\n        Timestamp.tzname : Return the name of the timezone.\n        Timestamp.dst : Return the daylight saving time (DST) adjustment.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')\n        >>> ts.utcoffset()\n        datetime.timedelta(seconds=3600)\n        ",
    'Timestamp.utctimetuple (line 2356)': "\n        Return UTC time tuple, compatible with `time.localtime()`.\n\n        This method converts the Timestamp to UTC and returns a time tuple\n        containing 9 components: year, month, day, hour, minute, second,\n        weekday, day of year, and DST flag. This is particularly useful for\n        converting a Timestamp to a format compatible with time module functions.\n\n        Returns\n        -------\n        time.struct_time\n            A time.struct_time object representing the UTC time.\n\n        See Also\n        --------\n        datetime.datetime.utctimetuple :\n            Return UTC time tuple, compatible with time.localtime().\n        Timestamp.timetuple : Return time tuple of local time.\n        time.struct_time : Time tuple structure used by time functions.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01 10:00:00', tz='Europe/Brussels')\n        >>> ts\n        Timestamp('2023-01-01 10:00:00+0100', tz='Europe/Brussels')\n        >>> ts.utctimetuple()\n        time.struct_time(tm_year=2023, tm_mon=1, tm_mday=1, tm_hour=9,\n        tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=0)\n        ",
    'Timestamp.weekday (line 3541)': "\n        Return the day of the week represented by the date.\n\n        Monday == 0 ... Sunday == 6.\n\n        See Also\n        --------\n        Timestamp.dayofweek : Return the day of the week with Monday=0, Sunday=6.\n        Timestamp.isoweekday : Return the day of the week with Monday=1, Sunday=7.\n        datetime.date.weekday : Equivalent method in datetime module.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2023-01-01')\n        >>> ts\n        Timestamp('2023-01-01  00:00:00')\n        >>> ts.weekday()\n        6\n        ",
    '_Timestamp.as_unit (line 1504)': '\n        Convert the underlying int64 representation to the given unit.\n\n        Parameters\n        ----------\n        unit : {"ns", "us", "ms", "s"}\n        round_ok : bool, default True\n            If False and the conversion requires rounding, raise.\n\n        Returns\n        -------\n        Timestamp\n\n        See Also\n        --------\n        Timestamp.asm8 : Return numpy datetime64 format with same precision.\n        Timestamp.to_pydatetime : Convert Timestamp object to a native\n            Python datetime object.\n        to_timedelta : Convert argument into timedelta object,\n            which can represent differences in times.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(\'2023-01-01 00:00:00.01\')\n        >>> ts\n        Timestamp(\'2023-01-01 00:00:00.010000\')\n        >>> ts.unit\n        \'ms\'\n        >>> ts = ts.as_unit(\'s\')\n        >>> ts\n        Timestamp(\'2023-01-01 00:00:00\')\n        >>> ts.unit\n        \'s\'\n        ',
    '_Timestamp.asm8.__get__ (line 1548)': "\n        Return numpy datetime64 format with same precision.\n\n        See Also\n        --------\n        numpy.datetime64 : Numpy datatype for dates and times with high precision.\n        Timestamp.to_numpy : Convert the Timestamp to a NumPy datetime64.\n        to_datetime : Convert argument to datetime.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14, 15)\n        >>> ts.asm8\n        numpy.datetime64('2020-03-14T15:00:00.000000')\n        ",
    '_Timestamp.day.__get__ (line 1057)': '\n        Return the day of the Timestamp.\n\n        Returns\n        -------\n        int\n            The day of the Timestamp.\n\n        See Also\n        --------\n        Timestamp.week : Return the week number of the year.\n        Timestamp.weekday : Return the day of the week.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30")\n        >>> ts.day\n        31\n        ',
    '_Timestamp.day_name (line 876)': "\n        Return the day name of the Timestamp with specified locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the day name.\n\n        Returns\n        -------\n        str\n\n        See Also\n        --------\n        Timestamp.day_of_week : Return day of the week.\n        Timestamp.day_of_year : Return day of the year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.day_name()\n        'Saturday'\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.day_name()\n        nan\n        ",
    '_Timestamp.day_of_week.__get__ (line 975)': '\n        Return day of the week.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Timestamp.isoweekday : Return the ISO day of the week represented by the date.\n        Timestamp.weekday : Return the day of the week represented by the date.\n        Timestamp.day_of_year : Return day of the year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.day_of_week\n        5\n        ',
    '_Timestamp.day_of_year.__get__ (line 998)': '\n        Return the day of the year.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Timestamp.day_of_week : Return day of the week.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.day_of_year\n        74\n        ',
    '_Timestamp.days_in_month.__get__ (line 1287)': '\n        Return the number of days in the month.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Timestamp.month_name : Return the month name of the Timestamp with\n            specified locale.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.days_in_month\n        31\n        ',
    '_Timestamp.fold.__get__ (line 1080)': '\n        Return the fold value of the Timestamp.\n\n        Returns\n        -------\n        int\n            The fold value of the Timestamp, where 0 indicates the first occurrence\n            of the ambiguous time, and 1 indicates the second.\n\n        See Also\n        --------\n        Timestamp.dst : Return the daylight saving time (DST) adjustment.\n        Timestamp.tzinfo : Return the timezone information associated.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-11-03 01:30:00")\n        >>> ts.fold\n        0\n        ',
    '_Timestamp.hour.__get__ (line 1150)': '\n        Return the hour of the Timestamp.\n\n        Returns\n        -------\n        int\n            The hour of the Timestamp.\n\n        See Also\n        --------\n        Timestamp.minute : Return the minute of the Timestamp.\n        Timestamp.second : Return the second of the Timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30")\n        >>> ts.hour\n        16\n        ',
    '_Timestamp.is_leap_year.__get__ (line 947)': '\n        Return True if year is a leap year.\n\n        A leap year is a year, which has 366 days (instead of 365) including 29th of\n        February as an intercalary day. Leap years are years which are multiples of\n        four with the exception of years divisible by 100 but not by 400.\n\n        Returns\n        -------\n        bool\n            True if year is a leap year, else False\n\n        See Also\n        --------\n        Period.is_leap_year : Return True if the period’s year is in a leap year.\n        DatetimeIndex.is_leap_year : Boolean indicator if the date belongs to a\n            leap year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_leap_year\n        True\n        ',
    '_Timestamp.is_month_end.__get__ (line 734)': '\n        Check if the date is the last day of the month.\n\n        Returns\n        -------\n        bool\n            True if the date is the last day of the month.\n\n        See Also\n        --------\n        Timestamp.is_month_start : Similar property indicating month start.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_month_end\n        False\n\n        >>> ts = pd.Timestamp(2020, 12, 31)\n        >>> ts.is_month_end\n        True\n        ',
    '_Timestamp.is_month_start.__get__ (line 708)': '\n        Check if the date is the first day of the month.\n\n        Returns\n        -------\n        bool\n            True if the date is the first day of the month.\n\n        See Also\n        --------\n        Timestamp.is_month_end : Similar property indicating the last day of the month.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_month_start\n        False\n\n        >>> ts = pd.Timestamp(2020, 1, 1)\n        >>> ts.is_month_start\n        True\n        ',
    '_Timestamp.is_quarter_end.__get__ (line 787)': '\n        Check if date is last day of the quarter.\n\n        Returns\n        -------\n        bool\n            True if date is last day of the quarter.\n\n        See Also\n        --------\n        Timestamp.is_quarter_start : Similar property indicating the quarter start.\n        Timestamp.quarter : Return the quarter of the date.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_quarter_end\n        False\n\n        >>> ts = pd.Timestamp(2020, 3, 31)\n        >>> ts.is_quarter_end\n        True\n        ',
    '_Timestamp.is_quarter_start.__get__ (line 760)': '\n        Check if the date is the first day of the quarter.\n\n        Returns\n        -------\n        bool\n            True if date is first day of the quarter.\n\n        See Also\n        --------\n        Timestamp.is_quarter_end : Similar property indicating the quarter end.\n        Timestamp.quarter : Return the quarter of the date.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_quarter_start\n        False\n\n        >>> ts = pd.Timestamp(2020, 4, 1)\n        >>> ts.is_quarter_start\n        True\n        ',
    '_Timestamp.is_year_end.__get__ (line 839)': '\n        Return True if date is last day of the year.\n\n        Returns\n        -------\n        bool\n\n        See Also\n        --------\n        Timestamp.is_year_start : Similar property indicating the start of the year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_year_end\n        False\n\n        >>> ts = pd.Timestamp(2020, 12, 31)\n        >>> ts.is_year_end\n        True\n        ',
    '_Timestamp.is_year_start.__get__ (line 814)': '\n        Return True if date is first day of the year.\n\n        Returns\n        -------\n        bool\n\n        See Also\n        --------\n        Timestamp.is_year_end : Similar property indicating the end of the year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.is_year_start\n        False\n\n        >>> ts = pd.Timestamp(2020, 1, 1)\n        >>> ts.is_year_start\n        True\n        ',
    '_Timestamp.isoformat (line 1380)': "\n        Return the time formatted according to ISO 8601.\n\n        The full format looks like 'YYYY-MM-DD HH:MM:SS.mmmmmmnnn'.\n        By default, the fractional part is omitted if self.microsecond == 0\n        and self._nanosecond == 0.\n\n        If self.tzinfo is not None, the UTC offset is also attached,\n        giving a full format of 'YYYY-MM-DD HH:MM:SS.mmmmmmnnn+HH:MM'.\n\n        Parameters\n        ----------\n        sep : str, default 'T'\n            String used as the separator between the date and time.\n\n        timespec : str, default 'auto'\n            Specifies the number of additional terms of the time to include.\n            The valid values are 'auto', 'hours', 'minutes', 'seconds',\n            'milliseconds', 'microseconds', and 'nanoseconds'.\n\n        Returns\n        -------\n        str\n\n        See Also\n        --------\n        Timestamp.strftime : Return a formatted string.\n        Timestamp.isocalendar : Return a tuple containing ISO year, week number and\n            weekday.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.isoformat()\n        '2020-03-14T15:32:52.192548651'\n        >>> ts.isoformat(timespec='microseconds')\n        '2020-03-14T15:32:52.192548'\n        ",
    '_Timestamp.microsecond.__get__ (line 1219)': '\n        Return the microsecond of the Timestamp.\n\n        Returns\n        -------\n        int\n            The microsecond of the Timestamp.\n\n        See Also\n        --------\n        Timestamp.second : Return the second of the Timestamp.\n        Timestamp.minute : Return the minute of the Timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30.2304")\n        >>> ts.microsecond\n        230400\n        ',
    '_Timestamp.minute.__get__ (line 1173)': '\n        Return the minute of the Timestamp.\n\n        Returns\n        -------\n        int\n            The minute of the Timestamp.\n\n        See Also\n        --------\n        Timestamp.hour : Return the hour of the Timestamp.\n        Timestamp.second : Return the second of the Timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30")\n        >>> ts.minute\n        16\n        ',
    '_Timestamp.month.__get__ (line 1127)': '\n        Return the month of the Timestamp.\n\n        Returns\n        -------\n        int\n            The month of the Timestamp.\n\n        See Also\n        --------\n        Timestamp.day : Return the day of the Timestamp.\n        Timestamp.year : Return the year of the Timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30")\n        >>> ts.month\n        8\n        ',
    '_Timestamp.month_name (line 907)': "\n        Return the month name of the Timestamp with specified locale.\n\n        This method returns the full name of the month corresponding to the\n        `Timestamp`, such as 'January', 'February', etc. The month name can\n        be returned in a specified locale if provided; otherwise, it defaults\n        to the English locale.\n\n        Parameters\n        ----------\n        locale : str, default None (English locale)\n            Locale determining the language in which to return the month name.\n\n        Returns\n        -------\n        str\n            The full month name as a string.\n\n        See Also\n        --------\n        Timestamp.day_name : Returns the name of the day of the week.\n        Timestamp.strftime : Returns a formatted string of the Timestamp.\n        datetime.datetime.strftime : Returns a string representing the date and time.\n\n        Examples\n        --------\n        Get the month name in English (default):\n\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.month_name()\n        'March'\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.month_name()\n        nan\n        ",
    '_Timestamp.nanosecond.__get__ (line 1242)': '\n        Return the nanosecond of the Timestamp.\n\n        Returns\n        -------\n        int\n            The nanosecond of the Timestamp.\n\n        See Also\n        --------\n        Timestamp.second : Return the second of the Timestamp.\n        Timestamp.microsecond : Return the microsecond of the Timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30.230400015")\n        >>> ts.nanosecond\n        15\n        ',
    '_Timestamp.normalize (line 1312)': "\n        Normalize Timestamp to midnight, preserving tz information.\n\n        This method sets the time component of the `Timestamp` to midnight (00:00:00),\n        while preserving the date and time zone information. It is useful when you\n        need to standardize the time across different `Timestamp` objects without\n        altering the time zone or the date.\n\n        Returns\n        -------\n        Timestamp\n\n        See Also\n        --------\n        Timestamp.floor : Rounds `Timestamp` down to the nearest frequency.\n        Timestamp.ceil : Rounds `Timestamp` up to the nearest frequency.\n        Timestamp.round : Rounds `Timestamp` to the nearest frequency.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14, 15, 30)\n        >>> ts.normalize()\n        Timestamp('2020-03-14 00:00:00')\n        ",
    '_Timestamp.quarter.__get__ (line 1019)': '\n        Return the quarter of the year for the `Timestamp`.\n\n        This property returns an integer representing the quarter of the year in\n        which the `Timestamp` falls. The quarters are defined as follows:\n        - Q1: January 1 to March 31\n        - Q2: April 1 to June 30\n        - Q3: July 1 to September 30\n        - Q4: October 1 to December 31\n\n        Returns\n        -------\n        int\n            The quarter of the year (1 through 4).\n\n        See Also\n        --------\n        Timestamp.month : Returns the month of the `Timestamp`.\n        Timestamp.year : Returns the year of the `Timestamp`.\n\n        Examples\n        --------\n        Get the quarter for a `Timestamp`:\n\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.quarter\n        1\n\n        For a `Timestamp` in the fourth quarter:\n\n        >>> ts = pd.Timestamp(2020, 10, 14)\n        >>> ts.quarter\n        4\n        ',
    '_Timestamp.second.__get__ (line 1196)': '\n        Return the second of the Timestamp.\n\n        Returns\n        -------\n        int\n            The second of the Timestamp.\n\n        See Also\n        --------\n        Timestamp.microsecond : Return the microsecond of the Timestamp.\n        Timestamp.minute : Return the minute of the Timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30")\n        >>> ts.second\n        30\n        ',
    '_Timestamp.timestamp (line 1567)': "\n        Return POSIX timestamp as float.\n\n        This method converts the `Timestamp` object to a POSIX timestamp, which is\n        the number of seconds since the Unix epoch (January 1, 1970). The returned\n        value is a floating-point number, where the integer part represents the\n        seconds, and the fractional part represents the microseconds.\n\n        Returns\n        -------\n        float\n            The POSIX timestamp representation of the `Timestamp` object.\n\n        See Also\n        --------\n        Timestamp.fromtimestamp : Construct a `Timestamp` from a POSIX timestamp.\n        datetime.datetime.timestamp : Equivalent method from the `datetime` module.\n        Timestamp.to_pydatetime : Convert the `Timestamp` to a `datetime` object.\n        Timestamp.to_datetime64 : Converts `Timestamp` to `numpy.datetime64`.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')\n        >>> ts.timestamp()\n        1584199972.192548\n        ",
    '_Timestamp.to_datetime64 (line 1649)': "\n        Return a NumPy datetime64 object with same precision.\n\n        This method returns a numpy.datetime64 object with the same\n        date and time information and precision as the pd.Timestamp object.\n\n        See Also\n        --------\n        numpy.datetime64 : Class to represent dates and times with high precision.\n        Timestamp.to_numpy : Alias for this method.\n        Timestamp.asm8 : Alias for this method.\n        pd.to_datetime : Convert argument to datetime.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(year=2023, month=1, day=1,\n        ...                   hour=10, second=15)\n        >>> ts\n        Timestamp('2023-01-01 10:00:15')\n        >>> ts.to_datetime64()\n        numpy.datetime64('2023-01-01T10:00:15.000000')\n        ",
    '_Timestamp.to_numpy (line 1676)': "\n        Convert the Timestamp to a NumPy datetime64.\n\n        This is an alias method for `Timestamp.to_datetime64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Parameters\n        ----------\n        dtype : dtype, optional\n            Data type of the output, ignored in this method as the return type\n            is always `numpy.datetime64`.\n        copy : bool, default False\n            Whether to ensure that the returned value is a new object. This\n            parameter is also ignored as the method does not support copying.\n\n        Returns\n        -------\n        numpy.datetime64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.to_numpy()\n        numpy.datetime64('2020-03-14T15:32:52.192548651')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.to_numpy()\n        numpy.datetime64('NaT', 'ns')\n        ",
    '_Timestamp.to_period (line 1718)': "\n        Return a period of which this timestamp is an observation.\n\n        This method converts the given Timestamp to a Period object,\n        which represents a span of time,such as a year, month, etc.,\n        based on the specified frequency.\n\n        Parameters\n        ----------\n        freq : str, optional\n            Frequency string for the period (e.g., 'Y', 'M', 'W'). Defaults to `None`.\n\n        See Also\n        --------\n        Timestamp : Represents a specific timestamp.\n        Period : Represents a span of time.\n        to_period : Converts an object to a Period.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> # Year end frequency\n        >>> ts.to_period(freq='Y')\n        Period('2020', 'Y-DEC')\n\n        >>> # Month end frequency\n        >>> ts.to_period(freq='M')\n        Period('2020-03', 'M')\n\n        >>> # Weekly frequency\n        >>> ts.to_period(freq='W')\n        Period('2020-03-09/2020-03-15', 'W-SUN')\n\n        >>> # Quarter end frequency\n        >>> ts.to_period(freq='Q')\n        Period('2020Q1', 'Q-DEC')\n        ",
    '_Timestamp.to_pydatetime (line 1601)': "\n        Convert a Timestamp object to a native Python datetime object.\n\n        This method is useful for when you need to utilize a pandas Timestamp\n        object in contexts where native Python datetime objects are expected\n        or required. The conversion discards the nanoseconds component, and a\n        warning can be issued in such cases if desired.\n\n        Parameters\n        ----------\n        warn : bool, default True\n            If True, issues a warning when the timestamp includes nonzero\n            nanoseconds, as these will be discarded during the conversion.\n\n        Returns\n        -------\n        datetime.datetime or NaT\n            Returns a datetime.datetime object representing the timestamp,\n            with year, month, day, hour, minute, second, and microsecond components.\n            If the timestamp is NaT (Not a Time), returns NaT.\n\n        See Also\n        --------\n        datetime.datetime : The standard Python datetime class that this method\n            returns.\n        Timestamp.timestamp : Convert a Timestamp object to POSIX timestamp.\n        Timestamp.to_datetime64 : Convert a Timestamp object to numpy.datetime64.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548')\n        >>> ts.to_pydatetime()\n        datetime.datetime(2020, 3, 14, 15, 32, 52, 192548)\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.to_pydatetime()\n        NaT\n        ",
    '_Timestamp.unit.__get__ (line 345)': '\n        The abbreviation associated with self._creso.\n\n        This property returns a string representing the time unit of the Timestamp\'s\n        resolution. It corresponds to the smallest time unit that can be represented\n        by this Timestamp object. The possible values are:\n        - \'s\' (second)\n        - \'ms\' (millisecond)\n        - \'us\' (microsecond)\n        - \'ns\' (nanosecond)\n\n        Returns\n        -------\n        str\n            A string abbreviation of the Timestamp\'s resolution unit:\n            - \'s\' for second\n            - \'ms\' for millisecond\n            - \'us\' for microsecond\n            - \'ns\' for nanosecond\n\n        See Also\n        --------\n        Timestamp.resolution : Return resolution of the Timestamp.\n        Timedelta : A duration expressing the difference between two dates or times.\n\n        Examples\n        --------\n        >>> pd.Timestamp("2020-01-01 12:34:56").unit\n        \'s\'\n\n        >>> pd.Timestamp("2020-01-01 12:34:56.123").unit\n        \'ms\'\n\n        >>> pd.Timestamp("2020-01-01 12:34:56.123456").unit\n        \'us\'\n\n        >>> pd.Timestamp("2020-01-01 12:34:56.123456789").unit\n        \'ns\'\n        ',
    '_Timestamp.value.__get__ (line 313)': '\n        Return the value of the Timestamp.\n\n        Returns\n        -------\n        int\n            The integer representation of the Timestamp object in nanoseconds\n            since the Unix epoch (1970-01-01 00:00:00 UTC).\n\n        See Also\n        --------\n        Timestamp.second : Return the second of the Timestamp.\n        Timestamp.minute : Return the minute of the Timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30")\n        >>> ts.value\n        1725120990000000000\n        ',
    '_Timestamp.week.__get__ (line 1265)': '\n        Return the week number of the year.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Timestamp.weekday : Return the day of the week.\n        Timestamp.quarter : Return the quarter of the year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2020, 3, 14)\n        >>> ts.week\n        11\n        ',
    '_Timestamp.year.__get__ (line 1104)': '\n        Return the year of the Timestamp.\n\n        Returns\n        -------\n        int\n            The year of the Timestamp.\n\n        See Also\n        --------\n        Timestamp.month : Return the month of the Timestamp.\n        Timestamp.day : Return the day of the Timestamp.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2024-08-31 16:16:30")\n        >>> ts.year\n        2024\n        ',
}

