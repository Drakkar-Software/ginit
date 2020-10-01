#  Drakkar-Software ginit
#  Copyright (c) Drakkar-Software, All rights reserved.
#  MIT License
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so.

from ginit import util
from ginit.util import (get_python_path_from_path, drop_file_extension, )

from ginit import module
from ginit.module import (ModuleVisitor)

from ginit import visitor
from ginit.visitor import (visit_path)

__project__ = "ginit"
__version__ = "1.1.0"

FILE_TO_IGNORE = ['__init__', '__main__']
PATCHER_FILES_TO_IGNORE = ['__init__.py', '__init__.pxd']
FOLDERS_TO_IGNORE = ['__pycache__']
FUNCTIONS_TO_IGNORE = ['__init__', '__str__', '__repr__', '__del__']
DIRECTORY_MODULES = "."
INIT_SEPARATOR = ", "
IMPORT_MODULE_SEPARATOR = "."

DEFAULT_IMPORT_PATCH_MAX_DEPTH = 2

PYTHON_IMPORT = "import"
PYTHON_INIT = "__init__.py"
PYTHON_EXTS = [".py"]

CYTHON_IMPORT = "cimport"
CYTHON_INIT = "__init__.pxd"
CYTHON_EXTS = [".pxd", ".pyx"]

__all__ = ['__project__', '__version__',
           'ModuleVisitor', 'visit_path',
           'get_python_path_from_path', 'drop_file_extension',
           'DIRECTORY_MODULES', 'FILE_TO_IGNORE', 'FOLDERS_TO_IGNORE', 'PATCHER_FILES_TO_IGNORE',
           'DEFAULT_IMPORT_PATCH_MAX_DEPTH', 'IMPORT_MODULE_SEPARATOR',
           'PYTHON_INIT', 'PYTHON_IMPORT', 'PYTHON_EXTS',
           'CYTHON_INIT', 'CYTHON_IMPORT', 'CYTHON_EXTS']
