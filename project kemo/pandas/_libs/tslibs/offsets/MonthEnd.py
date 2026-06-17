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


from .MonthOffset import MonthOffset

class MonthEnd(MonthOffset):
    """
    DateOffset of one month end.
    
        MonthEnd goes to the next date which is an end of the month.
    
        Attributes
        ----------
        n : int, default 1
            The number of months represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 30)
        >>> ts + pd.offsets.MonthEnd()
        Timestamp('2022-01-31 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 1, 31)
        >>> ts + pd.offsets.MonthEnd()
        Timestamp('2022-02-28 00:00:00')
    
        If you want to get the end of the current month:
    
        >>> ts = pd.Timestamp(2022, 1, 31)
        >>> pd.offsets.MonthEnd().rollforward(ts)
        Timestamp('2022-01-31 00:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'end'
    _period_dtype_code = 3000
    _prefix = 'ME'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56DB20>'


