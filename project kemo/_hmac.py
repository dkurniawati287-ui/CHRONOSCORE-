# encoding: utf-8
# module _hmac
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

_GIL_MINSIZE = 2048

# functions

def compute_blake2b_32(*args, **kwargs): # real signature unknown
    pass

def compute_blake2s_32(*args, **kwargs): # real signature unknown
    pass

def compute_digest(*args, **kwargs): # real signature unknown
    pass

def compute_md5(*args, **kwargs): # real signature unknown
    pass

def compute_sha1(*args, **kwargs): # real signature unknown
    pass

def compute_sha224(*args, **kwargs): # real signature unknown
    pass

def compute_sha256(*args, **kwargs): # real signature unknown
    pass

def compute_sha384(*args, **kwargs): # real signature unknown
    pass

def compute_sha3_224(*args, **kwargs): # real signature unknown
    pass

def compute_sha3_256(*args, **kwargs): # real signature unknown
    pass

def compute_sha3_384(*args, **kwargs): # real signature unknown
    pass

def compute_sha3_512(*args, **kwargs): # real signature unknown
    pass

def compute_sha512(*args, **kwargs): # real signature unknown
    pass

def new(*args, **kwargs): # real signature unknown
    """ Return a new HMAC object. """
    pass

# classes

class HMAC(object):
    # no doc
    def copy(self, clone): # real signature unknown; restored from __doc__
        """ Return a copy ("clone") of the HMAC object. """
        pass

    def digest(self, *args, **kwargs): # real signature unknown
        """
        Return the digest of the bytes passed to the update() method so far.
        
        This method may raise a MemoryError.
        """
        pass

    def hexdigest(self, *args, **kwargs): # real signature unknown
        """
        Return hexadecimal digest of the bytes passed to the update() method so far.
        
        This may be used to exchange the value safely in email or other non-binary
        environments.
        
        This method may raise a MemoryError.
        """
        pass

    def update(self, *args, **kwargs): # real signature unknown
        """ Update the HMAC object with the given message. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    block_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    digest_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UnknownHashError(ValueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class __loader__(object):
    """
    Meta path import for built-in modules.
    
    All methods are either class or static methods to avoid the need to
    instantiate the class.
    """
    @staticmethod
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    @staticmethod
    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
        This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 974, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000001643A59AB90>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000001643A59AC40>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000001643A59ACF0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000001643A59AE50>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000001643A59AFB0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000001643A59B110>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000001643A599DD0>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 974
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_hmac', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

