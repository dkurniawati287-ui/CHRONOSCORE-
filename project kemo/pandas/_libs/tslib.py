# encoding: utf-8
# module pandas._libs.tslib
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\tslib.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\numpy\__init__.py
from pandas._libs.tslibs.dtypes import Resolution

from pandas._libs.tslibs.vectorized import get_resolution

import datetime as __datetime
import pandas._libs.tslibs.timestamps as __pandas__libs_tslibs_timestamps


# functions

def array_to_datetime(*args, **kwargs): # real signature unknown
    """
    Converts a 1D array of date-like values to a numpy array of either:
            1) datetime64[ns] data
            2) datetime.datetime objects, if OutOfBoundsDatetime or TypeError
               is encountered
    
        Also returns a fixed-offset tzinfo object if an array of strings with the same
        timezone offset is passed and utc=True is not passed. Otherwise, None
        is returned
    
        Handles datetime.date, datetime.datetime, np.datetime64 objects, numeric,
        strings
    
        Parameters
        ----------
        values : ndarray of object
            date-like objects to convert
        errors : str, default 'raise'
            error behavior when parsing
        dayfirst : bool, default False
            dayfirst parsing behavior when encountering datetime strings
        yearfirst : bool, default False
            yearfirst parsing behavior when encountering datetime strings
        utc : bool, default False
            indicator whether the dates should be UTC
        creso : NPY_DATETIMEUNIT, default NPY_FR_GENERIC
            If NPY_FR_GENERIC, conduct inference.
        unit_for_numerics : str, default "ns"
    
        Returns
        -------
        np.ndarray
            May be datetime64[creso_unit] or object dtype
        tzinfo or None
    """
    pass

def array_to_datetime_with_tz(*args, **kwargs): # real signature unknown
    """
    Vectorized analogue to pd.Timestamp(value, tz=tz)
    
        values has object-dtype, unrestricted ndim.
    
        Major differences between this and array_to_datetime with utc=True
            - np.datetime64 objects are treated as _wall_ times.
            - tznaive datetimes are treated as _wall_ times.
    """
    pass

def first_non_null(*args, **kwargs): # real signature unknown
    """ Find position of first non-null value, return -1 if there isn't one. """
    pass

def format_array_from_datetime(*args, **kwargs): # real signature unknown
    """
    return an np object array of the string formatted values
    
        Parameters
        ----------
        values : ndarray[int64_t], arbitrary ndim
        tz : tzinfo or None, default None
        format : str or None, default None
              a strftime capable string
        na_rep : optional, default is None
              a nat format
        reso : NPY_DATETIMEUNIT, default NPY_FR_ns
    
        Returns
        -------
        np.ndarray[object]
    """
    pass

