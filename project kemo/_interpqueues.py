# encoding: utf-8
# module _interpqueues
# from (built-in)
# by generator 1.147
"""
This module provides primitive operations to manage Python interpreters.
The 'interpreters' module provides a more convenient interface.
"""

# imports
import concurrent.interpreters as __concurrent_interpreters


# functions

def bind(qid): # real signature unknown; restored from __doc__
    """
    bind(qid)
    
    Take a reference to the identified queue.
    The queue is not destroyed until there are no references left.
    """
    pass

def create(maxsize, unboundop, fallback): # real signature unknown; restored from __doc__
    """
    create(maxsize, unboundop, fallback) -> qid
    
    Create a new cross-interpreter queue and return its unique generated ID.
    It is a new reference as though bind() had been called on the queue.
    
    The caller is responsible for calling destroy() for the new queue
    before the runtime is finalized.
    """
    pass

def destroy(qid): # real signature unknown; restored from __doc__
    """
    destroy(qid)
    
    Clear and destroy the queue.  Afterward attempts to use the queue
    will behave as though it never existed.
    """
    pass

def get(qid): # real signature unknown; restored from __doc__
    """
    get(qid) -> (obj, unboundop)
    
    Return a new object from the data at the front of the queue.
    The unbound op is also returned.
    
    If there is nothing to receive then raise QueueEmpty.
    """
    pass

def get_count(qid): # real signature unknown; restored from __doc__
    """
    get_count(qid)
    
    Return the number of items in the queue.
    """
    pass

def get_maxsize(qid): # real signature unknown; restored from __doc__
    """
    get_maxsize(qid)
    
    Return the maximum number of items in the queue.
    """
    pass

def get_queue_defaults(qid): # real signature unknown; restored from __doc__
    """
    get_queue_defaults(qid)
    
    Return the queue's default values, set when it was created.
    """
    pass

def is_full(qid): # real signature unknown; restored from __doc__
    """
    is_full(qid)
    
    Return true if the queue has a maxsize and has reached it.
    """
    pass

def list_all(): # real signature unknown; restored from __doc__
    """
    list_all() -> [(qid, unboundop, fallback)]
    
    Return the list of IDs for all queues.
    Each corresponding default unbound op and fallback is also included.
    """
    pass

def put(qid, obj): # real signature unknown; restored from __doc__
    """
    put(qid, obj)
    
    Add the object's data to the queue.
    """
    pass

def release(qid): # real signature unknown; restored from __doc__
    """
    release(qid)
    
    Release a reference to the queue.
    The queue is destroyed once there are no references left.
    """
    pass

def _register_heap_types(*args, **kwargs): # real signature unknown
    pass

# classes

class QueueError(RuntimeError):
    """ Indicates that a queue-related error happened. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



class QueueNotFoundError(__concurrent_interpreters.QueueError):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 974, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000001BF7FAEAB90>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000001BF7FAEAC40>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000001BF7FAEACF0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000001BF7FAEAE50>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000001BF7FAEAFB0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000001BF7FAEB110>)>, 'load_module': <classmethod(<function _load_module_shim at 0x000001BF7FAE9DD0>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 974
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_interpqueues', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

