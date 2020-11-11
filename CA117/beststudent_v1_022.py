#!/usr/bin/env python

import sys
args = sys.argv[1]

def main():
    try:
        prev = 0
        maximum = 0
        with open(args, "r") as f:
            for line in f:
                a = line.rstrip().split()
                prev = a[0]

                if int(prev) > int(maximum):
                    maximum = prev
                    bestname = a[1] + " " + a[2]

        print("Best student: {}".format(bestname))
        print("Best mark: {}".format(maximum))

    except:
        print("The file {} could not be opened")

if __name__ == '__main__':
    main()