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


from .YearOffset import YearOffset

class BYearBegin(YearOffset):
    """
    DateOffset increments between the first business day of the year.
    
        Attributes
        ----------
        n : int, default 1
            The number of years represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        month : int, default 1
            A specific integer for the month of the year.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import BYearBegin
        >>> ts = pd.Timestamp('2020-05-24 05:01:15')
        >>> ts + BYearBegin()
        Timestamp('2021-01-01 05:01:15')
        >>> ts - BYearBegin()
        Timestamp('2020-01-01 05:01:15')
        >>> ts + BYearBegin(-1)
        Timestamp('2020-01-01 05:01:15')
        >>> ts + BYearBegin(2)
        Timestamp('2022-01-03 05:01:15')
        >>> ts + BYearBegin(month=11)
        Timestamp('2020-11-02 05:01:15')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'business_start'
    _default_month = 1
    _outputName = 'BusinessYearBegin'
    _prefix = 'BYS'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56C4F0>'


