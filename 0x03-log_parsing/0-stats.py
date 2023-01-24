#!/usr/bin/python3

""" script that reads stdin line by line and computes metrics """

import sys


def printStatus(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


# sourcery skip: use-contextlib-suppress
statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}

count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            printStatus(statusCodes, size)

        stlist = line.split()
        count += 1

        try:
            size += int(stlist[-1])
        except Exception:
            pass

        try:
            if stlist[-2] in statusCodes:
                statusCodes[stlist[-2]] += 1
        except Exception:
            pass
    printStatus(statusCodes, size)


except KeyboardInterrupt:
    printStatus(statusCodes, size)
    raise
