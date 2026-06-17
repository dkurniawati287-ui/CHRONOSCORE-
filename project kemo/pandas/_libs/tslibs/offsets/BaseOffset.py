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


from .object import object

class BaseOffset(object):
    """
    Base class for DateOffset methods that are not overridden by subclasses.
    
        Parameters
        ----------
        n : int
            Number of multiples of the frequency.
    
        normalize : bool
            Whether the frequency can align with midnight.
    
        Examples
        --------
        >>> pd.offsets.Hour(5).n
        5
        >>> pd.offsets.Hour(5).normalize
        False
    """
    def copy(self): # real signature unknown; restored from __doc__
        """
        Return a copy of the frequency.
        
                See Also
                --------
                tseries.offsets.Week.copy : Return a copy of Week offset.
                tseries.offsets.DateOffset.copy : Return a copy of date offset.
                tseries.offsets.MonthEnd.copy : Return a copy of MonthEnd offset.
                tseries.offsets.YearBegin.copy : Return a copy of YearBegin offset.
        
                Examples
                --------
                >>> freq = pd.DateOffset(1)
                >>> freq_copy = freq.copy()
                >>> freq is freq_copy
                False
        """
        pass

    def is_month_end(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the month end.
        
                Parameters
                ----------
                ts : Timestamp
                    The timestamp to check.
        
                See Also
                --------
                is_month_start : Return boolean whether a timestamp occurs on the month start.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_month_end(ts)
                False
        """
        pass

    def is_month_start(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the month start.
        
                This method determines if a given timestamp falls on the first day
                of a month, considering the frequency of the offset.
        
                Parameters
                ----------
                ts : Timestamp
                    The timestamp to check.
        
                See Also
                --------
                is_month_end : Return boolean whether a timestamp occurs on the month end.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_month_start(ts)
                True
        """
        pass

    def is_on_offset(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp intersects with this frequency.
        
                This method determines if a given timestamp aligns with the start
                of a custom business month, as defined by this offset. It accounts
                for custom rules, such as skipping weekends or other non-business days,
                and checks whether the provided datetime falls on a valid business day
                that marks the beginning of the custom business month.
        
                Parameters
                ----------
                dt : datetime.datetime
                    Timestamp to check intersections with frequency.
        
                See Also
                --------
                tseries.offsets.CustomBusinessMonthBegin : Represents the start of a custom
                    business month.
                tseries.offsets.CustomBusinessMonthEnd : Represents the end of a custom
                    business month.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Day(1)
                >>> freq.is_on_offset(ts)
                True
        
                >>> ts = pd.Timestamp(2022, 8, 6)
                >>> ts.day_name()
                'Saturday'
                >>> freq = pd.offsets.BusinessDay(1)
                >>> freq.is_on_offset(ts)
                False
        """
        pass

    def is_quarter_end(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the quarter end.
        
                Parameters
                ----------
                ts : Timestamp
                    The timestamp to check.
        
                See Also
                --------
                is_quarter_start : Return boolean whether a timestamp
                    occurs on the quarter start.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_quarter_end(ts)
                False
        """
        pass

    def is_quarter_start(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the quarter start.
        
                Parameters
                ----------
                ts : Timestamp
                    The timestamp to check.
        
                See Also
                --------
                is_quarter_end : Return boolean whether a timestamp occurs on the quarter end.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_quarter_start(ts)
                True
        """
        pass

    def is_year_end(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the year end.
        
                Parameters
                ----------
                ts : Timestamp
                    The timestamp to check.
        
                See Also
                --------
                is_year_start : Return boolean whether a timestamp occurs on the year start.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_year_end(ts)
                False
        """
        pass

    def is_year_start(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp occurs on the year start.
        
                Parameters
                ----------
                ts : Timestamp
                    The timestamp to check.
        
                See Also
                --------
                is_year_end : Return boolean whether a timestamp occurs on the year end.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.Hour(5)
                >>> freq.is_year_start(ts)
                True
        """
        pass

    def rollback(self, ts): # real signature unknown; restored from __doc__
        """
        Roll provided date backward to next offset only if not on offset.
        
                If the provided date is already on an offset, it is returned unchanged.
                Otherwise, the date is rolled backward to the previous offset boundary.
        
                Parameters
                ----------
                dt : datetime or Timestamp
                    Timestamp to rollback.
        
                Returns
                -------
                Timestamp
                    Rolled timestamp if not on offset, otherwise unchanged timestamp.
        
                See Also
                --------
                rollforward : Roll provided date forward to next offset only if not on offset.
                is_on_offset : Return boolean whether a timestamp intersects with this
                    frequency.
        
                Examples
                --------
                >>> ts = pd.Timestamp("2025-01-15 09:00:00")
                >>> offset = pd.tseries.offsets.MonthEnd()
        
                Timestamp is not on the offset (not a month end), so it rolls backward:
        
                >>> offset.rollback(ts)
                Timestamp('2024-12-31 00:00:00')
        
                If the timestamp is already on the offset, it remains unchanged:
        
                >>> ts_on_offset = pd.Timestamp("2025-01-31")
                >>> offset.rollback(ts_on_offset)
                Timestamp('2025-01-31 00:00:00')
        """
        pass

    def rollforward(self, ts): # real signature unknown; restored from __doc__
        """
        Roll provided date forward to next offset only if not on offset.
        
                If the provided date is already on an offset, it is returned unchanged.
                Otherwise, the date is rolled forward to the next offset boundary.
        
                Parameters
                ----------
                dt : datetime or Timestamp
                    Timestamp to roll forward.
        
                Returns
                -------
                Timestamp
                    Rolled timestamp if not on offset, otherwise unchanged timestamp.
        
                See Also
                --------
                rollback : Roll provided date backward to previous offset only if not
                    on offset.
                is_on_offset : Return boolean whether a timestamp intersects with this
                    frequency.
        
                Examples
                --------
                >>> ts = pd.Timestamp("2025-01-15 09:00:00")
                >>> offset = pd.tseries.offsets.MonthEnd()
        
                Timestamp is not on the offset (not a month end), so it rolls forward:
        
                >>> offset.rollforward(ts)
                Timestamp('2025-01-31 00:00:00')
        
                If the timestamp is already on the offset, it remains unchanged:
        
                >>> ts_on_offset = pd.Timestamp("2025-01-31")
                >>> offset.rollforward(ts_on_offset)
                Timestamp('2025-01-31 00:00:00')
        """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        pass

    def _offset_str(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod
    def _validate_n(*args, **kwargs): # real signature unknown
        """
        Require that `n` be an integer.
        
                Parameters
                ----------
                n : int
        
                Returns
                -------
                nint : int
        
                Raises
                ------
                TypeError if `int(n)` raises
                ValueError if n != int(n)
        """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        """ Return a picklable state """
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

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
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

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        """ Reconstruct an instance from a pickled state """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns a copy of the calling offset object with n=1 and all other
        attributes equal.
        """

    kwds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a dict of extra parameters for the offset.

        These parameters exclude ``n`` and ``normalize``, which are common
        to all offsets. The returned dictionary can be passed to the offset
        constructor to recreate the offset with the same settings.

        See Also
        --------
        tseries.offsets.DateOffset : The base class for all pandas date offsets.
        tseries.offsets.WeekOfMonth : Represents the week of the month.
        tseries.offsets.LastWeekOfMonth : Represents the last week of the month.

        Examples
        --------
        >>> pd.DateOffset(5).kwds
        {}

        >>> pd.offsets.FY5253Quarter().kwds
        {'weekday': 0,
         'startingMonth': 1,
         'qtr_with_extra_week': 1,
         'variation': 'nearest'}
        """

    n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the count of the number of periods.

        This represents how many multiples of the offset frequency should
        be applied. For example, ``Hour(5)`` has ``n=5``.

        See Also
        --------
        DateOffset.normalize : Return boolean whether the frequency can align
            with midnight.

        Examples
        --------
        >>> pd.offsets.Hour(5).n
        5

        >>> pd.offsets.Day(3).n
        3
        """

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representing the base frequency.

        See Also
        --------
        tseries.offsets.Week : Represents a weekly offset.
        DateOffset : Base class for all other offset classes.
        tseries.offsets.Day : Represents a single day offset.
        tseries.offsets.MonthEnd : Represents a monthly offset that
            snaps to the end of the month.

        Examples
        --------
        >>> pd.offsets.Hour().name
        'h'

        >>> pd.offsets.Hour(5).name
        'h'
        """

    nanos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns an integer of the total number of nanoseconds for fixed frequencies.

        Raises
        ------
        ValueError
            If the frequency is non-fixed.

        See Also
        --------
        tseries.offsets.Hour.nanos :
            Returns an integer of the total number of nanoseconds.
        tseries.offsets.Day.nanos :
            Returns an integer of the total number of nanoseconds.

        Examples
        --------
        >>> pd.offsets.Week(n=1).nanos
        ValueError: Week: weekday=None is a non-fixed frequency
        """

    normalize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return boolean whether the frequency can align with midnight.

        This is True for offsets that round the result of a DateOffset
        addition down to the previous midnight.

        See Also
        --------
        tseries.offsets.DateOffset : The standard kind of date increment.

        Examples
        --------
        >>> pd.offsets.Hour(5).normalize
        False

        >>> pd.offsets.Day(5).normalize
        False
        """

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representing the base frequency.

        See Also
        --------
        tseries.offsets.Hour.rule_code :
            Returns a string representing the base frequency of 'h'.
        tseries.offsets.Day.rule_code :
            Returns a string representing the base frequency of 'D'.

        Examples
        --------
        >>> pd.offsets.Hour().rule_code
        'h'

        >>> pd.offsets.Week(5).rule_code
        'W'
        """

    _cache = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _n = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _normalize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    freqstr = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4FF31F440>'
    _adjust_dst = True
    _attributes = (
        'n',
        'normalize',
    )
    _day_opt = None
    _params = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4FF56AD40>'
    _use_relativedelta = False
    __array_priority__ = 1000


