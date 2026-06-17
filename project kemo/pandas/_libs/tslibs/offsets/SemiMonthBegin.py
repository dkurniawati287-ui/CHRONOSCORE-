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

class SemiMonthBegin(SemiMonthOffset):
    """
    Two DateOffset's per month repeating on the first day of the month & day_of_month.
    
        This offset moves dates to the first day of the month and an additional specified
        day (typically the 15th by default), useful in scenarios where bi-monthly processing
        occurs on set days.
    
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
        tseries.offsets.SemiMonthEnd : Two DateOffset's per month repeating on the last day
            of the month & day_of_month.
        tseries.offsets.MonthEnd : Offset to the last calendar day of the month.
        tseries.offsets.MonthBegin : Offset to the first calendar day of the month.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.SemiMonthBegin()
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

    _prefix = 'SMS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56E480>'


