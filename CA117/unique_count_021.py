#!/usr/bin/env python

import sys
import string

def punc(s):
    for c in s:
        if c in string.punctuation:
            s = s.replace(c, '')
    return s

def unique():
    x = []
    for line in sys.stdin.readlines():
        line = punc(line.lower().strip())
        for token in line.strip().split():
            if token not in x and token.isalnum():
                x.append(token)
    return len(x)

def main():
    print(unique())

if __name__ == '__main__':
    main()
