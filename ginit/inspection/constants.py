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


def parse_constants(code: Union[ast.Module, ast.AST]) -> list:
    """
    :param code: the module code
    :return: the list of module constants
    """
    return [node for node in ast.walk(code) if isinstance(node, ast.Name) and node.id.isupper()]
