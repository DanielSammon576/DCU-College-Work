#!/usr/bin/env python

import sys
args = sys.argv[1]

def main():
    engirish = {}
    numeng = {}
    with open(args, "r") as f:
        f = f.readlines()
        i = 0
        for line in f:
            list1 = line.strip().split()
            engirish[list1[0]] = list1[1]
            numeng[str(i)] = list1[0]
            i = i + 1

    for line in sys.stdin:
        line = line.strip().split()
        string = ''
        for n in line:
            if n in numeng:
                string = string + engirish[numeng[n]] + " "
        print(string.rstrip())

if __name__ == '__main__':
    main()
