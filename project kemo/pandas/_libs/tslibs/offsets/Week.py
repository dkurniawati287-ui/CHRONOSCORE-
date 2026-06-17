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


from .SingleConstructorOffset import SingleConstructorOffset

class Week(SingleConstructorOffset):
    """
    Weekly offset.
    
        Attributes
        ----------
        n : int, default 1
            The number of weeks represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        weekday : int or None, default None
            Always generate specific day of week.
            0 for Monday and 6 for Sunday.
    
        See Also
        --------
        pd.tseries.offsets.WeekOfMonth :
         Describes monthly dates like, the Tuesday of the
         2nd week of each month.
    
        Examples
        --------
    
        >>> date_object = pd.Timestamp("2023-01-13")
        >>> date_object
        Timestamp('2023-01-13 00:00:00')
    
        >>> date_plus_one_week = date_object + pd.tseries.offsets.Week(n=1)
        >>> date_plus_one_week
        Timestamp('2023-01-20 00:00:00')
    
        >>> date_next_monday = date_object + pd.tseries.offsets.Week(weekday=0)
        >>> date_next_monday
        Timestamp('2023-01-16 00:00:00')
    
        >>> date_next_sunday = date_object + pd.tseries.offsets.Week(weekday=6)
        >>> date_next_sunday
        Timestamp('2023-01-15 00:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, n=1): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representing the base frequency.

        See Also
        --------
        tseries.offsets.Hour.name :
            Returns a string representing the base frequency of 'h'.
        tseries.offsets.Day.name :
            Returns a string representing the base frequency of 'D'.

        Examples
        --------
        >>> pd.offsets.Hour().rule_code
        'h'

        >>> pd.offsets.Week(5).rule_code
        'W'
        """

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the week on which the offset is applied.

        This is the weekday on which the weekly offset is anchored.
        The value is an integer representing the day of the week,
        where Monday is 0 and Sunday is 6, or None if no specific
        weekday is set.

        See Also
        --------
        Week : The weekly offset class.
        tseries.offsets.WeekOfMonth : Describes monthly dates like the Tuesday
            of the 2nd week of each month.

        Examples
        --------
        >>> pd.offsets.Week(weekday=0).weekday
        0

        >>> pd.offsets.Week(weekday=6).weekday
        6

        >>> pd.offsets.Week().weekday is None
        True
        """

    _period_dtype_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'weekday',
    )
    _inc = datetime.timedelta(days=7)
    _prefix = 'W'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56E750>'


