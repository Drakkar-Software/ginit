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

from ginit import __project__, __version__
from setuptools import find_packages, setup

PACKAGES = find_packages(exclude=["tests"])


# long description from README file
# with open('README.md', encoding='utf-8') as f:
#     DESCRIPTION = f.read()

REQUIRED = open('requirements.txt').readlines()
REQUIRES_PYTHON = '>=3.7'

setup(
    name=__project__,
    version=__version__,
    url='https://github.com/Drakkar-Software/ginit',
    license='LGPL-3.0',
    author='Drakkar-Software',
    author_email='drakkar-software@protonmail.com',
    description='Python __init__.py and __init__.pxd generator',
    packages=PACKAGES,
    include_package_data=True,
    # long_description=DESCRIPTION,
    tests_require=["pytest"],
    test_suite="tests",
    zip_safe=False,
    data_files=[],
    setup_requires=REQUIRED,
    install_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.7',
    ],
)
