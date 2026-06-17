# encoding: utf-8
# module pandas._libs.tslibs.period
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\tslibs\period.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\re\__init__.py
import numpy as np # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.offsets import BDay, Day

from pandas._libs.tslibs.parsing import parse_datetime_string_with_reso

import pandas._libs.tslibs.timestamps as __pandas__libs_tslibs_timestamps


# Variables with simple values

DIFFERENT_FREQ = 'Input has different freq={other_freq} from {cls}(freq={own_freq})'

INVALID_FREQ_ERR_MSG = 'Invalid frequency: {0}'

# functions

def extract_freq(*args, **kwargs): # real signature unknown
    pass

def extract_ordinals(*args, **kwargs): # real signature unknown
    pass

def freq_to_dtype_code(*args, **kwargs): # real signature unknown
    pass

def from_ordinals(*args, **kwargs): # real signature unknown
    pass

def get_period_field_arr(*args, **kwargs): # real signature unknown
    pass

def periodarr_to_dt64arr(*args, **kwargs): # real signature unknown
    """
    Convert array to datetime64 values from a set of ordinals corresponding to
        periods per period convention.
    """
    pass

def period_array_strftime(*args, **kwargs): # real signature unknown
    """
    Vectorized Period.strftime used for PeriodArray._format_native_types.
    
        Parameters
        ----------
        values : ndarray[int64_t], ndim unrestricted
        dtype_code : int
            Corresponds to PeriodDtype._dtype_code
        na_rep : any
        date_format : str or None
    """
    pass

def period_asfreq(*args, **kwargs): # real signature unknown
    """
    Convert period ordinal from one frequency to another, and if upsampling,
        choose to use start ('S') or end ('E') of period.
    """
    pass

def period_asfreq_arr(*args, **kwargs): # real signature unknown
    """
    Convert int64-array of period ordinals from one frequency to another, and
        if upsampling, choose to use start ('S') or end ('E') of period.
    """
    pass

def period_ordinal(*args, **kwargs): # real signature unknown
    """
    Find the ordinal representation of the given datetime components at the
        frequency `freq`.
    
        Parameters
        ----------
        y : int
        m : int
        d : int
        h : int
        min : int
        s : int
        us : int
        ps : int
    
        Returns
        -------
        ordinal : int64_t
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

def validate_end_alias(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_PeriodMixin(*args, **kwargs): # real signature unknown
    pass

# classes

class IncompatibleFrequency(TypeError):
    """
    Raised when trying to compare or operate between Periods with different frequencies.
    
        This error occurs when performing operations between Period objects or
        PeriodArrays that have different frequencies that cannot be aligned,
        such as comparing or doing arithmetic on periods with mismatched frequencies.
    
        See Also
        --------
        Period : Represents a period of time.
        PeriodIndex : Immutable ndarray holding ordinal values.
        PeriodDtype : An ExtensionDtype for Period data.
    
        Examples
        --------
        Trying to compare Period objects with different frequencies:
    
        >>> pd.Period("2024-01", freq="M") - pd.Period("2024-01-01", freq="D")
        Traceback (most recent call last):
        IncompatibleFrequency: Input has different freq=D from Period(freq=M)
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _module_source = 'pandas._libs.tslibs.period'


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



