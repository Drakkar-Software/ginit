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
import ginit.visitor as visitor
import ginit.generation as generation


def test_visitor():
    visit_result = visitor.visit_path("tests")
    assert "tests" in visit_result
    assert "test_project" in visit_result["tests"]
    assert "test_submodule" in visit_result["tests"]["test_project"]
    assert "test_submodule_2" in visit_result["tests"]["test_project"]
    assert "test_submodule_3" in visit_result["tests"]["test_project"]["test_submodule"]
    assert len(visit_result["tests"]["test_project"][ginit.DIRECTORY_MODULES]) == 5
    assert len(visit_result["tests"]["test_project"]["test_submodule"][ginit.DIRECTORY_MODULES]) == 2
    assert len(visit_result["tests"]["test_project"]["test_submodule_2"][ginit.DIRECTORY_MODULES]) == 2


def test_generation():
    visit_result = visitor.visit_path("tests")
    generation.gen_python_init("tests/test_project", visit_result["tests"]["test_project"][ginit.DIRECTORY_MODULES])
    # global_from_str, detailed_from_str, all_imports_list_str = generation.gen_python_init_str(
    #     visit_result["tests"]["test_project"][ginit.DIRECTORY_MODULES])
    # print(global_from_str, detailed_from_str, all_imports_list_str)
    # assert global_from_str == """from tests.test_project import test_async_functions \n'\n 'from tests.test_project import test_constants \n'\n 'from tests.test_project import test_functions \n'\n 'from tests.test_project import test_classes')"""
    # assert detailed_from_str == """
    # from tests.test_project.test_async_functions import (async_test_function_3, async_test_function_2, async_test_function_1, )
    # from tests.test_project.test_constants import (test_without_cst, TEST_CST, TEST_CST_3, TEST_CST_2, )
    # from tests.test_project.test_functions import (test_function_2, test_function_1, test_function_3, )
    # from tests.test_project.test_classes import (TestC1, test_function_not_in_class_1, test_function_not_in_class_2, test_f2, test_f3, TEST_NOT_CLASS_ATTR, TEST_CLASS_ATTR_1, TEST_CLASS_ATTR_2, )
    # """
    # assert all_imports_list_str == """
    # __all__ = ['async_test_function_3', 'async_test_function_2', 'async_test_function_1', 'test_without_cst', 'TEST_CST', 'TEST_CST_3', 'TEST_CST_2', 'test_function_2', 'test_function_1', 'test_function_3', 'TestC1', 'test_function_not_in_class_1', 'test_function_not_in_class_2', 'test_f2', 'test_f3', 'TEST_NOT_CLASS_ATTR', 'TEST_CLASS_ATTR_1', 'TEST_CLASS_ATTR_2', ]
    # """
