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
import os

import ginit
import ginit.util as util


def list_cython_modules(path: str,
                        keep_system_separator: bool = False) -> list:
    """
    List project cython modules
    :param path: the project root path
    :param keep_system_separator: When True, doesn't format module path to match python imports
    """
    cython_modules = []
    for (current_path, directory_names, filenames) in os.walk(path):
        for file in filenames:
            if file not in [ginit.PYTHON_INIT, ginit.CYTHON_INIT] and os.path.splitext(file)[-1] in ginit.CYTHON_EXTS:
                cython_module_path = os.path.join(current_path, util.drop_file_extension(file))
                if not keep_system_separator:
                    cython_module_path = ginit.IMPORT_MODULE_SEPARATOR.join(cython_module_path.split(os.sep))
                cython_modules.append(cython_module_path)
    return cython_modules