def _test_parse_iso8601(*args, **kwargs): # real signature unknown
    """
    TESTING ONLY: Parse string into Timestamp using iso8601 parser. Used
        only for testing, actual construction uses `convert_str_to_tsobject`
    """
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
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas\', \'__doc__\': "\\n    Pandas replacement for python datetime.datetime object.\\n\\n    Timestamp is the pandas equivalent of python\'s Datetime\\n    and is interchangeable with it in most cases. It\'s the type used\\n    for the entries that make up a DatetimeIndex, and other timeseries\\n    oriented data structures in pandas.\\n\\n    Parameters\\n    ----------\\n    ts_input : datetime-like, str, int, float\\n        Value to be converted to Timestamp.\\n    year : int\\n        Value of year.\\n    month : int\\n        Value of month.\\n    day : int\\n        Value of day.\\n    hour : int, optional, default 0\\n        Value of hour.\\n    minute : int, optional, default 0\\n        Value of minute.\\n    second : int, optional, default 0\\n        Value of second.\\n    microsecond : int, optional, default 0\\n        Value of microsecond.\\n    tzinfo : datetime.tzinfo, optional, default None\\n        Timezone info.\\n    nanosecond : int, optional, default 0\\n        Value of nanosecond.\\n    tz : str, zoneinfo.ZoneInfo, pytz.timezone, dateutil.tz.tzfile or None\\n        Time zone for time which Timestamp will have.\\n    unit : str\\n        Unit used for conversion if ts_input is of type int or float. The\\n        valid values are \'W\', \'D\', \'h\', \'m\', \'s\', \'ms\', \'us\', and \'ns\'. For\\n        example, \'s\' means seconds and \'ms\' means milliseconds.\\n\\n        For float inputs, the result will be stored in nanoseconds, and\\n        the unit attribute will be set as ``\'ns\'``.\\n    fold : {0, 1}, default None, keyword-only\\n        Due to daylight saving time, one wall clock time can occur twice\\n        when shifting from summer to winter time; fold describes whether the\\n        datetime-like corresponds  to the first (0) or the second time (1)\\n        the wall clock hits the ambiguous time.\\n\\n    See Also\\n    --------\\n    Timedelta : Represents a duration, the difference between two dates or times.\\n    datetime.datetime : Python datetime.datetime object.\\n\\n    Notes\\n    -----\\n    There are essentially three calling conventions for the constructor. The\\n    primary form accepts four parameters. They can be passed by position or\\n    keyword.\\n\\n    The other two forms mimic the parameters from ``datetime.datetime``. They\\n    can be passed by either position or keyword, but not both mixed together.\\n\\n    Examples\\n    --------\\n    Using the primary calling convention:\\n\\n    This converts a datetime-like string\\n\\n    >>> pd.Timestamp(\'2017-01-01T12\')\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    This converts a float representing a Unix epoch in units of seconds\\n\\n    >>> pd.Timestamp(1513393355.5, unit=\'s\')\\n    Timestamp(\'2017-12-16 03:02:35.500000\')\\n\\n    This converts an int representing a Unix-epoch in units of weeks\\n\\n    >>> pd.Timestamp(1535, unit=\'W\')\\n    Timestamp(\'1999-06-03 00:00:00\')\\n\\n    This converts an int representing a Unix-epoch in units of seconds\\n    and for a particular timezone\\n\\n    >>> pd.Timestamp(1513393355, unit=\'s\', tz=\'US/Pacific\')\\n    Timestamp(\'2017-12-15 19:02:35-0800\', tz=\'US/Pacific\')\\n\\n    Using the other two forms that mimic the API for ``datetime.datetime``:\\n\\n    >>> pd.Timestamp(2017, 1, 1, 12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n\\n    >>> pd.Timestamp(year=2017, month=1, day=1, hour=12)\\n    Timestamp(\'2017-01-01 12:00:00\')\\n    ", \'fromordinal\': <classmethod(<cyfunction Timestamp.fromordinal at 0x0000022F76E75C70>)>, \'now\': <classmethod(<cyfunction Timestamp.now at 0x0000022F76E75D60>)>, \'today\': <classmethod(<cyfunction Timestamp.today at 0x0000022F76E75E50>)>, \'utcnow\': <classmethod(<cyfunction Timestamp.utcnow at 0x0000022F76E75F40>)>, \'utcfromtimestamp\': <classmethod(<cyfunction Timestamp.utcfromtimestamp at 0x0000022F76E76030>)>, \'fromtimestamp\': <classmethod(<cyfunction Timestamp.fromtimestamp at 0x0000022F76E76120>)>, \'strftime\': <cyfunction Timestamp.strftime at 0x0000022F76E76210>, \'ctime\': <cyfunction Timestamp.ctime at 0x0000022F76E76300>, \'date\': <cyfunction Timestamp.date at 0x0000022F76E763F0>, \'dst\': <cyfunction Timestamp.dst at 0x0000022F76E764E0>, \'isocalendar\': <cyfunction Timestamp.isocalendar at 0x0000022F76E765D0>, \'tzname\': <cyfunction Timestamp.tzname at 0x0000022F76E766C0>, \'tzinfo\': <property object at 0x0000022F76DC3790>, \'utcoffset\': <cyfunction Timestamp.utcoffset at 0x0000022F76E768A0>, \'utctimetuple\': <cyfunction Timestamp.utctimetuple at 0x0000022F76E76990>, \'time\': <cyfunction Timestamp.time at 0x0000022F76E76A80>, \'timetuple\': <cyfunction Timestamp.timetuple at 0x0000022F76E76B70>, \'timetz\': <cyfunction Timestamp.timetz at 0x0000022F76E76C60>, \'toordinal\': <cyfunction Timestamp.toordinal at 0x0000022F76E76D50>, \'strptime\': <classmethod(<cyfunction Timestamp.strptime at 0x0000022F76E76E40>)>, \'combine\': <classmethod(<cyfunction Timestamp.combine at 0x0000022F76E76F30>)>, \'__new__\': <staticmethod(<cyfunction Timestamp.__new__ at 0x0000022F76E77020>)>, \'_round\': <cyfunction Timestamp._round at 0x0000022F76E77110>, \'round\': <cyfunction Timestamp.round at 0x0000022F76E77200>, \'floor\': <cyfunction Timestamp.floor at 0x0000022F76E772F0>, \'ceil\': <cyfunction Timestamp.ceil at 0x0000022F76E773E0>, \'tz\': <property object at 0x0000022F76DC36A0>, \'tz_localize\': <cyfunction Timestamp.tz_localize at 0x0000022F76E776B0>, \'tz_convert\': <cyfunction Timestamp.tz_convert at 0x0000022F76E777A0>, \'astimezone\': <cyfunction Timestamp.tz_convert at 0x0000022F76E777A0>, \'replace\': <cyfunction Timestamp.replace at 0x0000022F76E77890>, \'to_julian_date\': <cyfunction Timestamp.to_julian_date at 0x0000022F76E77980>, \'isoweekday\': <cyfunction Timestamp.isoweekday at 0x0000022F76E77A70>, \'weekday\': <cyfunction Timestamp.weekday at 0x0000022F76E77B60>, \'__dict__\': <attribute \'__dict__\' of \'Timestamp\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Timestamp\' objects>, \'_module_source\': \'pandas._libs.tslibs.timestamps\', \'weekofyear\': <attribute \'week\' of \'pandas._libs.tslibs.timestamps._Timestamp\' objects>, \'daysinmonth\': <attribute \'days_in_month\' of \'pandas._libs.tslibs.timestamps._Timestamp\' objects>})'


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


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022F772FA990>'

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs.tslib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022F772FA990>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\tslib.cp314-win_amd64.pyd')"

__test__ = {}

