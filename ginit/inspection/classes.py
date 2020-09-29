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
import ast
from typing import Union

import ginit.inspection as inspection


def parse_classes(code: Union[ast.Module, ast.AST]) -> list:
    """
    :param code: the module code
    :return: the list of module classes
    """
    return [node for node in ast.walk(code) if isinstance(node, ast.ClassDef)]


def parse_class_methods(ast_class: Union[ast.Module, ast.AST], with_async=True) -> list:
    """
    :param ast_class: the AST parsed class
    :param with_async: When True, include async methods
    :return: the list of class methods
    """
    return inspection.parse_functions(ast_class, with_async=with_async)


def parse_class_constants(ast_class: Union[ast.Module, ast.AST]) -> list:
    """
    :param ast_class: the AST parsed class
    :return: the list of class constants
    """
    return inspection.parse_constants(ast_class)
