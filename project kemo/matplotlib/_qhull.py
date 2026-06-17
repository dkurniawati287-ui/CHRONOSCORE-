# encoding: utf-8
# module matplotlib._qhull
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\matplotlib\_qhull.cp314-win_amd64.pyd
# by generator 1.147
""" Computing Delaunay triangulations. """
# no imports

# functions

def delaunay(x, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    delaunay(x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], verbose: typing.SupportsInt | typing.SupportsIndex) -> tuple
    
    --
    
    Compute a Delaunay triangulation.
    
    Parameters
    ----------
    x, y : 1d arrays
        The coordinates of the point set, which must consist of at least
        three unique points.
    verbose : int
        Python's verbosity level.
    
    Returns
    -------
    triangles, neighbors : int arrays, shape (ntri, 3)
        Indices of triangle vertices and indices of triangle neighbors.
    """
    pass

def version(): # real signature unknown; restored from __doc__
    """
    version() -> str
    
    version()
    --
    
    Return the qhull version string.
    """
    return ""

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025CE2B3D7B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._qhull', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000025CE2B3D7B0>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\_qhull.cp314-win_amd64.pyd')"

