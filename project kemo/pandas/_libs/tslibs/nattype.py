# encoding: utf-8
# module pandas._libs.tslibs.nattype
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\tslibs\nattype.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\numpy\__init__.py
import datetime as __datetime


# Variables with simple values

iNaT = -9223372036854775808

# functions

def _make_error_func(*args, **kwargs): # real signature unknown
    pass

def _make_nan_func(*args, **kwargs): # real signature unknown
    pass

def _make_nat_func(*args, **kwargs): # real signature unknown
    pass

def _nat_unpickle(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle__NaT(*args, **kwargs): # real signature unknown
    pass

# classes

class _NaT(__datetime.datetime):
    # no doc
    def isoformat(self, *args, **kwargs): # real signature unknown
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

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
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

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __setstate_cython__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        pass

    asm8 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_leap_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_month_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_quarter_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_year_start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __array_priority__ = 100


class NaTType(_NaT):
    """
    (N)ot-(A)-(T)ime, the time equivalent of NaN.
    
        NaT is used to denote missing or null values in datetime and timedelta objects
        in pandas. It functions similarly to how NaN is used for numerical data.
        Operations with NaT will generally propagate the NaT value, similar to NaN.
        NaT can be used in pandas data structures like Series and DataFrame
        to represent missing datetime values. It is useful in data analysis
        and time series analysis when working with incomplete or sparse
        time-based data. Pandas provides robust handling of NaT to ensure
        consistency and reliability in computations involving datetime objects.
    
        See Also
        --------
        NA : NA ("not available") missing value indicator.
        isna : Detect missing values (NaN or NaT) in an array-like object.
        notna : Detect non-missing values.
        numpy.nan : Floating point representation of Not a Number (NaN) for numerical data.
    
        Examples
        --------
        >>> pd.DataFrame([pd.Timestamp("2023"), np.nan], columns=["col_1"])
                col_1
        0  2023-01-01
        1         NaT
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

    def combine(self, date, time): # real signature unknown; restored from __doc__
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

    def fromisocalendar(self, *args, **kwargs): # real signature unknown
        """
        int, int, int -> Construct a date from the ISO year, week number and weekday.
        
        This is the inverse of the date.isocalendar() function
        """
        pass

    def fromordinal(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def fromtimestamp(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def now(self): # real signature unknown; restored from __doc__
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

    def strptime(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
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

    def today(self): # real signature unknown; restored from __doc__
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

    def total_seconds(self): # real signature unknown; restored from __doc__
        """
        Total seconds in the duration.
        
                This method calculates the total duration in seconds by combining
                the days, seconds, and microseconds of the `Timedelta` object.
        
                See Also
                --------
                to_timedelta : Convert argument to timedelta.
                Timedelta : Represents a duration, the difference between two dates or times.
                Timedelta.seconds : Returns the seconds component of the timedelta.
                Timedelta.microseconds : Returns the microseconds component of the timedelta.
        
                Examples
                --------
                >>> td = pd.Timedelta('1min')
                >>> td
                Timedelta('0 days 00:01:00')
                >>> td.total_seconds()
                60.0
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

    def utcfromtimestamp(self, ts): # real signature unknown; restored from __doc__
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

    def utcnow(self): # real signature unknown; restored from __doc__
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

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    def __reduce_ex__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    day = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofweek = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dayofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    daysinmonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    days_in_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    day_of_week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    day_of_year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hour = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microsecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    microseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    millisecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    minute = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanosecond = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nanoseconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    quarter = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    second = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    seconds = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tz = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tzinfo = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekofyear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    year = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas.api.typing\', \'__doc__\': \'\\n    (N)ot-(A)-(T)ime, the time equivalent of NaN.\\n\\n    NaT is used to denote missing or null values in datetime and timedelta objects\\n    in pandas. It functions similarly to how NaN is used for numerical data.\\n    Operations with NaT will generally propagate the NaT value, similar to NaN.\\n    NaT can be used in pandas data structures like Series and DataFrame\\n    to represent missing datetime values. It is useful in data analysis\\n    and time series analysis when working with incomplete or sparse\\n    time-based data. Pandas provides robust handling of NaT to ensure\\n    consistency and reliability in computations involving datetime objects.\\n\\n    See Also\\n    --------\\n    NA : NA ("not available") missing value indicator.\\n    isna : Detect missing values (NaN or NaT) in an array-like object.\\n    notna : Detect non-missing values.\\n    numpy.nan : Floating point representation of Not a Number (NaN) for numerical data.\\n\\n    Examples\\n    --------\\n    >>> pd.DataFrame([pd.Timestamp("2023"), np.nan], columns=["col_1"])\\n            col_1\\n    0  2023-01-01\\n    1         NaT\\n    \', \'__new__\': <staticmethod(<cyfunction NaTType.__new__ at 0x00000108B7B928A0>)>, \'value\': <property object at 0x00000108B7BB8DB0>, \'__reduce_ex__\': <cyfunction NaTType.__reduce_ex__ at 0x00000108B7B92A80>, \'__reduce__\': <cyfunction NaTType.__reduce__ at 0x00000108B7B92B70>, \'__rtruediv__\': <cyfunction NaTType.__rtruediv__ at 0x00000108B7B92C60>, \'__rfloordiv__\': <cyfunction NaTType.__rfloordiv__ at 0x00000108B7B92D50>, \'__rmul__\': <cyfunction NaTType.__rmul__ at 0x00000108B7B92E40>, \'year\': <property object at 0x00000108B7BB8D60>, \'quarter\': <property object at 0x00000108B7BB8D10>, \'month\': <property object at 0x00000108B7BB8A40>, \'day\': <property object at 0x00000108B7BB9080>, \'hour\': <property object at 0x00000108B7BB90D0>, \'minute\': <property object at 0x00000108B7BB9120>, \'second\': <property object at 0x00000108B7BB9170>, \'millisecond\': <property object at 0x00000108B7BB91C0>, \'microsecond\': <property object at 0x00000108B7BB9210>, \'nanosecond\': <property object at 0x00000108B7BB9260>, \'week\': <property object at 0x00000108B7BB92B0>, \'dayofyear\': <property object at 0x00000108B7BB9300>, \'day_of_year\': <property object at 0x00000108B7BB9350>, \'weekofyear\': <property object at 0x00000108B7BB93A0>, \'days_in_month\': <property object at 0x00000108B7BB93F0>, \'daysinmonth\': <property object at 0x00000108B7BB9440>, \'dayofweek\': <property object at 0x00000108B7BB9490>, \'day_of_week\': <property object at 0x00000108B7BB94E0>, \'days\': <property object at 0x00000108B7BB9530>, \'seconds\': <property object at 0x00000108B7BB9580>, \'microseconds\': <property object at 0x00000108B7BB95D0>, \'nanoseconds\': <property object at 0x00000108B7BB9620>, \'qyear\': <property object at 0x00000108B7BB9670>, \'weekday\': <cyfunction _make_nan_func.<locals>.f at 0x00000108B7BC4500>, \'isoweekday\': <cyfunction _make_nan_func.<locals>.f at 0x00000108B7BC45F0>, \'total_seconds\': <cyfunction _make_nan_func.<locals>.f at 0x00000108B7BC46E0>, \'month_name\': <cyfunction _make_nan_func.<locals>.f at 0x00000108B7BC47D0>, \'day_name\': <cyfunction _make_nan_func.<locals>.f at 0x00000108B7BC48C0>, \'fromisocalendar\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC49B0>, \'isocalendar\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC4AA0>, \'dst\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC4B90>, \'date\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC4C80>, \'utctimetuple\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC4D70>, \'utcoffset\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC4E60>, \'tzname\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC4F50>, \'time\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC5040>, \'timetuple\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC5130>, \'timetz\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC5220>, \'toordinal\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC5310>, \'ctime\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC5400>, \'strftime\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC54F0>, \'strptime\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC55E0>, \'utcfromtimestamp\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC56D0>, \'fromtimestamp\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC57C0>, \'combine\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC58B0>, \'utcnow\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC59A0>, \'timestamp\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC5A90>, \'astimezone\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC5B80>, \'fromordinal\': <cyfunction _make_error_func.<locals>.f at 0x00000108B7BC5C70>, \'to_pydatetime\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC5D60>, \'now\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC5E50>, \'today\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC5F40>, \'round\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC6030>, \'floor\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC6120>, \'ceil\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC6210>, \'tz_convert\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC6300>, \'tz_localize\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC63F0>, \'replace\': <cyfunction _make_nat_func.<locals>.f at 0x00000108B7BC64E0>, \'tz\': <property object at 0x00000108B7BB96C0>, \'tzinfo\': <property object at 0x00000108B7BB9710>, \'as_unit\': <cyfunction NaTType.as_unit at 0x00000108B7BC67B0>, \'__dict__\': <attribute \'__dict__\' of \'NaTType\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'NaTType\' objects>})'


# variables with complex values

NaT = None # (!) real value is 'NaT'

nat_strings = None # (!) real value is "{'NaN', 'nan', 'NaT', 'NAT', 'NAN', 'nat'}"

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000108B7B8E510>'

__pyx_capi__ = {
    'NPY_NAT': None, # (!) real value is '<capsule object "__pyx_t_5numpy_int64_t" at 0x00000108B7BB84A0>'
    'c_NaT': None, # (!) real value is '<capsule object "struct __pyx_obj_6pandas_5_libs_6tslibs_7nattype__NaT *" at 0x00000108B7BB84F0>'
    'c_nat_strings': None, # (!) real value is '<capsule object "PyObject *" at 0x00000108B7BB8450>'
    'checknull_with_nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x00000108B7BB8540>'
    'is_dt64nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x00000108B7BB8590>'
    'is_td64nat': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x00000108B7BB85E0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslibs.nattype', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000108B7B8E510>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslibs\\\\nattype.cp314-win_amd64.pyd')"

__test__ = {
    'NaTType.as_unit (line 1843)': '\n        Convert the underlying int64 representation to the given unit.\n\n        Parameters\n        ----------\n        unit : {"ns", "us", "ms", "s"}\n        round_ok : bool, default True\n            If False and the conversion requires rounding, raise.\n\n        Returns\n        -------\n        Timestamp\n\n        See Also\n        --------\n        Timestamp.asm8 : Return numpy datetime64 format with same precision.\n        Timestamp.to_pydatetime : Convert Timestamp object to a native\n            Python datetime object.\n        to_timedelta : Convert argument into timedelta object,\n            which can represent differences in times.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(\'2023-01-01 00:00:00.01\')\n        >>> ts\n        Timestamp(\'2023-01-01 00:00:00.010000\')\n        >>> ts.unit\n        \'ms\'\n        >>> ts = ts.as_unit(\'s\')\n        >>> ts\n        Timestamp(\'2023-01-01 00:00:00\')\n        >>> ts.unit\n        \'s\'\n        ',
    '_NaT.to_datetime64 (line 230)': "\n        Return a NumPy datetime64 object with same precision.\n\n        This method returns a numpy.datetime64 object with the same\n        date and time information and precision as the pd.Timestamp object.\n\n        See Also\n        --------\n        numpy.datetime64 : Class to represent dates and times with high precision.\n        Timestamp.to_numpy : Alias for this method.\n        Timestamp.asm8 : Alias for this method.\n        pd.to_datetime : Convert argument to datetime.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp(year=2023, month=1, day=1,\n        ...                   hour=10, second=15)\n        >>> ts\n        Timestamp('2023-01-01 10:00:15')\n        >>> ts.to_datetime64()\n        numpy.datetime64('2023-01-01T10:00:15.000000')\n        ",
    '_NaT.to_numpy (line 255)': "\n        Convert the Timestamp to a NumPy datetime64.\n\n        This is an alias method for `Timestamp.to_datetime64()`. The dtype and\n        copy parameters are available here only for compatibility. Their values\n        will not affect the return value.\n\n        Parameters\n        ----------\n        dtype : dtype, optional\n            Data type of the output, ignored in this method as the return type\n            is always `numpy.datetime64`.\n        copy : bool, default False\n            Whether to ensure that the returned value is a new object. This\n            parameter is also ignored as the method does not support copying.\n\n        Returns\n        -------\n        numpy.datetime64\n\n        See Also\n        --------\n        DatetimeIndex.to_numpy : Similar method for DatetimeIndex.\n\n        Examples\n        --------\n        >>> ts = pd.Timestamp('2020-03-14T15:32:52.192548651')\n        >>> ts.to_numpy()\n        numpy.datetime64('2020-03-14T15:32:52.192548651')\n\n        Analogous for ``pd.NaT``:\n\n        >>> pd.NaT.to_numpy()\n        numpy.datetime64('NaT', 'ns')\n        ",
}

