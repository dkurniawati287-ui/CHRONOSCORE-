# encoding: utf-8
# module _types
# from (built-in)
# by generator 1.147
""" Define names for built-in types. """
# no imports

# no functions
# classes

class AsyncGeneratorType(object):
    # no doc
    def aclose(self): # real signature unknown; restored from __doc__
        """ aclose() -> raise GeneratorExit inside generator. """
        pass

    def asend(self, v): # real signature unknown; restored from __doc__
        """ asend(v) -> send 'v' in generator. """
        pass

    def athrow(self, value): # real signature unknown; restored from __doc__
        """
        athrow(value)
        athrow(type[,value[,tb]])
        
        raise exception in generator.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        pass

    def __aiter__(self, *args, **kwargs): # real signature unknown
        """ Return an awaitable, that resolves in asynchronous iterator. """
        pass

    def __anext__(self, *args, **kwargs): # real signature unknown
        """ Return a value or raise StopAsyncIteration. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        """ Called when the instance is about to be destroyed. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ gen.__sizeof__() -> size of gen in memory, in bytes """
        pass

    ag_await = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being awaited on, or None"""

    ag_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ag_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ag_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ag_suspended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'async_generator'
    __qualname__ = 'async_generator'


class BuiltinMethodType(object):
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __self__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'builtin_function_or_method'
    __qualname__ = 'builtin_function_or_method'
    __text_signature__ = None


BuiltinFunctionType = BuiltinMethodType


class CapsuleType(object):
    """
    Capsule objects let you wrap a C "void *" pointer in a Python
    object.  They're a way of passing data through the Python interpreter
    without creating your own custom type.
    
    Capsules are used for communication between extension modules.
    They provide a way for an extension module to export a C interface
    to other extension modules, so that extension modules can use the
    Python import mechanism to link to one another.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class CellType(object):
    """
    Create a new cell object.
    
      contents
        the contents of the cell. If not specified, the cell will be empty,
        and 
     further attempts to access its cell_contents attribute will
        raise a ValueError.
    """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    cell_contents = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __hash__ = None


class ClassMethodDescriptorType(object):
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __objclass__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'classmethod_descriptor'
    __qualname__ = 'classmethod_descriptor'
    __text_signature__ = None


class CodeType(object):
    """ Create a code object.  Not for the faint of heart. """
    def co_branches(self, *args, **kwargs): # real signature unknown
        pass

    def co_lines(self, *args, **kwargs): # real signature unknown
        pass

    def co_positions(self, *args, **kwargs): # real signature unknown
        pass

    def replace(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the code object with new values for the specified fields. """
        pass

    def _varname_from_oparg(self, *args, **kwargs): # real signature unknown
        """
        (internal-only) Return the local variable name for the given oparg.
        
        WARNING: this method is for internal use only and may change or go away.
        """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __replace__(self, *args, **kwargs): # real signature unknown
        """ The same as replace(). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        pass

    co_argcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_cellvars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_consts = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_exceptiontable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_firstlineno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_flags = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_freevars = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_kwonlyargcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_linetable = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_lnotab = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_nlocals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_posonlyargcount = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_qualname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_stacksize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    co_varnames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _co_code_adaptive = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class CoroutineType(object):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> raise GeneratorExit inside coroutine. """
        pass

    def send(self, arg): # real signature unknown; restored from __doc__
        """
        send(arg) -> send 'arg' into coroutine,
        return next iterated value or raise StopIteration.
        """
        pass

    def throw(self, value): # real signature unknown; restored from __doc__
        """
        throw(value)
        throw(type[,value[,traceback]])
        
        Raise exception in coroutine, return next iterated value or raise
        StopIteration.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        pass

    def __await__(self, *args, **kwargs): # real signature unknown
        """ Return an iterator to be used in await expression. """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        """ Called when the instance is about to be destroyed. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ gen.__sizeof__() -> size of gen in memory, in bytes """
        pass

    cr_await = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being awaited on, or None"""

    cr_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_origin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cr_suspended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'coroutine'
    __qualname__ = 'coroutine'


class EllipsisType(object):
    """ The type of the Ellipsis singleton. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class FrameType(object):
    # no doc
    def clear(self, *args, **kwargs): # real signature unknown
        """ Clear all references held by the frame. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self, *args, **kwargs): # real signature unknown
        """ Return the size of the frame in memory, in bytes. """
        pass

    f_back = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_builtins = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the built-in variables in the frame."""

    f_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the code object being executed in this frame."""

    f_generator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the generator or coroutine associated with this frame, or None."""

    f_globals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the global variables in the frame."""

    f_lasti = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the index of the last attempted instruction in the frame."""

    f_lineno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the current line number in the frame."""

    f_locals = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the mapping used by the frame to look up local variables."""

    f_trace = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return the trace function for this frame, or None if no trace function is set."""

    f_trace_lines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    f_trace_opcodes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Return True if opcode tracing is enabled, False otherwise."""



class LambdaType(object):
    """
    Create a function object.
    
      code
        a code object
      globals
        the globals dictionary
      name
        a string that overrides the name from the code object
      argdefs
        a tuple that specifies the default argument values
      closure
        a tuple that supplies the bindings for free variables
      kwdefaults
        a dictionary that specifies the default keyword argument values
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __annotate__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the code object for a function."""

    __annotations__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Dict of annotations in a function object."""

    __builtins__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __closure__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __code__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __defaults__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __globals__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __kwdefaults__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __type_params__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the declared type parameters for a function."""


    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FF81A410B80>, '__repr__': <slot wrapper '__repr__' of 'function' objects>, '__call__': <slot wrapper '__call__' of 'function' objects>, '__get__': <slot wrapper '__get__' of 'function' objects>, '__closure__': <member '__closure__' of 'function' objects>, '__doc__': <member '__doc__' of 'function' objects>, '__globals__': <member '__globals__' of 'function' objects>, '__module__': <member '__module__' of 'function' objects>, '__builtins__': <member '__builtins__' of 'function' objects>, '__code__': <attribute '__code__' of 'function' objects>, '__defaults__': <attribute '__defaults__' of 'function' objects>, '__kwdefaults__': <attribute '__kwdefaults__' of 'function' objects>, '__annotations__': <attribute '__annotations__' of 'function' objects>, '__annotate__': <attribute '__annotate__' of 'function' objects>, '__dict__': <attribute '__dict__' of 'function' objects>, '__name__': <attribute '__name__' of 'function' objects>, '__qualname__': <attribute '__qualname__' of 'function' objects>, '__type_params__': <attribute '__type_params__' of 'function' objects>})"
    __name__ = 'function'
    __qualname__ = 'function'


