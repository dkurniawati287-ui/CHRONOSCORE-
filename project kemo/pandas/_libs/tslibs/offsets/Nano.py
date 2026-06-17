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


from .Tick import Tick

class Nano(Tick):
    """
    Offset ``n`` nanoseconds.
    
        Attributes
        ----------
        n : int, default 1
            The number of nanoseconds represented.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        You can use the parameter ``n`` to represent a shift of n nanoseconds.
    
        >>> from pandas.tseries.offsets import Nano
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts
        Timestamp('2022-12-09 15:00:00')
    
        >>> ts + Nano(n=1000)
        Timestamp('2022-12-09 15:00:00.000001')
    
        >>> ts - Nano(n=1000)
        Timestamp('2022-12-09 14:59:59.999999')
    
        >>> ts + Nano(n=-1000)
        Timestamp('2022-12-09 14:59:59.999999')
    """
    def __init__(self, n=1000): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    _creso = 10
    _nanos_inc = 1
    _period_dtype_code = 12000
    _prefix = 'ns'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF562F70>'


