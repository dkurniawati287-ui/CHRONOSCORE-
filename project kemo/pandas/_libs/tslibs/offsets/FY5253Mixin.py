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

class FY5253Mixin(SingleConstructorOffset):
    # no doc
    def get_rule_code_suffix(self): # real signature unknown; restored from __doc__
        """
        Return the suffix component of the rule code.
        
                The suffix combines the variation prefix, starting month abbreviation,
                and weekday abbreviation into a string format.
        
                Returns
                -------
                str
                    Suffix string in the format "{variation}-{month}-{weekday}".
                    The variation is "N" for nearest or "L" for last.
        
                See Also
                --------
                FY5253.rule_code : Return the complete rule code string.
                FY5253Quarter.rule_code : Return the complete rule code string for
                    FY5253Quarter.
        
                Examples
                --------
                >>> offset = pd.offsets.FY5253(weekday=4, startingMonth=12, variation="nearest")
                >>> offset.get_rule_code_suffix()
                'N-DEC-FRI'
        
                >>> offset = pd.offsets.FY5253(weekday=0, startingMonth=1, variation="last")
                >>> offset.get_rule_code_suffix()
                'L-JAN-MON'
        """
        pass

    def _get_suffix_prefix(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    startingMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    variation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the weekday used by the fiscal year.

        This is the day of the week on which the fiscal year ends.
        The value is an integer from 0 (Monday) to 6 (Sunday).

        See Also
        --------
        FY5253.startingMonth : Return the starting month of the fiscal year.
        FY5253.variation : Return the variation of the fiscal year.

        Examples
        --------
        >>> offset = pd.offsets.FY5253(weekday=4, startingMonth=12, variation="nearest")
        >>> offset.weekday
        4
        """

    _weekday = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56EDE0>'


