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

class YearOffset(SingleConstructorOffset):
    """ DateOffset that just needs a month. """
    def is_on_offset(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp intersects with this frequency.
        
                This method checks if a given datetime falls on a valid year
                boundary as defined by this offset.
        
                Parameters
                ----------
                dt : datetime
                    Timestamp to check intersections with frequency.
        
                Returns
                -------
                bool
                    True if the timestamp is on the offset, False otherwise.
        
                See Also
                --------
                YearEnd.is_on_offset : Check if a timestamp is at the end of a year.
                YearBegin.is_on_offset : Check if a timestamp is at the start of a year.
                BYearEnd.is_on_offset : Check if a timestamp is at the end of a
                    business year.
                BYearBegin.is_on_offset : Check if a timestamp is at the start of a
                    business year.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.YearBegin()
                >>> freq.is_on_offset(ts)
                True
        
                >>> freq = pd.offsets.BYearBegin()
                >>> freq.is_on_offset(ts)
                False
        
                >>> ts = pd.Timestamp(2022, 1, 3)
                >>> freq.is_on_offset(ts)
                True
        """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    def _get_offset_day(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the month of the year on which this offset applies.

        Returns an integer representing the month (1-12) that this offset
        targets. For year-based offsets, this determines which month is used
        for calculations.

        See Also
        --------
        tseries.offsets.YearEnd : Offset to end of year.
        tseries.offsets.YearBegin : Offset to start of year.
        tseries.offsets.BYearEnd : Offset to last business day of year.
        tseries.offsets.BYearBegin : Offset to first business day of year.

        Examples
        --------
        >>> pd.offsets.BYearBegin().month
        1

        >>> pd.offsets.BYearBegin(month=6).month
        6
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
        >>> pd.tseries.offsets.YearBegin(n=1, month=2).rule_code
        'YS-FEB'

        >>> pd.tseries.offsets.YearEnd(n=1, month=6).rule_code
        'YE-JUN'
        """

    _month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'month',
    )
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56C270>'


