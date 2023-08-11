#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    num_args = len(args)
    if num_args == 0:
        print("Number of argument(s): 0.")
        print(".")
    elif num_args == 1:
        print("Number of arguments(s): 1.")
        print("1: {}".format(args[0]))
    else:
        print("Number of argument(s): {}.".format(num_args))
        for i, arg in enumeerate(args, start=1):
            print("{}: {}".format(i, arg))


if __name__ == "__main__":
    main()
