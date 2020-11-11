#!/usr/bin/env python

import sys

def getpower(s):
    number = int(s[0])
    base = int(s[1])
    i = 0
    while base ** i < number:
        i = i + 1
    return i - 1

def getnumbers(p, s):
    number = int(s[0])
    base = int(s[1])
    a = []
    i = 0
    while i <= p:
        keynumber = (number // (base ** (p - i)))
        a.append(int(keynumber))
        number = (number - ((base ** (p - i)) * keynumber))
        i = i + 1
    print(a)
    return a

def calculations(l):
    finalfigure = 0
    for f in l:
        finalfigure = finalfigure + f ** 2
    return finalfigure

def main():
    lines = sys.stdin.readlines()
    try:
        a = []
        i = 0
        for line in lines:
            try:
                line = lines[i].strip().split()
                power = getpower(line)
                keyfigurelist = getnumbers(power, line)
                print(calculations(keyfigurelist))
            except ValueError:
                a.append(i)
            i = i + 1
    finally:
        if len(a) > 0:
            b = []
            i = 0
            while i < len(a):
                b.append(str(a[i] + 1))
                i = i + 1
            print("Failed to convert line(s): " + ", ".join(b) + " ")

if __name__ == '__main__':
    main()
