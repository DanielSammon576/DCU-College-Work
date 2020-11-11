#!/usr/bin/env python

import sys
args = sys.argv[1]

def main():
    try:
        prev = 0
        maximum = 0
        with open(args, "r") as f:
            for line in f:
                try:
                    a = line.rstrip().split()
                    prev = a[0]

                    if int(prev) > int(maximum):
                        maximum = prev
                        bestname = a[1] + " " + a[2]
                except(ValueError):
                    print("Invalid mark {} encountered. Skipping.".format(prev))

            print("Best student: {}".format(bestname))
            print("Best mark: {}".format(maximum))
    except(ValueError):
        print("Invalid mark {} encountered. Exiting.".format(prev))

if __name__ == '__main__':
    main()