#!/usr/bin/env python

import sys

def main():
    a = []
    for line in sys.stdin:
        a.append(line.strip())

    i = 0
    while i < len(a):
        if a[i].isdigit():
            print("Thank you for {:}".format(a[i]))
            i = len(a)
        else:
            print("{:} is not a number".format(a[i]))
        i += 1

if __name__ == '__main__':
    main()
