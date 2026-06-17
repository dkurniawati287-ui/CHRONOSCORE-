# encoding: utf-8
# module matplotlib.ft2font
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\matplotlib\ft2font.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import enum as __enum
import pybind11_builtins as __pybind11_builtins


# Variables with simple values

__freetype_build_type__ = 'local'

__freetype_version__ = '2.6.1'

# functions

def __getattr__(arg0): # real signature unknown; restored from __doc__
    """ __getattr__(arg0: str) -> object """
    return object()

# classes

class FaceFlags(__enum.Flag):
    """
    Flags returned by `FT2Font.face_flags`.
    
        For more information, see `the FreeType documentation
        <https://freetype.org/freetype2/docs/reference/ft2-face_creation.html#ft_face_flag_xxx>`_.
    
        .. versionadded:: 3.10
    """
    @staticmethod
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the last value assigned or None
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __and__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __or__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rand__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __ror__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rxor__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __xor__(self, other): # reliably restored by inspect
        # no doc
        pass

    CID_KEYED = None # (!) real value is '<FaceFlags.CID_KEYED: 4096>'
    COLOR = None # (!) real value is '<FaceFlags.COLOR: 16384>'
    EXTERNAL_STREAM = None # (!) real value is '<FaceFlags.EXTERNAL_STREAM: 1024>'
    FAST_GLYPHS = None # (!) real value is '<FaceFlags.FAST_GLYPHS: 128>'
    FIXED_SIZES = None # (!) real value is '<FaceFlags.FIXED_SIZES: 2>'
    FIXED_WIDTH = None # (!) real value is '<FaceFlags.FIXED_WIDTH: 4>'
    GLYPH_NAMES = None # (!) real value is '<FaceFlags.GLYPH_NAMES: 512>'
    HINTER = None # (!) real value is '<FaceFlags.HINTER: 2048>'
    HORIZONTAL = None # (!) real value is '<FaceFlags.HORIZONTAL: 16>'
    KERNING = None # (!) real value is '<FaceFlags.KERNING: 64>'
    MULTIPLE_MASTERS = None # (!) real value is '<FaceFlags.MULTIPLE_MASTERS: 256>'
    SCALABLE = None # (!) real value is '<FaceFlags.SCALABLE: 1>'
    SFNT = None # (!) real value is '<FaceFlags.SFNT: 8>'
    TRICKY = None # (!) real value is '<FaceFlags.TRICKY: 8192>'
    VERTICAL = None # (!) real value is '<FaceFlags.VERTICAL: 32>'
    _all_bits_ = 32767
    _boundary_ = <FlagBoundary.STRICT: 'strict'>
    _flag_mask_ = 32767
    _hashable_values_ = [
        1,
        2,
        4,
        8,
        16,
        32,
        64,
        128,
        256,
        512,
        1024,
        2048,
        4096,
        8192,
        16384,
    ]
    _inverted_ = None
    _member_map_ = {
        'CID_KEYED': None, # (!) real value is '<FaceFlags.CID_KEYED: 4096>'
        'COLOR': None, # (!) real value is '<FaceFlags.COLOR: 16384>'
        'EXTERNAL_STREAM': None, # (!) real value is '<FaceFlags.EXTERNAL_STREAM: 1024>'
        'FAST_GLYPHS': None, # (!) real value is '<FaceFlags.FAST_GLYPHS: 128>'
        'FIXED_SIZES': None, # (!) real value is '<FaceFlags.FIXED_SIZES: 2>'
        'FIXED_WIDTH': None, # (!) real value is '<FaceFlags.FIXED_WIDTH: 4>'
        'GLYPH_NAMES': None, # (!) real value is '<FaceFlags.GLYPH_NAMES: 512>'
        'HINTER': None, # (!) real value is '<FaceFlags.HINTER: 2048>'
        'HORIZONTAL': None, # (!) real value is '<FaceFlags.HORIZONTAL: 16>'
        'KERNING': None, # (!) real value is '<FaceFlags.KERNING: 64>'
        'MULTIPLE_MASTERS': None, # (!) real value is '<FaceFlags.MULTIPLE_MASTERS: 256>'
        'SCALABLE': None, # (!) real value is '<FaceFlags.SCALABLE: 1>'
        'SFNT': None, # (!) real value is '<FaceFlags.SFNT: 8>'
        'TRICKY': None, # (!) real value is '<FaceFlags.TRICKY: 8192>'
        'VERTICAL': None, # (!) real value is '<FaceFlags.VERTICAL: 32>'
    }
    _member_names_ = [
        'SCALABLE',
        'FIXED_SIZES',
        'FIXED_WIDTH',
        'SFNT',
        'HORIZONTAL',
        'VERTICAL',
        'KERNING',
        'FAST_GLYPHS',
        'MULTIPLE_MASTERS',
        'GLYPH_NAMES',
        'EXTERNAL_STREAM',
        'HINTER',
        'CID_KEYED',
        'TRICKY',
        'COLOR',
    ]
    _member_type_ = object
    _singles_mask_ = 32767
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        1: None, # (!) real value is '<FaceFlags.SCALABLE: 1>'
        2: None, # (!) real value is '<FaceFlags.FIXED_SIZES: 2>'
        4: None, # (!) real value is '<FaceFlags.FIXED_WIDTH: 4>'
        8: None, # (!) real value is '<FaceFlags.SFNT: 8>'
        16: None, # (!) real value is '<FaceFlags.HORIZONTAL: 16>'
        32: None, # (!) real value is '<FaceFlags.VERTICAL: 32>'
        64: None, # (!) real value is '<FaceFlags.KERNING: 64>'
        128: None, # (!) real value is '<FaceFlags.FAST_GLYPHS: 128>'
        256: None, # (!) real value is '<FaceFlags.MULTIPLE_MASTERS: 256>'
        512: None, # (!) real value is '<FaceFlags.GLYPH_NAMES: 512>'
        1024: None, # (!) real value is '<FaceFlags.EXTERNAL_STREAM: 1024>'
        2048: None, # (!) real value is '<FaceFlags.HINTER: 2048>'
        4096: None, # (!) real value is '<FaceFlags.CID_KEYED: 4096>'
        8192: None, # (!) real value is '<FaceFlags.TRICKY: 8192>'
        16384: None, # (!) real value is '<FaceFlags.COLOR: 16384>'
    }
    _value_repr_ = None


