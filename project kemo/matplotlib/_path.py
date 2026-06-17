# encoding: utf-8
# module matplotlib._path
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\matplotlib\_path.cp314-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# functions

def affine_transform(points, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ affine_transform(points: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], trans: trans_affine) -> object """
    pass

def cleanup_path(path, trans, remove_nans, clip_rect, snap_mode, stroke_width, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ cleanup_path(path: PathIterator, trans: trans_affine, remove_nans: bool, clip_rect: rect_d, snap_mode: e_snap_mode, stroke_width: typing.SupportsFloat | typing.SupportsIndex, simplify: bool | None, return_curves: bool, sketch: SketchParams) -> tuple """
    pass

def clip_path_to_rect(path, rect, inside): # real signature unknown; restored from __doc__
    """ clip_path_to_rect(path: PathIterator, rect: rect_d, inside: bool) -> list """
    return []

def convert_path_to_polygons(path, trans, width, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ convert_path_to_polygons(path: PathIterator, trans: trans_affine, width: typing.SupportsFloat | typing.SupportsIndex = 0.0, height: typing.SupportsFloat | typing.SupportsIndex = 0.0, closed_only: bool = False) -> list """
    pass

def convert_to_string(path, trans, clip_rect, simplify, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    convert_to_string(path: PathIterator, trans: trans_affine, clip_rect: rect_d, simplify: bool | None, sketch: SketchParams, precision: typing.SupportsInt | typing.SupportsIndex, codes: typing.Annotated[collections.abc.Sequence[str], "FixedSize(5)"], postfix: bool) -> object
    
    --
    
    Convert *path* to a bytestring.
    
    The first five parameters (up to *sketch*) are interpreted as in `.cleanup_path`. The
    following ones are detailed below.
    
    Parameters
    ----------
    path : Path
    trans : Transform or None
    clip_rect : sequence of 4 floats, or None
    simplify : bool
    sketch : tuple of 3 floats, or None
    precision : int
        The precision used to "%.*f"-format the values. Trailing zeros and decimal points
        are always removed. (precision=-1 is a special case used to implement
        ttconv-back-compatible conversion.)
    codes : sequence of 5 bytestrings
        The bytes representation of each opcode (MOVETO, LINETO, CURVE3, CURVE4, CLOSEPOLY),
        in that order. If the bytes for CURVE3 is empty, quad segments are automatically
        converted to cubic ones (this is used by backends such as pdf and ps, which do not
        support quads).
    postfix : bool
        Whether the opcode comes after the values (True) or before (False).
    """
    pass

def count_bboxes_overlapping_bbox(bbox, bboxes, numpy_typing_ArrayLike=None, numpy_float64=None): # real signature unknown; restored from __doc__
    """ count_bboxes_overlapping_bbox(bbox: rect_d, bboxes: typing.Annotated[numpy.typing.ArrayLike, numpy.float64]) -> int """
    return 0

def get_path_collection_extents(master_transform, paths, transforms, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ get_path_collection_extents(master_transform: trans_affine, paths: PathGenerator, transforms: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], offsets: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], offset_transform: trans_affine) -> tuple """
    pass

def is_sorted_and_has_non_nan(array): # real signature unknown; restored from __doc__
    """
    is_sorted_and_has_non_nan(array: object) -> bool
    
    --
    
    Return whether the 1D *array* is monotonically increasing, ignoring NaNs, and has at
    least one non-nan value.
    """
    return False

def path_intersects_path(path1, path2, filled=False): # real signature unknown; restored from __doc__
    """ path_intersects_path(path1: PathIterator, path2: PathIterator, filled: bool = False) -> bool """
    return False

def path_intersects_rectangle(path, rect_x1, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ path_intersects_rectangle(path: PathIterator, rect_x1: typing.SupportsFloat | typing.SupportsIndex, rect_y1: typing.SupportsFloat | typing.SupportsIndex, rect_x2: typing.SupportsFloat | typing.SupportsIndex, rect_y2: typing.SupportsFloat | typing.SupportsIndex, filled: bool = False) -> bool """
    pass

def path_in_path(path_a, trans_a, path_b, trans_b): # real signature unknown; restored from __doc__
    """ path_in_path(path_a: PathIterator, trans_a: trans_affine, path_b: PathIterator, trans_b: trans_affine) -> bool """
    return False

def points_in_path(points, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ points_in_path(points: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], radius: typing.SupportsFloat | typing.SupportsIndex, path: PathIterator, trans: trans_affine) -> numpy.typing.NDArray[numpy.float64] """
    pass

def point_in_path(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ point_in_path(x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, radius: typing.SupportsFloat | typing.SupportsIndex, path: PathIterator, trans: trans_affine) -> bool """
    pass

def point_in_path_collection(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ point_in_path_collection(x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, radius: typing.SupportsFloat | typing.SupportsIndex, master_transform: trans_affine, paths: PathGenerator, transforms: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], offsets: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], offset_trans: trans_affine, filled: bool) -> object """
    pass

def update_path_extents(path, trans, rect, minpos, numpy_typing_ArrayLike=None, numpy_float64=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """ update_path_extents(path: PathIterator, trans: trans_affine, rect: rect_d, minpos: typing.Annotated[numpy.typing.ArrayLike, numpy.float64], ignore: bool) -> tuple """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022AA225B5F0>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._path', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022AA225B5F0>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\_path.cp314-win_amd64.pyd')"

