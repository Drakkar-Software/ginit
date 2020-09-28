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


def get_python_path_from_path(path: str) -> str:
    """
    First replace '.' if exists and then replace os.path.sep by '.'
    :param path: the file path
    :return: the pythonized file path (folder/file -> folder.file)
    """
    return path.replace(".", "").replace(os.path.sep, ".")


def drop_file_extension(path: str) -> str:
    """
    :param path: the file path
    :return: the file path without extension
    """
    return os.path.splitext(path)[-2]
