#!/usr/bin/env python

if __name__ == "__main__":
   a = [8, 9, 4, 7, 2, 11]

i = 0
while i < len(a)/2:
   tmp = a[i]
   a[i] = a[len(a) - i - 1]
   a[len(a) - i - 1] = tmp
   i = i + 1

print a
