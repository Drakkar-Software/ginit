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

import ginit
import ginit.visitor as visitor
import ginit.generation as generation
import ginit.patching as patching


def main():
    import argparse
    import logging

    parser = argparse.ArgumentParser(description=ginit.__project__)
    parser.add_argument('path', nargs='?', help='path to generate __init__.py and __init__.pxd', default='.')

    parser.add_argument('-i', '--inplace', action='store_false',
                        help='modify / write to the file inplace',
                        default=True)

    parser.add_argument('-c', '--cython', action='store_true',
                        help='Enable cython __init__ generation',
                        default=False)

    parser.add_argument('-p', '--patch', action='store_true',
                        help='Patch imports of python files at path',
                        default=False)

    parser.add_argument('--verbose', nargs='?', default=0, type=int,
                        help='Verbosity level')

    parser.add_argument('-v', '--version', action='store_true',
                        help='print version and exit')

    args, unknown = parser.parse_known_args()

    if args.verbose == 0:
        level = logging.WARNING
    elif args.verbose == 1:
        level = logging.INFO
    else:
        level = logging.DEBUG

    logging.basicConfig(
        format='%(levelname)s: %(message)s',
        level=level,
    )

    visit_result = visitor.visit_path(args.path,
                                      visit_cython=args.cython)
    if args.patch:
        patching.patch_imports_form(module_visitor_dict=visit_result,
                                    is_cython_path=args.cython)
    else:
        generation.gen_python_init_from_visit(module_visitor_dict=visit_result,
                                              in_place=args.inplace,
                                              is_cython_init=args.cython)


if __name__ == '__main__':
    main()
