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


from ._YearEnd import _YearEnd

class YearEnd(_YearEnd):
    """
    DateOffset increments between calendar year end dates.
    
        YearEnd goes to the next date which is the end of the year.
    
        Parameters
        ----------
        n : int, default 1
            The number of years represented.
        normalize : bool, default False
            Normalize start/end dates to midnight before generating date range.
        month : int, default 12
            A specific integer for the month of the year.
    
        See Also
        --------
        :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.
    
        Examples
        --------
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.YearEnd()
        Timestamp('2022-12-31 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 12, 31)
        >>> ts + pd.offsets.YearEnd()
        Timestamp('2023-12-31 00:00:00')
    
        >>> ts = pd.Timestamp(2022, 1, 1)
        >>> ts + pd.offsets.YearEnd(month=2)
        Timestamp('2022-02-28 00:00:00')
    
        If you want to get the end of the current year:
    
        >>> ts = pd.Timestamp(2022, 12, 31)
        >>> pd.offsets.YearEnd().rollforward(ts)
        Timestamp('2022-12-31 00:00:00')
    """
    def __init__(self): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'pandas._libs.tslibs.offsets\', \'__doc__\': "\\n    DateOffset increments between calendar year end dates.\\n\\n    YearEnd goes to the next date which is the end of the year.\\n\\n    Parameters\\n    ----------\\n    n : int, default 1\\n        The number of years represented.\\n    normalize : bool, default False\\n        Normalize start/end dates to midnight before generating date range.\\n    month : int, default 12\\n        A specific integer for the month of the year.\\n\\n    See Also\\n    --------\\n    :class:`~pandas.tseries.offsets.DateOffset` : Standard kind of date increment.\\n\\n    Examples\\n    --------\\n    >>> ts = pd.Timestamp(2022, 1, 1)\\n    >>> ts + pd.offsets.YearEnd()\\n    Timestamp(\'2022-12-31 00:00:00\')\\n\\n    >>> ts = pd.Timestamp(2022, 12, 31)\\n    >>> ts + pd.offsets.YearEnd()\\n    Timestamp(\'2023-12-31 00:00:00\')\\n\\n    >>> ts = pd.Timestamp(2022, 1, 1)\\n    >>> ts + pd.offsets.YearEnd(month=2)\\n    Timestamp(\'2022-02-28 00:00:00\')\\n\\n    If you want to get the end of the current year:\\n\\n    >>> ts = pd.Timestamp(2022, 12, 31)\\n    >>> pd.offsets.YearEnd().rollforward(ts)\\n    Timestamp(\'2022-12-31 00:00:00\')\\n    ", \'__new__\': <staticmethod(<cyfunction YearEnd.__new__ at 0x000001A4FF640AA0>)>, \'__dict__\': <attribute \'__dict__\' of \'YearEnd\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'YearEnd\' objects>})'


