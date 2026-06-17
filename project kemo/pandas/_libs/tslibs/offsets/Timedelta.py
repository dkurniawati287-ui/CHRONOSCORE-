# encoding: utf-8
# module pandas._libs.tslibs.offsets
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\tslibs\offsets.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\re\__init__.py
import time as time # <module 'time' (built-in)>
import warnings as warnings # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\warnings.py
import numpy as np # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\numpy\__init__.py
from pandas._libs.properties import cache_readonly

import pandas._libs.tslibs.timedeltas as __pandas__libs_tslibs_timedeltas
import pandas._libs.tslibs.timestamps as __pandas__libs_tslibs_timestamps


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
    _req_any_kwargs_new = None # (!) real value is "{'weeks', 'minutes', 'days', 'hours', 'nanoseconds', 'milliseconds', 'seconds', 'microseconds'}"
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas\', \'__doc__\': \'\\n    Represents a duration, the difference between two dates or times.\\n\\n    Timedelta is the pandas equivalent of python\\\'s ``datetime.timedelta``\\n    and is interchangeable with it in most cases.\\n\\n    Parameters\\n    ----------\\n    value : Timedelta, timedelta, np.timedelta64, str, int or float\\n        Input value.\\n    unit : str, default \\\'ns\\\'\\n        If input is an integer, denote the unit of the input.\\n        If input is a float, denote the unit of the integer parts.\\n        The decimal parts with resolution lower than 1 nanosecond are ignored.\\n\\n        Possible values:\\n\\n        * \\\'W\\\', or \\\'D\\\'\\n        * \\\'days\\\', or \\\'day\\\'\\n        * \\\'hours\\\', \\\'hour\\\', \\\'hr\\\', or \\\'h\\\'\\n        * \\\'minutes\\\', \\\'minute\\\', \\\'min\\\', or \\\'m\\\'\\n        * \\\'seconds\\\', \\\'second\\\', \\\'sec\\\', or \\\'s\\\'\\n        * \\\'milliseconds\\\', \\\'millisecond\\\', \\\'millis\\\', \\\'milli\\\', or \\\'ms\\\'\\n        * \\\'microseconds\\\', \\\'microsecond\\\', \\\'micros\\\', \\\'micro\\\', or \\\'us\\\'\\n        * \\\'nanoseconds\\\', \\\'nanosecond\\\', \\\'nanos\\\', \\\'nano\\\', or \\\'ns\\\'.\\n\\n        .. deprecated:: 3.0.0\\n\\n            Allowing the values `w`, `d`, `MIN`, `MS`, `US` and `NS` to denote units\\n            are deprecated in favour of the values `W`, `D`, `min`, `ms`, `us` and `ns`.\\n\\n    **kwargs\\n        Available kwargs: {days, seconds, microseconds,\\n        milliseconds, minutes, hours, weeks}.\\n        Values for construction in compat with datetime.timedelta.\\n        Numpy ints and floats will be coerced to python ints and floats.\\n\\n    See Also\\n    --------\\n    Timestamp : Represents a single timestamp in time.\\n    TimedeltaIndex : Immutable Index of timedelta64 data.\\n    DateOffset : Standard kind of date increment used for a date range.\\n    to_timedelta : Convert argument to timedelta.\\n    datetime.timedelta : Represents a duration in the datetime module.\\n    numpy.timedelta64 : Represents a duration compatible with NumPy.\\n\\n    Notes\\n    -----\\n    The constructor may take in either both values of value and unit or\\n    kwargs as above. Either one of them must be used during initialization\\n\\n    The ``.value`` attribute is always in ns.\\n\\n    If the precision is higher than nanoseconds, the precision of the duration is\\n    truncated to nanoseconds.\\n\\n    Examples\\n    --------\\n    Here we initialize Timedelta object with both value and unit\\n\\n    >>> td = pd.Timedelta(1, "D")\\n    >>> td\\n    Timedelta(\\\'1 days 00:00:00\\\')\\n\\n    Here we initialize the Timedelta object with kwargs\\n\\n    >>> td2 = pd.Timedelta(days=1)\\n    >>> td2\\n    Timedelta(\\\'1 days 00:00:00\\\')\\n\\n    We see that either way we get the same result\\n    \', \'_req_any_kwargs_new\': {\'weeks\', \'minutes\', \'days\', \'hours\', \'nanoseconds\', \'milliseconds\', \'seconds\', \'microseconds\'}, \'__new__\': <staticmethod(<cyfunction Timedelta.__new__ at 0x000001A4FF65A3F0>)>, \'__setstate__\': <cyfunction Timedelta.__setstate__ at 0x000001A4FF65A4E0>, \'__reduce__\': <cyfunction Timedelta.__reduce__ at 0x000001A4FF65A5D0>, \'_round\': <cyfunction Timedelta._round at 0x000001A4FF65A6C0>, \'round\': <cyfunction Timedelta.round at 0x000001A4FF65A7B0>, \'floor\': <cyfunction Timedelta.floor at 0x000001A4FF65A8A0>, \'ceil\': <cyfunction Timedelta.ceil at 0x000001A4FF65A990>, \'__neg__\': <cyfunction _op_unary_method.<locals>.f at 0x000001A4FF65AB70>, \'__pos__\': <cyfunction _op_unary_method.<locals>.f at 0x000001A4FF65AD50>, \'__abs__\': <cyfunction _op_unary_method.<locals>.f at 0x000001A4FF65AF30>, \'__add__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001A4FF65B110>, \'__radd__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001A4FF65B2F0>, \'__sub__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001A4FF65B4D0>, \'__rsub__\': <cyfunction _binary_op_method_timedeltalike.<locals>.f at 0x000001A4FF65B6B0>, \'__mul__\': <cyfunction Timedelta.__mul__ at 0x000001A4FF65B7A0>, \'__rmul__\': <cyfunction Timedelta.__mul__ at 0x000001A4FF65B7A0>, \'__truediv__\': <cyfunction Timedelta.__truediv__ at 0x000001A4FF65B890>, \'__rtruediv__\': <cyfunction Timedelta.__rtruediv__ at 0x000001A4FF65B980>, \'__floordiv__\': <cyfunction Timedelta.__floordiv__ at 0x000001A4FF65BA70>, \'__rfloordiv__\': <cyfunction Timedelta.__rfloordiv__ at 0x000001A4FF65BB60>, \'__mod__\': <cyfunction Timedelta.__mod__ at 0x000001A4FF65BC50>, \'__rmod__\': <cyfunction Timedelta.__rmod__ at 0x000001A4FF65BD40>, \'__divmod__\': <cyfunction Timedelta.__divmod__ at 0x000001A4FF65BE30>, \'__rdivmod__\': <cyfunction Timedelta.__rdivmod__ at 0x000001A4FF65BF20>, \'__dict__\': <attribute \'__dict__\' of \'Timedelta\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timedelta\' objects>, \'_module_source\': \'pandas._libs.tslibs.timedeltas\'})'