FunctionType = LambdaType


class GeneratorType(object):
    # no doc
    def close(self): # real signature unknown; restored from __doc__
        """ close() -> raise GeneratorExit inside generator. """
        pass

    def send(self, arg): # real signature unknown; restored from __doc__
        """
        send(arg) -> send 'arg' into generator,
        return next yielded value or raise StopIteration.
        """
        pass

    def throw(self, value): # real signature unknown; restored from __doc__
        """
        throw(value)
        throw(type[,value[,tb]])
        
        Raise exception in generator, return next yielded value or raise
        StopIteration.
        the (type, val, tb) signature is deprecated, 
        and may be removed in a future version of Python.
        """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        """ Called when the instance is about to be destroyed. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __next__(self, *args, **kwargs): # real signature unknown
        """ Implement next(self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __sizeof__(self): # real signature unknown; restored from __doc__
        """ gen.__sizeof__() -> size of gen in memory, in bytes """
        pass

    gi_code = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_running = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_suspended = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    gi_yieldfrom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """object being iterated by yield from, or None"""


    __name__ = 'generator'
    __qualname__ = 'generator'


class GenericAlias(object):
    """
    Represent a PEP 585 generic type
    
    E.g. for t = list[int], t.__origin__ is list and t.__args__ is (int,).
    """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __instancecheck__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mro_entries__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __subclasscheck__(self, *args, **kwargs): # real signature unknown
        pass

    __args__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __origin__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __parameters__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type variables in the GenericAlias."""

    __typing_unpacked_tuple_args__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __unpacked__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class GetSetDescriptorType(object):
    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass

    __objclass__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'getset_descriptor'
    __qualname__ = 'getset_descriptor'


class MappingProxyType(object):
    """ Read-only proxy of a mapping. """
    def copy(self): # real signature unknown; restored from __doc__
        """ D.copy() -> a shallow copy of D """
        pass

    def get(self, *args, **kwargs): # real signature unknown
        """ Return the value for key if key is in the mapping, else default. """
        pass

    def items(self): # real signature unknown; restored from __doc__
        """ D.items() -> a set-like object providing a view on D's items """
        pass

    def keys(self): # real signature unknown; restored from __doc__
        """ D.keys() -> a set-like object providing a view on D's keys """
        pass

    def values(self): # real signature unknown; restored from __doc__
        """ D.values() -> an object providing a view on D's values """
        pass

    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __contains__(self, *args, **kwargs): # real signature unknown
        """ Return bool(key in self). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __ior__(self, *args, **kwargs): # real signature unknown
        """ Return self|=value. """
        pass

    def __iter__(self, *args, **kwargs): # real signature unknown
        """ Implement iter(self). """
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __reversed__(self): # real signature unknown; restored from __doc__
        """ D.__reversed__() -> reverse iterator """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass


class MemberDescriptorType(object):
    def __delete__(self, *args, **kwargs): # real signature unknown
        """ Delete an attribute of instance. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __set__(self, *args, **kwargs): # real signature unknown
        """ Set an attribute of instance to value. """
        pass

    __objclass__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'member_descriptor'
    __qualname__ = 'member_descriptor'


class MethodDescriptorType(object):
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __objclass__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'method_descriptor'
    __qualname__ = 'method_descriptor'
    __text_signature__ = None


class MethodType(object):
    """ Create a bound instance method object. """
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __func__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the function (or other callable) implementing a method"""

    __self__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """the instance to which a method is bound"""



class MethodWrapperType(object):
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __objclass__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __self__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'method-wrapper'
    __qualname__ = 'method-wrapper'
    __text_signature__ = None


class ModuleType(object):
    """
    Create a module object.
    
    The name must be a string; the optional doc argument can have any type.
    """
    def __dir__(self): # real signature unknown; restored from __doc__
        """
        __dir__() -> list
        specialized dir() implementation
        """
        return []

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __annotate__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __annotations__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FF81A413280>, '__repr__': <slot wrapper '__repr__' of 'module' objects>, '__getattribute__': <slot wrapper '__getattribute__' of 'module' objects>, '__init__': <slot wrapper '__init__' of 'module' objects>, '__dir__': <method '__dir__' of 'module' objects>, '__dict__': <member '__dict__' of 'module' objects>, '__annotations__': <attribute '__annotations__' of 'module' objects>, '__annotate__': <attribute '__annotate__' of 'module' objects>, '__doc__': 'Create a module object.\\n\\nThe name must be a string; the optional doc argument can have any type.'})"


class NoneType(object):
    """ The type of the None singleton. """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class NotImplementedType(object):
    """ The type of the NotImplemented singleton. """
    def __bool__(self, *args, **kwargs): # real signature unknown
        """ True if self else False """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass


class SimpleNamespace(object):
    """ A simple attribute-based namespace. """
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        """ Return state information for pickling """
        pass

    def __replace__(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the namespace object with new values for the specified attributes. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __dict__ = None # (!) real value is "mappingproxy({'__new__': <built-in method __new__ of type object at 0x00007FF81A413420>, '__repr__': <slot wrapper '__repr__' of 'types.SimpleNamespace' objects>, '__lt__': <slot wrapper '__lt__' of 'types.SimpleNamespace' objects>, '__le__': <slot wrapper '__le__' of 'types.SimpleNamespace' objects>, '__eq__': <slot wrapper '__eq__' of 'types.SimpleNamespace' objects>, '__ne__': <slot wrapper '__ne__' of 'types.SimpleNamespace' objects>, '__gt__': <slot wrapper '__gt__' of 'types.SimpleNamespace' objects>, '__ge__': <slot wrapper '__ge__' of 'types.SimpleNamespace' objects>, '__init__': <slot wrapper '__init__' of 'types.SimpleNamespace' objects>, '__reduce__': <method '__reduce__' of 'types.SimpleNamespace' objects>, '__replace__': <method '__replace__' of 'types.SimpleNamespace' objects>, '__dict__': <member '__dict__' of 'types.SimpleNamespace' objects>, '__doc__': 'A simple attribute-based namespace.', '__hash__': None})"
    __hash__ = None


class TracebackType(object):
    """ Create a new traceback object. """
    def __dir__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    tb_frame = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tb_lasti = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tb_lineno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tb_next = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class UnionType(object):
    """
    Represent a union type
    
    E.g. for int | str
    """
    @classmethod
    def __class_getitem__(cls, *args, **kwargs): # real signature unknown
        """ See PEP 585 """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mro_entries__(self, *args, **kwargs): # real signature unknown
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    __args__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    __origin__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Always returns the type"""

    __parameters__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Type variables in the types.UnionType."""


    __name__ = 'Union'
    __qualname__ = 'Union'


class WrapperDescriptorType(object):
    def __call__(self, *args, **kwargs): # real signature unknown
        """ Call self as a function. """
        pass

    def __get__(self, *args, **kwargs): # real signature unknown
        """ Return an attribute of instance, which is of type owner. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    __objclass__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __name__ = 'wrapper_descriptor'
    __qualname__ = 'wrapper_descriptor'
    __text_signature__ = None


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
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__firstlineno__': 974, '__doc__': 'Meta path import for built-in modules.\\n\\nAll methods are either class or static methods to avoid the need to\\ninstantiate the class.\\n\\n', '_ORIGIN': 'built-in', 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x000001986451AB90>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x000001986451AC40>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x000001986451ACF0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x000001986451AE50>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x000001986451AFB0>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x000001986451B110>)>, 'load_module': <classmethod(<function _load_module_shim at 0x0000019864519DD0>)>, '__static_attributes__': (), '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"
    __firstlineno__ = 974
    __static_attributes__ = ()


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_types', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

