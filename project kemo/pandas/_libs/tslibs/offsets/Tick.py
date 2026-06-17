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

class Tick(SingleConstructorOffset):
    """
    Base class for fixed frequency offsets (Milli, Micro, Second, Minute, Hour).
    
        This class should not be instantiated directly. Use one of the specific
        Tick subclasses for a concrete offset.
    
        Attributes
        ----------
        n : int, default 1
            The number of units (hours, minutes, etc.) the offset represents.
    
        See Also
        --------
        Hour : Offset ``n`` hours.
        Minute : Offset ``n`` minutes.
        Second : Offset ``n`` seconds.
        Milli : Offset ``n`` milliseconds.
        Micro : Offset ``n`` microseconds.
        Nano : Offset ``n`` nanoseconds.
    
        Examples
        --------
        >>> from pandas.tseries.offsets import Hour, Minute
        >>> ts = pd.Timestamp(2022, 12, 9, 15)
        >>> ts
        Timestamp('2022-12-09 15:00:00')
    
        >>> ts + Hour(1)
        Timestamp('2022-12-09 16:00:00')
    
        >>> ts + Minute(30)
        Timestamp('2022-12-09 15:30:00')
    """
    def is_on_offset(self, *args, **kwargs): # real signature unknown
        pass

    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def _next_higher_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
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


    _adjust_dst = False
    _as_pd_timedelta = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4FF5E1940>'
    _attributes = (
        'n',
        'normalize',
    )
    _prefix = 'undefined'
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF562570>'


