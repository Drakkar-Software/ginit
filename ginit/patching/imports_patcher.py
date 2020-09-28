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
import re

import sys

import ginit


def patch_imports_form(module_visitor_dict: dict,
                       is_cython_path: bool = False) -> None:
    """
    Search for modules with imports from in module_visitor_dict
    :param module_visitor_dict: the complete visitor result dictionary
    :param is_cython_path: When True, apply a cython patch instead of a python one
    """
    for module_path in module_visitor_dict.keys():
        if module_path == ginit.DIRECTORY_MODULES:
            _patch_modules_imports_from(module_visitor_list=module_visitor_dict[ginit.DIRECTORY_MODULES],
                                        is_cython_path=is_cython_path)
        else:
            patch_imports_form(module_visitor_dict[module_path],
                               is_cython_path=is_cython_path)


def _patch_modules_imports_from(module_visitor_list: list,
                                is_cython_path: bool = False) -> None:
    """
    Search modules with imports_from and call imports from patcher
    :param module_visitor_list: the module visitor list
    :param is_cython_path: When True, apply a cython patch instead of a python one
    """
    for module in module_visitor_list:
        if module.imports_from and module.path not in ginit.PATCHER_FILES_TO_IGNORE:
            _patch_module_import_from(module, is_cython_path=is_cython_path)


def _patch_module_import_from(module: ginit.ModuleVisitor,
                              is_cython_path: bool = False) -> None:
    """
    Patch module imports_from
    :param module: the module to patch
    :param is_cython_path: When True, apply a cython patch instead of a python one
    """
    import_str = ginit.CYTHON_IMPORT if is_cython_path else ginit.PYTHON_IMPORT
    from_imports = [
        f"from {from_import.module} {import_str} "
        for from_import in module.imports_from
    ]
    for line in fileinput.input([module.path_with_parent], inplace=True):
        if is_line_from_candidate(line, from_imports=from_imports, import_str=import_str):
            import_search = re.search(rf"from\s(.*){import_str}", line)
            if import_search:
                line = get_patched_import(import_search.group(1), import_str)
        sys.stdout.write(line)


def is_line_from_candidate(line: str, from_imports: list, import_str: str) -> bool:
    """
    Check if line has from import
    :param line: the line to check
    :param from_imports: the from imports list
    :param import_str: the import string
    :return: True if the line has from import to replace
    """
    if import_str not in line:
        return False
    for from_import in from_imports:
        if line.strip().startswith(from_import):
            return True
    return False


def get_patched_import(import_package: str, import_str: str) -> str:
    """
    :param import_package: the original imported package
    :param import_str: the import string
    :return: the patched from import package
    """
    package_names = import_package.split('.')
    imported_modules = f" as {import_package.split('.')[-1]}" if len(package_names) > 1 else ""
    return f"{import_str} {import_package}{imported_modules}"
