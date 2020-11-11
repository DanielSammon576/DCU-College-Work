#!/usr/bin/env python

import sys

from re import findall
import sys

car = r'\b[0-9]{2}[12] (?:C|CE|CN|CW|D|DL|G|KE|KK|KY|L|LD|LH|LM|LS|MH|MN|MO|OY|RN|SO|T|W|WH|WX|WW) [1-9][0-9]{0,5}\b'

def main():

    # Verify regular expression is not overly long
    assert(len(car) < 120)

    s = sys.stdin.read()

    carlist = findall(car, s)
    print(carlist)
    #print('Cars: {}'.format(carlist))

if __name__ == '__main__':
    main()
