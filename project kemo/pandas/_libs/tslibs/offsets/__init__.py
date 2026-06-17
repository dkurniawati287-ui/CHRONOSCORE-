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


# Variables with simple values

INVALID_FREQ_ERR_MSG = 'Invalid frequency: {0}'

# functions

def apply_wraps(*args, **kwargs): # real signature unknown
    pass

def ClassVar(*args, **kwargs): # real signature unknown
    """
    Special type construct to mark class variables.
    
    An annotation wrapped in ClassVar indicates that a given
    attribute is intended to be used as a class variable and
    should not be set on instances of that class.
    
    Usage::
    
        class Starship:
            stats: ClassVar[dict[str, int]] = {} # class variable
            damage: int = 10                     # instance variable
    
    ClassVar accepts only types and cannot be further subscribed.
    
    Note that ClassVar is not a class itself, and should not
    be used with isinstance() or issubclass().
    """
    pass

def delta_to_tick(*args, **kwargs): # real signature unknown
    pass

def find_stack_level(): # reliably restored by inspect
    """
    Find the first place in the stack that is not inside pandas
    (tests notwithstanding).
    """
    pass

def raise_invalid_freq(*args, **kwargs): # real signature unknown
    pass

def roll_convention(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : int, generally the day component of a datetime
        n : number of periods to increment, before adjusting for rolling
        compare : int, generally the day component of a datetime, in the same
                  month as the datetime form which `other` was taken.
    
        Returns
        -------
        n : int number of periods to increment
    """
    pass

def roll_qtrday(*args, **kwargs): # real signature unknown
    """
    Possibly increment or decrement the number of periods to shift
        based on rollforward/rollbackward conventions.
    
        Parameters
        ----------
        other : datetime or Timestamp
        n : number of periods to increment, before adjusting for rolling
        month : int reference month giving the first month of the year
        day_opt : {'start', 'end', 'business_start', 'business_end'}
            The convention to use in finding the day in a given month against
            which to compare for rollforward/rollbackward decisions.
        modby : int 3 for quarters, 12 for years
    
        Returns
        -------
        n : int number of periods to increment
    
        See Also
        --------
        get_day_of_month : Find the day in a month provided an offset.
    """
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

def shift_month(*args, **kwargs): # real signature unknown
    """
    Given a datetime (or Timestamp) `stamp`, an integer `months` and an
        option `day_opt`, return a new datetimelike that many months later,
        with day determined by `day_opt` using relativedelta semantics.
    
        Scalar analogue of shift_months.
    
        Parameters
        ----------
        stamp : datetime or Timestamp
        months : int
        day_opt : None, 'start', 'end', 'business_start', 'business_end', or int
            None: returned datetimelike has the same day as the input, or the
                  last day of the month if the new month is too short
            'start': returned datetimelike has day=1
            'end': returned datetimelike has day on the last day of the month
            'business_start': returned datetimelike has day on the first
                business day of the month
            'business_end': returned datetimelike has day on the last
                business day of the month
            int: returned datetimelike has day equal to day_opt
    
        Returns
        -------
        shifted : datetime or Timestamp (same as input `stamp`)
    """
    pass

def shift_months(*args, **kwargs): # real signature unknown
    """
    Given an int64-based datetime index, shift all elements
        specified number of months using DateOffset semantics
    
        day_opt: {None, 'start', 'end', 'business_start', 'business_end'}
           * None: day of month
           * 'start' 1st day of month
           * 'end' last day of month
    """
    pass

def to_offset(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Return DateOffset object from string or datetime.timedelta object.
    
        Parameters
        ----------
        freq : str, datetime.timedelta, BaseOffset or None
            The frequency represented.
        is_period : bool, default False
            Convert string denoting period frequency to corresponding offsets
            frequency if is_period=True.
    
        Returns
        -------
        BaseOffset subclass or None
    
        Raises
        ------
        ValueError
            If freq is an invalid frequency
    
        See Also
        --------
        BaseOffset : Standard kind of date increment used for a date range.
    
        Examples
        --------
        >>> from pandas.tseries.frequencies import to_offset
        >>> to_offset("5min")
        <5 * Minutes>
    
        >>> to_offset("1D1h")
        <25 * Hours>
    
        >>> to_offset("2W")
        <2 * Weeks: weekday=6>
    
        >>> to_offset("2B")
        <2 * BusinessDays>
    
        >>> to_offset(pd.Timedelta(days=1))
        <Day>
    
        >>> to_offset(pd.offsets.Hour())
        <Hour>
    
        Passing the parameter ``is_period`` equal to True, you can use a string
        denoting period frequency:
    
        >>> freq = to_offset(freq="ME", is_period=False)
        >>> freq.rule_code
        'ME'
    
        >>> freq = to_offset(freq="M", is_period=True)
        >>> freq.rule_code
        'ME'
    """
    pass

def _get_offset(EOM): # real signature unknown; restored from __doc__
    """
    Return DateOffset object associated with rule name.
    
        Examples
        --------
        _get_offset('EOM') --> BMonthEnd(1)
    """
    pass

def _validate_to_offset_alias(*args, **kwargs): # real signature unknown
    pass

def _warn_about_deprecated_aliases(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_BaseOffset(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_RelativeDeltaOffset(*args, **kwargs): # real signature unknown
    pass

# classes

from .ApplyTypeError import ApplyTypeError
from .BaseOffset import BaseOffset
from .SingleConstructorOffset import SingleConstructorOffset
from .BusinessMixin import BusinessMixin
from .BusinessDay import BusinessDay
from .BDay import BDay
from .HalfYearOffset import HalfYearOffset
from .BHalfYearBegin import BHalfYearBegin
from .BHalfYearEnd import BHalfYearEnd
from .MonthOffset import MonthOffset
from .BusinessMonthBegin import BusinessMonthBegin
from .BMonthBegin import BMonthBegin
from .BusinessMonthEnd import BusinessMonthEnd
from .BMonthEnd import BMonthEnd
from .QuarterOffset import QuarterOffset
from .BQuarterBegin import BQuarterBegin
from .BQuarterEnd import BQuarterEnd
from .BusinessHour import BusinessHour
from .YearOffset import YearOffset
from .BYearBegin import BYearBegin
from .BYearEnd import BYearEnd
from ._CustomBusinessMonth import _CustomBusinessMonth
from .CustomBusinessMonthBegin import CustomBusinessMonthBegin
from .CBMonthBegin import CBMonthBegin
from .CustomBusinessMonthEnd import CustomBusinessMonthEnd
from .CBMonthEnd import CBMonthEnd
from .CustomBusinessDay import CustomBusinessDay
from .CDay import CDay
from .CustomBusinessHour import CustomBusinessHour
from .RelativeDeltaOffset import RelativeDeltaOffset
from .DateOffset import DateOffset
from .Day import Day
from .Easter import Easter
from .FY5253Mixin import FY5253Mixin
from .FY5253 import FY5253
from .FY5253Quarter import FY5253Quarter
from .HalfYearBegin import HalfYearBegin
from .HalfYearEnd import HalfYearEnd
from .Tick import Tick
from .Hour import Hour
from .WeekOfMonthMixin import WeekOfMonthMixin
from .LastWeekOfMonth import LastWeekOfMonth
from .Micro import Micro
from .Milli import Milli
from .Minute import Minute
from .MonthBegin import MonthBegin
from .MonthEnd import MonthEnd
from .Nano import Nano
from .OffsetMeta import OffsetMeta
from .QuarterBegin import QuarterBegin
from .QuarterEnd import QuarterEnd
from .Second import Second
from .SemiMonthOffset import SemiMonthOffset
from .SemiMonthBegin import SemiMonthBegin
from .SemiMonthEnd import SemiMonthEnd
from .Timedelta import Timedelta
from .Timestamp import Timestamp
from .Week import Week
from .WeekOfMonth import WeekOfMonth
from .YearBegin import YearBegin
from ._YearEnd import _YearEnd
from .YearEnd import YearEnd
# variables with complex values

deprec_to_valid_alias = {
    'A': 'Y',
    'A-APR': 'Y-APR',
    'A-AUG': 'Y-AUG',
    'A-DEC': 'Y-DEC',
    'A-FEB': 'Y-FEB',
    'A-JAN': 'Y-JAN',
    'A-JUL': 'Y-JUL',
    'A-JUN': 'Y-JUN',
    'A-MAR': 'Y-MAR',
    'A-MAY': 'Y-MAY',
    'A-NOV': 'Y-NOV',
    'A-OCT': 'Y-OCT',
    'A-SEP': 'Y-SEP',
    'AS': 'YS',
    'AS-APR': 'YS-APR',
    'AS-AUG': 'YS-AUG',
    'AS-DEC': 'YS-DEC',
    'AS-FEB': 'YS-FEB',
    'AS-JAN': 'YS-JAN',
    'AS-JUL': 'YS-JUL',
    'AS-JUN': 'YS-JUN',
    'AS-MAR': 'YS-MAR',
    'AS-MAY': 'YS-MAY',
    'AS-NOV': 'YS-NOV',
    'AS-OCT': 'YS-OCT',
    'AS-SEP': 'YS-SEP',
    'BH': 'bh',
    'CBH': 'cbh',
    'H': 'h',
    'L': 'ms',
    'N': 'ns',
    'S': 's',
    'T': 'min',
    'U': 'us',
}

int_to_weekday = {
    0: 'MON',
    1: 'TUE',
    2: 'WED',
    3: 'THU',
    4: 'FRI',
    5: 'SAT',
    6: 'SUN',
}

MONTH_ALIASES = {
    1: 'JAN',
    2: 'FEB',
    3: 'MAR',
    4: 'APR',
    5: 'MAY',
    6: 'JUN',
    7: 'JUL',
    8: 'AUG',
    9: 'SEP',
    10: 'OCT',
    11: 'NOV',
    12: 'DEC',
}

opattern = None # (!) real value is "re.compile('([+\\\\-]?\\\\d*|[+\\\\-]?\\\\d*\\\\.\\\\d*)\\\\s*([A-Za-z]+([\\\\-][\\\\dA-Za-z\\\\-]+)?)')"

prefix_mapping = {
    'B': BusinessDay,
    'BHYE': BHalfYearEnd,
    'BHYS': BHalfYearBegin,
    'BME': BusinessMonthEnd,
    'BMS': BusinessMonthBegin,
    'BQE': BQuarterEnd,
    'BQS': BQuarterBegin,
    'BYE': BYearEnd,
    'BYS': BYearBegin,
    'C': CustomBusinessDay,
    'CBME': CustomBusinessMonthEnd,
    'CBMS': CustomBusinessMonthBegin,
    'D': Day,
    'HYE': HalfYearEnd,
    'HYS': HalfYearBegin,
    'LWOM': LastWeekOfMonth,
    'ME': MonthEnd,
    'MS': MonthBegin,
    'QE': QuarterEnd,
    'QS': QuarterBegin,
    'RE': FY5253,
    'REQ': FY5253Quarter,
    'SME': SemiMonthEnd,
    'SMS': SemiMonthBegin,
    'W': Week,
    'WOM': WeekOfMonth,
    'YE': YearEnd,
    'YS': YearBegin,
    'bh': BusinessHour,
    'cbh': CustomBusinessHour,
    'h': Hour,
    'min': Minute,
    'ms': Milli,
    'ns': Nano,
    's': Second,
    'us': Micro,
}

weekday_to_int = {
    'FRI': 4,
    'MON': 0,
    'SAT': 5,
    'SUN': 6,
    'THU': 3,
    'TUE': 1,
    'WED': 2,
}

_dont_uppercase = None # (!) real value is "{'min', 'ns', 'ms', 'h', 's', 'us', 'cbh', 'bh'}"

_lite_rule_alias = {
    'BYE': 'BYE-DEC',
    'BYS': 'BYS-JAN',
    'Min': 'min',
    'QE': 'QE-DEC',
    'W': 'W-SUN',
    'YE': 'YE-DEC',
    'YS': 'YS-JAN',
}

_offset_map = {}

_relativedelta_kwds = None # (!) real value is "{'microsecond', 'millisecond', 'months', 'hours', 'hour', 'second', 'seconds', 'microseconds', 'nanoseconds', 'nanosecond', 'weeks', 'years', 'milliseconds', 'year', 'days', 'month', 'minutes', 'weekday', 'day', 'minute'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A4FF4BB1D0>'

__pyx_capi__ = {
    'is_offset_object': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001A4FF560FE0>'
    'is_tick_object': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000001A4FF561030>'
    'to_offset': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int __pyx_skip_dispatch, struct __pyx_opt_args_6pandas_5_libs_6tslibs_7offsets_to_offset *__pyx_optional_args)" at 0x000001A4FF560F90>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.offsets', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A4FF4BB1D0>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\offsets.cp314-win_amd64.pyd')"

__test__ = {
    'BaseOffset.copy (line 562)': '\n        Return a copy of the frequency.\n\n        See Also\n        --------\n        tseries.offsets.Week.copy : Return a copy of Week offset.\n        tseries.offsets.DateOffset.copy : Return a copy of date offset.\n        tseries.offsets.MonthEnd.copy : Return a copy of MonthEnd offset.\n        tseries.offsets.YearBegin.copy : Return a copy of YearBegin offset.\n\n        Examples\n        --------\n        >>> freq = pd.DateOffset(1)\n        >>> freq_copy = freq.copy()\n        >>> freq is freq_copy\n        False\n        ',
    'BaseOffset.freqstr (line 670)': "\n        Return a string representing the frequency.\n\n        The string representation typically consists of the offset multiplier\n        and a frequency alias (e.g., ``'D'`` for daily, ``'h'`` for hourly).\n\n        See Also\n        --------\n        tseries.offsets.BusinessDay.freqstr :\n            Return a string representing an offset frequency in Business Days.\n        tseries.offsets.BusinessHour.freqstr :\n            Return a string representing an offset frequency in Business Hours.\n        tseries.offsets.Week.freqstr :\n            Return a string representing an offset frequency in Weeks.\n        tseries.offsets.Hour.freqstr :\n            Return a string representing an offset frequency in Hours.\n\n        Examples\n        --------\n        >>> pd.DateOffset(5).freqstr\n        '<5 * DateOffsets>'\n\n        >>> pd.offsets.BusinessHour(2).freqstr\n        '2bh'\n\n        >>> pd.offsets.Nano().freqstr\n        'ns'\n\n        >>> pd.offsets.Nano(-3).freqstr\n        '-3ns'\n        ",
    'BaseOffset.is_month_end (line 992)': '\n        Return boolean whether a timestamp occurs on the month end.\n\n        Parameters\n        ----------\n        ts : Timestamp\n            The timestamp to check.\n\n        See Also\n        --------\n        is_month_start : Return boolean whether a timestamp occurs on the month start.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_month_end(ts)\n        False\n        ',
    'BaseOffset.is_month_start (line 967)': '\n        Return boolean whether a timestamp occurs on the month start.\n\n        This method determines if a given timestamp falls on the first day\n        of a month, considering the frequency of the offset.\n\n        Parameters\n        ----------\n        ts : Timestamp\n            The timestamp to check.\n\n        See Also\n        --------\n        is_month_end : Return boolean whether a timestamp occurs on the month end.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_month_start(ts)\n        True\n        ',
    'BaseOffset.is_on_offset (line 838)': "\n        Return boolean whether a timestamp intersects with this frequency.\n\n        This method determines if a given timestamp aligns with the start\n        of a custom business month, as defined by this offset. It accounts\n        for custom rules, such as skipping weekends or other non-business days,\n        and checks whether the provided datetime falls on a valid business day\n        that marks the beginning of the custom business month.\n\n        Parameters\n        ----------\n        dt : datetime.datetime\n            Timestamp to check intersections with frequency.\n\n        See Also\n        --------\n        tseries.offsets.CustomBusinessMonthBegin : Represents the start of a custom\n            business month.\n        tseries.offsets.CustomBusinessMonthEnd : Represents the end of a custom\n            business month.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Day(1)\n        >>> freq.is_on_offset(ts)\n        True\n\n        >>> ts = pd.Timestamp(2022, 8, 6)\n        >>> ts.day_name()\n        'Saturday'\n        >>> freq = pd.offsets.BusinessDay(1)\n        >>> freq.is_on_offset(ts)\n        False\n        ",
    'BaseOffset.is_quarter_end (line 1036)': '\n        Return boolean whether a timestamp occurs on the quarter end.\n\n        Parameters\n        ----------\n        ts : Timestamp\n            The timestamp to check.\n\n        See Also\n        --------\n        is_quarter_start : Return boolean whether a timestamp\n            occurs on the quarter start.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_quarter_end(ts)\n        False\n        ',
    'BaseOffset.is_quarter_start (line 1014)': '\n        Return boolean whether a timestamp occurs on the quarter start.\n\n        Parameters\n        ----------\n        ts : Timestamp\n            The timestamp to check.\n\n        See Also\n        --------\n        is_quarter_end : Return boolean whether a timestamp occurs on the quarter end.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_quarter_start(ts)\n        True\n        ',
    'BaseOffset.is_year_end (line 1081)': '\n        Return boolean whether a timestamp occurs on the year end.\n\n        Parameters\n        ----------\n        ts : Timestamp\n            The timestamp to check.\n\n        See Also\n        --------\n        is_year_start : Return boolean whether a timestamp occurs on the year start.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_year_end(ts)\n        False\n        ',
    'BaseOffset.is_year_start (line 1059)': '\n        Return boolean whether a timestamp occurs on the year start.\n\n        Parameters\n        ----------\n        ts : Timestamp\n            The timestamp to check.\n\n        See Also\n        --------\n        is_year_end : Return boolean whether a timestamp occurs on the year end.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.Hour(5)\n        >>> freq.is_year_start(ts)\n        True\n        ',
    'BaseOffset.kwds.__get__ (line 476)': "\n        Return a dict of extra parameters for the offset.\n\n        These parameters exclude ``n`` and ``normalize``, which are common\n        to all offsets. The returned dictionary can be passed to the offset\n        constructor to recreate the offset with the same settings.\n\n        See Also\n        --------\n        tseries.offsets.DateOffset : The base class for all pandas date offsets.\n        tseries.offsets.WeekOfMonth : Represents the week of the month.\n        tseries.offsets.LastWeekOfMonth : Represents the last week of the month.\n\n        Examples\n        --------\n        >>> pd.DateOffset(5).kwds\n        {}\n\n        >>> pd.offsets.FY5253Quarter().kwds\n        {'weekday': 0,\n         'startingMonth': 1,\n         'qtr_with_extra_week': 1,\n         'variation': 'nearest'}\n        ",
    'BaseOffset.n.__get__ (line 387)': '\n        Return the count of the number of periods.\n\n        This represents how many multiples of the offset frequency should\n        be applied. For example, ``Hour(5)`` has ``n=5``.\n\n        See Also\n        --------\n        DateOffset.normalize : Return boolean whether the frequency can align\n            with midnight.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour(5).n\n        5\n\n        >>> pd.offsets.Day(3).n\n        3\n        ',
    'BaseOffset.name.__get__ (line 621)': "\n        Return a string representing the base frequency.\n\n        See Also\n        --------\n        tseries.offsets.Week : Represents a weekly offset.\n        DateOffset : Base class for all other offset classes.\n        tseries.offsets.Day : Represents a single day offset.\n        tseries.offsets.MonthEnd : Represents a monthly offset that\n            snaps to the end of the month.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour().name\n        'h'\n\n        >>> pd.offsets.Hour(5).name\n        'h'\n        ",
    'BaseOffset.nanos.__get__ (line 941)': '\n        Returns an integer of the total number of nanoseconds for fixed frequencies.\n\n        Raises\n        ------\n        ValueError\n            If the frequency is non-fixed.\n\n        See Also\n        --------\n        tseries.offsets.Hour.nanos :\n            Returns an integer of the total number of nanoseconds.\n        tseries.offsets.Day.nanos :\n            Returns an integer of the total number of nanoseconds.\n\n        Examples\n        --------\n        >>> pd.offsets.Week(n=1).nanos\n        ValueError: Week: weekday=None is a non-fixed frequency\n        ',
    'BaseOffset.normalize.__get__ (line 410)': '\n        Return boolean whether the frequency can align with midnight.\n\n        This is True for offsets that round the result of a DateOffset\n        addition down to the previous midnight.\n\n        See Also\n        --------\n        tseries.offsets.DateOffset : The standard kind of date increment.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour(5).normalize\n        False\n\n        >>> pd.offsets.Day(5).normalize\n        False\n        ',
    'BaseOffset.rollback (line 738)': '\n        Roll provided date backward to next offset only if not on offset.\n\n        If the provided date is already on an offset, it is returned unchanged.\n        Otherwise, the date is rolled backward to the previous offset boundary.\n\n        Parameters\n        ----------\n        dt : datetime or Timestamp\n            Timestamp to rollback.\n\n        Returns\n        -------\n        Timestamp\n            Rolled timestamp if not on offset, otherwise unchanged timestamp.\n\n        See Also\n        --------\n        rollforward : Roll provided date forward to next offset only if not on offset.\n        is_on_offset : Return boolean whether a timestamp intersects with this\n            frequency.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2025-01-15 09:00:00")\n        >>> offset = pd.tseries.offsets.MonthEnd()\n\n        Timestamp is not on the offset (not a month end), so it rolls backward:\n\n        >>> offset.rollback(ts)\n        Timestamp(\'2024-12-31 00:00:00\')\n\n        If the timestamp is already on the offset, it remains unchanged:\n\n        >>> ts_on_offset = pd.Timestamp("2025-01-31")\n        >>> offset.rollback(ts_on_offset)\n        Timestamp(\'2025-01-31 00:00:00\')\n        ',
    'BaseOffset.rollforward (line 785)': '\n        Roll provided date forward to next offset only if not on offset.\n\n        If the provided date is already on an offset, it is returned unchanged.\n        Otherwise, the date is rolled forward to the next offset boundary.\n\n        Parameters\n        ----------\n        dt : datetime or Timestamp\n            Timestamp to roll forward.\n\n        Returns\n        -------\n        Timestamp\n            Rolled timestamp if not on offset, otherwise unchanged timestamp.\n\n        See Also\n        --------\n        rollback : Roll provided date backward to previous offset only if not\n            on offset.\n        is_on_offset : Return boolean whether a timestamp intersects with this\n            frequency.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp("2025-01-15 09:00:00")\n        >>> offset = pd.tseries.offsets.MonthEnd()\n\n        Timestamp is not on the offset (not a month end), so it rolls forward:\n\n        >>> offset.rollforward(ts)\n        Timestamp(\'2025-01-31 00:00:00\')\n\n        If the timestamp is already on the offset, it remains unchanged:\n\n        >>> ts_on_offset = pd.Timestamp("2025-01-31")\n        >>> offset.rollforward(ts_on_offset)\n        Timestamp(\'2025-01-31 00:00:00\')\n        ',
    'BaseOffset.rule_code.__get__ (line 648)': "\n        Return a string representing the base frequency.\n\n        See Also\n        --------\n        tseries.offsets.Hour.rule_code :\n            Returns a string representing the base frequency of 'h'.\n        tseries.offsets.Day.rule_code :\n            Returns a string representing the base frequency of 'D'.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour().rule_code\n        'h'\n\n        >>> pd.offsets.Week(5).rule_code\n        'W'\n        ",
    'BusinessDay.is_on_offset (line 2419)': "\n        Return boolean whether a timestamp intersects with this frequency.\n\n        This method determines if a given timestamp falls on a business day\n        (Monday through Friday). If ``normalize`` is True, it also checks that\n        the time component is midnight.\n\n        Parameters\n        ----------\n        dt : datetime\n            Timestamp to check intersection with frequency.\n\n        Returns\n        -------\n        bool\n            True if the timestamp is on a business day, False otherwise.\n\n        See Also\n        --------\n        tseries.offsets.BusinessDay : Represents business day offset.\n        tseries.offsets.CustomBusinessDay : Represents custom business day offset.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 8, 5)\n        >>> ts.day_name()\n        'Friday'\n        >>> pd.offsets.BusinessDay().is_on_offset(ts)\n        True\n\n        >>> ts = pd.Timestamp(2022, 8, 6)\n        >>> ts.day_name()\n        'Saturday'\n        >>> pd.offsets.BusinessDay().is_on_offset(ts)\n        False\n\n        With ``normalize=True``, the timestamp must also be at midnight:\n\n        >>> ts = pd.Timestamp(2022, 8, 5, 12, 0)\n        >>> pd.offsets.BusinessDay(normalize=True).is_on_offset(ts)\n        False\n        >>> ts = pd.Timestamp(2022, 8, 5, 0, 0)\n        >>> pd.offsets.BusinessDay(normalize=True).is_on_offset(ts)\n        True\n        ",
    'BusinessHour.end.__get__ (line 2556)': '\n        Return the end time(s) of the business hour.\n\n        This property returns a tuple of `datetime.time` objects representing\n        the end times of business hours.\n\n        See Also\n        --------\n        BusinessHour.start : Return the start time(s) of the business hour.\n        CustomBusinessHour.start : Return the start time(s) of the custom business hour.\n\n        Examples\n        --------\n        >>> pd.offsets.BusinessHour().end\n        (datetime.time(17, 0),)\n        ',
    'BusinessHour.is_on_offset (line 2906)': "\n        Return boolean whether a timestamp intersects with this frequency.\n\n        This method determines if a given timestamp falls within business hours.\n        Business hours are defined by the ``start`` and ``end`` parameters\n        (default 09:00 to 17:00). The timestamp must also fall on a business day\n        (Monday through Friday). If ``normalize`` is True, it also checks that\n        the time component is midnight.\n\n        Parameters\n        ----------\n        dt : datetime\n            Timestamp to check intersection with frequency.\n\n        Returns\n        -------\n        bool\n            True if the timestamp is within business hours, False otherwise.\n\n        See Also\n        --------\n        tseries.offsets.BusinessHour : Represents business hour offset.\n        tseries.offsets.BusinessDay.is_on_offset : Check if a timestamp is on\n            a business day.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 8, 5, 10)\n        >>> ts.day_name()\n        'Friday'\n        >>> pd.offsets.BusinessHour().is_on_offset(ts)\n        True\n\n        >>> ts = pd.Timestamp(2022, 8, 5, 20)\n        >>> pd.offsets.BusinessHour().is_on_offset(ts)\n        False\n\n        >>> ts = pd.Timestamp(2022, 8, 6, 10)\n        >>> ts.day_name()\n        'Saturday'\n        >>> pd.offsets.BusinessHour().is_on_offset(ts)\n        False\n        ",
    'BusinessHour.start.__get__ (line 2536)': '\n        Return the start time(s) of the business hour.\n\n        This property returns a tuple of `datetime.time` objects representing\n        the start times of business hours.\n\n        See Also\n        --------\n        BusinessHour.end : Return the end time(s) of the business hour.\n        CustomBusinessHour.end : Return the end time(s) of the custom business hour.\n\n        Examples\n        --------\n        >>> pd.offsets.BusinessHour().start\n        (datetime.time(9, 0),)\n        ',
    'BusinessMixin.calendar.__get__ (line 2108)': '\n        Return the calendar used for business day calculations.\n\n        This property returns the numpy busdaycalendar object used for\n        determining valid business days. For standard business day offsets\n        (e.g., BusinessDay, BusinessHour), this returns None. For custom\n        business day offsets, this returns the calendar that was either\n        passed directly or constructed from weekmask and holidays.\n\n        Returns\n        -------\n        np.busdaycalendar or None\n            The business day calendar used for calculations, or None if\n            using default business day rules.\n\n        See Also\n        --------\n        BusinessDay.holidays : Holidays for standard business day offset.\n        CustomBusinessDay.holidays : Holidays for custom business day offset.\n        CustomBusinessDay.weekmask : Weekmask for custom business day offset.\n\n        Examples\n        --------\n        For standard business offsets, calendar is None:\n\n        >>> bd = pd.offsets.BusinessDay()\n        >>> bd.calendar is None\n        True\n\n        >>> bh = pd.offsets.BusinessHour()\n        >>> bh.calendar is None\n        True\n\n        For custom business day with explicit holidays:\n\n        >>> holidays = [pd.Timestamp("2023-12-25"), pd.Timestamp("2024-01-01")]\n        >>> cbd = pd.offsets.CustomBusinessDay(holidays=holidays)\n        >>> isinstance(cbd.calendar, np.busdaycalendar)\n        True\n        ',
    'BusinessMixin.holidays.__get__ (line 2030)': '\n        Return the holidays used for custom business day calculations.\n\n        This property returns a tuple or list of holidays used when calculating\n        business days for custom business day offsets. For non-custom business\n        offsets (e.g., standard BusinessDay, BusinessHour), this will be None.\n\n        Returns\n        -------\n        tuple, list, or None\n            Holidays used in business day calculations, or None if no custom\n            holidays are specified.\n\n        See Also\n        --------\n        BusinessDay.holidays : Holidays for standard business day offset.\n        BusinessHour.holidays : Holidays for standard business hour offset.\n        CustomBusinessDay.holidays : Holidays for custom business day offset.\n        CustomBusinessHour.holidays : Holidays for custom business hour offset.\n        CustomBusinessMonthEnd.holidays : Holidays for custom business month end offset.\n        CustomBusinessMonthBegin.holidays : Holidays for custom business month begin\n            offset.\n        CustomBusinessDay.weekmask : Weekmask for custom business day offset.\n        CustomBusinessDay.calendar : Calendar for custom business day offset.\n\n        Examples\n        --------\n        For standard business offsets, holidays is None:\n\n        >>> bd = pd.offsets.BusinessDay()\n        >>> bd.holidays is None\n        True\n\n        >>> bh = pd.offsets.BusinessHour()\n        >>> bh.holidays is None\n        True\n\n        For custom business day with explicit holidays:\n\n        >>> holidays = [pd.Timestamp("2023-12-25"), pd.Timestamp("2024-01-01")]\n        >>> cbd = pd.offsets.CustomBusinessDay(holidays=holidays)\n        >>> cbd.holidays  # doctest: +SKIP\n        (Timestamp(\'2023-12-25 00:00:00\'), Timestamp(\'2024-01-01 00:00:00\'))\n\n        For custom business hour with explicit holidays:\n\n        >>> cbh = pd.offsets.CustomBusinessHour(holidays=holidays)\n        >>> cbh.holidays  # doctest: +SKIP\n        (Timestamp(\'2023-12-25 00:00:00\'), Timestamp(\'2024-01-01 00:00:00\'))\n\n        For custom business month end with explicit holidays:\n\n        >>> cbme = pd.offsets.CustomBusinessMonthEnd(holidays=holidays)\n        >>> cbme.holidays  # doctest: +SKIP\n        (Timestamp(\'2023-12-25 00:00:00\'), Timestamp(\'2024-01-01 00:00:00\'))\n\n        For custom business month begin with explicit holidays:\n\n        >>> cbmb = pd.offsets.CustomBusinessMonthBegin(holidays=holidays)\n        >>> cbmb.holidays  # doctest: +SKIP\n        (Timestamp(\'2023-12-25 00:00:00\'), Timestamp(\'2024-01-01 00:00:00\'))\n\n        For custom business offsets with a calendar:\n\n        >>> from pandas.tseries.holiday import USFederalHolidayCalendar\n        >>> cal = USFederalHolidayCalendar()\n        >>> cbd_cal = pd.offsets.CustomBusinessDay(calendar=cal)\n        >>> isinstance(cbd_cal.holidays, tuple)\n        True\n\n        >>> cbh_cal = pd.offsets.CustomBusinessHour(calendar=cal)\n        >>> isinstance(cbh_cal.holidays, tuple)\n        True\n        ',
    'BusinessMixin.weekmask.__get__ (line 2152)': '\n        Return the weekmask used for custom business day calculations.\n\n        This property returns the weekmask string that defines which days of the\n        week are considered business days. For non-custom business offsets (e.g.,\n        standard BusinessDay, BusinessHour), this will be None. For custom business\n        day offsets, this returns the weekmask that was specified or the default\n        \'Mon Tue Wed Thu Fri\'.\n\n        Returns\n        -------\n        str or None\n            String representing valid business days (e.g., \'Mon Tue Wed Thu Fri\'),\n            or None if using default business day rules.\n\n        See Also\n        --------\n        BusinessDay.holidays : Holidays for standard business day offset.\n        CustomBusinessDay.holidays : Holidays for custom business day offset.\n        CustomBusinessDay.calendar : Calendar for custom business day offset.\n\n        Examples\n        --------\n        For standard business offsets, weekmask is None:\n\n        >>> bd = pd.offsets.BusinessDay()\n        >>> bd.weekmask is None\n        True\n\n        >>> bh = pd.offsets.BusinessHour()\n        >>> bh.weekmask is None\n        True\n\n        For custom business day with default weekmask:\n\n        >>> cbd = pd.offsets.CustomBusinessDay()\n        >>> cbd.weekmask\n        \'Mon Tue Wed Thu Fri\'\n\n        For custom business day with custom weekmask:\n\n        >>> cbd = pd.offsets.CustomBusinessDay(weekmask="Mon Wed Fri")\n        >>> cbd.weekmask\n        \'Mon Wed Fri\'\n        ',
    'Day.freqstr (line 1385)': "\n        Return a string representing the frequency.\n\n        The frequency string is composed of a multiplier (if greater than 1)\n        followed by the offset alias 'D' for days.\n\n        See Also\n        --------\n        tseries.offsets.Hour.freqstr :\n            Return a string representing an offset frequency in hours.\n        tseries.offsets.Minute.freqstr :\n            Return a string representing an offset frequency in minutes.\n        tseries.offsets.Second.freqstr :\n            Return a string representing an offset frequency in seconds.\n\n        Examples\n        --------\n        >>> pd.Day(5).freqstr\n        '5D'\n\n        >>> pd.offsets.Day(1).freqstr\n        'D'\n        ",
    'Day.nanos.__get__ (line 1417)': '\n        Returns an integer of the total number of nanoseconds.\n\n        See Also\n        --------\n        tseries.offsets.Hour.nanos :\n            Returns an integer of the total number of nanoseconds.\n        tseries.offsets.Day.nanos :\n            Returns an integer of the total number of nanoseconds.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour(5).nanos\n        18000000000000\n        ',
    'FY5253Mixin.get_rule_code_suffix (line 4969)': '\n        Return the suffix component of the rule code.\n\n        The suffix combines the variation prefix, starting month abbreviation,\n        and weekday abbreviation into a string format.\n\n        Returns\n        -------\n        str\n            Suffix string in the format "{variation}-{month}-{weekday}".\n            The variation is "N" for nearest or "L" for last.\n\n        See Also\n        --------\n        FY5253.rule_code : Return the complete rule code string.\n        FY5253Quarter.rule_code : Return the complete rule code string for\n            FY5253Quarter.\n\n        Examples\n        --------\n        >>> offset = pd.offsets.FY5253(weekday=4, startingMonth=12, variation="nearest")\n        >>> offset.get_rule_code_suffix()\n        \'N-DEC-FRI\'\n\n        >>> offset = pd.offsets.FY5253(weekday=0, startingMonth=1, variation="last")\n        >>> offset.get_rule_code_suffix()\n        \'L-JAN-MON\'\n        ',
    'FY5253Mixin.weekday.__get__ (line 4913)': '\n        Return the weekday used by the fiscal year.\n\n        This is the day of the week on which the fiscal year ends.\n        The value is an integer from 0 (Monday) to 6 (Sunday).\n\n        See Also\n        --------\n        FY5253.startingMonth : Return the starting month of the fiscal year.\n        FY5253.variation : Return the variation of the fiscal year.\n\n        Examples\n        --------\n        >>> offset = pd.offsets.FY5253(weekday=4, startingMonth=12, variation="nearest")\n        >>> offset.weekday\n        4\n        ',
    'HalfYearOffset.is_on_offset (line 3820)': '\n        Return boolean whether a timestamp intersects with this frequency.\n\n        This method checks if a given datetime falls on a valid half-year\n        boundary as defined by this offset.\n\n        Parameters\n        ----------\n        dt : datetime\n            Timestamp to check intersections with frequency.\n\n        Returns\n        -------\n        bool\n            True if the timestamp is on the offset, False otherwise.\n\n        See Also\n        --------\n        HalfYearEnd.is_on_offset : Check if a timestamp is at the end of a\n            half-year.\n        HalfYearBegin.is_on_offset : Check if a timestamp is at the start of a\n            half-year.\n        BHalfYearEnd.is_on_offset : Check if a timestamp is at the end of a\n            business half-year.\n        BHalfYearBegin.is_on_offset : Check if a timestamp is at the start of a\n            business half-year.\n\n        Examples\n        --------\n        >>> freq = pd.offsets.BHalfYearBegin()\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq.is_on_offset(ts)\n        False\n\n        >>> ts = pd.Timestamp(2022, 1, 3)\n        >>> freq.is_on_offset(ts)\n        True\n        ',
    'HalfYearOffset.rule_code.__get__ (line 3796)': "\n        Return a string representing the frequency with month suffix.\n\n        This property generates a rule code string that combines the offset's\n        prefix with the abbreviated month name of the starting month.\n\n        See Also\n        --------\n        FY5253Quarter.get_rule_code_suffix : Return the suffix component of the rule\n            code for FY5253Quarter.\n        FY5253.get_rule_code_suffix : Return the suffix component of the rule code for\n            FY5253.\n\n        Examples\n        --------\n        >>> offset = pd.offsets.BHalfYearEnd(startingMonth=6)\n        >>> offset.rule_code\n        'BHYE-JUN'\n        ",
    'HalfYearOffset.startingMonth.__get__ (line 3760)': '\n        Return the month of the year from which half-years start.\n\n        This value determines which month marks the beginning of a half-year period.\n        For example, with startingMonth=1, half-years start in January and July.\n\n        See Also\n        --------\n        HalfYearOffset.rule_code : Return the rule code for the half-year offset.\n        QuarterOffset.startingMonth : Similar property for quarter-based offsets.\n\n        Examples\n        --------\n        >>> pd.offsets.BHalfYearBegin().startingMonth\n        1\n\n        >>> pd.offsets.BHalfYearEnd().startingMonth\n        6\n\n        >>> pd.offsets.HalfYearBegin(startingMonth=3).startingMonth\n        3\n        ',
    'MonthOffset.is_on_offset (line 4043)': "\n        Return boolean whether a timestamp intersects with this frequency.\n\n        This method determines if a given timestamp aligns with the specific\n        day of the month defined by this offset. For month-based offsets,\n        it checks whether the timestamp's day matches the expected day\n        according to the offset's configuration (e.g., start of month,\n        end of month, or first/last business day).\n\n        Parameters\n        ----------\n        dt : datetime\n            Timestamp to check intersection with frequency.\n\n        Returns\n        -------\n        bool\n            True if the timestamp is on the offset, False otherwise.\n\n        See Also\n        --------\n        tseries.offsets.MonthBegin : DateOffset of one month at beginning.\n        tseries.offsets.MonthEnd : DateOffset of one month end.\n        tseries.offsets.BusinessMonthBegin : DateOffset of one month at the first\n            business day.\n        tseries.offsets.BusinessMonthEnd : DateOffset of one month at the last\n            business day.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> pd.offsets.MonthBegin().is_on_offset(ts)\n        True\n\n        >>> ts = pd.Timestamp(2022, 1, 15)\n        >>> pd.offsets.MonthBegin().is_on_offset(ts)\n        False\n\n        >>> ts = pd.Timestamp(2022, 1, 31)\n        >>> pd.offsets.MonthEnd().is_on_offset(ts)\n        True\n        ",
    'QuarterOffset.is_on_offset (line 3516)': "\n        Return boolean whether a timestamp intersects with this frequency.\n\n        This method checks if the given datetime falls on a quarter boundary\n        as defined by the offset's ``startingMonth`` and day option.\n\n        Parameters\n        ----------\n        dt : datetime\n            Timestamp to check intersections with frequency.\n\n        Returns\n        -------\n        bool\n            True if the timestamp is on the offset, False otherwise.\n\n        See Also\n        --------\n        QuarterOffset : Parent class with quarterly offset logic.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.BQuarterBegin()\n        >>> freq.is_on_offset(ts)\n        False\n        >>> ts = pd.Timestamp(2022, 3, 1)\n        >>> freq.is_on_offset(ts)\n        True\n        ",
    'QuarterOffset.rule_code.__get__ (line 3442)': "\n        Return a string representing the frequency with month suffix.\n\n        This property generates a rule code string that combines the offset's\n        prefix with the abbreviated month name of the starting month.\n\n        Returns\n        -------\n        str\n            Rule code string with format 'PREFIX-MONTH', where PREFIX is the\n            offset's frequency abbreviation and MONTH is the three-letter\n            abbreviation of the starting month.\n\n        See Also\n        --------\n        BQuarterBegin.rule_code : Rule code for business quarter begin offset.\n        BQuarterEnd.rule_code : Rule code for business quarter end offset.\n        QuarterBegin.rule_code : Rule code for quarter begin offset.\n        QuarterEnd.rule_code : Rule code for quarter end offset.\n        FY5253Quarter.get_rule_code_suffix : Suffix component of rule code for\n            FY5253Quarter.\n        FY5253.get_rule_code_suffix : Suffix component of rule code for FY5253.\n\n        Examples\n        --------\n        Business quarter begin with different starting months:\n\n        >>> bqb = pd.offsets.BQuarterBegin(startingMonth=1)\n        >>> bqb.rule_code\n        'BQS-JAN'\n\n        >>> bqb = pd.offsets.BQuarterBegin(startingMonth=2)\n        >>> bqb.rule_code\n        'BQS-FEB'\n\n        >>> bqb = pd.offsets.BQuarterBegin(startingMonth=3)\n        >>> bqb.rule_code\n        'BQS-MAR'\n\n        Business quarter end with different starting months:\n\n        >>> bqe = pd.offsets.BQuarterEnd(startingMonth=1)\n        >>> bqe.rule_code\n        'BQE-JAN'\n\n        >>> bqe = pd.offsets.BQuarterEnd(startingMonth=12)\n        >>> bqe.rule_code\n        'BQE-DEC'\n\n        Quarter begin with different starting months:\n\n        >>> qb = pd.offsets.QuarterBegin(startingMonth=1)\n        >>> qb.rule_code\n        'QS-JAN'\n\n        >>> qb = pd.offsets.QuarterBegin(startingMonth=3)\n        >>> qb.rule_code\n        'QS-MAR'\n\n        Quarter end with different starting months:\n\n        >>> qe = pd.offsets.QuarterEnd(startingMonth=1)\n        >>> qe.rule_code\n        'QE-JAN'\n\n        >>> qe = pd.offsets.QuarterEnd(startingMonth=3)\n        >>> qe.rule_code\n        'QE-MAR'\n        ",
    'QuarterOffset.startingMonth.__get__ (line 3405)': '\n        Return the month of the year from which quarters start.\n\n        This value determines which month marks the beginning of a quarterly period.\n        For example, with startingMonth=1, quarters start in January, April, July,\n        and October.\n\n        See Also\n        --------\n        QuarterOffset.rule_code : Return the rule code for the quarter offset.\n        HalfYearOffset.startingMonth : Similar property for half-year-based offsets.\n\n        Examples\n        --------\n        >>> pd.offsets.BQuarterBegin().startingMonth\n        3\n\n        >>> pd.offsets.QuarterEnd().startingMonth\n        3\n\n        >>> pd.offsets.QuarterBegin(startingMonth=1).startingMonth\n        1\n        ',
    'SemiMonthOffset.day_of_month.__get__ (line 4271)': '\n        Return the day of the month for the semi-monthly offset.\n\n        This specifies the day of the month on which the offset falls,\n        in addition to the start (1st) or end (last day) of the month.\n\n        See Also\n        --------\n        SemiMonthBegin : Offset at the start of the month and mid-month.\n        SemiMonthEnd : Offset at mid-month and end of month.\n\n        Examples\n        --------\n        >>> pd.offsets.SemiMonthBegin().day_of_month\n        15\n\n        >>> pd.offsets.SemiMonthBegin(day_of_month=20).day_of_month\n        20\n        ',
    'Tick.nanos.__get__ (line 1201)': '\n        Returns an integer of the total number of nanoseconds.\n\n        See Also\n        --------\n        tseries.offsets.Hour.nanos :\n            Returns an integer of the total number of nanoseconds.\n        tseries.offsets.Day.nanos :\n            Returns an integer of the total number of nanoseconds.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour(5).nanos\n        18000000000000\n        ',
    'Week.rule_code.__get__ (line 4701)': "\n        Return a string representing the base frequency.\n\n        See Also\n        --------\n        tseries.offsets.Hour.name :\n            Returns a string representing the base frequency of 'h'.\n        tseries.offsets.Day.name :\n            Returns a string representing the base frequency of 'D'.\n\n        Examples\n        --------\n        >>> pd.offsets.Hour().rule_code\n        'h'\n\n        >>> pd.offsets.Week(5).rule_code\n        'W'\n        ",
    'Week.weekday.__get__ (line 4564)': '\n        Return the day of the week on which the offset is applied.\n\n        This is the weekday on which the weekly offset is anchored.\n        The value is an integer representing the day of the week,\n        where Monday is 0 and Sunday is 6, or None if no specific\n        weekday is set.\n\n        See Also\n        --------\n        Week : The weekly offset class.\n        tseries.offsets.WeekOfMonth : Describes monthly dates like the Tuesday\n            of the 2nd week of each month.\n\n        Examples\n        --------\n        >>> pd.offsets.Week(weekday=0).weekday\n        0\n\n        >>> pd.offsets.Week(weekday=6).weekday\n        6\n\n        >>> pd.offsets.Week().weekday is None\n        True\n        ',
    'WeekOfMonthMixin.rule_code.__get__ (line 3015)': "\n        Return a string representing the base frequency.\n\n        See Also\n        --------\n        tseries.offsets.Hour.rule_code :\n            Returns a string representing the base frequency of 'h'.\n        tseries.offsets.Day.rule_code :\n            Returns a string representing the base frequency of 'D'.\n\n        Examples\n        --------\n        >>> pd.offsets.Week(5).rule_code\n        'W'\n\n        >>> pd.offsets.WeekOfMonth(n=1, week=0, weekday=0).rule_code\n        'WOM-1MON'\n        ",
    'YearOffset.is_on_offset (line 3127)': '\n        Return boolean whether a timestamp intersects with this frequency.\n\n        This method checks if a given datetime falls on a valid year\n        boundary as defined by this offset.\n\n        Parameters\n        ----------\n        dt : datetime\n            Timestamp to check intersections with frequency.\n\n        Returns\n        -------\n        bool\n            True if the timestamp is on the offset, False otherwise.\n\n        See Also\n        --------\n        YearEnd.is_on_offset : Check if a timestamp is at the end of a year.\n        YearBegin.is_on_offset : Check if a timestamp is at the start of a year.\n        BYearEnd.is_on_offset : Check if a timestamp is at the end of a\n            business year.\n        BYearBegin.is_on_offset : Check if a timestamp is at the start of a\n            business year.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(2022, 1, 1)\n        >>> freq = pd.offsets.YearBegin()\n        >>> freq.is_on_offset(ts)\n        True\n\n        >>> freq = pd.offsets.BYearBegin()\n        >>> freq.is_on_offset(ts)\n        False\n\n        >>> ts = pd.Timestamp(2022, 1, 3)\n        >>> freq.is_on_offset(ts)\n        True\n        ',
    'YearOffset.month.__get__ (line 3071)': '\n        Return the month of the year on which this offset applies.\n\n        Returns an integer representing the month (1-12) that this offset\n        targets. For year-based offsets, this determines which month is used\n        for calculations.\n\n        See Also\n        --------\n        tseries.offsets.YearEnd : Offset to end of year.\n        tseries.offsets.YearBegin : Offset to start of year.\n        tseries.offsets.BYearEnd : Offset to last business day of year.\n        tseries.offsets.BYearBegin : Offset to first business day of year.\n\n        Examples\n        --------\n        >>> pd.offsets.BYearBegin().month\n        1\n\n        >>> pd.offsets.BYearBegin(month=6).month\n        6\n        ',
    'YearOffset.rule_code.__get__ (line 3104)': "\n        Return a string representing the base frequency.\n\n        See Also\n        --------\n        tseries.offsets.Hour.rule_code :\n            Returns a string representing the base frequency of 'h'.\n        tseries.offsets.Day.rule_code :\n            Returns a string representing the base frequency of 'D'.\n\n        Examples\n        --------\n        >>> pd.tseries.offsets.YearBegin(n=1, month=2).rule_code\n        'YS-FEB'\n\n        >>> pd.tseries.offsets.YearEnd(n=1, month=6).rule_code\n        'YE-JUN'\n        ",
    '_CustomBusinessMonth.m_offset (line 5833)': '\n        Return a MonthBegin or MonthEnd offset.\n\n        This is used internally to compute the month-based component\n        of the custom business month offset calculation.\n\n        See Also\n        --------\n        tseries.offsets.MonthBegin : Represents the start of the month.\n        tseries.offsets.MonthEnd : Represents the end of the month.\n\n        Examples\n        --------\n        >>> pd.offsets.CustomBusinessMonthBegin().m_offset\n        <MonthBegin>\n\n        >>> pd.offsets.CustomBusinessMonthEnd().m_offset\n        <MonthEnd>\n        ',
    'to_offset (line 6229)': '\n    Return DateOffset object from string or datetime.timedelta object.\n\n    Parameters\n    ----------\n    freq : str, datetime.timedelta, BaseOffset or None\n        The frequency represented.\n    is_period : bool, default False\n        Convert string denoting period frequency to corresponding offsets\n        frequency if is_period=True.\n\n    Returns\n    -------\n    BaseOffset subclass or None\n\n    Raises\n    ------\n    ValueError\n        If freq is an invalid frequency\n\n    See Also\n    --------\n    BaseOffset : Standard kind of date increment used for a date range.\n\n    Examples\n    --------\n    >>> from pandas.tseries.frequencies import to_offset\n    >>> to_offset("5min")\n    <5 * Minutes>\n\n    >>> to_offset("1D1h")\n    <25 * Hours>\n\n    >>> to_offset("2W")\n    <2 * Weeks: weekday=6>\n\n    >>> to_offset("2B")\n    <2 * BusinessDays>\n\n    >>> to_offset(pd.Timedelta(days=1))\n    <Day>\n\n    >>> to_offset(pd.offsets.Hour())\n    <Hour>\n\n    Passing the parameter ``is_period`` equal to True, you can use a string\n    denoting period frequency:\n\n    >>> freq = to_offset(freq="ME", is_period=False)\n    >>> freq.rule_code\n    \'ME\'\n\n    >>> freq = to_offset(freq="M", is_period=True)\n    >>> freq.rule_code\n    \'ME\'\n    ',
}

