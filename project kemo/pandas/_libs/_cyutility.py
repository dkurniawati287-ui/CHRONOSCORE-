# encoding: utf-8
# module pandas._libs._cyutility
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\pandas\_libs\_cyutility.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import _cyutility as ___cyutility


# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class array(object):
    # no doc
    def count(self, value): # reliably restored by inspect
        """ S.count(value) -> integer -- return number of occurrences of value """
        pass

    def index(self, value, start=0, stop=None): # reliably restored by inspect
        """
        S.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        
        Supporting start and stop arguments is optional, but
        recommended.
        """
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getattribute__(self, *args, **kwargs): # real signature unknown
        """ Return getattr(self, name). """
        pass

    def __getattr__(self, *args, **kwargs): # real signature unknown
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    memview = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002A05E0F5DA0>'


class Enum(object):
    # no doc
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

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass


class memoryview(object):
    # no doc
    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def copy_fortran(self, *args, **kwargs): # real signature unknown
        pass

    def is_c_contig(self, *args, **kwargs): # real signature unknown
        pass

    def is_f_contig(self, *args, **kwargs): # real signature unknown
        pass

    def __buffer__(self, *args, **kwargs): # real signature unknown
        """ Return a buffer object that exposes the underlying memory of the object. """
        pass

    def __delitem__(self, *args, **kwargs): # real signature unknown
        """ Delete self[key]. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
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

    def __setitem__(self, *args, **kwargs): # real signature unknown
        """ Set self[key] to value. """
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    base = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    itemsize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbytes = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ndim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    shape = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    strides = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    suboffsets = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    T = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002A05E0F6480>'


class _memoryviewslice(___cyutility.memoryview):
    """ Internal class for passing memoryview slices to Python """
    def count(self, value): # reliably restored by inspect
        """ S.count(value) -> integer -- return number of occurrences of value """
        pass

    def index(self, value, start=0, stop=None): # reliably restored by inspect
        """
        S.index(value, [start, [stop]]) -> integer -- return first index of value.
        Raises ValueError if the value is not present.
        
        Supporting start and stop arguments is optional, but
        recommended.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x000002A05E0F6610>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A05DF5A930>'

