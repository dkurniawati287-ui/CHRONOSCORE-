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


from .BusinessMixin import BusinessMixin

class _CustomBusinessMonth(BusinessMixin):
    # no doc
    def _apply(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    cbday_roll = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4FF5E21C0>'
    month_roll = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4FF48A380>'
    m_offset = None # (!) real value is '<pandas._libs.properties.CachedProperty object at 0x000001A4FF2DBE80>'
    _attributes = (
        'n',
        'normalize',
        'weekmask',
        'holidays',
        'calendar',
        'offset',
    )
    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF56FD30>'


