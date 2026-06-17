# encoding: utf-8
# module yaml._yaml
# from C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\yaml\_yaml.cp314-win_amd64.pyd
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import yaml as yaml # C:\Users\T14\PyCharmMiscProject\.venv\Lib\site-packages\yaml\__init__.py
import yaml.error as __yaml_error
import yaml.events as __yaml_events
import yaml.nodes as __yaml_nodes
import yaml.tokens as __yaml_tokens


class ReaderError(__yaml_error.YAMLError):
    # no doc
    def __init__(self, name, position, character, encoding, reason): # reliably restored by inspect
        # no doc
        pass

    def __str__(self): # reliably restored by inspect
        # no doc
        pass

    __firstlineno__ = 24
    __static_attributes__ = (
        'character',
        'encoding',
        'name',
        'position',
        'reason',
    )


