# encoding: utf-8
# module fontTools.feaLib.lexer
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\fontTools\feaLib\lexer.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import re as re # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\re\__init__.py
import os as os # C:\Users\T14\AppData\Local\Programs\Python\Python314\Lib\os.py
import fontTools.feaLib.error as __fontTools_feaLib_error


# no functions
# classes

class FeatureLibError(Exception):
    # no doc
    def __init__(self, message, location=None): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __firstlineno__ = 1
    __static_attributes__ = (
        'location',
    )


class FeatureLibLocation(tuple):
    """ A location in a feature file """
    def _asdict(self): # reliably restored by inspect
        """ Return a new dict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new FeatureLibLocation object from a sequence or iterable """
        pass

    def _replace(self, **kwds): # reliably restored by inspect
        """ Return a new FeatureLibLocation object replacing specified fields with new values """
        pass

    def __annotate_func__(format): # reliably restored by inspect
        # no doc
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, file, line, column): # reliably restored by inspect
        """ Create new instance of FeatureLibLocation(file, line, column) """
        pass

    def __replace__(self, **kwds): # reliably restored by inspect
        """ Return a new FeatureLibLocation object replacing specified fields with new values """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    column = _tuplegetter(2, 'Alias for field number 2')
    file = _tuplegetter(0, 'Alias for field number 0')
    line = _tuplegetter(1, 'Alias for field number 1')
    _fields = (
        'file',
        'line',
        'column',
    )
    _field_defaults = {}
    __classdictcell__ = None # (!) real value is '<cell at 0x000001A4A8EFA830: dict object at 0x000001A4AA78E540>'
    __firstlineno__ = 4
    __match_args__ = (
        'file',
        'line',
        'column',
    )
    __orig_bases__ = (
        None, # (!) real value is '<function NamedTuple at 0x000001A4AA748BF0>'
    )
    __slots__ = ()
    __static_attributes__ = ()


class IncludedFeaNotFound(__fontTools_feaLib_error.FeatureLibError):
    # no doc
    def __init__(self, message, location=None): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __firstlineno__ = 14
    __static_attributes__ = ()


class IncludingLexer(object):
    """
    A Lexer that follows include statements.
    
        The OpenType feature file specification states that due to
        historical reasons, relative imports should be resolved in this
        order:
    
        1. If the source font is UFO format, then relative to the UFO's
           font directory
        2. relative to the top-level include file
        3. relative to the parent include file
    
        We only support 1 (via includeDir) and 2.
    """
    @staticmethod
    def make_lexer_(file_or_path): # real signature unknown; restored from __doc__
        """ IncludingLexer.make_lexer_(file_or_path) """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ IncludingLexer.next(self) """
        pass

    def scan_anonymous_block(self, tag): # real signature unknown; restored from __doc__
        """ IncludingLexer.scan_anonymous_block(self, tag) """
        pass

    def __init__(self, featurefile, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        IncludingLexer.__init__(self, featurefile, *, includeDir=None)
        
        Initializes an IncludingLexer.
        
        Behavior:
            If includeDir is passed, it will be used to determine the top-level
            include directory to use for all encountered include statements. If it is
            not passed, ``os.path.dirname(featurefile)`` will be considered the
            include directory.
        """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ IncludingLexer.__iter__(self) """
        pass

    def __next__(self): # real signature unknown; restored from __doc__
        """ IncludingLexer.__next__(self) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'fontTools.feaLib.lexer\', \'__doc__\': "A Lexer that follows include statements.\\n\\n    The OpenType feature file specification states that due to\\n    historical reasons, relative imports should be resolved in this\\n    order:\\n\\n    1. If the source font is UFO format, then relative to the UFO\'s\\n       font directory\\n    2. relative to the top-level include file\\n    3. relative to the parent include file\\n\\n    We only support 1 (via includeDir) and 2.\\n    ", \'__init__\': <cyfunction IncludingLexer.__init__ at 0x000001A4AA7D3A20>, \'__iter__\': <cyfunction IncludingLexer.__iter__ at 0x000001A4AA7D3BB0>, \'next\': <cyfunction IncludingLexer.next at 0x000001A4AA776150>, \'__next__\': <cyfunction IncludingLexer.__next__ at 0x000001A4AA7762D0>, \'make_lexer_\': <staticmethod(<cyfunction IncludingLexer.make_lexer_ at 0x000001A4AA7AC1C0>)>, \'scan_anonymous_block\': <cyfunction IncludingLexer.scan_anonymous_block at 0x000001A4A8E3A570>, \'__dict__\': <attribute \'__dict__\' of \'IncludingLexer\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'IncludingLexer\' objects>})'


