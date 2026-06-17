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

class QuarterOffset(SingleConstructorOffset):
    # no doc
    def is_on_offset(self, ts): # real signature unknown; restored from __doc__
        """
        Return boolean whether a timestamp intersects with this frequency.
        
                This method checks if the given datetime falls on a quarter boundary
                as defined by the offset's ``startingMonth`` and day option.
        
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
                QuarterOffset : Parent class with quarterly offset logic.
        
                Examples
                --------
                >>> ts = pd.Timestamp(2022, 1, 1)
                >>> freq = pd.offsets.BQuarterBegin()
                >>> freq.is_on_offset(ts)
                False
                >>> ts = pd.Timestamp(2022, 3, 1)
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

        Returns
        -------
        str
            Rule code string with format 'PREFIX-MONTH', where PREFIX is the
            offset's frequency abbreviation and MONTH is the three-letter
            abbreviation of the starting month.

        See Also
        --------
        BQuarterBegin.rule_code : Rule code for business quarter begin offset.
        BQuarterEnd.rule_code : Rule code for business quarter end offset.
        QuarterBegin.rule_code : Rule code for quarter begin offset.
        QuarterEnd.rule_code : Rule code for quarter end offset.
        FY5253Quarter.get_rule_code_suffix : Suffix component of rule code for
            FY5253Quarter.
        FY5253.get_rule_code_suffix : Suffix component of rule code for FY5253.

        Examples
        --------
        Business quarter begin with different starting months:

        >>> bqb = pd.offsets.BQuarterBegin(startingMonth=1)
        >>> bqb.rule_code
        'BQS-JAN'

        >>> bqb = pd.offsets.BQuarterBegin(startingMonth=2)
        >>> bqb.rule_code
        'BQS-FEB'

        >>> bqb = pd.offsets.BQuarterBegin(startingMonth=3)
        >>> bqb.rule_code
        'BQS-MAR'

        Business quarter end with different starting months:

        >>> bqe = pd.offsets.BQuarterEnd(startingMonth=1)
        >>> bqe.rule_code
        'BQE-JAN'

        >>> bqe = pd.offsets.BQuarterEnd(startingMonth=12)
        >>> bqe.rule_code
        'BQE-DEC'

        Quarter begin with different starting months:

        >>> qb = pd.offsets.QuarterBegin(startingMonth=1)
        >>> qb.rule_code
        'QS-JAN'

        >>> qb = pd.offsets.QuarterBegin(startingMonth=3)
        >>> qb.rule_code
        'QS-MAR'

        Quarter end with different starting months:

        >>> qe = pd.offsets.QuarterEnd(startingMonth=1)
        >>> qe.rule_code
        'QE-JAN'

        >>> qe = pd.offsets.QuarterEnd(startingMonth=3)
        >>> qe.rule_code
        'QE-MAR'
        """

    startingMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the month of the year from which quarters start.

        This value determines which month marks the beginning of a quarterly period.
        For example, with startingMonth=1, quarters start in January, April, July,
        and October.

        See Also
        --------
        QuarterOffset.rule_code : Return the rule code for the quarter offset.
        HalfYearOffset.startingMonth : Similar property for half-year-based offsets.

        Examples
        --------
        >>> pd.offsets.BQuarterBegin().startingMonth
        3

        >>> pd.offsets.QuarterEnd().startingMonth
        3

        >>> pd.offsets.QuarterBegin(startingMonth=1).startingMonth
        1
        """

    _startingMonth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _attributes = (
        'n',
        'normalize',
        'startingMonth',
    )
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56CA90>'


