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


from .SemiMonthOffset import SemiMonthOffset

class SemiMonthEnd(SemiMonthOffset):
    """
    Two DateOffset's per month repeating on the last day of the month & day_of_month.
    
        This offset allows for flexibility in generating date ranges or adjusting dates
        to the end of a month or a specific day in the month, such as the 15th or the last
        day of the month. It is useful for financial or scheduling applications where
        events occur bi-monthly.
    
        Attributes
        ----------
        n : int, default 1
            The number of months represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        day_of_month : int, {1, 3,...,27}, default 15
            A specific integer for the day of the month.
    
        See Also
        --------
        tseries.offsets.SemiMonthBegin : Offset for semi-monthly frequencies, starting at
            the beginning of the month.
        tseries.offsets.MonthEnd : Offset to the last calendar day of the month.
        tseries.offsets.MonthBegin : Offset to the first calendar day of the month.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 14)
        >>> ts + pd.offsets.SemiMonthEnd()
        Timestamp('2022-01-15 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 1, 15)
        >>> ts + pd.offsets.SemiMonthEnd()
        Timestamp('2022-01-31 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 1, 31)
        >>> ts + pd.offsets.SemiMonthEnd()
        Timestamp('2022-02-15 00:00:00')
    
        If you want to get the result for the current month:
    
        >>> ts = pd.Timestamp(2022, 1, 15)
        >>> pd.offsets.SemiMonthEnd().rollforward(ts)
        Timestamp('2022-01-15 00:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _min_day_of_month = 1
    _prefix = 'SME'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56E2F0>'


