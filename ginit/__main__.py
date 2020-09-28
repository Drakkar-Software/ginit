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

def main():
    import argparse
    import logging

    parser = argparse.ArgumentParser(description='Ginit')
    parser.add_argument('path', nargs='?', help='path to generate __init__.py and __init__.pxd', default='.')

    parser.add_argument('-i', '--inplace', action='store_false',
                        help='modify / write to the file inplace',
                        default=True)

    parser.add_argument('-c', '--cython', action='store_false',
                        help='Enable cython __init__ generation')

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


if __name__ == '__main__':
    main()
