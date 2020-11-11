#!/usr/bin/env python

import sys

def token(a):
    a = a.split()
    return len(a)

def main():
    line = sys.stdin.read()
    print(token(line))

if __name__ == '__main__':
    main()
