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
import ginit.generation as generation
import ginit.patching as patching
import ginit.visitor as visitor


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

    parser.add_argument('-l', '--list_cython_modules', action='store_true',
                        help='List project cython modules',
                        default=False)

    parser.add_argument('-cpi', '--convert_python_init', action='store_true',
                        help='Convert python init files to cython init files',
                        default=False)
    args, unknown = parser.parse_known_args()

    logging.basicConfig(
        format='%(levelname)s: %(message)s',
        level=logging.INFO,
    )

    if args.convert_python_init:
        generation.migrate_python_init_to_cython(args.path)
    elif args.list_cython_modules:
        import black
        print(black.format_str(str(generation.list_cython_modules(args.path)), mode=black.Mode()))
    elif args.patch and args.cython:
        patching.imports_regex_patcher(args.path, is_cython_path=args.cython)
    else:
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