class PeriodMixin(object):
    # no doc
    def _require_matching_freq(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    end_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the Timestamp for the end of the period.

        Returns
        -------
        Timestamp

        See Also
        --------
        Period.start_time : Return the start Timestamp.
        Period.dayofyear : Return the day of year.
        Period.daysinmonth : Return the days in that month.
        Period.dayofweek : Return the day of the week.

        Examples
        --------
        For Period:

        >>> pd.Period('2020-01', 'D').end_time
        Timestamp('2020-01-01 23:59:59.999999')

        For Series:

        >>> period_index = pd.period_range('2020-1-1 00:00', '2020-3-1 00:00', freq='M')
        >>> s = pd.Series(period_index)
        >>> s
        0   2020-01
        1   2020-02
        2   2020-03
        dtype: period[M]
        >>> s.dt.end_time
        0   2020-01-31 23:59:59.999999
        1   2020-02-29 23:59:59.999999
        2   2020-03-31 23:59:59.999999
        dtype: datetime64[us]

        For PeriodIndex:

        >>> idx = pd.PeriodIndex(["2023-01", "2023-02", "2023-03"], freq="M")
        >>> idx.end_time
        DatetimeIndex(['2023-01-31 23:59:59.999999',
                       '2023-02-28 23:59:59.999999',
                       '2023-03-31 23:59:59.999999'],
                       dtype='datetime64[us]', freq=None)
        """

    start_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the Timestamp for the start of the period.

        Returns
        -------
        Timestamp

        See Also
        --------
        Period.end_time : Return the end Timestamp.
        Period.dayofyear : Return the day of year.
        Period.daysinmonth : Return the days in that month.
        Period.dayofweek : Return the day of the week.

        Examples
        --------
        >>> period = pd.Period('2012-1-1', freq='D')
        >>> period
        Period('2012-01-01', 'D')

        >>> period.start_time
        Timestamp('2012-01-01 00:00:00')

        >>> period.end_time
        Timestamp('2012-01-01 23:59:59.999999')
        """



class _Period(PeriodMixin):
    # no doc
    def asfreq(self, h): # real signature unknown; restored from __doc__
        """
        Convert Period to desired frequency, at the start or end of the interval.
        
                Parameters
                ----------
                freq : str, DateOffset
                    The target frequency to convert the Period object to.
                    If a string is provided,
                    it must be a valid :ref:`period alias <timeseries.period_aliases>`.
        
                how : {'E', 'S', 'end', 'start'}, default 'end'
                    Specifies whether to align the period to the start or end of the interval:
                    - 'E' or 'end': Align to the end of the interval.
                    - 'S' or 'start': Align to the start of the interval.
        
                Returns
                -------
                Period : Period object with the specified frequency, aligned to the parameter.
        
                See Also
                --------
                Period.end_time : Return the end Timestamp.
                Period.start_time : Return the start Timestamp.
                Period.dayofyear : Return the day of the year.
                Period.dayofweek : Return the day of the week.
        
                Examples
                --------
                Convert a daily period to an hourly period, aligning to the end of the day:
        
                >>> period = pd.Period('2023-01-01', freq='D')
                >>> period.asfreq('h')
                Period('2023-01-01 23:00', 'h')
        
                Convert a monthly period to a daily period, aligning to the start of the month:
        
                >>> period = pd.Period('2023-01', freq='M')
                >>> period.asfreq('D', how='start')
                Period('2023-01-01', 'D')
        
                Convert a yearly period to a monthly period, aligning to the last month:
        
                >>> period = pd.Period('2023', freq='Y')
                >>> period.asfreq('M', how='end')
                Period('2023-12', 'M')
        
                Convert a monthly period to an hourly period,
                aligning to the first day of the month:
        
                >>> period = pd.Period('2023-01', freq='M')
                >>> period.asfreq('h', how='start')
                Period('2023-01-01 00:00', 'H')
        
                Convert a weekly period to a daily period, aligning to the last day of the week:
        
                >>> period = pd.Period('2023-08-01', freq='W')
                >>> period.asfreq('D', how='end')
                Period('2023-08-04', 'D')
        """
        pass

    @classmethod
    def now(cls, h): # real signature unknown; restored from __doc__
        """
        Return the period of now's date.
        
                The `now` method provides a convenient way to generate a period
                object for the current date and time. This can be particularly
                useful in financial and economic analysis, where data is often
                collected and analyzed in regular intervals (e.g., hourly, daily,
                monthly). By specifying the frequency, users can create periods
                that match the granularity of their data.
        
                Parameters
                ----------
                freq : str, DateOffset
                    Frequency to use for the returned period.
        
                See Also
                --------
                to_datetime : Convert argument to datetime.
                Period : Represents a period of time.
                Period.to_timestamp : Return the Timestamp representation of the Period.
        
                Examples
                --------
                >>> pd.Period.now('h')  # doctest: +SKIP
                Period('2023-06-12 11:00', 'h')
        """
        pass

    def strftime(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Returns a formatted string representation of the :class:`Period`.
        
                ``fmt`` must be ``None`` or a string containing one or several directives.
                When ``None``, the format will be determined from the frequency of the Period.
                The method recognizes the same directives as the :func:`time.strftime`
                function of the standard Python distribution, as well as the specific
                additional directives ``%f``, ``%F``, ``%q``, ``%l``, ``%u``, ``%n``.
                (formatting & docs originally from scikits.timeries).
        
                +-----------+--------------------------------+-------+
                | Directive | Meaning                        | Notes |
                +===========+================================+=======+
                | ``%a``    | Locale's abbreviated weekday   |       |
                |           | name.                          |       |
                +-----------+--------------------------------+-------+
                | ``%A``    | Locale's full weekday name.    |       |
                +-----------+--------------------------------+-------+
                | ``%b``    | Locale's abbreviated month     |       |
                |           | name.                          |       |
                +-----------+--------------------------------+-------+
                | ``%B``    | Locale's full month name.      |       |
                +-----------+--------------------------------+-------+
                | ``%c``    | Locale's appropriate date and  |       |
                |           | time representation.           |       |
                +-----------+--------------------------------+-------+
                | ``%d``    | Day of the month as a decimal  |       |
                |           | number [01,31].                |       |
                +-----------+--------------------------------+-------+
                | ``%f``    | 'Fiscal' year without a        | \(1)  |
                |           | century  as a decimal number   |       |
                |           | [00,99]                        |       |
                +-----------+--------------------------------+-------+
                | ``%F``    | 'Fiscal' year with a century   | \(2)  |
                |           | as a decimal number            |       |
                +-----------+--------------------------------+-------+
                | ``%H``    | Hour (24-hour clock) as a      |       |
                |           | decimal number [00,23].        |       |
                +-----------+--------------------------------+-------+
                | ``%I``    | Hour (12-hour clock) as a      |       |
                |           | decimal number [01,12].        |       |
                +-----------+--------------------------------+-------+
                | ``%j``    | Day of the year as a decimal   |       |
                |           | number [001,366].              |       |
                +-----------+--------------------------------+-------+
                | ``%m``    | Month as a decimal number      |       |
                |           | [01,12].                       |       |
                +-----------+--------------------------------+-------+
                | ``%M``    | Minute as a decimal number     |       |
                |           | [00,59].                       |       |
                +-----------+--------------------------------+-------+
                | ``%p``    | Locale's equivalent of either  | \(3)  |
                |           | AM or PM.                      |       |
                +-----------+--------------------------------+-------+
                | ``%q``    | Quarter as a decimal number    |       |
                |           | [1,4]                          |       |
                +-----------+--------------------------------+-------+
                | ``%S``    | Second as a decimal number     | \(4)  |
                |           | [00,61].                       |       |
                +-----------+--------------------------------+-------+
                | ``%l``    | Millisecond as a decimal number|       |
                |           | [000,999].                     |       |
                +-----------+--------------------------------+-------+
                | ``%u``    | Microsecond as a decimal number|       |
                |           | [000000,999999].               |       |
                +-----------+--------------------------------+-------+
                | ``%n``    | Nanosecond as a decimal number |       |
                |           | [000000000,999999999].         |       |
                +-----------+--------------------------------+-------+
                | ``%U``    | Week number of the year        | \(5)  |
                |           | (Sunday as the first day of    |       |
                |           | the week) as a decimal number  |       |
                |           | [00,53].  All days in a new    |       |
                |           | year preceding the first       |       |
                |           | Sunday are considered to be in |       |
                |           | week 0.                        |       |
                +-----------+--------------------------------+-------+
                | ``%w``    | Weekday as a decimal number    |       |
                |           | [0(Sunday),6].                 |       |
                +-----------+--------------------------------+-------+
                | ``%W``    | Week number of the year        | \(5)  |
                |           | (Monday as the first day of    |       |
                |           | the week) as a decimal number  |       |
                |           | [00,53].  All days in a new    |       |
                |           | year preceding the first       |       |
                |           | Monday are considered to be in |       |
                |           | week 0.                        |       |
                +-----------+--------------------------------+-------+
                | ``%x``    | Locale's appropriate date      |       |
                |           | representation.                |       |
                +-----------+--------------------------------+-------+
                | ``%X``    | Locale's appropriate time      |       |
                |           | representation.                |       |
                +-----------+--------------------------------+-------+
                | ``%y``    | Year without century as a      |       |
                |           | decimal number [00,99].        |       |
                +-----------+--------------------------------+-------+
                | ``%Y``    | Year with century as a decimal |       |
                |           | number.                        |       |
                +-----------+--------------------------------+-------+
                | ``%Z``    | Time zone name (no characters  |       |
                |           | if no time zone exists).       |       |
                +-----------+--------------------------------+-------+
                | ``%%``    | A literal ``'%'`` character.   |       |
                +-----------+--------------------------------+-------+
        
                The `strftime` method provides a way to represent a :class:`Period`
                object as a string in a specified format. This is particularly useful
                when displaying date and time data in different locales or customized
                formats, suitable for reports or user interfaces. It extends the standard
                Python string formatting capabilities with additional directives specific
                to `pandas`, accommodating features like fiscal years and precise
                sub-second components.
        
                Parameters
                ----------
                fmt : str or None
                    String containing the desired format directives. If ``None``, the
                    format is determined based on the Period's frequency.
        
                See Also
                --------
                Timestamp.strftime : Return a formatted string of the Timestamp.
                to_datetime : Convert argument to datetime.
                time.strftime : Format a time object as a string according to a
                    specified format string in the standard Python library.
        
                Notes
                -----
        
                (1)
                    The ``%f`` directive is the same as ``%y`` if the frequency is
                    not quarterly.
                    Otherwise, it corresponds to the 'fiscal' year, as defined by
                    the :attr:`qyear` attribute.
        
                (2)
                    The ``%F`` directive is the same as ``%Y`` if the frequency is
                    not quarterly.
                    Otherwise, it corresponds to the 'fiscal' year, as defined by
                    the :attr:`qyear` attribute.
        
                (3)
                    The ``%p`` directive only affects the output hour field
                    if the ``%I`` directive is used to parse the hour.
        
                (4)
                    The range really is ``0`` to ``61``; this accounts for leap
                    seconds and the (very rare) double leap seconds.
        
                (5)
                    The ``%U`` and ``%W`` directives are only used in calculations
                    when the day of the week and the year are specified.
        
                Examples
                --------
        
                >>> from pandas import Period
                >>> a = Period(freq='Q-JUL', year=2006, quarter=1)
                >>> a.strftime('%F-Q%q')
                '2006-Q1'
                >>> # Output the last month in the quarter of this date
                >>> a.strftime('%b-%Y')
                'Oct-2005'
                >>>
                >>> a = Period(freq='D', year=2001, month=1, day=1)
                >>> a.strftime('%d-%b-%Y')
                '01-Jan-2001'
                >>> a.strftime('%b. %d, %Y was a %A')
                'Jan. 01, 2001 was a Monday'
        """
        pass

    def to_timestamp(self): # real signature unknown; restored from __doc__
        """
        Return the Timestamp representation of the Period.
        
                Uses the target frequency specified at the part of the period specified
                by `how`, which is either `Start` or `Finish`.
        
                If possible, gives microsecond-unit Timestamp. Otherwise gives nanosecond
                unit.
        
                Parameters
                ----------
                freq : str or DateOffset
                    Target frequency. Default is 'D' if self._freq is week or
                    longer and 'S' otherwise.
                how : str, default 'S' (start)
                    One of 'S', 'E'. Can be aliased as case insensitive
                    'Start', 'Finish', 'Begin', 'End'.
        
                Returns
                -------
                Timestamp
        
                See Also
                --------
                Timestamp : A class representing a single point in time.
                Period : Represents a span of time with a fixed frequency.
                PeriodIndex.to_timestamp : Convert a `PeriodIndex` to a `DatetimeIndex`.
        
                Examples
                --------
                >>> period = pd.Period('2023-1-1', freq='D')
                >>> timestamp = period.to_timestamp()
                >>> timestamp
                Timestamp('2023-01-01 00:00:00')
        """
        pass

    def _add_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _add_timedeltalike_scalar(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_ordinal(cls, *args, **kwargs): # real signature unknown
        """ Fast creation from an ordinal and freq that are already validated! """
        pass

    @classmethod
    def _maybe_convert_freq(cls, *args, **kwargs): # real signature unknown
        """
        A Period's freq attribute must have `freq.n > 0`, which we check for here.
        
                Returns
                -------
                DateOffset
        """
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

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return a string representation for a particular DataFrame """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get day of the month that a Period falls on.

        The `day` property provides a simple way to access the day component
        of a `Period` object, which represents time spans in various frequencies
        (e.g., daily, hourly, monthly). If the period's frequency does not include
        a day component (e.g., yearly or quarterly periods), the returned day
        corresponds to the first day of that period.

        Returns
        -------
        int

        See Also
        --------
        Period.dayofweek : Get the day of the week.
        Period.dayofyear : Get the day of the year.

        Examples
        --------
        >>> p = pd.Period("2018-03-11", freq='h')
        >>> p.day
        11
        """

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Day of the week the period lies in, with Monday=0 and Sunday=6.

        If the period frequency is lower than daily (e.g. hourly), and the
        period spans over multiple days, the day at the start of the period is
        used.

        If the frequency is higher than daily (e.g. monthly), the last day
        of the period is used.

        Returns
        -------
        int
            Day of the week.

        See Also
        --------
        Period.day_of_week : Day of the week the period lies in.
        Period.weekday : Alias of Period.day_of_week.
        Period.day : Day of the month.
        Period.dayofyear : Day of the year.

        Examples
        --------
        >>> per = pd.Period('2017-12-31 22:00', 'h')
        >>> per.day_of_week
        6

        For periods that span over multiple days, the day at the beginning of
        the period is returned.

        >>> per = pd.Period('2017-12-31 22:00', '4h')
        >>> per.day_of_week
        6
        >>> per.start_time.day_of_week
        6

        For periods with a frequency higher than days, the last day of the
        period is returned.

        >>> per = pd.Period('2018-01', 'M')
        >>> per.day_of_week
        2
        >>> per.end_time.day_of_week
        2
        """

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the year.

        This attribute returns the day of the year on which the particular
        date occurs. The return value ranges between 1 to 365 for regular
        years and 1 to 366 for leap years.

        Returns
        -------
        int
            The day of year.

        See Also
        --------
        Period.day : Return the day of the month.
        Period.day_of_week : Return the day of week.
        PeriodIndex.day_of_year : Return the day of year of all indexes.

        Examples
        --------
        >>> period = pd.Period("2015-10-23", freq='h')
        >>> period.day_of_year
        296
        >>> period = pd.Period("2012-12-31", freq='D')
        >>> period.day_of_year
        366
        >>> period = pd.Period("2013-01-01", freq='D')
        >>> period.day_of_year
        1
        """

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the total number of days of the month that this period falls on.

        Returns
        -------
        int

        See Also
        --------
        Period.days_in_month : Return the days of the month.
        Period.dayofyear : Return the day of the year.

        Examples
        --------
        >>> p = pd.Period("2018-03-11", freq='h')
        >>> p.daysinmonth
        31
        """

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the total number of days in the month that this period falls on.

        Returns
        -------
        int

        See Also
        --------
        Period.daysinmonth : Gets the number of days in the month.
        DatetimeIndex.daysinmonth : Gets the number of days in the month.
        calendar.monthrange : Returns a tuple containing weekday
            (0-6 ~ Mon-Sun) and number of days (28-31).

        Examples
        --------
        >>> p = pd.Period('2018-2-17')
        >>> p.days_in_month
        28

        >>> pd.Period('2018-03-01').days_in_month
        31

        Handles the leap year case as well:

        >>> p = pd.Period('2016-2-17')
        >>> p.days_in_month
        29
        """

    day_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Day of the week the period lies in, with Monday=0 and Sunday=6.

        If the period frequency is lower than daily (e.g. hourly), and the
        period spans over multiple days, the day at the start of the period is
        used.

        If the frequency is higher than daily (e.g. monthly), the last day
        of the period is used.

        Returns
        -------
        int
            Day of the week.

        See Also
        --------
        Period.day_of_week : Day of the week the period lies in.
        Period.weekday : Alias of Period.day_of_week.
        Period.day : Day of the month.
        Period.dayofyear : Day of the year.

        Examples
        --------
        >>> per = pd.Period('2017-12-31 22:00', 'h')
        >>> per.day_of_week
        6

        For periods that span over multiple days, the day at the beginning of
        the period is returned.

        >>> per = pd.Period('2017-12-31 22:00', '4h')
        >>> per.day_of_week
        6
        >>> per.start_time.day_of_week
        6

        For periods with a frequency higher than days, the last day of the
        period is returned.

        >>> per = pd.Period('2018-01', 'M')
        >>> per.day_of_week
        2
        >>> per.end_time.day_of_week
        2
        """

    day_of_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the year.

        This attribute returns the day of the year on which the particular
        date occurs. The return value ranges between 1 to 365 for regular
        years and 1 to 366 for leap years.

        Returns
        -------
        int
            The day of year.

        See Also
        --------
        Period.day : Return the day of the month.
        Period.day_of_week : Return the day of week.
        PeriodIndex.day_of_year : Return the day of year of all indexes.

        Examples
        --------
        >>> period = pd.Period("2015-10-23", freq='h')
        >>> period.day_of_year
        296
        >>> period = pd.Period("2012-12-31", freq='D')
        >>> period.day_of_year
        366
        >>> period = pd.Period("2013-01-01", freq='D')
        >>> period.day_of_year
        1
        """

    freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the frequency object for this Period.

        The frequency object represents the span of time that this Period covers.
        It is a DateOffset that defines the interval type (e.g., daily, monthly).

        See Also
        --------
        Period.freqstr : Return a string representation of the frequency.
        Period.asfreq : Convert Period to desired frequency.

        Examples
        --------
        >>> period = pd.Period('2020-01', freq='M')
        >>> period.freq
        <MonthEnd>
        """

    freqstr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representation of the frequency.

        This property provides the frequency string associated with the `Period`
        object. The frequency string describes the granularity of the time span
        represented by the `Period`. Common frequency strings include 'D' for
        daily, 'M' for monthly, 'Y' for yearly, etc.

        See Also
        --------
        Period.asfreq : Convert Period to desired frequency, at the start or end
            of the interval.
        period_range : Return a fixed frequency PeriodIndex.

        Examples
        --------
        >>> pd.Period('2020-01', 'D').freqstr
        'D'
        """

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the hour of the day component of the Period.

        Returns
        -------
        int
            The hour as an integer, between 0 and 23.

        See Also
        --------
        Period.second : Get the second component of the Period.
        Period.minute : Get the minute component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11 13:03:12.050000")
        >>> p.hour
        13

        Period longer than a day

        >>> p = pd.Period("2018-03-11", freq="M")
        >>> p.hour
        0
        """

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return True if the period's year is in a leap year.

        See Also
        --------
        Timestamp.is_leap_year : Check if the year in a Timestamp is a leap year.
        DatetimeIndex.is_leap_year : Boolean indicator if the date belongs to a
            leap year.

        Examples
        --------
        >>> period = pd.Period('2022-01', 'M')
        >>> period.is_leap_year
        False

        >>> period = pd.Period('2020-01', 'M')
        >>> period.is_leap_year
        True
        """

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get minute of the hour component of the Period.

        Returns
        -------
        int
            The minute as an integer, between 0 and 59.

        See Also
        --------
        Period.hour : Get the hour component of the Period.
        Period.second : Get the second component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11 13:03:12.050000")
        >>> p.minute
        3
        """

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the month this Period falls on.

        Returns
        -------
        int

        See Also
        --------
        period.week : Get the week of the year on the given Period.
        Period.year : Return the year this Period falls on.
        Period.day : Return the day of the month this Period falls on.

        Notes
        -----
        The month is based on the `ordinal` and `base` attributes of the Period.

        Examples
        --------
        Create a Period object for January 2022 and get the month:

        >>> period = pd.Period('2022-01', 'M')
        >>> period.month
        1

        Period object with no specified frequency, resulting in a default frequency:

        >>> period = pd.Period('2022', 'Y')
        >>> period.month
        12

        Create a Period object with a specified frequency but an incomplete date string:

        >>> period = pd.Period('2022', 'M')
        >>> period.month
        1

        Handle a case where the Period object is empty, which results in `NaN`:

        >>> period = pd.Period('nan', 'M')
        >>> period.month
        nan
        """

    ordinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the integer ordinal for this Period.

        The ordinal is the internal integer representation of the Period,
        representing its position in the sequence of periods of the given
        frequency. It counts from an epoch (e.g., for daily frequency,
        ordinal 0 corresponds to January 1, 1970).

        See Also
        --------
        Period.freq : Return the frequency of the Period.
        Period.start_time : Return the start time of the Period.

        Examples
        --------
        >>> period = pd.Period('2020-01', freq='M')
        >>> period.ordinal
        600

        >>> period = pd.Period('2020-01-01', freq='D')
        >>> period.ordinal
        18262
        """

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the quarter this Period falls on.

        See Also
        --------
        Timestamp.quarter : Return the quarter of the Timestamp.
        Period.year : Return the year of the period.
        Period.month : Return the month of the period.

        Examples
        --------
        >>> period = pd.Period('2022-04', 'M')
        >>> period.quarter
        2
        """

    qyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Fiscal year the Period lies in according to its starting-quarter.

        The `year` and the `qyear` of the period will be the same if the fiscal
        and calendar years are the same. When they are not, the fiscal year
        can be different from the calendar year of the period.

        Returns
        -------
        int
            The fiscal year of the period.

        See Also
        --------
        Period.year : Return the calendar year of the period.

        Examples
        --------
        If the natural and fiscal year are the same, `qyear` and `year` will
        be the same.

        >>> per = pd.Period('2018Q1', freq='Q')
        >>> per.qyear
        2018
        >>> per.year
        2018

        If the fiscal year starts in April (`Q-MAR`), the first quarter of
        2018 will start in April 2017. `year` will then be 2017, but `qyear`
        will be the fiscal year, 2018.

        >>> per = pd.Period('2018Q1', freq='Q-MAR')
        >>> per.start_time
        Timestamp('2017-04-01 00:00:00')
        >>> per.qyear
        2018
        >>> per.year
        2017
        """

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the second component of the Period.

        Returns
        -------
        int
            The second of the Period (ranges from 0 to 59).

        See Also
        --------
        Period.hour : Get the hour component of the Period.
        Period.minute : Get the minute component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11 13:03:12.050000")
        >>> p.second
        12
        """

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the week of the year on the given Period.

        Returns
        -------
        int

        See Also
        --------
        Period.dayofweek : Get the day component of the Period.
        Period.weekday : Get the day component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11", "h")
        >>> p.week
        10

        >>> p = pd.Period("2018-02-01", "D")
        >>> p.week
        5

        >>> p = pd.Period("2018-01-06", "D")
        >>> p.week
        1
        """

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Day of the week the period lies in, with Monday=0 and Sunday=6.

        If the period frequency is lower than daily (e.g. hourly), and the
        period spans over multiple days, the day at the start of the period is
        used.

        If the frequency is higher than daily (e.g. monthly), the last day
        of the period is used.

        Returns
        -------
        int
            Day of the week.

        See Also
        --------
        Period.dayofweek : Day of the week the period lies in.
        Period.weekday : Alias of Period.dayofweek.
        Period.day : Day of the month.
        Period.dayofyear : Day of the year.

        Examples
        --------
        >>> per = pd.Period('2017-12-31 22:00', 'h')
        >>> per.dayofweek
        6

        For periods that span over multiple days, the day at the beginning of
        the period is returned.

        >>> per = pd.Period('2017-12-31 22:00', '4h')
        >>> per.dayofweek
        6
        >>> per.start_time.dayofweek
        6

        For periods with a frequency higher than days, the last day of the
        period is returned.

        >>> per = pd.Period('2018-01', 'M')
        >>> per.dayofweek
        2
        >>> per.end_time.dayofweek
        2
        """

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Get the week of the year on the given Period.

        Returns
        -------
        int

        See Also
        --------
        Period.dayofweek : Get the day component of the Period.
        Period.weekday : Get the day component of the Period.

        Examples
        --------
        >>> p = pd.Period("2018-03-11", "h")
        >>> p.weekofyear
        10

        >>> p = pd.Period("2018-02-01", "D")
        >>> p.weekofyear
        5

        >>> p = pd.Period("2018-01-06", "D")
        >>> p.weekofyear
        1
        """

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the year this Period falls on.

        Returns
        -------
        int

        See Also
        --------
        period.month : Get the month of the year for the given Period.
        period.day : Return the day of the month the Period falls on.

        Notes
        -----
        The year is based on the `ordinal` and `base` attributes of the Period.

        Examples
        --------
        Create a Period object for January 2023 and get the year:

        >>> period = pd.Period('2023-01', 'M')
        >>> period.year
        2023

        Create a Period object for 01 January 2023 and get the year:

        >>> period = pd.Period('2023', 'D')
        >>> period.year
        2023

        Get the year for a period representing a quarter:

        >>> period = pd.Period('2023Q2', 'Q')
        >>> period.year
        2023

        Handle a case where the Period object is empty, which results in `NaN`:

        >>> period = pd.Period('nan', 'M')
        >>> period.year
        nan
        """

    _dtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _freq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _ordinal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __array_priority__ = 100


class Period(_Period):
    """
    Represents a period of time.
    
        A `Period` represents a specific time span rather than a point in time.
        Unlike `Timestamp`, which represents a single instant, a `Period` defines a
        duration, such as a month, quarter, or year. The exact representation is
        determined by the `freq` parameter.
    
        Parameters
        ----------
        value : Period, str, datetime, date or pandas.Timestamp, default None
            The time period represented (e.g., '4Q2005'). This represents neither
            the start or the end of the period, but rather the entire period itself.
        freq : str, default None
            One of pandas period strings or corresponding objects. Accepted
            strings are listed in the
            :ref:`period alias section <timeseries.period_aliases>` in the user docs.
            If value is datetime, freq is required.
        ordinal : int, default None
            The period offset from the proleptic Gregorian epoch.
        year : int, default None
            Year value of the period.
        month : int, default 1
            Month value of the period.
        quarter : int, default None
            Quarter value of the period.
        day : int, default 1
            Day value of the period.
        hour : int, default 0
            Hour value of the period.
        minute : int, default 0
            Minute value of the period.
        second : int, default 0
            Second value of the period.
    
        See Also
        --------
        Timestamp : Pandas replacement for python datetime.datetime object.
        date_range : Return a fixed frequency DatetimeIndex.
        timedelta_range : Generates a fixed frequency range of timedeltas.
    
        Examples
        --------
        >>> period = pd.Period('2012-1-1', freq='D')
        >>> period
        Period('2012-01-01', 'D')
    """
    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _module_source = 'pandas._libs.tslibs.period'
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas\', \'__doc__\': "\\n    Represents a period of time.\\n\\n    A `Period` represents a specific time span rather than a point in time.\\n    Unlike `Timestamp`, which represents a single instant, a `Period` defines a\\n    duration, such as a month, quarter, or year. The exact representation is\\n    determined by the `freq` parameter.\\n\\n    Parameters\\n    ----------\\n    value : Period, str, datetime, date or pandas.Timestamp, default None\\n        The time period represented (e.g., \'4Q2005\'). This represents neither\\n        the start or the end of the period, but rather the entire period itself.\\n    freq : str, default None\\n        One of pandas period strings or corresponding objects. Accepted\\n        strings are listed in the\\n        :ref:`period alias section <timeseries.period_aliases>` in the user docs.\\n        If value is datetime, freq is required.\\n    ordinal : int, default None\\n        The period offset from the proleptic Gregorian epoch.\\n    year : int, default None\\n        Year value of the period.\\n    month : int, default 1\\n        Month value of the period.\\n    quarter : int, default None\\n        Quarter value of the period.\\n    day : int, default 1\\n        Day value of the period.\\n    hour : int, default 0\\n        Hour value of the period.\\n    minute : int, default 0\\n        Minute value of the period.\\n    second : int, default 0\\n        Second value of the period.\\n\\n    See Also\\n    --------\\n    Timestamp : Pandas replacement for python datetime.datetime object.\\n    date_range : Return a fixed frequency DatetimeIndex.\\n    timedelta_range : Generates a fixed frequency range of timedeltas.\\n\\n    Examples\\n    --------\\n    >>> period = pd.Period(\'2012-1-1\', freq=\'D\')\\n    >>> period\\n    Period(\'2012-01-01\', \'D\')\\n    ", \'__new__\': <staticmethod(<cyfunction Period.__new__ at 0x0000016F5D3B4AA0>)>, \'__dict__\': <attribute \'__dict__\' of \'Period\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Period\' objects>, \'_module_source\': \'pandas._libs.tslibs.period\'})'


class Timestamp(__pandas__libs_tslibs_timestamps._Timestamp):
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
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas\', \'__doc__\': "\\n    Pandas replacement for python datetime.datetime object.\\n\\n    Timestamp is the pandas equivalent of python\'s Datetime\\n    and is interchangeable with it in most cases. It\'s the type used\\n    for the entries that make up a DatetimeIndex, and other timeseries\\n    oriented data structures in pandas.\\n\\n    Parameters\\n    ----------\\n    ts_input : datetime-like, str, int, float\\n        Value to be converted to Timestamp.\\n    year : int\\n        Value of year.\\n    month : int\\n        Value of month.\\n    day : int\\n        Value of day.\\n    hour : int, optional, default 0\\n        Value of hour.\\n    minute : int, optional, default 0\\n        Value of minute.\\n    second : int, optional, default 0\\n        Value of second.\\n    microsecond : int, optional, default 0\\n        Value of microsecond.\\n    tzinfo : datetime.tzinfo, optional, default None\\n        Timezone info.\\n    nanosecond : int, optional, default 0\\n        Value of nanosecond.\\n    tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None\\n        Time zone for time which Timestamp will have.\\n    unit : str\\n        Unit used for conversion if ts_input is of type int or float. The\\n        valid values are \'W\', \'D\', \'h\', \'m\', \'s\', \'ms\', \'us\', and \'ns\'. For\\n        example, \'s\' means seconds and \'ms\' means milliseconds.\\n\\n        For float inputs, the result will be stored in nanoseconds, and\\n        the unit attribute will be set as ``\'ns\'``.\\n    fold : {0, 1}, default None, keyword-only\\n        Due to daylight saving time, one wall clock time can occur twice\\n        when shifting from summer to winter time; fold describes whether the\\n        datetime-like corresponds  to the first (0) or the second time (1)\\n        the wall clock hits the ambiguous time.\\n\\n    See Also\\n    --------\\n    Timedelta : Represents a duration, the difference between two dates or times.\\n    datetime.datetime : Python datetime.datetime object.\\n\\n    Notes\\n    -----\\n    There are essentially three calling conventions for the constructor. The\\n    primary form accepts four parameters. They can be passed by position or\\n    keyword.\\n\\n    The other two forms mimic the parameters from ``datetime.datetime``. They\\n    can be passed by either position or keyword, but not both mixed together.\\n\\n    Examples\\n    --------\\n    Using the primary calling convention:\\n\\n    This converts a datetime-like string\\n\\n    >>> pd.Timestamp(\'2017-01-01T12\')\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    This converts a float representing a Unix epoch in units of seconds\\n\\n    >>> pd.Timestamp(1513393355.5, unit=\'s\')\\n    Timestamp(\'2017-12-16 03:02:35.500000\')\\n\\n    This converts an int representing a Unix-epoch in units of weeks\\n\\n    >>> pd.Timestamp(1535, unit=\'W\')\\n    Timestamp(\'1999-06-03 00:00:00\')\\n\\n    This converts an int representing a Unix-epoch in units of seconds\\n    and for a particular timezone\\n\\n    >>> pd.Timestamp(1513393355, unit=\'s\', tz=\'US/Pacific\')\\n    Timestamp(\'2017-12-15 19:02:35-0800\', tz=\'US/Pacific\')\\n\\n    Using the other two forms that mimic the API for ``datetime.datetime``:\\n\\n    >>> pd.Timestamp(2017, 1, 1, 12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n    ", \'fromordinal\': <classmethod(<cyfunction Timestamp.fromordinal at 0x0000016F5D325C70>)>, \'now\': <classmethod(<cyfunction Timestamp.now at 0x0000016F5D325D60>)>, \'today\': <classmethod(<cyfunction Timestamp.today at 0x0000016F5D325E50>)>, \'utcnow\': <classmethod(<cyfunction Timestamp.utcnow at 0x0000016F5D325F40>)>, \'utcfromtimestamp\': <classmethod(<cyfunction Timestamp.utcfromtimestamp at 0x0000016F5D326030>)>, \'fromtimestamp\': <classmethod(<cyfunction Timestamp.fromtimestamp at 0x0000016F5D326120>)>, \'strftime\': <cyfunction Timestamp.strftime at 0x0000016F5D326210>, \'ctime\': <cyfunction Timestamp.ctime at 0x0000016F5D326300>, \'date\': <cyfunction Timestamp.date at 0x0000016F5D3263F0>, \'dst\': <cyfunction Timestamp.dst at 0x0000016F5D3264E0>, \'isocalendar\': <cyfunction Timestamp.isocalendar at 0x0000016F5D3265D0>, \'tzname\': <cyfunction Timestamp.tzname at 0x0000016F5D3266C0>, \'tzinfo\': <property object at 0x0000016F5D2138D0>, \'utcoffset\': <cyfunction Timestamp.utcoffset at 0x0000016F5D3268A0>, \'utctimetuple\': <cyfunction Timestamp.utctimetuple at 0x0000016F5D326990>, \'time\': <cyfunction Timestamp.time at 0x0000016F5D326A80>, \'timetuple\': <cyfunction Timestamp.timetuple at 0x0000016F5D326B70>, \'timetz\': <cyfunction Timestamp.timetz at 0x0000016F5D326C60>, \'toordinal\': <cyfunction Timestamp.toordinal at 0x0000016F5D326D50>, \'strptime\': <classmethod(<cyfunction Timestamp.strptime at 0x0000016F5D326E40>)>, \'combine\': <classmethod(<cyfunction Timestamp.combine at 0x0000016F5D326F30>)>, \'__new__\': <staticmethod(<cyfunction Timestamp.__new__ at 0x0000016F5D327020>)>, \'_round\': <cyfunction Timestamp._round at 0x0000016F5D327110>, \'round\': <cyfunction Timestamp.round at 0x0000016F5D327200>, \'floor\': <cyfunction Timestamp.floor at 0x0000016F5D3272F0>, \'ceil\': <cyfunction Timestamp.ceil at 0x0000016F5D3273E0>, \'tz\': <property object at 0x0000016F5D2137E0>, \'tz_localize\': <cyfunction Timestamp.tz_localize at 0x0000016F5D3276B0>, \'tz_convert\': <cyfunction Timestamp.tz_convert at 0x0000016F5D3277A0>, \'astimezone\': <cyfunction Timestamp.tz_convert at 0x0000016F5D3277A0>, \'replace\': <cyfunction Timestamp.replace at 0x0000016F5D327890>, \'to_julian_date\': <cyfunction Timestamp.to_julian_date at 0x0000016F5D327980>, \'isoweekday\': <cyfunction Timestamp.isoweekday at 0x0000016F5D327A70>, \'weekday\': <cyfunction Timestamp.weekday at 0x0000016F5D327B60>, \'__dict__\': <attribute \'__dict__\' of \'Timestamp\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timestamp\' objects>, \'_module_source\': \'pandas._libs.tslibs.timestamps\', \'weekofyear\': <attribute \'week\' of \'pandas._libs.tslibs.timestamps._Timestamp\' objects>, \'daysinmonth\': <attribute \'days_in_month\' of \'pandas._libs.tslibs.timestamps._Timestamp\' objects>})'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016F5D15B0B0>'

__pyx_capi__ = {
    'get_period_ordinal': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t (npy_datetimestruct *, int)" at 0x0000016F5D3A6CF0>'
    'is_period_object': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x0000016F5D3A6D40>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.period', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000016F5D15B0B0>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\period.cp314-win_amd64.pyd')"

__test__ = {
    'PeriodMixin.end_time.__get__ (line 1695)': '\n        Get the Timestamp for the end of the period.\n\n        Returns\n        -------\n        Timestamp\n\n        See Also\n        --------\n        Period.start_time : Return the start Timestamp.\n        Period.dayofyear : Return the day of year.\n        Period.daysinmonth : Return the days in that month.\n        Period.dayofweek : Return the day of the week.\n\n        Examples\n        --------\n        For Period:\n\n        >>> pd.Period(\'2020-01\', \'D\').end_time\n        Timestamp(\'2020-01-01 23:59:59.999999\')\n\n        For Series:\n\n        >>> period_index = pd.period_range(\'2020-1-1 00:00\', \'2020-3-1 00:00\', freq=\'M\')\n        >>> s = pd.Series(period_index)\n        >>> s\n        0   2020-01\n        1   2020-02\n        2   2020-03\n        dtype: period[M]\n        >>> s.dt.end_time\n        0   2020-01-31 23:59:59.999999\n        1   2020-02-29 23:59:59.999999\n        2   2020-03-31 23:59:59.999999\n        dtype: datetime64[us]\n\n        For PeriodIndex:\n\n        >>> idx = pd.PeriodIndex(["2023-01", "2023-02", "2023-03"], freq="M")\n        >>> idx.end_time\n        DatetimeIndex([\'2023-01-31 23:59:59.999999\',\n                       \'2023-02-28 23:59:59.999999\',\n                       \'2023-03-31 23:59:59.999999\'],\n                       dtype=\'datetime64[us]\', freq=None)\n        ',
    'PeriodMixin.start_time.__get__ (line 1665)': "\n        Get the Timestamp for the start of the period.\n\n        Returns\n        -------\n        Timestamp\n\n        See Also\n        --------\n        Period.end_time : Return the end Timestamp.\n        Period.dayofyear : Return the day of year.\n        Period.daysinmonth : Return the days in that month.\n        Period.dayofweek : Return the day of the week.\n\n        Examples\n        --------\n        >>> period = pd.Period('2012-1-1', freq='D')\n        >>> period\n        Period('2012-01-01', 'D')\n\n        >>> period.start_time\n        Timestamp('2012-01-01 00:00:00')\n\n        >>> period.end_time\n        Timestamp('2012-01-01 23:59:59.999999')\n        ",
    '_Period.asfreq (line 1989)': "\n        Convert Period to desired frequency, at the start or end of the interval.\n\n        Parameters\n        ----------\n        freq : str, DateOffset\n            The target frequency to convert the Period object to.\n            If a string is provided,\n            it must be a valid :ref:`period alias <timeseries.period_aliases>`.\n\n        how : {'E', 'S', 'end', 'start'}, default 'end'\n            Specifies whether to align the period to the start or end of the interval:\n            - 'E' or 'end': Align to the end of the interval.\n            - 'S' or 'start': Align to the start of the interval.\n\n        Returns\n        -------\n        Period : Period object with the specified frequency, aligned to the parameter.\n\n        See Also\n        --------\n        Period.end_time : Return the end Timestamp.\n        Period.start_time : Return the start Timestamp.\n        Period.dayofyear : Return the day of the year.\n        Period.dayofweek : Return the day of the week.\n\n        Examples\n        --------\n        Convert a daily period to an hourly period, aligning to the end of the day:\n\n        >>> period = pd.Period('2023-01-01', freq='D')\n        >>> period.asfreq('h')\n        Period('2023-01-01 23:00', 'h')\n\n        Convert a monthly period to a daily period, aligning to the start of the month:\n\n        >>> period = pd.Period('2023-01', freq='M')\n        >>> period.asfreq('D', how='start')\n        Period('2023-01-01', 'D')\n\n        Convert a yearly period to a monthly period, aligning to the last month:\n\n        >>> period = pd.Period('2023', freq='Y')\n        >>> period.asfreq('M', how='end')\n        Period('2023-12', 'M')\n\n        Convert a monthly period to an hourly period,\n        aligning to the first day of the month:\n\n        >>> period = pd.Period('2023-01', freq='M')\n        >>> period.asfreq('h', how='start')\n        Period('2023-01-01 00:00', 'H')\n\n        Convert a weekly period to a daily period, aligning to the last day of the week:\n\n        >>> period = pd.Period('2023-08-01', freq='W')\n        >>> period.asfreq('D', how='end')\n        Period('2023-08-04', 'D')\n        ",
    '_Period.day.__get__ (line 2225)': '\n        Get day of the month that a Period falls on.\n\n        The `day` property provides a simple way to access the day component\n        of a `Period` object, which represents time spans in various frequencies\n        (e.g., daily, hourly, monthly). If the period\'s frequency does not include\n        a day component (e.g., yearly or quarterly periods), the returned day\n        corresponds to the first day of that period.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.dayofweek : Get the day of the week.\n        Period.dayofyear : Get the day of the year.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", freq=\'h\')\n        >>> p.day\n        11\n        ',
    '_Period.day_of_week.__get__ (line 2393)': "\n        Day of the week the period lies in, with Monday=0 and Sunday=6.\n\n        If the period frequency is lower than daily (e.g. hourly), and the\n        period spans over multiple days, the day at the start of the period is\n        used.\n\n        If the frequency is higher than daily (e.g. monthly), the last day\n        of the period is used.\n\n        Returns\n        -------\n        int\n            Day of the week.\n\n        See Also\n        --------\n        Period.day_of_week : Day of the week the period lies in.\n        Period.weekday : Alias of Period.day_of_week.\n        Period.day : Day of the month.\n        Period.dayofyear : Day of the year.\n\n        Examples\n        --------\n        >>> per = pd.Period('2017-12-31 22:00', 'h')\n        >>> per.day_of_week\n        6\n\n        For periods that span over multiple days, the day at the beginning of\n        the period is returned.\n\n        >>> per = pd.Period('2017-12-31 22:00', '4h')\n        >>> per.day_of_week\n        6\n        >>> per.start_time.day_of_week\n        6\n\n        For periods with a frequency higher than days, the last day of the\n        period is returned.\n\n        >>> per = pd.Period('2018-01', 'M')\n        >>> per.day_of_week\n        2\n        >>> per.end_time.day_of_week\n        2\n        ",
    '_Period.day_of_year.__get__ (line 2497)': '\n        Return the day of the year.\n\n        This attribute returns the day of the year on which the particular\n        date occurs. The return value ranges between 1 to 365 for regular\n        years and 1 to 366 for leap years.\n\n        Returns\n        -------\n        int\n            The day of year.\n\n        See Also\n        --------\n        Period.day : Return the day of the month.\n        Period.day_of_week : Return the day of week.\n        PeriodIndex.day_of_year : Return the day of year of all indexes.\n\n        Examples\n        --------\n        >>> period = pd.Period("2015-10-23", freq=\'h\')\n        >>> period.day_of_year\n        296\n        >>> period = pd.Period("2012-12-31", freq=\'D\')\n        >>> period.day_of_year\n        366\n        >>> period = pd.Period("2013-01-01", freq=\'D\')\n        >>> period.day_of_year\n        1\n        ',
    '_Period.days_in_month.__get__ (line 2596)': "\n        Get the total number of days in the month that this period falls on.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.daysinmonth : Gets the number of days in the month.\n        DatetimeIndex.daysinmonth : Gets the number of days in the month.\n        calendar.monthrange : Returns a tuple containing weekday\n            (0-6 ~ Mon-Sun) and number of days (28-31).\n\n        Examples\n        --------\n        >>> p = pd.Period('2018-2-17')\n        >>> p.days_in_month\n        28\n\n        >>> pd.Period('2018-03-01').days_in_month\n        31\n\n        Handles the leap year case as well:\n\n        >>> p = pd.Period('2016-2-17')\n        >>> p.days_in_month\n        29\n        ",
    '_Period.daysinmonth.__get__ (line 2630)': '\n        Get the total number of days of the month that this period falls on.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.days_in_month : Return the days of the month.\n        Period.dayofyear : Return the day of the year.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", freq=\'h\')\n        >>> p.daysinmonth\n        31\n        ',
    '_Period.freq.__get__ (line 1803)': "\n        Return the frequency object for this Period.\n\n        The frequency object represents the span of time that this Period covers.\n        It is a DateOffset that defines the interval type (e.g., daily, monthly).\n\n        See Also\n        --------\n        Period.freqstr : Return a string representation of the frequency.\n        Period.asfreq : Convert Period to desired frequency.\n\n        Examples\n        --------\n        >>> period = pd.Period('2020-01', freq='M')\n        >>> period.freq\n        <MonthEnd>\n        ",
    '_Period.freqstr.__get__ (line 2705)': "\n        Return a string representation of the frequency.\n\n        This property provides the frequency string associated with the `Period`\n        object. The frequency string describes the granularity of the time span\n        represented by the `Period`. Common frequency strings include 'D' for\n        daily, 'M' for monthly, 'Y' for yearly, etc.\n\n        See Also\n        --------\n        Period.asfreq : Convert Period to desired frequency, at the start or end\n            of the interval.\n        period_range : Return a fixed frequency PeriodIndex.\n\n        Examples\n        --------\n        >>> pd.Period('2020-01', 'D').freqstr\n        'D'\n        ",
    '_Period.hour.__get__ (line 2254)': '\n        Get the hour of the day component of the Period.\n\n        Returns\n        -------\n        int\n            The hour as an integer, between 0 and 23.\n\n        See Also\n        --------\n        Period.second : Get the second component of the Period.\n        Period.minute : Get the minute component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.hour\n        13\n\n        Period longer than a day\n\n        >>> p = pd.Period("2018-03-11", freq="M")\n        >>> p.hour\n        0\n        ',
    '_Period.is_leap_year.__get__ (line 2652)': "\n        Return True if the period's year is in a leap year.\n\n        See Also\n        --------\n        Timestamp.is_leap_year : Check if the year in a Timestamp is a leap year.\n        DatetimeIndex.is_leap_year : Boolean indicator if the date belongs to a\n            leap year.\n\n        Examples\n        --------\n        >>> period = pd.Period('2022-01', 'M')\n        >>> period.is_leap_year\n        False\n\n        >>> period = pd.Period('2020-01', 'M')\n        >>> period.is_leap_year\n        True\n        ",
    '_Period.minute.__get__ (line 2284)': '\n        Get minute of the hour component of the Period.\n\n        Returns\n        -------\n        int\n            The minute as an integer, between 0 and 59.\n\n        See Also\n        --------\n        Period.hour : Get the hour component of the Period.\n        Period.second : Get the second component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.minute\n        3\n        ',
    '_Period.month.__get__ (line 2177)': "\n        Return the month this Period falls on.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        period.week : Get the week of the year on the given Period.\n        Period.year : Return the year this Period falls on.\n        Period.day : Return the day of the month this Period falls on.\n\n        Notes\n        -----\n        The month is based on the `ordinal` and `base` attributes of the Period.\n\n        Examples\n        --------\n        Create a Period object for January 2022 and get the month:\n\n        >>> period = pd.Period('2022-01', 'M')\n        >>> period.month\n        1\n\n        Period object with no specified frequency, resulting in a default frequency:\n\n        >>> period = pd.Period('2022', 'Y')\n        >>> period.month\n        12\n\n        Create a Period object with a specified frequency but an incomplete date string:\n\n        >>> period = pd.Period('2022', 'M')\n        >>> period.month\n        1\n\n        Handle a case where the Period object is empty, which results in `NaN`:\n\n        >>> period = pd.Period('nan', 'M')\n        >>> period.month\n        nan\n        ",
    '_Period.now (line 2675)': "\n        Return the period of now's date.\n\n        The `now` method provides a convenient way to generate a period\n        object for the current date and time. This can be particularly\n        useful in financial and economic analysis, where data is often\n        collected and analyzed in regular intervals (e.g., hourly, daily,\n        monthly). By specifying the frequency, users can create periods\n        that match the granularity of their data.\n\n        Parameters\n        ----------\n        freq : str, DateOffset\n            Frequency to use for the returned period.\n\n        See Also\n        --------\n        to_datetime : Convert argument to datetime.\n        Period : Represents a period of time.\n        Period.to_timestamp : Return the Timestamp representation of the Period.\n\n        Examples\n        --------\n        >>> pd.Period.now('h')  # doctest: +SKIP\n        Period('2023-06-12 11:00', 'h')\n        ",
    '_Period.ordinal.__get__ (line 1776)': "\n        Return the integer ordinal for this Period.\n\n        The ordinal is the internal integer representation of the Period,\n        representing its position in the sequence of periods of the given\n        frequency. It counts from an epoch (e.g., for daily frequency,\n        ordinal 0 corresponds to January 1, 1970).\n\n        See Also\n        --------\n        Period.freq : Return the frequency of the Period.\n        Period.start_time : Return the start time of the Period.\n\n        Examples\n        --------\n        >>> period = pd.Period('2020-01', freq='M')\n        >>> period.ordinal\n        600\n\n        >>> period = pd.Period('2020-01-01', freq='D')\n        >>> period.ordinal\n        18262\n        ",
    '_Period.quarter.__get__ (line 2532)': "\n        Return the quarter this Period falls on.\n\n        See Also\n        --------\n        Timestamp.quarter : Return the quarter of the Timestamp.\n        Period.year : Return the year of the period.\n        Period.month : Return the month of the period.\n\n        Examples\n        --------\n        >>> period = pd.Period('2022-04', 'M')\n        >>> period.quarter\n        2\n        ",
    '_Period.qyear.__get__ (line 2552)': "\n        Fiscal year the Period lies in according to its starting-quarter.\n\n        The `year` and the `qyear` of the period will be the same if the fiscal\n        and calendar years are the same. When they are not, the fiscal year\n        can be different from the calendar year of the period.\n\n        Returns\n        -------\n        int\n            The fiscal year of the period.\n\n        See Also\n        --------\n        Period.year : Return the calendar year of the period.\n\n        Examples\n        --------\n        If the natural and fiscal year are the same, `qyear` and `year` will\n        be the same.\n\n        >>> per = pd.Period('2018Q1', freq='Q')\n        >>> per.qyear\n        2018\n        >>> per.year\n        2018\n\n        If the fiscal year starts in April (`Q-MAR`), the first quarter of\n        2018 will start in April 2017. `year` will then be 2017, but `qyear`\n        will be the fiscal year, 2018.\n\n        >>> per = pd.Period('2018Q1', freq='Q-MAR')\n        >>> per.start_time\n        Timestamp('2017-04-01 00:00:00')\n        >>> per.qyear\n        2018\n        >>> per.year\n        2017\n        ",
    '_Period.second.__get__ (line 2308)': '\n        Get the second component of the Period.\n\n        Returns\n        -------\n        int\n            The second of the Period (ranges from 0 to 59).\n\n        See Also\n        --------\n        Period.hour : Get the hour component of the Period.\n        Period.minute : Get the minute component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11 13:03:12.050000")\n        >>> p.second\n        12\n        ',
    '_Period.strftime (line 2751)': "\n        Returns a formatted string representation of the :class:`Period`.\n\n        ``fmt`` must be ``None`` or a string containing one or several directives.\n        When ``None``, the format will be determined from the frequency of the Period.\n        The method recognizes the same directives as the :func:`time.strftime`\n        function of the standard Python distribution, as well as the specific\n        additional directives ``%f``, ``%F``, ``%q``, ``%l``, ``%u``, ``%n``.\n        (formatting & docs originally from scikits.timeries).\n\n        +-----------+--------------------------------+-------+\n        | Directive | Meaning                        | Notes |\n        +===========+================================+=======+\n        | ``%a``    | Locale's abbreviated weekday   |       |\n        |           | name.                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%A``    | Locale's full weekday name.    |       |\n        +-----------+--------------------------------+-------+\n        | ``%b``    | Locale's abbreviated month     |       |\n        |           | name.                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%B``    | Locale's full month name.      |       |\n        +-----------+--------------------------------+-------+\n        | ``%c``    | Locale's appropriate date and  |       |\n        |           | time representation.           |       |\n        +-----------+--------------------------------+-------+\n        | ``%d``    | Day of the month as a decimal  |       |\n        |           | number [01,31].                |       |\n        +-----------+--------------------------------+-------+\n        | ``%f``    | 'Fiscal' year without a        | \\(1)  |\n        |           | century  as a decimal number   |       |\n        |           | [00,99]                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%F``    | 'Fiscal' year with a century   | \\(2)  |\n        |           | as a decimal number            |       |\n        +-----------+--------------------------------+-------+\n        | ``%H``    | Hour (24-hour clock) as a      |       |\n        |           | decimal number [00,23].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%I``    | Hour (12-hour clock) as a      |       |\n        |           | decimal number [01,12].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%j``    | Day of the year as a decimal   |       |\n        |           | number [001,366].              |       |\n        +-----------+--------------------------------+-------+\n        | ``%m``    | Month as a decimal number      |       |\n        |           | [01,12].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%M``    | Minute as a decimal number     |       |\n        |           | [00,59].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%p``    | Locale's equivalent of either  | \\(3)  |\n        |           | AM or PM.                      |       |\n        +-----------+--------------------------------+-------+\n        | ``%q``    | Quarter as a decimal number    |       |\n        |           | [1,4]                          |       |\n        +-----------+--------------------------------+-------+\n        | ``%S``    | Second as a decimal number     | \\(4)  |\n        |           | [00,61].                       |       |\n        +-----------+--------------------------------+-------+\n        | ``%l``    | Millisecond as a decimal number|       |\n        |           | [000,999].                     |       |\n        +-----------+--------------------------------+-------+\n        | ``%u``    | Microsecond as a decimal number|       |\n        |           | [000000,999999].               |       |\n        +-----------+--------------------------------+-------+\n        | ``%n``    | Nanosecond as a decimal number |       |\n        |           | [000000000,999999999].         |       |\n        +-----------+--------------------------------+-------+\n        | ``%U``    | Week number of the year        | \\(5)  |\n        |           | (Sunday as the first day of    |       |\n        |           | the week) as a decimal number  |       |\n        |           | [00,53].  All days in a new    |       |\n        |           | year preceding the first       |       |\n        |           | Sunday are considered to be in |       |\n        |           | week 0.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%w``    | Weekday as a decimal number    |       |\n        |           | [0(Sunday),6].                 |       |\n        +-----------+--------------------------------+-------+\n        | ``%W``    | Week number of the year        | \\(5)  |\n        |           | (Monday as the first day of    |       |\n        |           | the week) as a decimal number  |       |\n        |           | [00,53].  All days in a new    |       |\n        |           | year preceding the first       |       |\n        |           | Monday are considered to be in |       |\n        |           | week 0.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%x``    | Locale's appropriate date      |       |\n        |           | representation.                |       |\n        +-----------+--------------------------------+-------+\n        | ``%X``    | Locale's appropriate time      |       |\n        |           | representation.                |       |\n        +-----------+--------------------------------+-------+\n        | ``%y``    | Year without century as a      |       |\n        |           | decimal number [00,99].        |       |\n        +-----------+--------------------------------+-------+\n        | ``%Y``    | Year with century as a decimal |       |\n        |           | number.                        |       |\n        +-----------+--------------------------------+-------+\n        | ``%Z``    | Time zone name (no characters  |       |\n        |           | if no time zone exists).       |       |\n        +-----------+--------------------------------+-------+\n        | ``%%``    | A literal ``'%'`` character.   |       |\n        +-----------+--------------------------------+-------+\n\n        The `strftime` method provides a way to represent a :class:`Period`\n        object as a string in a specified format. This is particularly useful\n        when displaying date and time data in different locales or customized\n        formats, suitable for reports or user interfaces. It extends the standard\n        Python string formatting capabilities with additional directives specific\n        to `pandas`, accommodating features like fiscal years and precise\n        sub-second components.\n\n        Parameters\n        ----------\n        fmt : str or None\n            String containing the desired format directives. If ``None``, the\n            format is determined based on the Period's frequency.\n\n        See Also\n        --------\n        Timestamp.strftime : Return a formatted string of the Timestamp.\n        to_datetime : Convert argument to datetime.\n        time.strftime : Format a time object as a string according to a\n            specified format string in the standard Python library.\n\n        Notes\n        -----\n\n        (1)\n            The ``%f`` directive is the same as ``%y`` if the frequency is\n            not quarterly.\n            Otherwise, it corresponds to the 'fiscal' year, as defined by\n            the :attr:`qyear` attribute.\n\n        (2)\n            The ``%F`` directive is the same as ``%Y`` if the frequency is\n            not quarterly.\n            Otherwise, it corresponds to the 'fiscal' year, as defined by\n            the :attr:`qyear` attribute.\n\n        (3)\n            The ``%p`` directive only affects the output hour field\n            if the ``%I`` directive is used to parse the hour.\n\n        (4)\n            The range really is ``0`` to ``61``; this accounts for leap\n            seconds and the (very rare) double leap seconds.\n\n        (5)\n            The ``%U`` and ``%W`` directives are only used in calculations\n            when the day of the week and the year are specified.\n\n        Examples\n        --------\n\n        >>> from pandas import Period\n        >>> a = Period(freq='Q-JUL', year=2006, quarter=1)\n        >>> a.strftime('%F-Q%q')\n        '2006-Q1'\n        >>> # Output the last month in the quarter of this date\n        >>> a.strftime('%b-%Y')\n        'Oct-2005'\n        >>>\n        >>> a = Period(freq='D', year=2001, month=1, day=1)\n        >>> a.strftime('%d-%b-%Y')\n        '01-Jan-2001'\n        >>> a.strftime('%b. %d, %Y was a %A')\n        'Jan. 01, 2001 was a Monday'\n        ",
    '_Period.to_timestamp (line 2064)': "\n        Return the Timestamp representation of the Period.\n\n        Uses the target frequency specified at the part of the period specified\n        by `how`, which is either `Start` or `Finish`.\n\n        If possible, gives microsecond-unit Timestamp. Otherwise gives nanosecond\n        unit.\n\n        Parameters\n        ----------\n        freq : str or DateOffset\n            Target frequency. Default is 'D' if self._freq is week or\n            longer and 'S' otherwise.\n        how : str, default 'S' (start)\n            One of 'S', 'E'. Can be aliased as case insensitive\n            'Start', 'Finish', 'Begin', 'End'.\n\n        Returns\n        -------\n        Timestamp\n\n        See Also\n        --------\n        Timestamp : A class representing a single point in time.\n        Period : Represents a span of time with a fixed frequency.\n        PeriodIndex.to_timestamp : Convert a `PeriodIndex` to a `DatetimeIndex`.\n\n        Examples\n        --------\n        >>> period = pd.Period('2023-1-1', freq='D')\n        >>> timestamp = period.to_timestamp()\n        >>> timestamp\n        Timestamp('2023-01-01 00:00:00')\n        ",
    '_Period.week.__get__ (line 2363)': '\n        Get the week of the year on the given Period.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.dayofweek : Get the day component of the Period.\n        Period.weekday : Get the day component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", "h")\n        >>> p.week\n        10\n\n        >>> p = pd.Period("2018-02-01", "D")\n        >>> p.week\n        5\n\n        >>> p = pd.Period("2018-01-06", "D")\n        >>> p.week\n        1\n        ',
    '_Period.weekday.__get__ (line 2444)': "\n        Day of the week the period lies in, with Monday=0 and Sunday=6.\n\n        If the period frequency is lower than daily (e.g. hourly), and the\n        period spans over multiple days, the day at the start of the period is\n        used.\n\n        If the frequency is higher than daily (e.g. monthly), the last day\n        of the period is used.\n\n        Returns\n        -------\n        int\n            Day of the week.\n\n        See Also\n        --------\n        Period.dayofweek : Day of the week the period lies in.\n        Period.weekday : Alias of Period.dayofweek.\n        Period.day : Day of the month.\n        Period.dayofyear : Day of the year.\n\n        Examples\n        --------\n        >>> per = pd.Period('2017-12-31 22:00', 'h')\n        >>> per.dayofweek\n        6\n\n        For periods that span over multiple days, the day at the beginning of\n        the period is returned.\n\n        >>> per = pd.Period('2017-12-31 22:00', '4h')\n        >>> per.dayofweek\n        6\n        >>> per.start_time.dayofweek\n        6\n\n        For periods with a frequency higher than days, the last day of the\n        period is returned.\n\n        >>> per = pd.Period('2018-01', 'M')\n        >>> per.dayofweek\n        2\n        >>> per.end_time.dayofweek\n        2\n        ",
    '_Period.weekofyear.__get__ (line 2332)': '\n        Get the week of the year on the given Period.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        Period.dayofweek : Get the day component of the Period.\n        Period.weekday : Get the day component of the Period.\n\n        Examples\n        --------\n        >>> p = pd.Period("2018-03-11", "h")\n        >>> p.weekofyear\n        10\n\n        >>> p = pd.Period("2018-02-01", "D")\n        >>> p.weekofyear\n        5\n\n        >>> p = pd.Period("2018-01-06", "D")\n        >>> p.weekofyear\n        1\n        ',
    '_Period.year.__get__ (line 2130)': "\n        Return the year this Period falls on.\n\n        Returns\n        -------\n        int\n\n        See Also\n        --------\n        period.month : Get the month of the year for the given Period.\n        period.day : Return the day of the month the Period falls on.\n\n        Notes\n        -----\n        The year is based on the `ordinal` and `base` attributes of the Period.\n\n        Examples\n        --------\n        Create a Period object for January 2023 and get the year:\n\n        >>> period = pd.Period('2023-01', 'M')\n        >>> period.year\n        2023\n\n        Create a Period object for 01 January 2023 and get the year:\n\n        >>> period = pd.Period('2023', 'D')\n        >>> period.year\n        2023\n\n        Get the year for a period representing a quarter:\n\n        >>> period = pd.Period('2023Q2', 'Q')\n        >>> period.year\n        2023\n\n        Handle a case where the Period object is empty, which results in `NaN`:\n\n        >>> period = pd.Period('nan', 'M')\n        >>> period.year\n        nan\n        ",
}