class FT2Font(__pybind11_builtins.pybind11_object):
    """
    An object representing a single font face.
    
        Outside of the font itself and querying its properties, this object provides methods
        for processing text strings into glyph shapes.
    
        Commonly, one will use `FT2Font.set_text` to load some glyph metrics and outlines.
        Then `FT2Font.draw_glyphs_to_bitmap` and `FT2Font.get_image` may be used to get a
        rendered form of the loaded string.
    
        For single characters, `FT2Font.load_char` or `FT2Font.load_glyph` may be used,
        either directly for their return values, or to use `FT2Font.draw_glyph_to_bitmap` or
        `FT2Font.get_path`.
    
        Useful metrics may be examined via the `Glyph` return values or
        `FT2Font.get_kerning`. Most dimensions are given in 26.6 or 16.6 fixed-point
        integers representing subpixels. Divide these values by 64 to produce floating-point
        pixels.
    """
    def clear(self): # real signature unknown; restored from __doc__
        """
        clear(self: matplotlib.ft2font.FT2Font) -> None
        
        Clear all the glyphs, reset for a new call to `.set_text`.
        """
        pass

    def draw_glyphs_to_bitmap(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        draw_glyphs_to_bitmap(self: matplotlib.ft2font.FT2Font, *, antialiased: bool = True) -> None
        
        
            Draw the glyphs that were loaded by `.set_text` to the bitmap.
        
            The bitmap size will be automatically set to include the glyphs.
        
            Parameters
            ----------
            antialiased : bool, default: True
                Whether to render glyphs 8-bit antialiased or in pure black-and-white.
        
            See Also
            --------
            .draw_glyph_to_bitmap
        """
        pass

    def draw_glyph_to_bitmap(self, image, x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        draw_glyph_to_bitmap(self: matplotlib.ft2font.FT2Font, image: matplotlib.ft2font.FT2Image, x: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex, glyph: matplotlib.ft2font.Glyph, *, antialiased: bool = True) -> None
        
        
            Draw a single glyph to the bitmap at pixel locations x, y.
        
            Note it is your responsibility to create the image manually with the correct size
            before this call is made.
        
            If you want automatic layout, use `.set_text` in combinations with
            `.draw_glyphs_to_bitmap`. This function is instead intended for people who want to
            render individual glyphs (e.g., returned by `.load_char`) at precise locations.
        
            Parameters
            ----------
            image : FT2Image
                The image buffer on which to draw the glyph.
            x, y : int
                The pixel location at which to draw the glyph.
            glyph : Glyph
                The glyph to draw.
            antialiased : bool, default: True
                Whether to render glyphs 8-bit antialiased or in pure black-and-white.
        
            See Also
            --------
            .draw_glyphs_to_bitmap
        """
        pass

    def get_bitmap_offset(self): # real signature unknown; restored from __doc__
        """
        get_bitmap_offset(self: matplotlib.ft2font.FT2Font) -> tuple
        
        
            Get the (x, y) offset for the bitmap if ink hangs left or below (0, 0).
        
            Since Matplotlib only supports left-to-right text, y is always 0.
        
            Returns
            -------
            x, y : float
                The x and y offset in 26.6 subpixels of the bitmap. To get x and y in pixels,
                divide these values by 64.
        
            See Also
            --------
            .get_width_height
            .get_descent
        """
        return ()

    def get_charmap(self): # real signature unknown; restored from __doc__
        """
        get_charmap(self: matplotlib.ft2font.FT2Font) -> dict
        
        
            Return a mapping of character codes to glyph indices in the font.
        
            The charmap is Unicode by default, but may be changed by `.set_charmap` or
            `.select_charmap`.
        
            Returns
            -------
            dict[int, int]
                A dictionary of the selected charmap mapping character codes to their
                corresponding glyph indices.
        """
        return {}

    def get_char_index(self, codepoint, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_char_index(self: matplotlib.ft2font.FT2Font, codepoint: typing.SupportsInt | typing.SupportsIndex) -> int
        
        
            Return the glyph index corresponding to a character code point.
        
            Parameters
            ----------
            codepoint : int
                A character code point in the current charmap (which defaults to Unicode.)
        
            Returns
            -------
            int
                The corresponding glyph index.
        
            See Also
            --------
            .set_charmap
            .select_charmap
            .get_glyph_name
            .get_name_index
        """
        pass

    def get_descent(self): # real signature unknown; restored from __doc__
        """
        get_descent(self: matplotlib.ft2font.FT2Font) -> int
        
        
            Get the descent of the current string set by `.set_text`.
        
            The rotation of the string is accounted for.
        
            Returns
            -------
            int
                The descent in 26.6 subpixels of the bitmap. To get the descent in pixels,
                divide these values by 64.
        
            See Also
            --------
            .get_bitmap_offset
            .get_width_height
        """
        return 0

    def get_glyph_name(self, index, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_glyph_name(self: matplotlib.ft2font.FT2Font, index: typing.SupportsInt | typing.SupportsIndex) -> str
        
        
            Retrieve the ASCII name of a given glyph *index* in a face.
        
            Due to Matplotlib's internal design, for fonts that do not contain glyph names (per
            ``FT_FACE_FLAG_GLYPH_NAMES``), this returns a made-up name which does *not*
            roundtrip through `.get_name_index`.
        
            Parameters
            ----------
            index : int
                The glyph number to query.
        
            Returns
            -------
            str
                The name of the glyph, or if the font does not contain names, a name synthesized
                by Matplotlib.
        
            See Also
            --------
            .get_name_index
        """
        pass

    def get_image(self): # real signature unknown; restored from __doc__
        """
        get_image(self: matplotlib.ft2font.FT2Font) -> numpy.ndarray
        
        
            Return the underlying image buffer for this font object.
        
            Returns
            -------
            np.ndarray[int]
        
            See Also
            --------
            .get_path
        """
        pass

    def get_kerning(self, left, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        get_kerning(self: matplotlib.ft2font.FT2Font, left: typing.SupportsInt | typing.SupportsIndex, right: typing.SupportsInt | typing.SupportsIndex, mode: Kerning | typing.SupportsInt | typing.SupportsIndex) -> int
        
        
            Get the kerning between two glyphs.
        
            Parameters
            ----------
            left, right : int
                The glyph indices. Note these are not characters nor character codes.
                Use `.get_char_index` to convert character codes to glyph indices.
        
            mode : Kerning
                A kerning mode constant:
        
                - ``DEFAULT``  - Return scaled and grid-fitted kerning distances.
                - ``UNFITTED`` - Return scaled but un-grid-fitted kerning distances.
                - ``UNSCALED`` - Return the kerning vector in original font units.
        
                .. versionchanged:: 3.10
                    This now takes a `.ft2font.Kerning` value instead of an `int`.
        
            Returns
            -------
            int
                The kerning adjustment between the two glyphs.
        """
        pass

    def get_name_index(self, name): # real signature unknown; restored from __doc__
        """
        get_name_index(self: matplotlib.ft2font.FT2Font, name: str) -> int
        
        
            Return the glyph index of a given glyph *name*.
        
            Parameters
            ----------
            name : str
                The name of the glyph to query.
        
            Returns
            -------
            int
                The corresponding glyph index; 0 means 'undefined character code'.
        
            See Also
            --------
            .get_char_index
            .get_glyph_name
        """
        return 0

    def get_num_glyphs(self): # real signature unknown; restored from __doc__
        """
        get_num_glyphs(self: matplotlib.ft2font.FT2Font) -> int
        
        Return the number of loaded glyphs.
        """
        return 0

    def get_path(self): # real signature unknown; restored from __doc__
        """
        get_path(self: matplotlib.ft2font.FT2Font) -> tuple
        
        
            Get the path data from the currently loaded glyph.
        
            Returns
            -------
            vertices : np.ndarray[double]
                The (N, 2) array of vertices describing the current glyph.
            codes : np.ndarray[np.uint8]
                The (N, ) array of codes corresponding to the vertices.
        
            See Also
            --------
            .get_image
            .load_char
            .load_glyph
            .set_text
        """
        return ()

    def get_ps_font_info(self): # real signature unknown; restored from __doc__
        """
        get_ps_font_info(self: matplotlib.ft2font.FT2Font) -> tuple
        
        
            Return the information in the PS Font Info structure.
        
            For more information, see the `FreeType documentation on this structure
            <https://freetype.org/freetype2/docs/reference/ft2-type1_tables.html#ps_fontinforec>`_.
        
            Returns
            -------
            version : str
            notice : str
            full_name : str
            family_name : str
            weight : str
            italic_angle : int
            is_fixed_pitch : bool
            underline_position : int
            underline_thickness : int
        """
        return ()

    def get_sfnt(self): # real signature unknown; restored from __doc__
        """
        get_sfnt(self: matplotlib.ft2font.FT2Font) -> dict
        
        
            Load the entire SFNT names table.
        
            Returns
            -------
            dict[tuple[int, int, int, int], bytes]
                The SFNT names table; the dictionary keys are tuples of:
        
                    (platform-ID, ISO-encoding-scheme, language-code, description)
        
                and the values are the direct information from the font table.
        """
        return {}

    def get_sfnt_table(self, name): # real signature unknown; restored from __doc__
        """
        get_sfnt_table(self: matplotlib.ft2font.FT2Font, name: str) -> dict | None
        
        
            Return one of the SFNT tables.
        
            Parameters
            ----------
            name : {"head", "maxp", "OS/2", "hhea", "vhea", "post", "pclt"}
                Which table to return.
        
            Returns
            -------
            dict[str, Any]
                The corresponding table; for more information, see `the FreeType documentation
                <https://freetype.org/freetype2/docs/reference/ft2-truetype_tables.html>`_.
        """
        return {}

    def get_width_height(self): # real signature unknown; restored from __doc__
        """
        get_width_height(self: matplotlib.ft2font.FT2Font) -> tuple
        
        
            Get the dimensions of the current string set by `.set_text`.
        
            The rotation of the string is accounted for.
        
            Returns
            -------
            width, height : float
                The width and height in 26.6 subpixels of the current string. To get width and
                height in pixels, divide these values by 64.
        
            See Also
            --------
            .get_bitmap_offset
            .get_descent
        """
        return ()

    def load_char(self, charcode, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        load_char(self: matplotlib.ft2font.FT2Font, charcode: typing.SupportsInt | typing.SupportsIndex, flags: LoadFlags | typing.SupportsInt | typing.SupportsIndex = <LoadFlags.FORCE_AUTOHINT: 32>) -> matplotlib.ft2font.Glyph
        
        
            Load character in current fontfile and set glyph.
        
            Parameters
            ----------
            charcode : int
                The character code to prepare rendering information for. This code must be in
                the charmap, or else a ``.notdef`` glyph may be returned instead.
            flags : LoadFlags, default: `.LoadFlags.FORCE_AUTOHINT`
                Any bitwise-OR combination of the `.LoadFlags` flags.
        
                .. versionchanged:: 3.10
                    This now takes an `.ft2font.LoadFlags` instead of an int.
        
            Returns
            -------
            Glyph
                The glyph information corresponding to the specified character.
        
            See Also
            --------
            .load_glyph
            .select_charmap
            .set_charmap
        """
        pass

    def load_glyph(self, glyph_index, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        load_glyph(self: matplotlib.ft2font.FT2Font, glyph_index: typing.SupportsInt | typing.SupportsIndex, flags: LoadFlags | typing.SupportsInt | typing.SupportsIndex = <LoadFlags.FORCE_AUTOHINT: 32>) -> matplotlib.ft2font.Glyph
        
        
            Load glyph index in current fontfile and set glyph.
        
            Note that the glyph index is specific to a font, and not universal like a Unicode
            code point.
        
            Parameters
            ----------
            glyph_index : int
                The glyph index to prepare rendering information for.
            flags : LoadFlags, default: `.LoadFlags.FORCE_AUTOHINT`
                Any bitwise-OR combination of the `.LoadFlags` flags.
        
                .. versionchanged:: 3.10
                    This now takes an `.ft2font.LoadFlags` instead of an int.
        
            Returns
            -------
            Glyph
                The glyph information corresponding to the specified index.
        
            See Also
            --------
            .load_char
        """
        pass

    def select_charmap(self, i, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        select_charmap(self: matplotlib.ft2font.FT2Font, i: typing.SupportsInt | typing.SupportsIndex) -> None
        
        
            Select a charmap by its FT_Encoding number.
        
            For more details on character mapping, see the `FreeType documentation
            <https://freetype.org/freetype2/docs/reference/ft2-character_mapping.html>`_.
        
            Parameters
            ----------
            i : int
                The charmap in the form defined by FreeType:
                https://freetype.org/freetype2/docs/reference/ft2-character_mapping.html#ft_encoding
        
            See Also
            --------
            .set_charmap
            .get_charmap
        """
        pass

    def set_charmap(self, i, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_charmap(self: matplotlib.ft2font.FT2Font, i: typing.SupportsInt | typing.SupportsIndex) -> None
        
        
            Make the i-th charmap current.
        
            For more details on character mapping, see the `FreeType documentation
            <https://freetype.org/freetype2/docs/reference/ft2-character_mapping.html>`_.
        
            Parameters
            ----------
            i : int
                The charmap number in the range [0, `.num_charmaps`).
        
            See Also
            --------
            .num_charmaps
            .select_charmap
            .get_charmap
        """
        pass

    def set_size(self, ptsize, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_size(self: matplotlib.ft2font.FT2Font, ptsize: typing.SupportsFloat | typing.SupportsIndex, dpi: typing.SupportsFloat | typing.SupportsIndex) -> None
        
        
            Set the size of the text.
        
            Parameters
            ----------
            ptsize : float
                The size of the text in points.
            dpi : float
                The DPI used for rendering the text.
        """
        pass

    def set_text(self, string, angle, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        set_text(self: matplotlib.ft2font.FT2Font, string: str, angle: typing.SupportsFloat | typing.SupportsIndex = 0.0, flags: LoadFlags | typing.SupportsInt | typing.SupportsIndex = <LoadFlags.FORCE_AUTOHINT: 32>) -> numpy.typing.NDArray[numpy.float64]
        
        
            Set the text *string* and *angle*.
        
            You must call this before `.draw_glyphs_to_bitmap`.
        
            Parameters
            ----------
            string : str
                The text to prepare rendering information for.
            angle : float
                The angle at which to render the supplied text.
            flags : LoadFlags, default: `.LoadFlags.FORCE_AUTOHINT`
                Any bitwise-OR combination of the `.LoadFlags` flags.
        
                .. versionchanged:: 3.10
                    This now takes an `.ft2font.LoadFlags` instead of an int.
        
            Returns
            -------
            np.ndarray[double]
                A sequence of x,y glyph positions in 26.6 subpixels; divide by 64 for pixels.
        """
        pass

    def _get_fontmap(self, string): # real signature unknown; restored from __doc__
        """
        _get_fontmap(self: matplotlib.ft2font.FT2Font, string: str) -> dict
        
        
            Get a mapping between characters and the font that includes them.
        
            .. warning::
                This API uses the fallback list and is both private and provisional: do not use
                it directly.
        
            Parameters
            ----------
            text : str
                The characters for which to find fonts.
        
            Returns
            -------
            dict[str, FT2Font]
                A dictionary mapping unicode characters to `.FT2Font` objects.
        """
        return {}

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, filename, hinting_factor, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__(self: matplotlib.ft2font.FT2Font, filename: object, hinting_factor: typing.SupportsInt | typing.SupportsIndex = 8, *, _fallback_list: collections.abc.Sequence[matplotlib.ft2font.FT2Font] | None = None, _kerning_factor: typing.SupportsInt | typing.SupportsIndex = 0) -> None
        
        
            Parameters
            ----------
            filename : str or file-like
                The source of the font data in a format (ttf or ttc) that FreeType can read.
        
            hinting_factor : int, optional
                Must be positive. Used to scale the hinting in the x-direction.
        
            _fallback_list : list of FT2Font, optional
                A list of FT2Font objects used to find missing glyphs.
        
                .. warning::
                    This API is both private and provisional: do not use it directly.
        
            _kerning_factor : int, optional
                Used to adjust the degree of kerning.
        
                .. warning::
                    This API is private: do not use it directly.
        """
        pass

    def __release_buffer__(self, *args, **kwargs): # real signature unknown
        """ Release the buffer object that exposes the underlying memory of the object. """
        pass

    ascender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Ascender in 26.6 units."""

    bbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Face global bounding box (xmin, ymin, xmax, ymax)."""

    descender = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Descender in 26.6 units."""

    face_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Face flags; see `.FaceFlags`."""

    family_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Face family name."""

    fname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The original filename for this object."""

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Height in 26.6 units; used to compute a default line spacing (baseline-to-baseline distance)."""

    max_advance_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum vertical cursor advance for all glyphs."""

    max_advance_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Maximum horizontal cursor advance for all glyphs."""

    num_charmaps = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of charmaps in the face."""

    num_faces = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of faces in file."""

    num_fixed_sizes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of bitmap in the face."""

    num_glyphs = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of glyphs in the face."""

    num_named_instances = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of named instances in the face."""

    postscript_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """PostScript name of the font."""

    scalable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Whether face is scalable; attributes after this one are only defined for scalable faces."""

    style_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Style flags; see `.StyleFlags`."""

    style_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Style name."""

    underline_position = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Vertical position of the underline bar."""

    underline_thickness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thickness of the underline bar."""

    units_per_EM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of font units covered by the EM."""



class FT2Image(__pybind11_builtins.pybind11_object):
    """ An image buffer for drawing glyphs. """
    def draw_rect_filled(self, x0, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        draw_rect_filled(self: matplotlib.ft2font.FT2Image, x0: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex, y0: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex, x1: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex, y1: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex) -> None
        
        
            Draw a filled rectangle to the image.
        
            Parameters
            ----------
            x0, y0, x1, y1 : float
                The bounds of the rectangle from (x0, y0) to (x1, y1).
        """
        pass

    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __init__(self, width, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        __init__(self: matplotlib.ft2font.FT2Image, width: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex, height: typing.SupportsInt | typing.SupportsIndex | typing.SupportsFloat | typing.SupportsIndex) -> None
        
        
            Parameters
            ----------
            width, height : int
                The dimensions of the image buffer.
        """
        pass

    def __release_buffer__(self, *args, **kwargs): # real signature unknown
        """ Release the buffer object that exposes the underlying memory of the object. """
        pass


class Glyph(__pybind11_builtins.pybind11_object):
    """
    Information about a single glyph.
    
        You cannot create instances of this object yourself, but must use
        `.FT2Font.load_char` or `.FT2Font.load_glyph` to generate one. This object may be
        used in a call to `.FT2Font.draw_glyph_to_bitmap`.
    
        For more information on the various metrics, see `the FreeType documentation
        <https://freetype.org/freetype2/docs/glyphs/glyphs-3.html>`_.
    """
    def _pybind11_conduit_v1_(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self): # real signature unknown; restored from __doc__
        """ __init__(self: matplotlib.ft2font.Glyph) -> None """
        pass

    bbox = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The control box of the glyph."""

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The glyph's height."""

    horiAdvance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Advance width for horizontal layout."""

    horiBearingX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Left side bearing for horizontal layout."""

    horiBearingY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top side bearing for horizontal layout."""

    linearHoriAdvance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The advance width of the unhinted glyph."""

    vertAdvance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Advance height for vertical layout."""

    vertBearingX = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Left side bearing for vertical layout."""

    vertBearingY = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Top side bearing for vertical layout."""

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The glyph's width."""



class Kerning(__enum.Enum):
    """
    Kerning modes for `.FT2Font.get_kerning`.
    
        For more information, see `the FreeType documentation
        <https://freetype.org/freetype2/docs/reference/ft2-glyph_retrieval.html#ft_kerning_mode>`_.
    
        .. versionadded:: 3.10
    """
    @staticmethod
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the list of values assigned
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    DEFAULT = None # (!) real value is '<Kerning.DEFAULT: 0>'
    UNFITTED = None # (!) real value is '<Kerning.UNFITTED: 1>'
    UNSCALED = None # (!) real value is '<Kerning.UNSCALED: 2>'
    _hashable_values_ = [
        0,
        1,
        2,
    ]
    _member_map_ = {
        'DEFAULT': None, # (!) real value is '<Kerning.DEFAULT: 0>'
        'UNFITTED': None, # (!) real value is '<Kerning.UNFITTED: 1>'
        'UNSCALED': None, # (!) real value is '<Kerning.UNSCALED: 2>'
    }
    _member_names_ = [
        'DEFAULT',
        'UNFITTED',
        'UNSCALED',
    ]
    _member_type_ = object
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        0: None, # (!) real value is '<Kerning.DEFAULT: 0>'
        1: None, # (!) real value is '<Kerning.UNFITTED: 1>'
        2: None, # (!) real value is '<Kerning.UNSCALED: 2>'
    }
    _value_repr_ = None


class LoadFlags(__enum.Flag):
    """
    Flags for `FT2Font.load_char`, `FT2Font.load_glyph`, and `FT2Font.set_text`.
    
        For more information, see `the FreeType documentation
        <https://freetype.org/freetype2/docs/reference/ft2-glyph_retrieval.html#ft_load_xxx>`_.
    
        .. versionadded:: 3.10
    """
    @staticmethod
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the last value assigned or None
        """
        pass

    def _iter_member_(self, *args, **kwargs): # real signature unknown
        """ Extract all members from the value in definition order. """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __and__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __or__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rand__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __ror__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rxor__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __xor__(self, other): # reliably restored by inspect
        # no doc
        pass

    COLOR = None # (!) real value is '<LoadFlags.COLOR: 1048576>'
    COMPUTE_METRICS = None # (!) real value is '<LoadFlags.COMPUTE_METRICS: 2097152>'
    CROP_BITMAP = None # (!) real value is '<LoadFlags.CROP_BITMAP: 64>'
    DEFAULT = None # (!) real value is '<LoadFlags.DEFAULT: 0>'
    FORCE_AUTOHINT = None # (!) real value is '<LoadFlags.FORCE_AUTOHINT: 32>'
    IGNORE_GLOBAL_ADVANCE_WIDTH = None # (!) real value is '<LoadFlags.IGNORE_GLOBAL_ADVANCE_WIDTH: 512>'
    IGNORE_TRANSFORM = None # (!) real value is '<LoadFlags.IGNORE_TRANSFORM: 2048>'
    LINEAR_DESIGN = None # (!) real value is '<LoadFlags.LINEAR_DESIGN: 8192>'
    MONOCHROME = None # (!) real value is '<LoadFlags.MONOCHROME: 4096>'
    NO_AUTOHINT = None # (!) real value is '<LoadFlags.NO_AUTOHINT: 32768>'
    NO_BITMAP = None # (!) real value is '<LoadFlags.NO_BITMAP: 8>'
    NO_HINTING = None # (!) real value is '<LoadFlags.NO_HINTING: 2>'
    NO_RECURSE = None # (!) real value is '<LoadFlags.NO_RECURSE: 1024>'
    NO_SCALE = None # (!) real value is '<LoadFlags.NO_SCALE: 1>'
    PEDANTIC = None # (!) real value is '<LoadFlags.PEDANTIC: 128>'
    RENDER = None # (!) real value is '<LoadFlags.RENDER: 4>'
    TARGET_LCD = None # (!) real value is '<LoadFlags.TARGET_LCD: 196608>'
    TARGET_LCD_V = None # (!) real value is '<LoadFlags.TARGET_LCD_V: 262144>'
    TARGET_LIGHT = None # (!) real value is '<LoadFlags.TARGET_LIGHT: 65536>'
    TARGET_MONO = None # (!) real value is '<LoadFlags.TARGET_MONO: 131072>'
    TARGET_NORMAL = None # (!) real value is '<LoadFlags.DEFAULT: 0>'
    VERTICAL_LAYOUT = None # (!) real value is '<LoadFlags.VERTICAL_LAYOUT: 16>'
    _all_bits_ = 4194303
    _boundary_ = <FlagBoundary.STRICT: 'strict'>
    _flag_mask_ = 3653375
    _hashable_values_ = [
        0,
        1,
        2,
        4,
        8,
        16,
        32,
        64,
        128,
        512,
        1024,
        2048,
        4096,
        8192,
        32768,
        1048576,
        2097152,
        65536,
        131072,
        196608,
        262144,
    ]
    _inverted_ = None
    _member_map_ = {
        'COLOR': None, # (!) real value is '<LoadFlags.COLOR: 1048576>'
        'COMPUTE_METRICS': None, # (!) real value is '<LoadFlags.COMPUTE_METRICS: 2097152>'
        'CROP_BITMAP': None, # (!) real value is '<LoadFlags.CROP_BITMAP: 64>'
        'DEFAULT': None, # (!) real value is '<LoadFlags.DEFAULT: 0>'
        'FORCE_AUTOHINT': None, # (!) real value is '<LoadFlags.FORCE_AUTOHINT: 32>'
        'IGNORE_GLOBAL_ADVANCE_WIDTH': None, # (!) real value is '<LoadFlags.IGNORE_GLOBAL_ADVANCE_WIDTH: 512>'
        'IGNORE_TRANSFORM': None, # (!) real value is '<LoadFlags.IGNORE_TRANSFORM: 2048>'
        'LINEAR_DESIGN': None, # (!) real value is '<LoadFlags.LINEAR_DESIGN: 8192>'
        'MONOCHROME': None, # (!) real value is '<LoadFlags.MONOCHROME: 4096>'
        'NO_AUTOHINT': None, # (!) real value is '<LoadFlags.NO_AUTOHINT: 32768>'
        'NO_BITMAP': None, # (!) real value is '<LoadFlags.NO_BITMAP: 8>'
        'NO_HINTING': None, # (!) real value is '<LoadFlags.NO_HINTING: 2>'
        'NO_RECURSE': None, # (!) real value is '<LoadFlags.NO_RECURSE: 1024>'
        'NO_SCALE': None, # (!) real value is '<LoadFlags.NO_SCALE: 1>'
        'PEDANTIC': None, # (!) real value is '<LoadFlags.PEDANTIC: 128>'
        'RENDER': None, # (!) real value is '<LoadFlags.RENDER: 4>'
        'TARGET_LCD': None, # (!) real value is '<LoadFlags.TARGET_LCD: 196608>'
        'TARGET_LCD_V': None, # (!) real value is '<LoadFlags.TARGET_LCD_V: 262144>'
        'TARGET_LIGHT': None, # (!) real value is '<LoadFlags.TARGET_LIGHT: 65536>'
        'TARGET_MONO': None, # (!) real value is '<LoadFlags.TARGET_MONO: 131072>'
        'TARGET_NORMAL': '<value is a self-reference, replaced by this string>',
        'VERTICAL_LAYOUT': None, # (!) real value is '<LoadFlags.VERTICAL_LAYOUT: 16>'
    }
    _member_names_ = [
        'NO_SCALE',
        'NO_HINTING',
        'RENDER',
        'NO_BITMAP',
        'VERTICAL_LAYOUT',
        'FORCE_AUTOHINT',
        'CROP_BITMAP',
        'PEDANTIC',
        'IGNORE_GLOBAL_ADVANCE_WIDTH',
        'NO_RECURSE',
        'IGNORE_TRANSFORM',
        'MONOCHROME',
        'LINEAR_DESIGN',
        'NO_AUTOHINT',
        'COLOR',
        'COMPUTE_METRICS',
        'TARGET_LIGHT',
        'TARGET_MONO',
        'TARGET_LCD_V',
    ]
    _member_type_ = object
    _singles_mask_ = 3653375
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        0: None, # (!) real value is '<LoadFlags.DEFAULT: 0>'
        1: None, # (!) real value is '<LoadFlags.NO_SCALE: 1>'
        2: None, # (!) real value is '<LoadFlags.NO_HINTING: 2>'
        4: None, # (!) real value is '<LoadFlags.RENDER: 4>'
        8: None, # (!) real value is '<LoadFlags.NO_BITMAP: 8>'
        16: None, # (!) real value is '<LoadFlags.VERTICAL_LAYOUT: 16>'
        32: None, # (!) real value is '<LoadFlags.FORCE_AUTOHINT: 32>'
        64: None, # (!) real value is '<LoadFlags.CROP_BITMAP: 64>'
        128: None, # (!) real value is '<LoadFlags.PEDANTIC: 128>'
        512: None, # (!) real value is '<LoadFlags.IGNORE_GLOBAL_ADVANCE_WIDTH: 512>'
        1024: None, # (!) real value is '<LoadFlags.NO_RECURSE: 1024>'
        2048: None, # (!) real value is '<LoadFlags.IGNORE_TRANSFORM: 2048>'
        4096: None, # (!) real value is '<LoadFlags.MONOCHROME: 4096>'
        8192: None, # (!) real value is '<LoadFlags.LINEAR_DESIGN: 8192>'
        32768: None, # (!) real value is '<LoadFlags.NO_AUTOHINT: 32768>'
        65536: None, # (!) real value is '<LoadFlags.TARGET_LIGHT: 65536>'
        131072: None, # (!) real value is '<LoadFlags.TARGET_MONO: 131072>'
        196608: None, # (!) real value is '<LoadFlags.TARGET_LCD: 196608>'
        262144: None, # (!) real value is '<LoadFlags.TARGET_LCD_V: 262144>'
        1048576: None, # (!) real value is '<LoadFlags.COLOR: 1048576>'
        2097152: None, # (!) real value is '<LoadFlags.COMPUTE_METRICS: 2097152>'
    }
    _value_repr_ = None


class StyleFlags(__enum.Flag):
    """
    Flags returned by `FT2Font.style_flags`.
    
        For more information, see `the FreeType documentation
        <https://freetype.org/freetype2/docs/reference/ft2-face_creation.html#ft_style_flag_xxx>`_.
    
        .. versionadded:: 3.10
    """
    @staticmethod
    def _generate_next_value_(name, start, count, last_values): # reliably restored by inspect
        """
        Generate the next value when not given.
        
        name: the name of the member
        start: the initial start value or None
        count: the number of existing members
        last_values: the last value assigned or None
        """
        pass

    def _new_member_(self, *args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __and__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __invert__(self): # reliably restored by inspect
        # no doc
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    def __or__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rand__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __ror__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __rxor__(self, other): # reliably restored by inspect
        # no doc
        pass

    def __xor__(self, other): # reliably restored by inspect
        # no doc
        pass

    BOLD = None # (!) real value is '<StyleFlags.BOLD: 2>'
    ITALIC = None # (!) real value is '<StyleFlags.ITALIC: 1>'
    NORMAL = None # (!) real value is '<StyleFlags.NORMAL: 0>'
    _all_bits_ = 3
    _boundary_ = <FlagBoundary.STRICT: 'strict'>
    _flag_mask_ = 3
    _hashable_values_ = [
        0,
        1,
        2,
    ]
    _inverted_ = None
    _member_map_ = {
        'BOLD': None, # (!) real value is '<StyleFlags.BOLD: 2>'
        'ITALIC': None, # (!) real value is '<StyleFlags.ITALIC: 1>'
        'NORMAL': None, # (!) real value is '<StyleFlags.NORMAL: 0>'
    }
    _member_names_ = [
        'ITALIC',
        'BOLD',
    ]
    _member_type_ = object
    _singles_mask_ = 3
    _unhashable_values_ = []
    _unhashable_values_map_ = {}
    _use_args_ = False
    _value2member_map_ = {
        0: None, # (!) real value is '<StyleFlags.NORMAL: 0>'
        1: None, # (!) real value is '<StyleFlags.ITALIC: 1>'
        2: None, # (!) real value is '<StyleFlags.BOLD: 2>'
    }
    _value_repr_ = None


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026284874710>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib.ft2font', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000026284874710>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\matplotlib\\\\ft2font.cp314-win_amd64.pyd')"