__pyx_capi__ = {
    '__Pyx_ParseKeywordDict': None, # (!) real value is '<capsule object "int(PyObject *kwds, PyObject ** const argnames[], PyObject *values[], Py_ssize_t num_pos_args, Py_ssize_t num_kwargs, const char* function_name, int ignore_unknown_kwargs)" at 0x000002A05E0F58A0>'
    '__Pyx_ParseKeywordDictToDict': None, # (!) real value is '<capsule object "int(PyObject *kwds, PyObject ** const argnames[], PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args, const char* function_name)" at 0x000002A05E0F5800>'
    '__Pyx_ParseKeywordsTuple': None, # (!) real value is '<capsule object "int(PyObject *kwds, PyObject * const *kwvalues, PyObject ** const argnames[], PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args, Py_ssize_t num_kwargs, const char* function_name, int ignore_unknown_kwargs)" at 0x000002A05E0F5760>'
    '__Pyx_PyUnicode_Join': None, # (!) real value is '<capsule object "PyObject*(PyObject** values, Py_ssize_t value_count, Py_ssize_t result_ulength, Py_UCS4 max_char)" at 0x000002A05E0F5710>'
    '__Pyx_Raise': None, # (!) real value is '<capsule object "void(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause)" at 0x000002A05E0F59E0>'
    '__Pyx_RejectKeywords': None, # (!) real value is '<capsule object "void(const char* function_name, PyObject *kwds)" at 0x000002A05E0F5A30>'
    '__Pyx_ValidateAndInit_memviewslice': None, # (!) real value is '<capsule object "int(int *axes_specs, int c_or_f_flag, int buf_flags, int ndim, const __Pyx_TypeInfo *dtype, __Pyx_BufFmt_StackElem stack[], __Pyx_memviewslice *memviewslice, PyObject *original_obj)" at 0x000002A05E0F5940>'
    '__Pyx__ArgTypeTest': None, # (!) real value is '<capsule object "int(PyObject *obj, PyTypeObject *type, const char *name, int exact)" at 0x000002A05E0F58F0>'
    '__Pyx__Import': None, # (!) real value is '<capsule object "PyObject *(PyObject *name, PyObject *const *imported_names, Py_ssize_t len_imported_names, PyObject *qualname, PyObject *moddict, int level)" at 0x000002A05E0F56C0>'
    '__pyx_collections_abc_Sequence': None, # (!) real value is '<capsule object "PyObject *" at 0x000002A05E0F45E0>'
    '__pyx_memoryview_thread_locks': None, # (!) real value is '<capsule object "PyThread_type_lock [8]" at 0x000002A05E0F4810>'
    '__pyx_memoryview_thread_locks_used': None, # (!) real value is '<capsule object "int" at 0x000002A05E0F48B0>'
    '__pyx_unpickle_Enum__set_state': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_MemviewEnum_obj *, PyObject *)" at 0x000002A05E0F4A90>'
    '_allocate_buffer': None, # (!) real value is '<capsule object "int (struct __pyx_array_obj *)" at 0x000002A05E0F5170>'
    '_copy_strided_to_strided': None, # (!) real value is '<capsule object "void (char *, Py_ssize_t *, char *, Py_ssize_t *, Py_ssize_t *, Py_ssize_t *, int, size_t)" at 0x000002A05E0F5580>'
    '_err': None, # (!) real value is '<capsule object "int (PyObject *, PyObject *)" at 0x000002A05E0F4EA0>'
    '_err_dim': None, # (!) real value is '<capsule object "int (PyObject *, PyObject *, int)" at 0x000002A05E0F4EF0>'
    '_err_extents': None, # (!) real value is '<capsule object "int (int, Py_ssize_t, Py_ssize_t)" at 0x000002A05E0F5120>'
    '_err_no_memory': None, # (!) real value is '<capsule object "int (void)" at 0x000002A05E0F51C0>'
    '_slice_assign_scalar': None, # (!) real value is '<capsule object "void (char *, Py_ssize_t *, Py_ssize_t *, int, size_t, void *)" at 0x000002A05E0F5530>'
    '_unellipsify': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int)" at 0x000002A05E0F4950>'
    'abs_py_ssize_t': None, # (!) real value is '<capsule object "Py_ssize_t (Py_ssize_t)" at 0x000002A05E0F4CC0>'
    'array_cwrapper': None, # (!) real value is '<capsule object "struct __pyx_array_obj *(PyObject *, Py_ssize_t, char *, char const *, char *)" at 0x000002A05E0F5210>'
    'assert_direct_dimensions': None, # (!) real value is '<capsule object "int (Py_ssize_t *, int)" at 0x000002A05E0F4F40>'
    'broadcast_leading': None, # (!) real value is '<capsule object "void (__Pyx_memviewslice *, int, int)" at 0x000002A05E0F5300>'
    'contiguous': None, # (!) real value is '<capsule object "PyObject *" at 0x000002A05E0F4680>'
    'copy_data_to_temp': None, # (!) real value is '<capsule object "void *(__Pyx_memviewslice *, __Pyx_memviewslice *, char, int)" at 0x000002A05E0F5670>'
    'copy_strided_to_strided': None, # (!) real value is '<capsule object "void (__Pyx_memviewslice *, __Pyx_memviewslice *, int, size_t)" at 0x000002A05E0F52B0>'
    'fill_contig_strides_array': None, # (!) real value is '<capsule object "Py_ssize_t (Py_ssize_t *, Py_ssize_t *, Py_ssize_t, int, char)" at 0x000002A05E0F4C20>'
    'format_from_typeinfo': None, # (!) real value is '<capsule object "PyObject *(__Pyx_TypeInfo const *)" at 0x000002A05E0F49F0>'
    'generic': None, # (!) real value is '<capsule object "PyObject *" at 0x000002A05E0F46D0>'
    'get_best_order': None, # (!) real value is '<capsule object "char (__Pyx_memviewslice *, int)" at 0x000002A05E0F4DB0>'
    'get_slice_from_memview': None, # (!) real value is '<capsule object "__Pyx_memviewslice *(struct __pyx_memoryview_obj *, __Pyx_memviewslice *)" at 0x000002A05E0F4D60>'
    'indirect': None, # (!) real value is '<capsule object "PyObject *" at 0x000002A05E0F4720>'
    'indirect_contiguous': None, # (!) real value is '<capsule object "PyObject *" at 0x000002A05E0F4770>'
    'memoryview_check': None, # (!) real value is '<capsule object "int (PyObject *)" at 0x000002A05E0F4E50>'
    'memoryview_copy': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_memoryview_obj *)" at 0x000002A05E0F4B30>'
    'memoryview_copy_contents': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice, __Pyx_memviewslice, int, int, int)" at 0x000002A05E0F5080>'
    'memoryview_copy_from_slice': None, # (!) real value is '<capsule object "PyObject *(struct __pyx_memoryview_obj *, __Pyx_memviewslice *)" at 0x000002A05E0F4B80>'
    'memoryview_cwrapper': None, # (!) real value is '<capsule object "PyObject *(PyObject *, int, int, __Pyx_TypeInfo const *)" at 0x000002A05E0F49A0>'
    'memoryview_fromslice': None, # (!) real value is '<capsule object "PyObject *(__Pyx_memviewslice, int, PyObject *(*)(char *), int (*)(char *, PyObject *), int)" at 0x000002A05E0F4A40>'
    'memview_slice': None, # (!) real value is '<capsule object "struct __pyx_memoryview_obj *(struct __pyx_memoryview_obj *, PyObject *)" at 0x000002A05E0F5260>'
    'pybuffer_index': None, # (!) real value is '<capsule object "char *(Py_buffer *, char *, Py_ssize_t, Py_ssize_t)" at 0x000002A05E0F4E00>'
    'refcount_copying': None, # (!) real value is '<capsule object "void (__Pyx_memviewslice *, int, int, int)" at 0x000002A05E0F5350>'
    'refcount_objects_in_slice': None, # (!) real value is '<capsule object "void (char *, Py_ssize_t *, Py_ssize_t *, int, int)" at 0x000002A05E0F53F0>'
    'refcount_objects_in_slice_with_gil': None, # (!) real value is '<capsule object "void (char *, Py_ssize_t *, Py_ssize_t *, int, int)" at 0x000002A05E0F5490>'
    'slice_assign_scalar': None, # (!) real value is '<capsule object "void (__Pyx_memviewslice *, int, size_t, void *, int)" at 0x000002A05E0F53A0>'
    'slice_copy': None, # (!) real value is '<capsule object "void (struct __pyx_memoryview_obj *, __Pyx_memviewslice *)" at 0x000002A05E0F5620>'
    'slice_get_size': None, # (!) real value is '<capsule object "Py_ssize_t (__Pyx_memviewslice *, int)" at 0x000002A05E0F4D10>'
    'slice_memviewslice': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice *, Py_ssize_t, Py_ssize_t, Py_ssize_t, int, int, int *, Py_ssize_t, Py_ssize_t, Py_ssize_t, int, int, int, int)" at 0x000002A05E0F5030>'
    'strided': None, # (!) real value is '<capsule object "PyObject *" at 0x000002A05E0F47C0>'
    'transpose_memslice': None, # (!) real value is '<capsule object "int (__Pyx_memviewslice *)" at 0x000002A05E0F4FE0>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='pandas._libs._cyutility', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000002A05DF5A930>, origin='C:\\\\Users\\\\T14\\\\PyCharmMiscProject\\\\.venv\\\\Lib\\\\site-packages\\\\pandas\\\\_libs\\\\_cyutility.cp314-win_amd64.pyd')"

__test__ = {}

