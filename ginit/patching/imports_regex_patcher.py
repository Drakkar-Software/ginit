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
import fileinput
import os
import re
import sys

import ginit
import ginit.patching as patching


def imports_regex_patcher(path: str, is_cython_path: bool = False) -> None:
    """
    Patch files of path imports from regex
    :param path: the path to patch
    :param is_cython_path: When True, apply a cython patch instead of a python one
    """
    for (current_path, directory_names, filenames) in os.walk(path):
        for file in filenames:
            if _is_imports_regex_patcher_file_candidate(file, is_cython_path=is_cython_path):
                _patch_file_imports(os.path.join(current_path, file), is_cython_path=is_cython_path)


def _is_imports_regex_patcher_file_candidate(file: str, is_cython_path: bool = False) -> bool:
    """
    :param file: the file name
    :param is_cython_path: When True, apply a cython patch instead of a python one
    :return: True if the file should be patched
    """
    return file \
           and os.path.splitext(file)[-1] in (ginit.CYTHON_EXTS if is_cython_path else ginit.PYTHON_EXTS) \
           and ginit.drop_file_extension(file) not in ginit.FILE_TO_IGNORE


def _patch_file_imports(file_path: str, is_cython_path: bool = False) -> None:
    """
    Patch file imports_from
    :param file_path: the file to patch path
    :param is_cython_path: When True, apply a cython patch instead of a python one
    """
    import_str = ginit.CYTHON_IMPORT if is_cython_path else ginit.PYTHON_IMPORT
    for line in fileinput.input([file_path], inplace=True):
        if _is_line_from_candidate(line, import_str=import_str):
            import_search = re.search(rf"from\s(.*){import_str}", line)
            if import_search:
                line = f"{patching.get_patched_import(import_search.group(1), import_str)}{os.linesep}"
        sys.stdout.write(line)


def _is_line_from_candidate(line: str, import_str: str) -> bool:
    """
    Check if line has from import
    :param line: the line to check
    :param import_str: the import string
    :return: True if the line has from import to replace
    """
    if not (import_str in line and "from" in line):
        return False
    return True