class Lexer(object):
    # no doc
    def location_(self): # real signature unknown; restored from __doc__
        """ Lexer.location_(self) """
        pass

    def next(self): # real signature unknown; restored from __doc__
        """ Lexer.next(self) """
        pass

    def next_(self): # real signature unknown; restored from __doc__
        """ Lexer.next_(self) """
        pass

    def scan_anonymous_block(self, tag): # real signature unknown; restored from __doc__
        """ Lexer.scan_anonymous_block(self, tag) """
        pass

    def scan_over_(self, valid): # real signature unknown; restored from __doc__
        """ Lexer.scan_over_(self, valid) """
        pass

    def scan_until_(self, stop_at): # real signature unknown; restored from __doc__
        """ Lexer.scan_until_(self, stop_at) """
        pass

    def __init__(self, text, filename): # real signature unknown; restored from __doc__
        """ Lexer.__init__(self, text, filename) """
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ Lexer.__iter__(self) """
        pass

    def __next__(self): # real signature unknown; restored from __doc__
        """ Lexer.__next__(self) """
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    ANONYMOUS_BLOCK = 'ANONYMOUS_BLOCK'
    CHAR_DIGIT_ = '0123456789'
    CHAR_HEXDIGIT_ = '0123456789ABCDEFabcdef'
    CHAR_LETTER_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    CHAR_NAME_CONTINUATION_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.+*:^~!/-'
    CHAR_NAME_START_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_+*:.^~!\\'
    CHAR_NEWLINE_ = '\r\n'
    CHAR_SYMBOL_ = ",;:-+'{}[]<>()="
    CHAR_WHITESPACE_ = ' \t'
    CID = 'CID'
    COMMENT = 'COMMENT'
    FILENAME = 'FILENAME'
    FLOAT = 'FLOAT'
    GLYPHCLASS = 'GLYPHCLASS'
    HEXADECIMAL = 'HEXADECIMAL'
    MODE_FILENAME_ = 'FILENAME'
    MODE_NORMAL_ = 'NORMAL'
    NAME = 'NAME'
    NEWLINE = 'NEWLINE'
    NUMBER = 'NUMBER'
    NUMBERS = (
        'NUMBER',
        'HEXADECIMAL',
        'OCTAL',
    )
    OCTAL = 'OCTAL'
    RE_GLYPHCLASS = re.compile('^[A-Za-z_0-9.\\-]+$')
    STRING = 'STRING'
    SYMBOL = 'SYMBOL'
    __dict__ = None # (!) real value is 'mappingproxy({\'__module__\': \'fontTools.feaLib.lexer\', \'NUMBER\': \'NUMBER\', \'HEXADECIMAL\': \'HEXADECIMAL\', \'OCTAL\': \'OCTAL\', \'NUMBERS\': (\'NUMBER\', \'HEXADECIMAL\', \'OCTAL\'), \'FLOAT\': \'FLOAT\', \'STRING\': \'STRING\', \'NAME\': \'NAME\', \'FILENAME\': \'FILENAME\', \'GLYPHCLASS\': \'GLYPHCLASS\', \'CID\': \'CID\', \'SYMBOL\': \'SYMBOL\', \'COMMENT\': \'COMMENT\', \'NEWLINE\': \'NEWLINE\', \'ANONYMOUS_BLOCK\': \'ANONYMOUS_BLOCK\', \'CHAR_WHITESPACE_\': \' \\t\', \'CHAR_NEWLINE_\': \'\\r\\n\', \'CHAR_SYMBOL_\': ",;:-+\'{}[]<>()=", \'CHAR_DIGIT_\': \'0123456789\', \'CHAR_HEXDIGIT_\': \'0123456789ABCDEFabcdef\', \'CHAR_LETTER_\': \'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\', \'CHAR_NAME_START_\': \'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_+*:.^~!\\\\\', \'CHAR_NAME_CONTINUATION_\': \'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.+*:^~!/-\', \'RE_GLYPHCLASS\': re.compile(\'^[A-Za-z_0-9.\\\\-]+$\'), \'MODE_NORMAL_\': \'NORMAL\', \'MODE_FILENAME_\': \'FILENAME\', \'__init__\': <cyfunction Lexer.__init__ at 0x000001A4A8F11130>, \'__iter__\': <cyfunction Lexer.__iter__ at 0x000001A4A8F11310>, \'next\': <cyfunction Lexer.next at 0x000001A4AA7117E0>, \'__next__\': <cyfunction Lexer.__next__ at 0x000001A4AA711B80>, \'location_\': <cyfunction Lexer.location_ at 0x000001A4AA738050>, \'next_\': <cyfunction Lexer.next_ at 0x000001A4AA738210>, \'scan_over_\': <cyfunction Lexer.scan_over_ at 0x000001A4AA77DEB0>, \'scan_until_\': <cyfunction Lexer.scan_until_ at 0x000001A4AA7A41F0>, \'scan_anonymous_block\': <cyfunction Lexer.scan_anonymous_block at 0x000001A4AA7A4870>, \'__dict__\': <attribute \'__dict__\' of \'Lexer\' objects>, \'__weakref__\': <attribute \'__weakref__\' of \'Lexer\' objects>, \'__doc__\': None})'


class NonIncludingLexer(IncludingLexer):
    """ Lexer that does not follow `include` statements, emits them as-is. """
    def __init__(self, featurefile, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        IncludingLexer.__init__(self, featurefile, *, includeDir=None)
        
        Initializes an IncludingLexer.
        
        Behavior:
            If includeDir is passed, it will be used to determine the top-level
            include directory to use for all encountered include statements. If it is
            not passed, ``os.path.dirname(featurefile)`` will be considered the
            include directory.
        """
        pass

    def __next__(self): # real signature unknown; restored from __doc__
        """ NonIncludingLexer.__next__(self) """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A4AA772AD0>'

__spec__ = None # (!) real value is "ModuleSpec(name='fontTools.feaLib.lexer', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001A4AA772AD0>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\fontTools\\\\feaLib\\\\lexer.cp314-win_amd64.pyd')"

__test__ = {}

