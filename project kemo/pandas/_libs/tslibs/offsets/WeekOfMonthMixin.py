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

class WeekOfMonthMixin(SingleConstructorOffset):
    """ Mixin for methods common to WeekOfMonth and LastWeekOfMonth. """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representing the base frequency.

        See Also
        --------
        tseries.offsets.Hour.rule_code :
            Returns a string representing the base frequency of 'h'.
        tseries.offsets.Day.rule_code :
            Returns a string representing the base frequency of 'D'.

        Examples
        --------
        >>> pd.offsets.Week(5).rule_code
        'W'

        >>> pd.offsets.WeekOfMonth(n=1, week=0, weekday=0).rule_code
        'WOM-1MON'
        """

    week = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



