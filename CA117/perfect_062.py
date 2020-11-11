#!usr/bin/env python

import sys

def sumFac(n):
    n = int(n)
    factors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            factors.append(i)
    return sum(factors)

def isPerfect(n):
    return int(n) == sumFac(int(n))

def main():
    for line in sys.stdin:
        line = line.strip()
        num = int(line)
        print(isPerfect(line))

if __name__ == '__main__':
    main()
