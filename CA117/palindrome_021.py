#!/usr/bin/env python

import sys

def palindrome(s):
    s = s.lower()
    for c in s:
        if not c.isalnum():
            s = s.replace(c, "")
    a = s[::-1]
    print(a)
    if s == a:
        return True
    else:
        return False

def main():
    lines = sys.stdin.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        print(palindrome(line))
        i = i + 1

if __name__ == '__main__':
    main()