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
    '10': "ten",
    '11': "eleven",
    '12': "twelve",
    '13': "thirteen",
    '14': "fourteen",
    '15': "fifteen",
    '16': "sixteen",
    '17': "seventeen",
    '18': "eighteen",
    '19': "nineteen"
}

highnum = {
    '20': "twenty",
    '30': "thirty",
    '40': "forty",
    '50': "fifty",
    '60': "sixty",
    '70': "seventy",
    '80': "eighty",
    '90': "ninety",
    '100': "one hundred"
}

def main():
    for line in sys.stdin:
        string = ''
        line = line.strip().split()
        for n in line:
            if n in numbers:
                string = string + numbers[n] + " "
            elif n in highnum:
                string = string + highnum[n] + " "
            else:
                snum = int(n) % 10
                fnum = int(n) - snum
                string = string + highnum[str(fnum)] + "-" + numbers[str(snum)] + " "
        print(string.rstrip())
if __name__ == '__main__':
    main()
