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


from .HalfYearOffset import HalfYearOffset

class BHalfYearEnd(HalfYearOffset):
    """
    DateOffset increments between the last business day of each half-year.
    
        startingMonth = 1 corresponds to dates like 1/31/2007, 7/31/2007, ...
        startingMonth = 2 corresponds to dates like 2/28/2007, 8/31/2007, ...
        startingMonth = 6 corresponds to dates like 6/30/2007, 12/31/2007, ...
    
        Attributes
        ----------
        n : int, default 1
            The number of half-years represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        startingMonth : int, default 6
            A specific integer for the month of the year from which we start half-years.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import BHalfYearEnd
        >>> ts = pd.Timestamp('2020-05-24 05:01:15')
        >>> ts + BHalfYearEnd()
        Timestamp('2020-06-30 05:01:15')
        >>> ts + BHalfYearEnd(2)
        Timestamp('2020-12-31 05:01:15')
        >>> ts + BHalfYearEnd(1, startingMonth=2)
        Timestamp('2020-08-31 05:01:15')
        >>> ts + BHalfYearEnd(startingMonth=2)
        Timestamp('2020-08-31 05:01:15')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _day_opt = 'business_end'
    _default_starting_month = 6
    _from_name_starting_month = 12
    _output_name = 'BusinessHalfYearEnd'
    _prefix = 'BHYE'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56D3F0>'


