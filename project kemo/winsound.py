# encoding: utf-8
# module winsound
# from C:\Users\T14\AppData\Local\Programs\Python\Python314\DLLs\winsound.pyd
# by generator 1.147
"""
PlaySound(sound, flags) - play a sound
SND_FILENAME - sound is a wav file name
SND_ALIAS - sound is a registry sound association name
SND_LOOP - Play the sound repeatedly; must also specify SND_ASYNC
SND_MEMORY - sound is a memory image of a wav file
SND_PURGE - stop all instances of the specified sound
SND_ASYNC - PlaySound returns immediately
SND_NODEFAULT - Do not play a default beep if the sound can not be found
SND_NOSTOP - Do not interrupt any sounds currently playing
SND_NOWAIT - Return immediately if the sound driver is busy
SND_APPLICATION - sound is an application-specific alias in the registry.
SND_SENTRY - Triggers a SoundSentry event when the sound is played.
SND_SYNC - Play the sound synchronously, default behavior.
SND_SYSTEM - Assign sound to the audio session for system notification sounds.

Beep(frequency, duration) - Make a beep through the PC speaker.
MessageBeep(type) - Call Windows MessageBeep.
"""
# no imports

# Variables with simple values

MB_ICONASTERISK = 64
MB_ICONERROR = 16
MB_ICONEXCLAMATION = 48
MB_ICONHAND = 16
MB_ICONINFORMATION = 64
MB_ICONQUESTION = 32
MB_ICONSTOP = 16
MB_ICONWARNING = 48
MB_OK = 0

SND_ALIAS = 65536
SND_APPLICATION = 128
SND_ASYNC = 1
SND_FILENAME = 131072
SND_LOOP = 8
SND_MEMORY = 4
SND_NODEFAULT = 2
SND_NOSTOP = 16
SND_NOWAIT = 8192
SND_PURGE = 64
SND_SENTRY = 524288
SND_SYNC = 0
SND_SYSTEM = 2097152

# functions

def Beep(*args, **kwargs): # real signature unknown
    """
    A wrapper around the Windows Beep API.
    
      frequency
        Frequency of the sound in hertz.
        Must be in the range 37 through 32,767.
      duration
        How long the sound should play, in milliseconds.
    """
    pass

def MessageBeep(x): # real signature unknown; restored from __doc__
    """
    Call Windows MessageBeep(x).
    
    x defaults to MB_OK.
    """
    pass

def PlaySound(*args, **kwargs): # real signature unknown
    """
    A wrapper around the Windows PlaySound API.
    
      sound
        The sound to play; a filename, data, or None.
      flags
        Flag values, ored together.  See module documentation.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021F26FA8050>'

__spec__ = None # (!) real value is "ModuleSpec(name='winsound', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x0000021F26FA8050>, origin='C:\\\\Users\\\\T14\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python314\\\\DLLs\\\\winsound.pyd')"

