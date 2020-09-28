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
import logging
from black import format_str, Mode

import ginit


def gen_python_init_from_visit(module_visitor_dict: dict,
                               current_path: str = "",
                               use_black_formatting: bool = True,
                               is_cython_init: bool = False,
                               in_place: bool = False
                               ) -> None:
    """
    Call gen_python_init for each init candidate found during inspection
    :param current_path: the path of the current folder
    :param module_visitor_dict: the complete visitor result dictionary
    :param is_cython_init: when True, generate cython init
    :param in_place: when True, generate init file inplace
    :param use_black_formatting: when True, format init str using black
    """
    for init_path in module_visitor_dict.keys():
        if init_path == ginit.DIRECTORY_MODULES:
            gen_python_init(init_path=current_path,
                            module_visitor_list=module_visitor_dict[ginit.DIRECTORY_MODULES],
                            use_black_formatting=use_black_formatting,
                            is_cython_init=is_cython_init,
                            in_place=in_place)
        else:
            gen_python_init_from_visit(current_path=os.path.join(current_path, init_path),
                                       module_visitor_dict=module_visitor_dict[init_path],
                                       use_black_formatting=use_black_formatting,
                                       is_cython_init=is_cython_init,
                                       in_place=in_place)


def gen_python_init(init_path: str,
                    module_visitor_list: list,
                    use_black_formatting: bool = True,
                    is_cython_init: bool = False,
                    in_place: bool = False) -> None:
    """
    Write the global from str, detailed from str and all imports list str parts in the init file
    :param init_path: the path of __init__ file
    :param module_visitor_list: the module visitor list
    :param is_cython_init: when True, generate cython init
    :param in_place: when True, generate init file inplace
    :param use_black_formatting: when True, format init str using black
    """
    global_from_str, detailed_from_str, all_imports_list_str = gen_python_init_str(module_visitor_list)
    init_file_content = f"{os.linesep}" \
                        f"{format_str(global_from_str, mode=Mode())}" \
                        f"{format_str(detailed_from_str, mode=Mode())}" \
                        f"{format_str(all_imports_list_str, mode=Mode())}" \
        if use_black_formatting else os.linesep + global_from_str + detailed_from_str + all_imports_list_str

    if is_cython_init:  # prevent black to raise an InvalidInput with cimport
        init_file_content = init_file_content.replace(ginit.PYTHON_IMPORT, ginit.CYTHON_IMPORT)

    init_file_path = os.path.join(init_path, ginit.CYTHON_INIT if is_cython_init else ginit.PYTHON_INIT)
    if in_place:
        with open(init_file_path, "a") as init_file:
            init_file.write(init_file_content)
    else:
        logging.getLogger("InitGenerator").info(f"** {init_file_path} ** {os.linesep} {init_file_content}")


def gen_python_init_str(module_visitor_list: list) -> tuple:
    """
    Generate the global from str, detailed from str and all imports list str parts of init
    :param module_visitor_list: the module visitor list
    :return: global_from_str, detailed_from_str, all_imports_list_str
    """
    global_from_str = os.linesep
    detailed_from_str = os.linesep
    all_imports_list_str = f"{os.linesep} __all__ = ["
    for module_visitor in module_visitor_list:
        module_file = ginit.drop_file_extension(module_visitor.path)
        if module_file not in ginit.FILE_TO_IGNORE:
            global_from_str += gen_global_from(module_visitor.parent_path, module_file)
            detailed_from_str += gen_detailed_from(module_visitor, module_file)
            all_imports_list_str += get_detailed_from_module_visitor(module_visitor,
                                                                     separator=f"'{ginit.INIT_SEPARATOR}'",
                                                                     prefix="'",
                                                                     suffix=f"'{ginit.INIT_SEPARATOR}")
    all_imports_list_str += "]"
    return global_from_str, detailed_from_str, all_imports_list_str


def gen_global_from(parent_path: str, module_path: str) -> str:
    """
    :param parent_path: the module parent path
    :param module_path: the module path
    :return: the module global imports line
    """
    return f"from {ginit.get_python_path_from_path(parent_path)} {ginit.PYTHON_IMPORT} {module_path} {os.linesep}"


def gen_detailed_from(module_visitor: ginit.ModuleVisitor, module_path: str) -> str:
    """
    :param module_visitor: the module visitor instance
    :param module_path: the module path
    :return: the module detailed imports line
    """
    return f"from {ginit.get_python_path_from_path(os.path.join(module_visitor.parent_path, module_path))} " \
           f"{ginit.PYTHON_IMPORT} ({get_detailed_from_module_visitor(module_visitor)}) {os.linesep}"


def get_detailed_from_module_visitor(module_visitor: ginit.ModuleVisitor,
                                     separator: str = ginit.INIT_SEPARATOR,
                                     prefix: str = "",
                                     suffix: str = ginit.INIT_SEPARATOR) -> str:
    """
    :param module_visitor: the module visitor instance
    :param separator: the detailed list separator
    :param prefix: the detailed list prefix
    :param suffix: the detailed list suffix
    :return: the module detailed imports list as str
    """
    return prefix + separator.join(module_visitor.get_classes_str() +
                                   module_visitor.get_functions_str() +
                                   module_visitor.get_constants_str()) + suffix
