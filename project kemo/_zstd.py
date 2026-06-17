# encoding: utf-8
# module _zstd
# from C:\Users\T14\AppData\Local\Programs\Python\Python314\DLLs\_zstd.pyd
# by generator 1.147
""" Implementation module for Zstandard compression. """
# no imports

# Variables with simple values

ZSTD_btlazy2 = 6
ZSTD_btopt = 7
ZSTD_btultra = 8
ZSTD_btultra2 = 9

ZSTD_CLEVEL_DEFAULT = 3

ZSTD_c_chainLog = 103
ZSTD_c_checksumFlag = 201
ZSTD_c_compressionLevel = 100
ZSTD_c_contentSizeFlag = 200
ZSTD_c_dictIDFlag = 202
ZSTD_c_enableLongDistanceMatching = 160
ZSTD_c_hashLog = 102
ZSTD_c_jobSize = 401
ZSTD_c_ldmBucketSizeLog = 163
ZSTD_c_ldmHashLog = 161
ZSTD_c_ldmHashRateLog = 164
ZSTD_c_ldmMinMatch = 162
ZSTD_c_minMatch = 105
ZSTD_c_nbWorkers = 400
ZSTD_c_overlapLog = 402
ZSTD_c_searchLog = 104
ZSTD_c_strategy = 107
ZSTD_c_targetLength = 106
ZSTD_c_windowLog = 101

ZSTD_dfast = 2
ZSTD_DStreamOutSize = 131072

ZSTD_d_windowLogMax = 100

ZSTD_fast = 1
ZSTD_greedy = 3
ZSTD_lazy = 4
ZSTD_lazy2 = 5

zstd_version = '1.5.7'

zstd_version_number = 10507

# functions

def finalize_dict(*args, **kwargs): # real signature unknown
    """
    Finalize a Zstandard dictionary.
    
      custom_dict_bytes
        Custom dictionary content.
      samples_bytes
        Concatenation of samples.
      samples_sizes
        Tuple of samples' sizes.
      dict_size
        The size of the dictionary.
      compression_level
        Optimize for a specific Zstandard compression level, 0 means default.
    """
    pass

def get_frame_info(*args, **kwargs): # real signature unknown
    """
    Get Zstandard frame infomation from a frame header.
    
      frame_buffer
        A bytes-like object, containing the header of a Zstandard frame.
    """
    pass

def get_frame_size(*args, **kwargs): # real signature unknown
    """
    Get the size of a Zstandard frame, including the header and optional checksum.
    
      frame_buffer
        A bytes-like object, it should start from the beginning of a frame,
        and contains at least one complete frame.
    """
    pass

def get_param_bounds(*args, **kwargs): # real signature unknown
    """
    Get CompressionParameter/DecompressionParameter bounds.
    
      parameter
        The parameter to get bounds.
      is_compress
        True for CompressionParameter, False for DecompressionParameter.
    """
    pass

def set_parameter_types(*args, **kwargs): # real signature unknown
    """
    Set CompressionParameter and DecompressionParameter types for validity check.
    
      c_parameter_type
        CompressionParameter IntEnum type object
      d_parameter_type
        DecompressionParameter IntEnum type object
    """
    pass

def train_dict(*args, **kwargs): # real signature unknown
    """
    Train a Zstandard dictionary on sample data.
    
      samples_bytes
        Concatenation of samples.
      samples_sizes
        Tuple of samples' sizes.
      dict_size
        The size of the dictionary.
    """
    pass

# classes

class ZstdCompressor(object):
    """
    Create a compressor object for compressing data incrementally.
    
      level
        The compression level to use. Defaults to COMPRESSION_LEVEL_DEFAULT.
      options
        A dict object that contains advanced compression parameters.
      zstd_dict
        A ZstdDict object, a pre-trained Zstandard dictionary.
    
    Thread-safe at method level. For one-shot compression, use the compress()
    function instead.
    """
    def compress(self, *args, **kwargs): # real signature unknown
        """
        Provide data to the compressor object.
        
          mode
            Can be these 3 values ZstdCompressor.CONTINUE,
            ZstdCompressor.FLUSH_BLOCK, ZstdCompressor.FLUSH_FRAME
        
        Return a chunk of compressed data if possible, or b'' otherwise. When you have
        finished providing data to the compressor, call the flush() method to finish
        the compression process.
        """
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        """
        Finish the compression process.
        
          mode
            Can be these 2 values ZstdCompressor.FLUSH_FRAME,
            ZstdCompressor.FLUSH_BLOCK
        
        Flush any remaining data left in internal buffers. Since Zstandard data
        consists of one or more independent frames, the compressor object can still
        be used after this method is called.
        """
        pass

    def set_pledged_input_size(self, *args, **kwargs): # real signature unknown
        """
        Set the uncompressed content size to be written into the frame header.
        
          size
            The size of the uncompressed data to be provided to the compressor.
        
        This method can be used to ensure the header of the frame about to be written
        includes the size of the data, unless the CompressionParameter.content_size_flag
        is set to False. If last_mode != FLUSH_FRAME, then a RuntimeError is raised.
        
        It is important to ensure that the pledged data size matches the actual data
        size. If they do not match the compressed output data may be corrupted and the
        final chunk written may be lost.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    last_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The last mode used to this compressor object, its value can be .CONTINUE,
.FLUSH_BLOCK, .FLUSH_FRAME. Initialized to .FLUSH_FRAME.

It can be used to get the current state of a compressor, such as, data
flushed, or a frame ended."""


    CONTINUE = 0
    FLUSH_BLOCK = 1
    FLUSH_FRAME = 2


