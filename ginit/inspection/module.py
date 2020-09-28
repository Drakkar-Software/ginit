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


def get_code(module_path: str) -> Union[ast.Module, ast.AST]:
    """
    :param module_path: the module path
    :return: the module raw code
    """
    with open(module_path, "r") as module_file:
        module_code = ast.parse(module_file.read())
    return module_code
