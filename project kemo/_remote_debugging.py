# encoding: utf-8
# module _remote_debugging
# from C:\Users\T14\AppData\Local\Programs\Python\Python314\DLLs\_remote_debugging.pyd
# by generator 1.147
# no doc
# no imports

# Variables with simple values

PROCESS_VM_READV_SUPPORTED = 0

# no functions
# classes

class AwaitedInfo(tuple):
    """ Information about what a thread is awaiting """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __replace__(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the structure with new values for the specified fields. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    awaited_by = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """List of tasks awaited by this thread"""

    thread_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thread ID"""


    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0
    __match_args__ = (
        'thread_id',
        'awaited_by',
    )


class CoroInfo(tuple):
    """ Information about a coroutine """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __replace__(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the structure with new values for the specified fields. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    call_stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Coroutine call stack"""

    task_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Task name"""


    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0
    __match_args__ = (
        'call_stack',
        'task_name',
    )


class FrameInfo(tuple):
    """ Information about a frame """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __replace__(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the structure with new values for the specified fields. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    filename = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Source code filename"""

    funcname = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Function name"""

    lineno = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Line number"""


    n_fields = 3
    n_sequence_fields = 3
    n_unnamed_fields = 0
    __match_args__ = (
        'filename',
        'lineno',
        'funcname',
    )


class RemoteUnwinder(object):
    """ RemoteUnwinder(pid): Inspect stack of a remote Python process. """
    def get_all_awaited_by(self, *args, **kwargs): # real signature unknown
        """
        Get all tasks and their awaited_by relationships from the remote process.
        
        This provides a tree structure showing which tasks are waiting for other tasks.
        
        For each task, returns:
        1. The call stack frames leading to where the task is currently executing
        2. The name of the task
        3. A list of tasks that this task is waiting for, with their own frames/names/etc
        
        Returns a list of [frames, task_name, subtasks] where:
        - frames: List of (func_name, filename, lineno) showing the call stack
        - task_name: String identifier for the task
        - subtasks: List of tasks being awaited by this task, in same format
        
        Raises:
            RuntimeError: If AsyncioDebug section is not available in the remote process
            MemoryError: If memory allocation fails
            OSError: If reading from the remote process fails
        
        Example output:
        [
            [
                [("c5", "script.py", 10), ("c4", "script.py", 14)],
                "c2_root",
                [
                    [
                        [("c1", "script.py", 23)],
                        "sub_main_2",
                        [...]
                    ],
                    [...]
                ]
            ]
        ]
        """
        pass

    def get_async_stack_trace(self, *args, **kwargs): # real signature unknown
        """
        Get the currently running async tasks and their dependency graphs from the remote process.
        
        This returns information about running tasks and all tasks that are waiting for them,
        forming a complete dependency graph for each thread's active task.
        
        For each thread with a running task, returns the running task plus all tasks that
        transitively depend on it (tasks waiting for the running task, tasks waiting for
        those tasks, etc.).
        
        Returns a list of per-thread results, where each thread result contains:
        - Thread ID
        - List of task information for the running task and all its waiters
        
        Each task info contains:
        - Task ID (memory address)
        - Task name
        - Call stack frames: List of (func_name, filename, lineno)
        - List of tasks waiting for this task (recursive structure)
        
        Raises:
            RuntimeError: If AsyncioDebug section is not available in the target process
            MemoryError: If memory allocation fails
            OSError: If reading from the remote process fails
        
        Example output (similar structure to get_all_awaited_by but only for running tasks):
        [
            (140234, [
                (4345585712, 'main_task',
                 [("run_server", "server.py", 127), ("main", "app.py", 23)],
                 [
                     (4345585800, 'worker_1', [...], [...]),
                     (4345585900, 'worker_2', [...], [...])
                 ])
            ])
        ]
        """
        pass

    def get_stack_trace(self, *args, **kwargs): # real signature unknown
        """
        Returns a list of stack traces for threads in the target process.
        
        Each element in the returned list is a tuple of (thread_id, frame_list), where:
        - thread_id is the OS thread identifier
        - frame_list is a list of tuples (function_name, filename, line_number) representing
          the Python stack frames for that thread, ordered from most recent to oldest
        
        The threads returned depend on the initialization parameters:
        - If only_active_thread was True: returns only the thread holding the GIL
        - If all_threads was True: returns all threads
        - Otherwise: returns only the main thread
        
        Example:
            [
                (1234, [
                    ('process_data', 'worker.py', 127),
                    ('run_worker', 'worker.py', 45),
                    ('main', 'app.py', 23)
                ]),
                (1235, [
                    ('handle_request', 'server.py', 89),
                    ('serve_forever', 'server.py', 52)
                ])
            ]
        
        Raises:
            RuntimeError: If there is an error copying memory from the target process
            OSError: If there is an error accessing the target process
            PermissionError: If access to the target process is denied
            UnicodeDecodeError: If there is an error decoding strings from the target process
        """
        pass

    def __init__(self, pid): # real signature unknown; restored from __doc__
        pass


class TaskInfo(tuple):
    """ Information about an asyncio task """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __replace__(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the structure with new values for the specified fields. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    awaited_by = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Tasks awaiting this task"""

    coroutine_stack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Coroutine call stack"""

    task_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Task ID (memory address)"""

    task_name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Task name"""


    n_fields = 4
    n_sequence_fields = 4
    n_unnamed_fields = 0
    __match_args__ = (
        'task_id',
        'task_name',
        'coroutine_stack',
        'awaited_by',
    )


class ThreadInfo(tuple):
    """ Information about a thread """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __replace__(self, *args, **kwargs): # real signature unknown
        """ Return a copy of the structure with new values for the specified fields. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    frame_info = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Frame information"""

    thread_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Thread ID"""


    n_fields = 2
    n_sequence_fields = 2
    n_unnamed_fields = 0
    __match_args__ = (
        'thread_id',
        'frame_info',
    )


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x00000179C2B18050>'

__spec__ = None # (!) real value is "ModuleSpec(name='_remote_debugging', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x00000179C2B18050>, origin='C:\\\\Users\\\\T14\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python314\\\\DLLs\\\\_remote_debugging.pyd')"

