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

class MonthOffset(SingleConstructorOffset):
    # no doc
    def is_on_offset(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp intersects with this frequency.
        
                This method determines if a given timestamp aligns with the specific
                day of the month defined by this offset. For month-based offsets,
                it checks whether the timestamp's day matches the expected day
                according to the offset's configuration (e.g., start of month,
                end of month, or first/last business day).
        
                Parameters
                ----------
                dt : datetime
                    Timestamp to check intersection with frequency.
        
                Returns
                -------
                bool
                    True if the timestamp is on the offset, False otherwise.
        
                See Also
                --------
                tseries.offsets.MonthBegin : DateOffset of one month at beginning.
                tseries.offsets.MonthEnd : DateOffset of one month end.
                tseries.offsets.BusinessMonthBegin : DateOffset of one month at the first
                    business day.
                tseries.offsets.BusinessMonthEnd : DateOffset of one month at the last
                    business day.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> pd.offsets.MonthBegin().is_on_offset(ts)
                True
        
                >>> ts = pd.Timestamp(2022, 1, 15)
                >>> pd.offsets.MonthBegin().is_on_offset(ts)
                False
        
                >>> ts = pd.Timestamp(2022, 1, 31)
                >>> pd.offsets.MonthEnd().is_on_offset(ts)
                True
        """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56D9E0>'


