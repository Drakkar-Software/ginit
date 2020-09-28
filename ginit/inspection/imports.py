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


def parse_imports(code) -> list:
    """
    :param code: the input code
    :return: code imports list
    """
    return [node for node in ast.walk(code) if isinstance(node, ast.Import)]
    # imports = set()
    # tree = ast.parse(code)
    # for node in ast.walk(tree):
    #     if isinstance(node, ast.Import):
    #         for sub_node in node.names:
    #             imports.add(sub_node.name)
    #     if isinstance(node, ast.ImportFrom):
    #         imports.add(('.' * node.level) + node.module)
    # return list(imports)


def parse_imports_from(code) -> list:
    """
    :param code: the input code
    :return: code imports_from list
    """
    return [node for node in ast.walk(code) if isinstance(node, ast.ImportFrom)]
