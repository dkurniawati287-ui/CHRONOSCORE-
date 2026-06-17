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

class Easter(SingleConstructorOffset):
    """
    DateOffset for the Easter holiday using logic defined in dateutil.
    
        Right now uses the revised method which is valid in years 1583-4099.
    
        Attributes
        ----------
        n : int, default 1
            The number of years represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        method : int, default 3
            The method used to calculate the date of Easter. Valid options are:
            - 1 (EASTER_JULIAN): Original calculation in Julian calendar
            - 2 (EASTER_ORTHODOX): Original method, date converted to Gregorian calendar
            - 3 (EASTER_WESTERN): Revised method, in Gregorian calendar
            These constants are defined in the `dateutil.easter` module.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.Easter()
        Timestamp('2022-04-17 00:00:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    method = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    EASTER_WESTERN = 3
    _attributes = (
        'n',
        'normalize',
        'method',
    )
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56F6A0>'


