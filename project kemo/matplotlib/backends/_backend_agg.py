# encoding: utf-8
# module matplotlib.backends._backend_agg
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\matplotlib\backends\_backend_agg.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import pybind11_builtins as __pybind11_builtins


# no functions
# classes

class BufferRegion(__pybind11_builtins.pybind11_object):
    # no doc
    def get_extents(self): # real signature unknown; restored from __doc__
        """ get_extents(self: matplotlib.backends._backend_agg.BufferRegion) -> object """
        return object()

    def set_x(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ set_x(self: matplotlib.backends._backend_agg.BufferRegion, arg0: typing.SupportsInt | typing.SupportsIndex) -> None """
        pass

    def set_y(self, arg0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ set_y(self: matplotlib.backends._backend_agg.BufferRegion, arg0: typing.SupportsInt | typing.SupportsIndex) -> None """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __release_buffer__(self, *args, **kwargs): # real signature unknown
        """ Release the buffer object that exposes the underlying memory of the object. """
        pass


class RendererAgg(__pybind11_builtins.pybind11_object):
    # no doc
    def clear(self): # real signature unknown; restored from __doc__
        """ clear(self: matplotlib.backends._backend_agg.RendererAgg) -> None """
        pass

    def copy_from_bbox(self, bbox): # real signature unknown; restored from __doc__
        """ copy_from_bbox(self: matplotlib.backends._backend_agg.RendererAgg, bbox: rect_d) -> BufferRegion """
        return BufferRegion

    def draw_gouraud_triangles(self, gc, points, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw_gouraud_triangles(self: matplotlib.backends._backend_agg.RendererAgg, gc: GCAgg, points: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], colors: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], trans: trans_affine = None) -> None """
        pass

    def draw_image(self, gc, x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw_image(self: matplotlib.backends._backend_agg.RendererAgg, gc: GCAgg, x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, image: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> None """
        pass

    def draw_markers(self, gc, marker_path, marker_path_trans, path, trans, face=None): # real signature unknown; restored from __doc__
        """ draw_markers(self: matplotlib.backends._backend_agg.RendererAgg, gc: GCAgg, marker_path: PathIterator, marker_path_trans: trans_affine, path: PathIterator, trans: trans_affine, face: object = None) -> None """
        pass

    def draw_path(self, gc, path, trans, face=None): # real signature unknown; restored from __doc__
        """ draw_path(self: matplotlib.backends._backend_agg.RendererAgg, gc: GCAgg, path: PathIterator, trans: trans_affine, face: object = None) -> None """
        pass

    def draw_path_collection(self, gc, master_transform, paths, transforms, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw_path_collection(self: matplotlib.backends._backend_agg.RendererAgg, gc: GCAgg, master_transform: trans_affine, paths: PathGenerator, transforms: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], offsets: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], offset_trans: trans_affine, facecolors: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], edgecolors: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], linewidths: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], dashes: collections.abc.Sequence[Dashes], antialiaseds: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8], ignored: object, offset_position: object) -> None """
        pass

    def draw_quad_mesh(self, gc, master_transform, mesh_width, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw_quad_mesh(self: matplotlib.backends._backend_agg.RendererAgg, gc: GCAgg, master_transform: trans_affine, mesh_width: typing.SupportsInt | typing.SupportsIndex, mesh_height: typing.SupportsInt | typing.SupportsIndex, coordinates: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], offsets: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], offset_trans: trans_affine, facecolors: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], antialiased: bool, edgecolors: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> None """
        pass

    def draw_text_image(self, image, numpy_typing_ArrayLike=None, numpy_uint8=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ draw_text_image(self: matplotlib.backends._backend_agg.RendererAgg, image: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8], x: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex, angle: typing.SupportsFloat | typing.SupportsIndex, gc: GCAgg) -> None """
        pass

    def restore_region(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        restore_region(*args, **kwargs)
        Overloaded function.
        
        1. restore_region(self: matplotlib.backends._backend_agg.RendererAgg, region: BufferRegion) -> None
        
        2. restore_region(self: matplotlib.backends._backend_agg.RendererAgg, region: BufferRegion, xx1: typing.SupportsInt | typing.SupportsIndex, yy1: typing.SupportsInt | typing.SupportsIndex, xx2: typing.SupportsInt | typing.SupportsIndex, yy2: typing.SupportsInt | typing.SupportsIndex, x: typing.SupportsInt | typing.SupportsIndex, y: typing.SupportsInt | typing.SupportsIndex) -> None
        """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, width, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """ __init__(self: matplotlib.backends._backend_agg.RendererAgg, width: typing.SupportsInt | typing.SupportsIndex, height: typing.SupportsInt | typing.SupportsIndex, dpi: typing.SupportsFloat | typing.SupportsIndex) -> None """
        pass

    def __release_buffer__(self, *args, **kwargs): # real signature unknown
        """ Release the buffer object that exposes the underlying memory of the object. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001BA6D38D7B0>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib.backends._backend_agg', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001BA6D38D7B0>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\backends\\\\_backend_agg.cp314-win_amd64.pyd')"

