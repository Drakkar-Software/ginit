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
from os import walk

import ginit


def visit_path(path: str, visit_cython: bool = False) -> dict:
    """
    Visit a specific path
    :param path: the path to visit
    :param visit_cython: When True, ignore python module and take cython modules
    :return: the dict of visited modules as ModuleVisitor instances
    """
    visited_modules_by_path = {}
    for (current_path, directory_names, filenames) in walk(path):
        if filenames and os.path.split(current_path)[-1] not in ginit.FOLDERS_TO_IGNORE:
            _set_dict_value_from_keys(visited_modules_by_path,
                                      current_path.split(os.path.sep),
                                      visit_files(parent_path=current_path,
                                                  files=filenames,
                                                  visit_cython=visit_cython))
    return visited_modules_by_path


def _set_dict_value_from_keys(dictionary: dict, keys: list, value: object) -> object:
    """
    Set the value at dictionary nested key list
    :param dictionary: the dictionary
    :param keys: the nested key list
    :param value: the value to be set
    """
    if keys[0] not in dictionary:
        dictionary[keys[0]] = {}
    if len(keys) == 1 and isinstance(keys, list):
        dictionary[keys[0]][ginit.DIRECTORY_MODULES] = value
        return
    if isinstance(keys, str):
        if keys not in dictionary:
            dictionary[keys] = {}
        dictionary[keys][ginit.DIRECTORY_MODULES] = value
        return
    current_dictionary = dictionary[keys[0]]
    del keys[0]
    return _set_dict_value_from_keys(current_dictionary, keys, value)


def visit_files(parent_path: str, files: list, visit_cython: bool = False) -> list:
    """
    Visit of files of directory
    :param parent_path: the current directory
    :param files: directory files list
    :param visit_cython: When True, ignore python module and take cython modules
    :return: the list of visited modules as ModuleVisitor instances
    """
    visited_modules = []
    for file in files:
        if file and os.path.splitext(file)[-1] in ginit.CYTHON_EXTS if visit_cython else ginit.PYTHON_EXTS:
            visited_modules.append(visit_module(parent_path, file))
    return visited_modules


def visit_module(parent_path: str, file_path: str) -> ginit.ModuleVisitor:
    """
    Visit a python module
    :param parent_path: the module directory
    :param file_path: the module path
    :return: the module visitor instance for the file_path
    """
    module = ginit.ModuleVisitor(parent_path, file_path)
    module.set_module_classes()
    module.set_module_functions()
    module.set_module_constants()
    module.set_module_imports()
    return module
