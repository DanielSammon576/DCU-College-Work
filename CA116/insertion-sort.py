#!/usr/bin/env python

a = [ 1, 6, 9, 2, 6, 7, 9, 5, 3, 12, 345, 5, 1, 0, 345]

i = 1
while i < len(a):
   v = a[i]
   p = i
   while 0 < p and v < a[p - 1]:
      a[p] = a[p - 1]
      p = p - 1
   a[p] = v

   i = i + 1

print a
