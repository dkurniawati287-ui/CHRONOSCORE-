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

class HalfYearOffset(SingleConstructorOffset):
    # no doc
    def is_on_offset(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp intersects with this frequency.
        
                This method checks if a given datetime falls on a valid half-year
                boundary as defined by this offset.
        
                Parameters
                ----------
                dt : datetime
                    Timestamp to check intersections with frequency.
        
                Returns
                -------
                bool
                    True if the timestamp is on the offset, False otherwise.
        
                See Also
                --------
                HalfYearEnd.is_on_offset : Check if a timestamp is at the end of a
                    half-year.
                HalfYearBegin.is_on_offset : Check if a timestamp is at the start of a
                    half-year.
                BHalfYearEnd.is_on_offset : Check if a timestamp is at the end of a
                    business half-year.
                BHalfYearBegin.is_on_offset : Check if a timestamp is at the start of a
                    business half-year.
        
                Examples
                --------
                >>> freq = pd.offsets.BHalfYearBegin()
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq.is_on_offset(ts)
                False
        
                >>> ts = pd.Timestamp(2022, 1, 3)
                >>> freq.is_on_offset(ts)
                True
        """
        pass

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

    rule_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return a string representing the frequency with month suffix.

        This property generates a rule code string that combines the offset's
        prefix with the abbreviated month name of the starting month.

        See Also
        --------
        FY5253Quarter.get_rule_code_suffix : Return the suffix component of the rule
            code for FY5253Quarter.
        FY5253.get_rule_code_suffix : Return the suffix component of the rule code for
            FY5253.

        Examples
        --------
        >>> offset = pd.offsets.BHalfYearEnd(startingMonth=6)
        >>> offset.rule_code
        'BHYE-JUN'
        """

    startingMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the month of the year from which half-years start.

        This value determines which month marks the beginning of a half-year period.
        For example, with startingMonth=1, half-years start in January and July.

        See Also
        --------
        HalfYearOffset.rule_code : Return the rule code for the half-year offset.
        QuarterOffset.startingMonth : Similar property for quarter-based offsets.

        Examples
        --------
        >>> pd.offsets.BHalfYearBegin().startingMonth
        1

        >>> pd.offsets.BHalfYearEnd().startingMonth
        6

        >>> pd.offsets.HalfYearBegin(startingMonth=3).startingMonth
        3
        """

    _startingMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'startingMonth',
    )
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56D2B0>'


