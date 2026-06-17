# encoding: utf-8
# module matplotlib._image
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\matplotlib\_image.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


# functions

def resample(input_array, output_array, transform, interpolation, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    resample(input_array: numpy.ndarray, output_array: numpy.ndarray, transform: object, interpolation: matplotlib._image._InterpolationType = <_InterpolationType.NEAREST: 0>, resample: bool = False, alpha: typing.SupportsFloat | typing.SupportsIndex = 1, norm: bool = False, radius: typing.SupportsFloat | typing.SupportsIndex = 1) -> None
    
    Resample input_array, blending it in-place into output_array, using an affine transform.
    
    Parameters
    ----------
    input_array : 2-d or 3-d NumPy array of float, double or `numpy.uint8`
        If 2-d, the image is grayscale.  If 3-d, the image must be of size 4 in the last
        dimension and represents RGBA data.
    
    output_array : 2-d or 3-d NumPy array of float, double or `numpy.uint8`
        The dtype and number of dimensions must match `input_array`.
    
    transform : matplotlib.transforms.Transform instance
        The transformation from the input array to the output array.
    
    interpolation : int, default: NEAREST
        The interpolation method.  Must be one of the following constants defined in this
        module:
    
          NEAREST, BILINEAR, BICUBIC, SPLINE16, SPLINE36, HANNING, HAMMING, HERMITE, KAISER,
          QUADRIC, CATROM, GAUSSIAN, BESSEL, MITCHELL, SINC, LANCZOS, BLACKMAN
    
    resample : bool, optional
        When `True`, use a full resampling method.  When `False`, only resample when the
        output image is larger than the input image.
    
    alpha : float, default: 1
        The transparency level, from 0 (transparent) to 1 (opaque).
    
    norm : bool, default: False
        Whether to norm the interpolation function.
    
    radius: float, default: 1
        The radius of the kernel, if method is SINC, LANCZOS or BLACKMAN.
    """
    pass

# classes

class _InterpolationType(__pybind11_builtins.pybind11_object):
    """
    Members:
    
      NEAREST
    
      BILINEAR
    
      BICUBIC
    
      SPLINE16
    
      SPLINE36
    
      HANNING
    
      HAMMING
    
      HERMITE
    
      KAISER
    
      QUADRIC
    
      CATROM
    
      GAUSSIAN
    
      BESSEL
    
      MITCHELL
    
      SINC
    
      LANCZOS
    
      BLACKMAN
    """
    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, other, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __eq__(self: object, other: object, /) -> bool """
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __getstate__(self: object, /) -> int """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __hash__(self: object, /) -> int """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __index__(self: matplotlib._image._InterpolationType, /) -> int """
        pass

    def __init__(self, value, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __init__(self: matplotlib._image._InterpolationType, value: typing.SupportsInt | typing.SupportsIndex) -> None """
        pass

    def __int__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __int__(self: matplotlib._image._InterpolationType, /) -> int """
        pass

    def __ne__(self, other, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __ne__(self: object, other: object, /) -> bool """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __repr__(self: object, /) -> str """
        pass

    def __setstate__(self, state, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __setstate__(self: matplotlib._image._InterpolationType, state: typing.SupportsInt | typing.SupportsIndex, /) -> None """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __str__(self: object, /) -> str """
        pass

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """name(self: object, /) -> str
"""

    value = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    BESSEL = None # (!) forward: BESSEL, real value is '<_InterpolationType.BESSEL: 12>'
    BICUBIC = None # (!) forward: BICUBIC, real value is '<_InterpolationType.BICUBIC: 2>'
    BILINEAR = None # (!) forward: BILINEAR, real value is '<_InterpolationType.BILINEAR: 1>'
    BLACKMAN = None # (!) forward: BLACKMAN, real value is '<_InterpolationType.BLACKMAN: 16>'
    CATROM = None # (!) forward: CATROM, real value is '<_InterpolationType.CATROM: 10>'
    GAUSSIAN = None # (!) forward: GAUSSIAN, real value is '<_InterpolationType.GAUSSIAN: 11>'
    HAMMING = None # (!) forward: HAMMING, real value is '<_InterpolationType.HAMMING: 6>'
    HANNING = None # (!) forward: HANNING, real value is '<_InterpolationType.HANNING: 5>'
    HERMITE = None # (!) forward: HERMITE, real value is '<_InterpolationType.HERMITE: 7>'
    KAISER = None # (!) forward: KAISER, real value is '<_InterpolationType.KAISER: 8>'
    LANCZOS = None # (!) forward: LANCZOS, real value is '<_InterpolationType.LANCZOS: 15>'
    MITCHELL = None # (!) forward: MITCHELL, real value is '<_InterpolationType.MITCHELL: 13>'
    NEAREST = None # (!) forward: NEAREST, real value is '<_InterpolationType.NEAREST: 0>'
    QUADRIC = None # (!) forward: QUADRIC, real value is '<_InterpolationType.QUADRIC: 9>'
    SINC = None # (!) forward: SINC, real value is '<_InterpolationType.SINC: 14>'
    SPLINE16 = None # (!) forward: SPLINE16, real value is '<_InterpolationType.SPLINE16: 3>'
    SPLINE36 = None # (!) forward: SPLINE36, real value is '<_InterpolationType.SPLINE36: 4>'
    __entries = {
        'BESSEL': (
            None, # (!) forward: BESSEL, real value is '<_InterpolationType.BESSEL: 12>'
            None,
        ),
        'BICUBIC': (
            None, # (!) forward: BICUBIC, real value is '<_InterpolationType.BICUBIC: 2>'
            None,
        ),
        'BILINEAR': (
            None, # (!) forward: BILINEAR, real value is '<_InterpolationType.BILINEAR: 1>'
            None,
        ),
        'BLACKMAN': (
            None, # (!) forward: BLACKMAN, real value is '<_InterpolationType.BLACKMAN: 16>'
            None,
        ),
        'CATROM': (
            None, # (!) forward: CATROM, real value is '<_InterpolationType.CATROM: 10>'
            None,
        ),
        'GAUSSIAN': (
            None, # (!) forward: GAUSSIAN, real value is '<_InterpolationType.GAUSSIAN: 11>'
            None,
        ),
        'HAMMING': (
            None, # (!) forward: HAMMING, real value is '<_InterpolationType.HAMMING: 6>'
            None,
        ),
        'HANNING': (
            None, # (!) forward: HANNING, real value is '<_InterpolationType.HANNING: 5>'
            None,
        ),
        'HERMITE': (
            None, # (!) forward: HERMITE, real value is '<_InterpolationType.HERMITE: 7>'
            None,
        ),
        'KAISER': (
            None, # (!) forward: KAISER, real value is '<_InterpolationType.KAISER: 8>'
            None,
        ),
        'LANCZOS': (
            None, # (!) forward: LANCZOS, real value is '<_InterpolationType.LANCZOS: 15>'
            None,
        ),
        'MITCHELL': (
            None, # (!) forward: MITCHELL, real value is '<_InterpolationType.MITCHELL: 13>'
            None,
        ),
        'NEAREST': (
            None, # (!) forward: NEAREST, real value is '<_InterpolationType.NEAREST: 0>'
            None,
        ),
        'QUADRIC': (
            None, # (!) forward: QUADRIC, real value is '<_InterpolationType.QUADRIC: 9>'
            None,
        ),
        'SINC': (
            None, # (!) forward: SINC, real value is '<_InterpolationType.SINC: 14>'
            None,
        ),
        'SPLINE16': (
            None, # (!) forward: SPLINE16, real value is '<_InterpolationType.SPLINE16: 3>'
            None,
        ),
        'SPLINE36': (
            None, # (!) forward: SPLINE36, real value is '<_InterpolationType.SPLINE36: 4>'
            None,
        ),
    }
    __members__ = {
        'BESSEL': None, # (!) forward: BESSEL, real value is '<_InterpolationType.BESSEL: 12>'
        'BICUBIC': None, # (!) forward: BICUBIC, real value is '<_InterpolationType.BICUBIC: 2>'
        'BILINEAR': None, # (!) forward: BILINEAR, real value is '<_InterpolationType.BILINEAR: 1>'
        'BLACKMAN': None, # (!) forward: BLACKMAN, real value is '<_InterpolationType.BLACKMAN: 16>'
        'CATROM': None, # (!) forward: CATROM, real value is '<_InterpolationType.CATROM: 10>'
        'GAUSSIAN': None, # (!) forward: GAUSSIAN, real value is '<_InterpolationType.GAUSSIAN: 11>'
        'HAMMING': None, # (!) forward: HAMMING, real value is '<_InterpolationType.HAMMING: 6>'
        'HANNING': None, # (!) forward: HANNING, real value is '<_InterpolationType.HANNING: 5>'
        'HERMITE': None, # (!) forward: HERMITE, real value is '<_InterpolationType.HERMITE: 7>'
        'KAISER': None, # (!) forward: KAISER, real value is '<_InterpolationType.KAISER: 8>'
        'LANCZOS': None, # (!) forward: LANCZOS, real value is '<_InterpolationType.LANCZOS: 15>'
        'MITCHELL': None, # (!) forward: MITCHELL, real value is '<_InterpolationType.MITCHELL: 13>'
        'NEAREST': None, # (!) forward: NEAREST, real value is '<_InterpolationType.NEAREST: 0>'
        'QUADRIC': None, # (!) forward: QUADRIC, real value is '<_InterpolationType.QUADRIC: 9>'
        'SINC': None, # (!) forward: SINC, real value is '<_InterpolationType.SINC: 14>'
        'SPLINE16': None, # (!) forward: SPLINE16, real value is '<_InterpolationType.SPLINE16: 3>'
        'SPLINE36': None, # (!) forward: SPLINE36, real value is '<_InterpolationType.SPLINE36: 4>'
    }


# variables with complex values

BESSEL = None # (!) real value is '<_InterpolationType.BESSEL: 12>'

BICUBIC = None # (!) real value is '<_InterpolationType.BICUBIC: 2>'

BILINEAR = None # (!) real value is '<_InterpolationType.BILINEAR: 1>'

BLACKMAN = None # (!) real value is '<_InterpolationType.BLACKMAN: 16>'

CATROM = None # (!) real value is '<_InterpolationType.CATROM: 10>'

GAUSSIAN = None # (!) real value is '<_InterpolationType.GAUSSIAN: 11>'

HAMMING = None # (!) real value is '<_InterpolationType.HAMMING: 6>'

HANNING = None # (!) real value is '<_InterpolationType.HANNING: 5>'

HERMITE = None # (!) real value is '<_InterpolationType.HERMITE: 7>'

KAISER = None # (!) real value is '<_InterpolationType.KAISER: 8>'

LANCZOS = None # (!) real value is '<_InterpolationType.LANCZOS: 15>'

MITCHELL = None # (!) real value is '<_InterpolationType.MITCHELL: 13>'

NEAREST = None # (!) real value is '<_InterpolationType.NEAREST: 0>'

QUADRIC = None # (!) real value is '<_InterpolationType.QUADRIC: 9>'

SINC = None # (!) real value is '<_InterpolationType.SINC: 14>'

SPLINE16 = None # (!) real value is '<_InterpolationType.SPLINE16: 3>'

SPLINE36 = None # (!) real value is '<_InterpolationType.SPLINE36: 4>'

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017BE77E0A10>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._image', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000017BE77E0A10>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\_image.cp314-win_amd64.pyd')"