class ZstdDecompressor(object):
    """
    Create a decompressor object for decompressing data incrementally.
    
      zstd_dict
        A ZstdDict object, a pre-trained Zstandard dictionary.
      options
        A dict object that contains advanced decompression parameters.
    
    Thread-safe at method level. For one-shot decompression, use the decompress()
    function instead.
    """
    def decompress(self): # real signature unknown; restored from __doc__
        """
        Decompress *data*, returning uncompressed bytes if possible, or b'' otherwise.
        
          data
            A bytes-like object, Zstandard data to be decompressed.
          max_length
            Maximum size of returned data. When it is negative, the size of
            output buffer is unlimited. When it is nonnegative, returns at
            most max_length bytes of decompressed data.
        
        If *max_length* is nonnegative, returns at most *max_length* bytes of
        decompressed data. If this limit is reached and further output can be
        produced, *self.needs_input* will be set to ``False``. In this case, the next
        call to *decompress()* may provide *data* as b'' to obtain more of the output.
        
        If all of the input data was decompressed and returned (either because this
        was less than *max_length* bytes, or because *max_length* was negative),
        *self.needs_input* will be set to True.
        
        Attempting to decompress data after the end of a frame is reached raises an
        EOFError. Any data found after the end of the frame is ignored and saved in
        the self.unused_data attribute.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    eof = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """True means the end of the first frame has been reached. If decompress data
after that, an EOFError exception will be raised."""

    needs_input = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """If the max_length output limit in .decompress() method has been reached,
and the decompressor has (or may has) unconsumed input data, it will be set
to False. In this case, passing b'' to the .decompress() method may output
further data."""

    unused_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """A bytes object of un-consumed input data.

When ZstdDecompressor object stops after a frame is
decompressed, unused input data after the frame. Otherwise this will be b''."""



class ZstdDict(object):
    """
    Represents a Zstandard dictionary.
    
      dict_content
        The content of a Zstandard dictionary as a bytes-like object.
      is_raw
        If true, perform no checks on *dict_content*, useful for some
        advanced cases. Otherwise, check that the content represents
        a Zstandard dictionary created by the zstd library or CLI.
    
    The dictionary can be used for compression or decompression, and can be shared
    by multiple ZstdCompressor or ZstdDecompressor objects.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __len__(self, *args, **kwargs): # real signature unknown
        """ Return len(self). """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    as_digested_dict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Load as a digested dictionary to compressor.

Pass this attribute as zstd_dict argument:
compress(dat, zstd_dict=zd.as_digested_dict)

1. Some advanced compression parameters of compressor may be overridden
   by parameters of digested dictionary.
2. ZstdDict has a digested dictionaries cache for each compression level.
   It's faster when loading again a digested dictionary with the same
   compression level.
3. No need to use this for decompression."""

    as_prefix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Load as a prefix to compressor/decompressor.

Pass this attribute as zstd_dict argument:
compress(dat, zstd_dict=zd.as_prefix)

1. Prefix is compatible with long distance matching, while dictionary is not.
2. It only works for the first frame, then the compressor/decompressor will
   return to no prefix state.
3. When decompressing, must use the same prefix as when compressing."""

    as_undigested_dict = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Load as an undigested dictionary to compressor.

Pass this attribute as zstd_dict argument:
compress(dat, zstd_dict=zd.as_undigested_dict)

1. The advanced compression parameters of compressor will not be overridden.
2. Loading an undigested dictionary is costly. If load an undigested dictionary
   multiple times, consider reusing a compressor object.
3. No need to use this for decompression."""

    dict_content = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The content of a Zstandard dictionary, as a bytes object."""

    dict_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """The Zstandard dictionary, an int between 0 and 2**32.

A non-zero value represents an ordinary Zstandard dictionary,
conforming to the standardised format.

A value of zero indicates a 'raw content' dictionary,
without any restrictions on format or content."""



class ZstdError(Exception):
    """ An error occurred in the zstd library. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022D8EC19350>'

__spec__ = None # (!) real value is "ModuleSpec(name='_zstd', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000022D8EC19350>, origin='C:\\\\Users\\\\T14\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python314\\\\DLLs\\\\_zstd.pyd')"

