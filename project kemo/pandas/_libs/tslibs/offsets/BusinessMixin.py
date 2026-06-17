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

class BusinessMixin(SingleConstructorOffset):
    """ Mixin to business types to provide related functions. """
    def _init_custom(self, *args, **kwargs): # real signature unknown
        """ Additional __init__ for Custom subclasses. """
        pass

    def _repr_attrs(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    calendar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the calendar used for business day calculations.

        This property returns the numpy busdaycalendar object used for
        determining valid business days. For standard business day offsets
        (e.g., BusinessDay, BusinessHour), this returns None. For custom
        business day offsets, this returns the calendar that was either
        passed directly or constructed from weekmask and holidays.

        Returns
        -------
        np.busdaycalendar or None
            The business day calendar used for calculations, or None if
            using default business day rules.

        See Also
        --------
        BusinessDay.holidays : Holidays for standard business day offset.
        CustomBusinessDay.holidays : Holidays for custom business day offset.
        CustomBusinessDay.weekmask : Weekmask for custom business day offset.

        Examples
        --------
        For standard business offsets, calendar is None:

        >>> bd = pd.offsets.BusinessDay()
        >>> bd.calendar is None
        True

        >>> bh = pd.offsets.BusinessHour()
        >>> bh.calendar is None
        True

        For custom business day with explicit holidays:

        >>> holidays = [pd.Timestamp("2023-12-25"), pd.Timestamp("2024-01-01")]
        >>> cbd = pd.offsets.CustomBusinessDay(holidays=holidays)
        >>> isinstance(cbd.calendar, np.busdaycalendar)
        True
        """

    holidays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the holidays used for custom business day calculations.

        This property returns a tuple or list of holidays used when calculating
        business days for custom business day offsets. For non-custom business
        offsets (e.g., standard BusinessDay, BusinessHour), this will be None.

        Returns
        -------
        tuple, list, or None
            Holidays used in business day calculations, or None if no custom
            holidays are specified.

        See Also
        --------
        BusinessDay.holidays : Holidays for standard business day offset.
        BusinessHour.holidays : Holidays for standard business hour offset.
        CustomBusinessDay.holidays : Holidays for custom business day offset.
        CustomBusinessHour.holidays : Holidays for custom business hour offset.
        CustomBusinessMonthEnd.holidays : Holidays for custom business month end offset.
        CustomBusinessMonthBegin.holidays : Holidays for custom business month begin
            offset.
        CustomBusinessDay.weekmask : Weekmask for custom business day offset.
        CustomBusinessDay.calendar : Calendar for custom business day offset.

        Examples
        --------
        For standard business offsets, holidays is None:

        >>> bd = pd.offsets.BusinessDay()
        >>> bd.holidays is None
        True

        >>> bh = pd.offsets.BusinessHour()
        >>> bh.holidays is None
        True

        For custom business day with explicit holidays:

        >>> holidays = [pd.Timestamp("2023-12-25"), pd.Timestamp("2024-01-01")]
        >>> cbd = pd.offsets.CustomBusinessDay(holidays=holidays)
        >>> cbd.holidays  # doctest: +SKIP
        (Timestamp('2023-12-25 00:00:00'), Timestamp('2024-01-01 00:00:00'))

        For custom business hour with explicit holidays:

        >>> cbh = pd.offsets.CustomBusinessHour(holidays=holidays)
        >>> cbh.holidays  # doctest: +SKIP
        (Timestamp('2023-12-25 00:00:00'), Timestamp('2024-01-01 00:00:00'))

        For custom business month end with explicit holidays:

        >>> cbme = pd.offsets.CustomBusinessMonthEnd(holidays=holidays)
        >>> cbme.holidays  # doctest: +SKIP
        (Timestamp('2023-12-25 00:00:00'), Timestamp('2024-01-01 00:00:00'))

        For custom business month begin with explicit holidays:

        >>> cbmb = pd.offsets.CustomBusinessMonthBegin(holidays=holidays)
        >>> cbmb.holidays  # doctest: +SKIP
        (Timestamp('2023-12-25 00:00:00'), Timestamp('2024-01-01 00:00:00'))

        For custom business offsets with a calendar:

        >>> from pandas.tseries.holiday import USFederalHolidayCalendar
        >>> cal = USFederalHolidayCalendar()
        >>> cbd_cal = pd.offsets.CustomBusinessDay(calendar=cal)
        >>> isinstance(cbd_cal.holidays, tuple)
        True

        >>> cbh_cal = pd.offsets.CustomBusinessHour(calendar=cal)
        >>> isinstance(cbh_cal.holidays, tuple)
        True
        """

    offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Alias for self._offset.
        """

    weekmask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """
        Return the weekmask used for custom business day calculations.

        This property returns the weekmask string that defines which days of the
        week are considered business days. For non-custom business offsets (e.g.,
        standard BusinessDay, BusinessHour), this will be None. For custom business
        day offsets, this returns the weekmask that was specified or the default
        'Mon Tue Wed Thu Fri'.

        Returns
        -------
        str or None
            String representing valid business days (e.g., 'Mon Tue Wed Thu Fri'),
            or None if using default business day rules.

        See Also
        --------
        BusinessDay.holidays : Holidays for standard business day offset.
        CustomBusinessDay.holidays : Holidays for custom business day offset.
        CustomBusinessDay.calendar : Calendar for custom business day offset.

        Examples
        --------
        For standard business offsets, weekmask is None:

        >>> bd = pd.offsets.BusinessDay()
        >>> bd.weekmask is None
        True

        >>> bh = pd.offsets.BusinessHour()
        >>> bh.weekmask is None
        True

        For custom business day with default weekmask:

        >>> cbd = pd.offsets.CustomBusinessDay()
        >>> cbd.weekmask
        'Mon Tue Wed Thu Fri'

        For custom business day with custom weekmask:

        >>> cbd = pd.offsets.CustomBusinessDay(weekmask="Mon Wed Fri")
        >>> cbd.weekmask
        'Mon Wed Fri'
        """

    _calendar = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _holidays = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _offset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _weekmask = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000001A4FF563560>'


