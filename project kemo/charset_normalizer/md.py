# encoding: utf-8
# module charset_normalizer.md
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\charset_normalizer\md.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import sys as sys # <module 'sys' (built-in)>

# Variables with simple values

TRACE = 5

_ACCENTUATED = 2
_ARABIC = 128

_ARABIC_ISOLATED_FORM = 256

_CJK = 4

_GLYPH_MASK = 124

_HANGUL = 8
_HIRAGANA = 32

_KATAKANA = 16

_LATIN = 1

_THAI = 64

# functions

def final(f): # reliably restored by inspect
    """
    Decorator to indicate final methods and final classes.
    
    Use this decorator to indicate to type checkers that the decorated
    method cannot be overridden, and decorated class cannot be subclassed.
    
    For example::
    
        class Base:
            @final
            def done(self) -> None:
                ...
        class Sub(Base):
            def done(self) -> None:  # Error reported by type checker
                ...
    
        @final
        class Leaf:
            ...
        class Other(Leaf):  # Error reported by type checker
            ...
    
    There is no runtime checking of these properties. The decorator
    attempts to set the ``__final__`` attribute to ``True`` on the decorated
    object to allow runtime introspection.
    """
    pass

def getLogger(name=None): # reliably restored by inspect
    """
    Return a logger with the specified name, creating it if necessary.
    
    If no name is specified, return the root logger.
    """
    pass

def is_emoticon(*args, **kwargs): # real signature unknown
    pass

def is_punctuation(*args, **kwargs): # real signature unknown
    pass

def is_separator(*args, **kwargs): # real signature unknown
    pass

def is_suspiciously_successive_range(*args, **kwargs): # real signature unknown
    pass

def is_symbol(*args, **kwargs): # real signature unknown
    pass

def lru_cache(maxsize=128, typed=False): # reliably restored by inspect
    """
    Least-recently-used cache decorator.
    
    If *maxsize* is set to None, the LRU features are disabled and the cache
    can grow without bound.
    
    If *typed* is True, arguments of different types will be cached separately.
    For example, f(decimal.Decimal("3.0")) and f(3.0) will be treated as
    distinct calls with distinct results. Some types such as str and int may
    be cached separately even when typed is false.
    
    Arguments to the cached function must be hashable.
    
    View the cache statistics named tuple (hits, misses, maxsize, currsize)
    with f.cache_info().  Clear the cache and statistics with f.cache_clear().
    Access the underlying function with f.__wrapped__.
    
    See:  https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)
    """
    pass

def mess_ratio(*args, **kwargs): # real signature unknown
    pass

def remove_accent(*args, **kwargs): # real signature unknown
    pass

def unicode_range(*args, **kwargs): # real signature unknown
    """ Retrieve the Unicode range official name from a single character. """
    pass

def _character_flags(*args, **kwargs): # real signature unknown
    """ Compute all name-based classification flags with a single unicodedata.name() call. """
    pass

# classes

class MessDetectorPlugin(object):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = ()


class ArabicIsolatedFormPlugin(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _isolated_form_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_character_count',
        '_isolated_form_count',
    )


class ArchaicUpperLowerPlugin(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buf = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count_since_last_sep = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _current_ascii_only = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_alpha_seen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_alpha_seen_lower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_alpha_seen_upper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _successive_upper_lower_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _successive_upper_lower_count_final = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_buf',
        '_character_count_since_last_sep',
        '_successive_upper_lower_count',
        '_successive_upper_lower_count_final',
        '_character_count',
        '_last_alpha_seen',
        '_last_alpha_seen_upper',
        '_last_alpha_seen_lower',
        '_current_ascii_only',
    )


class CharInfo(object):
    # no doc
    def update(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    accentuated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    alpha = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    case_variable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    character = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digit = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_arabic = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_ascii = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_cjk = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    is_glyph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    latin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    lower = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    printable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    punct = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    space = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sym = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    upper = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        'character',
        'printable',
        'alpha',
        'upper',
        'lower',
        'space',
        'digit',
        'is_ascii',
        'case_variable',
        'flags',
        'accentuated',
        'latin',
        'is_cjk',
        'is_arabic',
        'is_glyph',
        'punct',
        'sym',
    )


class CjkUncommonPlugin(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _uncommon_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_character_count',
        '_uncommon_count',
    )


class SuperWeirdWordPlugin(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _bad_character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _bad_word_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buffer_accent_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buffer_glyph_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buffer_last_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buffer_last_char_accentuated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buffer_length = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _buffer_upper_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _foreign_long_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _foreign_long_watch = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _is_current_word_bad = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _word_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_word_count',
        '_bad_word_count',
        '_foreign_long_count',
        '_is_current_word_bad',
        '_foreign_long_watch',
        '_character_count',
        '_bad_character_count',
        '_buffer_length',
        '_buffer_last_char',
        '_buffer_last_char_accentuated',
        '_buffer_accent_count',
        '_buffer_glyph_count',
        '_buffer_upper_count',
    )


class SuspiciousDuplicateAccentPlugin(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_latin_character = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_was_accentuated = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _successive_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_successive_count',
        '_character_count',
        '_last_latin_character',
        '_last_was_accentuated',
    )


class SuspiciousRange(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_printable_range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_printable_seen = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _suspicious_successive_range_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_suspicious_successive_range_count',
        '_character_count',
        '_last_printable_seen',
        '_last_printable_range',
    )


class TooManyAccentuatedPlugin(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _accentuated_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_character_count',
        '_accentuated_count',
    )


class TooManySymbolOrPunctuationPlugin(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _frenzy_symbol_in_word = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _last_printable_char = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _punctuation_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _symbol_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_punctuation_count',
        '_symbol_count',
        '_character_count',
        '_last_printable_char',
        '_frenzy_symbol_in_word',
    )


class UnprintablePlugin(MessDetectorPlugin):
    # no doc
    def feed_info(self, *args, **kwargs): # real signature unknown
        pass

    def reset(self, *args, **kwargs): # real signature unknown
        pass

    def __getstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __internal_mypyc_setup(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _character_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _unprintable_count = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __mypyc_attrs__ = (
        '_unprintable_count',
        '_character_count',
    )


# variables with complex values

annotations = None # (!) real value is "_Feature((3, 7, 0, 'beta', 1), None, 16777216)"

COMMON_CJK_CHARACTERS = None # (!) real value is "frozenset({'?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?', '?'})"

COMMON_SAFE_ASCII_CHARACTERS = None # (!) real value is 'frozenset({\';\', \'-\', \'[\', \'/\', \'>\', \'}\', \'{\', \',\', \'|\', \'&\', \')\', \'=\', \'<\', \':\', \'(\', \']\', \'"\'})'

UNICODE_SECONDARY_RANGE_KEYWORD = [
    'Supplement',
    'Extended',
    'Extensions',
    'Modifier',
    'Marks',
    'Punctuation',
    'Symbols',
    'Forms',
    'Operators',
    'Miscellaneous',
    'Drawing',
    'Block',
    'Shapes',
    'Supplemental',
    'Tags',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F2202AE050>'

__spec__ = None # (!) real value is "ModuleSpec(name='charset_normalizer.md', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001F2202AE050>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\charset_normalizer\\\\md.cp314-win_amd64.pyd')"

