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

import ginit.inspection as inspection


class ModuleVisitor:
    def __init__(self, parent_path: str, path: str):
        self.parent_path: str = parent_path
        self.path: str = path
        self.path_with_parent: str = os.path.join(parent_path, path)

        self.classes: list = []
        self.functions: list = []
        self.constants: list = []

        self.imports: list = []
        self.imports_from: list = []

    def set_module_classes(self) -> None:
        """
        Set the result of module class inspection
        """
        self.classes = inspection.parse_classes(inspection.get_code(self.path_with_parent))

    def set_module_functions(self, with_async=True) -> None:
        """
        Set the result of the subtraction of class methods and global methods
        with found class methods = method for clazz in classes for method in inspection.parse_class_methods(clazz)
        and with all module methods = inspection.parse_functions(inspection.get_code(file_path)))
        :param with_async: When True, include async methods
        """
        self.functions = [function
                          for function in inspection.parse_functions(inspection.get_code(self.path_with_parent),
                                                                     with_async=with_async)
                          if function.name not in [method.name
                                                   for clazz in self.classes
                                                   for method in inspection.parse_class_methods(clazz,
                                                                                                with_async=with_async)]]

    def set_module_constants(self) -> None:
        """
        Set the result of the subtraction of class constants and global constants
        with found class constants = method for clazz in classes for method in inspection.parse_class_constants(clazz)
        and with all module constants = inspection.parse_constants(inspection.get_code(file_path)))
        """
        self.constants = [constant
                          for constant in inspection.parse_constants(inspection.get_code(self.path_with_parent))
                          if constant.id not in [class_constant.id
                                                 for clazz in self.classes
                                                 for class_constant in inspection.parse_class_constants(clazz)]]

    def set_module_imports(self) -> None:
        """
        Set the result of module imports inspection
        """
        self.imports = inspection.parse_imports(inspection.get_code(self.path_with_parent))
        self.imports_from = inspection.parse_imports_from(inspection.get_code(self.path_with_parent))

    def get_functions_str(self) -> list:
        """
        :return: functions list as str
        """
        return [function.name for function in self.functions]

    def get_classes_str(self) -> list:
        """
        :return: classes list as str
        """
        return [clazz.name for clazz in self.classes]

    def get_constants_str(self) -> list:
        """
        :return: constants list as str
        """
        return [constant.id for constant in self.constants]

    def __str__(self) -> str:
        return f"Path : {self.path} | " \
               f"Classes : {self.classes} | " \
               f"Functions : {self.functions} | " \
               f"Constants : {self.constants}"
