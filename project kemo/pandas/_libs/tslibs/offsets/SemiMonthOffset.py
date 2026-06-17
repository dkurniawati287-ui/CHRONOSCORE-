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

class SemiMonthOffset(SingleConstructorOffset):
    # no doc
    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _apply_array(self, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def _from_name(cls, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    day_of_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the day of the month for the semi-monthly offset.

        This specifies the day of the month on which the offset falls,
        in addition to the start (1st) or end (last day) of the month.

        See Also
        --------
        SemiMonthBegin : Offset at the start of the month and mid-month.
        SemiMonthEnd : Offset at mid-month and end of month.

        Examples
        --------
        >>> pd.offsets.SemiMonthBegin().day_of_month
        15

        >>> pd.offsets.SemiMonthBegin(day_of_month=20).day_of_month
        20
        """

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _day_of_month = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'day_of_month',
    )
    _default_day_of_month = 15
    _min_day_of_month = 2
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56E160>'


