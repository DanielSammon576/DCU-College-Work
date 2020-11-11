#!/usr/bin/env python

import sys

numbers = {
    '0': "zero",
    '1': "one",
    '2': "two",
    '3': "three",
    '4': "four",
    '5': "five",
    '6': "six",
    '7': "seven",
    '8': "eight",
    '9': "nine",
    '10': "ten"
}

def main():
    for line in sys.stdin:
        string = ''
        line = line.strip().split()
        for n in line:
            if n in numbers:
                string = string + numbers[n] + " "
            else:
                string = string + "unknown" + " "
        print(string.rstrip())

if __name__ == '__main__':
    main()
