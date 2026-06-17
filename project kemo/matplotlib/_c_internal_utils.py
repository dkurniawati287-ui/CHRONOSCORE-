# encoding: utf-8
# module matplotlib._c_internal_utils
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\matplotlib\_c_internal_utils.cp314-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# functions

def display_is_valid(): # real signature unknown; restored from __doc__
    """
    display_is_valid() -> bool
    
            --
            Check whether the current X11 or Wayland display is valid.
    
            On Linux, returns True if either $DISPLAY is set and XOpenDisplay(NULL)
            succeeds, or $WAYLAND_DISPLAY is set and wl_display_connect(NULL)
            succeeds.
    
            On other platforms, always returns True.
    """
    return False

def Win32_GetCurrentProcessExplicitAppUserModelID(): # real signature unknown; restored from __doc__
    """
    Win32_GetCurrentProcessExplicitAppUserModelID() -> object
    
            --
            Wrapper for Windows's GetCurrentProcessExplicitAppUserModelID.
    
            On non-Windows platforms, always returns None.
    """
    return object()

def Win32_GetForegroundWindow(): # real signature unknown; restored from __doc__
    """
    Win32_GetForegroundWindow() -> object
    
            --
            Wrapper for Windows' GetForegroundWindow.
    
            On non-Windows platforms, always returns None.
    """
    return object()

def Win32_SetCurrentProcessExplicitAppUserModelID(appid, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Win32_SetCurrentProcessExplicitAppUserModelID(appid: str, /) -> None
    
            --
            Wrapper for Windows's SetCurrentProcessExplicitAppUserModelID.
    
            On non-Windows platforms, does nothing.
    """
    pass

def Win32_SetForegroundWindow(hwnd): # real signature unknown; restored from __doc__
    """
    Win32_SetForegroundWindow(hwnd: types.CapsuleType) -> None
    
            --
            Wrapper for Windows' SetForegroundWindow.
    
            On non-Windows platforms, does nothing.
    """
    pass

def Win32_SetProcessDpiAwareness_max(): # real signature unknown; restored from __doc__
    """
    Win32_SetProcessDpiAwareness_max() -> None
    
            --
            Set Windows' process DPI awareness to best option available.
    
            On non-Windows platforms, does nothing.
    """
    pass

def xdisplay_is_valid(): # real signature unknown; restored from __doc__
    """
    xdisplay_is_valid() -> bool
    
            --
            Check whether the current X11 display is valid.
    
            On Linux, returns True if either $DISPLAY is set and XOpenDisplay(NULL)
            succeeds. Use this function if you need to specifically check for X11
            only (e.g., for Tkinter).
    
            On other platforms, always returns True.
    """
    return False

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000011A39689220>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._c_internal_utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000011A39689220>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\_c_internal_utils.cp314-win_amd64.pyd')"

