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

class BusinessDay(BusinessMixin):
    """
    DateOffset subclass representing possibly n business days.
    
        Parameters
        ----------
        n : int, default 1
            The number of days represented.
        normalize : bool, default False
            Normalize start/end dates to midnight.
        offset : timedelta, default timedelta(0)
            Time offset to apply.
    
        Examples
        --------
        You can use the parameter ``n`` to represent a shift of n business days.
    
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts.strftime('%a %d %b %Y %H:%M')
        'Fri 09 Dec 2022 15:00'
        >>> (ts + pd.offsets.BusinessDay(n=5)).strftime('%a %d %b %Y %H:%M')
        'Fri 16 Dec 2022 15:00'
    
        Passing the parameter ``normalize`` equal to True, you shift the start
        of the next business day to midnight.
    
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts + pd.offsets.BusinessDay(normalize=True)
        Timestamp('2022-12-12 00:00:00')
    """
    def is_on_offset(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp intersects with this frequency.
        
                This method determines if a given timestamp falls on a business day
                (Monday through Friday). If ``normalize`` is True, it also checks that
                the time component is midnight.
        
                Parameters
                ----------
                dt : datetime
                    Timestamp to check intersection with frequency.
        
                Returns
                -------
                bool
                    True if the timestamp is on a business day, False otherwise.
        
                See Also
                --------
                tseries.offsets.BusinessDay : Represents business day offset.
                tseries.offsets.CustomBusinessDay : Represents custom business day offset.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 8, 5)
                >>> ts.day_name()
                'Friday'
                >>> pd.offsets.BusinessDay().is_on_offset(ts)
                True
        
                >>> ts = pd.Timestamp(2022, 8, 6)
                >>> ts.day_name()
                'Saturday'
                >>> pd.offsets.BusinessDay().is_on_offset(ts)
                False
        
                With ``normalize=True``, the timestamp must also be at midnight:
        
                >>> ts = pd.Timestamp(2022, 8, 5, 12, 0)
                >>> pd.offsets.BusinessDay(normalize=True).is_on_offset(ts)
                False
                >>> ts = pd.Timestamp(2022, 8, 5, 0, 0)
                >>> pd.offsets.BusinessDay(normalize=True).is_on_offset(ts)
                True
        """
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def _offset_str(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, n=5): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    _attributes = (
        'n',
        'normalize',
        'offset',
    )
    _period_dtype_code = 5000
    _prefix = 'B'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF5637E0>'


