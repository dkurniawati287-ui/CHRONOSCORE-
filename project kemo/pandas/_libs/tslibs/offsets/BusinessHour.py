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


from .BusinessMixin import BusinessMixin

class BusinessHour(BusinessMixin):
    """
    DateOffset subclass representing possibly n business hours.
    
        Parameters
        ----------
        n : int, default 1
            The number of hours represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        start : str, time, or list of str/time, default "09:00"
            Start time of your custom business hour in 24h format.
        end : str, time, or list of str/time, default: "17:00"
            End time of your custom business hour in 24h format.
        offset : timedelta, default timedelta(0)
            Time offset to apply.
    
        Examples
        --------
        You can use the parameter ``n`` to represent a shift of n hours.
    
        >>> ts = pd.Timestamp(2022, 12, 9, 8)
        >>> ts + pd.offsets.BusinessHour(n=5)
        Timestamp('2022-12-09 14:00:00')
    
        You can also change the start and the end of business hours.
    
        >>> ts = pd.Timestamp(2022, 8, 5, 16)
        >>> ts + pd.offsets.BusinessHour(start="11:00")
        Timestamp('2022-08-08 11:00:00')
    
        >>> from datetime import time as dt_time
        >>> ts = pd.Timestamp(2022, 8, 5, 22)
        >>> ts + pd.offsets.BusinessHour(end=dt_time(19, 0))
        Timestamp('2022-08-08 10:00:00')
    
        Passing the parameter ``normalize`` equal to True, you shift the start
        of the next business hour to midnight.
    
        >>> ts = pd.Timestamp(2022, 12, 9, 8)
        >>> ts + pd.offsets.BusinessHour(normalize=True)
        Timestamp('2022-12-09 00:00:00')
    
        You can divide your business day hours into several parts.
    
        >>> import datetime as dt
        >>> freq = pd.offsets.BusinessHour(start=["06:00", "10:00", "15:00"],
        ...                                end=["08:00", "12:00", "17:00"])
        >>> pd.date_range(dt.datetime(2022, 12, 9), dt.datetime(2022, 12, 13), freq=freq)
        DatetimeIndex(['2022-12-09 06:00:00', '2022-12-09 07:00:00',
                       '2022-12-09 10:00:00', '2022-12-09 11:00:00',
                       '2022-12-09 15:00:00', '2022-12-09 16:00:00',
                       '2022-12-12 06:00:00', '2022-12-12 07:00:00',
                       '2022-12-12 10:00:00', '2022-12-12 11:00:00',
                       '2022-12-12 15:00:00', '2022-12-12 16:00:00'],
                       dtype='datetime64[ns]', freq='bh')
    """
    def is_on_offset(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp intersects with this frequency.
        
                This method determines if a given timestamp falls within business hours.
                Business hours are defined by the ``start`` and ``end`` parameters
                (default 09:00 to 17:00). The timestamp must also fall on a business day
                (Monday through Friday). If ``normalize`` is True, it also checks that
                the time component is midnight.
        
                Parameters
                ----------
                dt : datetime
                    Timestamp to check intersection with frequency.
        
                Returns
                -------
                bool
                    True if the timestamp is within business hours, False otherwise.
        
                See Also
                --------
                tseries.offsets.BusinessHour : Represents business hour offset.
                tseries.offsets.BusinessDay.is_on_offset : Check if a timestamp is on
                    a business day.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 8, 5, 10)
                >>> ts.day_name()
                'Friday'
                >>> pd.offsets.BusinessHour().is_on_offset(ts)
                True
        
                >>> ts = pd.Timestamp(2022, 8, 5, 20)
                >>> pd.offsets.BusinessHour().is_on_offset(ts)
                False
        
                >>> ts = pd.Timestamp(2022, 8, 6, 10)
                >>> ts.day_name()
                'Saturday'
                >>> pd.offsets.BusinessHour().is_on_offset(ts)
                False
        """
        pass

    def rollback(self, *args, **kwargs): # real signature unknown
        """ Roll provided date backward to next offset only if not on offset. """
        pass

    def rollforward(self, *args, **kwargs): # real signature unknown
        """ Roll provided date forward to next offset only if not on offset. """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _get_business_hours_by_sec(self, *args, **kwargs): # real signature unknown
        """ Return business hours in a day by seconds. """
        pass

    def _get_closing_time(self, *args, **kwargs): # real signature unknown
        """
        Get the closing time of a business hour interval by its opening time.
        
                Parameters
                ----------
                dt : datetime
                    Opening time of a business hour interval.
        
                Returns
                -------
                result : datetime
                    Corresponding closing time.
        """
        pass

    def _is_on_offset(self, *args, **kwargs): # real signature unknown
        """ Slight speedups using calculated values. """
        pass

    def _next_opening_time(self, *args, **kwargs): # real signature unknown
        """
        If self._n and sign have the same sign, return the earliest opening time
                later than or equal to current time.
                Otherwise the latest opening time earlier than or equal to current
                time.
        
                Opening time always locates on BusinessDay.
                However, closing time may not if business hour extends over midnight.
        
                Parameters
                ----------
                other : datetime
                    Current time.
                sign : int, default 1.
                    Either 1 or -1. Going forward in time if it has the same sign as
                    self._n. Going backward in time otherwise.
        
                Returns
                -------
                result : datetime
                    Next opening time.
        """
        pass

    def _prev_opening_time(self, *args, **kwargs): # real signature unknown
        """
        If n is positive, return the latest opening time earlier than or equal
                to current time.
                Otherwise the earliest opening time later than or equal to current
                time.
        
                Parameters
                ----------
                other : datetime
                    Current time.
        
                Returns
                -------
                result : datetime
                    Previous opening time.
        """
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, n=5): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the end time(s) of the business hour.

        This property returns a tuple of `datetime.time` objects representing
        the end times of business hours.

        See Also
        --------
        BusinessHour.start : Return the start time(s) of the business hour.
        CustomBusinessHour.start : Return the start time(s) of the custom business hour.

        Examples
        --------
        >>> pd.offsets.BusinessHour().end
        (datetime.time(17, 0),)
        """

    start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the start time(s) of the business hour.

        This property returns a tuple of `datetime.time` objects representing
        the start times of business hours.

        See Also
        --------
        BusinessHour.end : Return the end time(s) of the business hour.
        CustomBusinessHour.end : Return the end time(s) of the custom business hour.

        Examples
        --------
        >>> pd.offsets.BusinessHour().start
        (datetime.time(9, 0),)
        """

    _end = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _start = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    next_bday = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4FF5E1F40>'
    _adjust_dst = False
    _anchor = 0
    _attributes = (
        'n',
        'normalize',
        'start',
        'end',
        'offset',
    )
    _prefix = 'bh'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF563CE0>'


