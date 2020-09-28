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

import ginit


def parse_functions(code: Union[ast.Module, ast.AST],
                    with_async: bool = True,
                    with_private: bool = False) -> list:
    """
    :param code: the module code
    :param with_async: When True, include async methods
    :param with_private: When True, include private methods
    :return: the list of module functions
    """
    return _parse_non_async_functions(code, with_private=with_private) + \
           (_parse_async_functions(code, with_private=with_private) if with_async else [])


def _parse_async_functions(code: Union[ast.Module, ast.AST],
                           with_private: bool = False) -> list:
    """
    :param code: the module code
    :param with_private: When True, include private methods
    :return: the list of module async functions
    """
    return [node for node in ast.walk(code)
            if isinstance(node, ast.AsyncFunctionDef) and _validate_function(node, with_private=with_private)]


def _parse_non_async_functions(code: Union[ast.Module, ast.AST],
                               with_private: bool = False) -> list:
    """
    :param code: the module code
    :param with_private: When True, include private methods
    :return: the list of module non async functions
    """
    return [node for node in ast.walk(code)
            if isinstance(node, ast.FunctionDef) and _validate_function(node, with_private=with_private)]


def _validate_function(function_node: Union[ast.Module, ast.AST], with_private: bool) -> bool:
    return function_node.name not in ginit.FUNCTIONS_TO_IGNORE and \
           (not function_node.name.startswith("_") or with_private)
