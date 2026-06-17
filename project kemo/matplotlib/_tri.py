# encoding: utf-8
# module matplotlib._tri
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\matplotlib\_tri.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


# no functions
# classes

class TrapezoidMapTriFinder(__pybind11_builtins.pybind11_object):
    # no doc
    def find_many(self, arg0, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        find_many(self: matplotlib._tri.TrapezoidMapTriFinder, arg0: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], arg1: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> numpy.typing.NDArray[numpy.int32]
        
        Find indices of triangles containing the point coordinates (x, y).
        """
        pass

    def get_tree_stats(self): # real signature unknown; restored from __doc__
        """
        get_tree_stats(self: matplotlib._tri.TrapezoidMapTriFinder) -> list
        
        Return statistics about the tree used by the trapezoid map.
        """
        return []

    def initialize(self): # real signature unknown; restored from __doc__
        """
        initialize(self: matplotlib._tri.TrapezoidMapTriFinder) -> None
        
        Initialize this object, creating the trapezoid map from the triangulation.
        """
        pass

    def print_tree(self): # real signature unknown; restored from __doc__
        """
        print_tree(self: matplotlib._tri.TrapezoidMapTriFinder) -> None
        
        Print the search tree as text to stdout; useful for debug purposes.
        """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, triangulation): # real signature unknown; restored from __doc__
        """
        __init__(self: matplotlib._tri.TrapezoidMapTriFinder, triangulation: matplotlib._tri.Triangulation) -> None
        
        Create a new C++ TrapezoidMapTriFinder object.
        This should not be called directly, use the python class
        matplotlib.tri.TrapezoidMapTriFinder instead.
        """
        pass


class Triangulation(__pybind11_builtins.pybind11_object):
    # no doc
    def calculate_plane_coefficients(self, arg0, numpy_typing_ArrayLike=None, numpy_float64=None): # real signature unknown; restored from __doc__
        """
        calculate_plane_coefficients(self: matplotlib._tri.Triangulation, arg0: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> numpy.typing.NDArray[numpy.float64]
        
        Calculate plane equation coefficients for all unmasked triangles.
        """
        pass

    def get_edges(self): # real signature unknown; restored from __doc__
        """
        get_edges(self: matplotlib._tri.Triangulation) -> numpy.typing.NDArray[numpy.int32]
        
        Return edges array.
        """
        pass

    def get_neighbors(self): # real signature unknown; restored from __doc__
        """
        get_neighbors(self: matplotlib._tri.Triangulation) -> numpy.typing.NDArray[numpy.int32]
        
        Return neighbors array.
        """
        pass

    def set_mask(self, arg0, numpy_typing_ArrayLike=None, numpy_bool=None): # real signature unknown; restored from __doc__
        """
        set_mask(self: matplotlib._tri.Triangulation, arg0: typing.Annotated[numpy.typing.ArrayLike, numpy.bool]) -> None
        
        Set or clear the mask array.
        """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, x, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__(self: matplotlib._tri.Triangulation, x: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], y: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], triangles: typing.Annotated[numpy.typing.ArrayLike, numpy.int32], mask: typing.Annotated[numpy.typing.ArrayLike, numpy.bool], edges: typing.Annotated[numpy.typing.ArrayLike, numpy.int32], neighbors: typing.Annotated[numpy.typing.ArrayLike, numpy.int32], correct_triangle_orientations: bool) -> None
        
        Create a new C++ Triangulation object.
        This should not be called directly, use the python class
        matplotlib.tri.Triangulation instead.
        """
        pass


class TriContourGenerator(__pybind11_builtins.pybind11_object):
    # no doc
    def create_contour(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        create_contour(self: matplotlib._tri.TriContourGenerator, arg0: typing.SupportsFloat | typing.SupportsIndex) -> tuple
        
        Create and return a non-filled contour.
        """
        pass

    def create_filled_contour(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        create_filled_contour(self: matplotlib._tri.TriContourGenerator, arg0: typing.SupportsFloat | typing.SupportsIndex, arg1: typing.SupportsFloat | typing.SupportsIndex) -> tuple
        
        Create and return a filled contour.
        """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, triangulation, z, numpy_typing_ArrayLike=None, numpy_float64=None): # real signature unknown; restored from __doc__
        """
        __init__(self: matplotlib._tri.TriContourGenerator, triangulation: matplotlib._tri.Triangulation, z: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> None
        
        Create a new C++ TriContourGenerator object.
        This should not be called directly, use the functions
        matplotlib.axes.tricontour and tricontourf instead.
        """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001627044D7B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._tri', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001627044D7B0>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\_tri.cp314-win_amd64.pyd')"

