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

class Day(SingleConstructorOffset):
    """
    Offset ``n`` days.
    
        Attributes
        ----------
        n : int, default 1
            The number of days represented.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        You can use the parameter ``n`` to represent a shift of n days.
    
        >>> from pandas.tseries.offsets import Day
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts
        Timestamp('2022-12-09 15:00:00')
    
        >>> ts + Day()
        Timestamp('2022-12-10 15:00:00')
        >>> ts - Day(4)
        Timestamp('2022-12-05 15:00:00')
    
        >>> ts + Day(-4)
        Timestamp('2022-12-05 15:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    nanos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Returns an integer of the total number of nanoseconds.

        See Also
        --------
        tseries.offsets.Hour.nanos :
            Returns an integer of the total number of nanoseconds.
        tseries.offsets.Day.nanos :
            Returns an integer of the total number of nanoseconds.

        Examples
        --------
        >>> pd.offsets.Hour(5).nanos
        18000000000000
        """


    freqstr = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4FF5E1A40>'
    _adjust_dst = True
    _attributes = (
        'n',
        'normalize',
    )
    _creso = 4
    _nanos_inc = 86400000000000
    _period_dtype_code = 6000
    _prefix = 'D'


