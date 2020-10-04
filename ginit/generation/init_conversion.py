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


def migrate_python_init_to_cython(path: str) -> None:
    """
    Generate cython init file from python init file
    :param path: the project root path
    """
    for (current_path, directory_names, filenames) in os.walk(path):
        for file in filenames:
            if file == ginit.PYTHON_INIT:
                convert_python_file(current_path)


def convert_python_file(current_path: str) -> None:
    """
    Convert the python init file to a cython init
    :param current_path: the init folder
    """
    with open(os.path.join(current_path, ginit.CYTHON_INIT), 'w') as cython_init:
        python_init_content = f"# cython: language_level=3{os.linesep}"
        with open(os.path.join(current_path, ginit.PYTHON_INIT), 'r') as python_init:
            python_init_content += python_init.read()
        python_init_content = python_init_content.replace(ginit.PYTHON_IMPORT, ginit.CYTHON_IMPORT)
        cython_init.write(python_init_content)
