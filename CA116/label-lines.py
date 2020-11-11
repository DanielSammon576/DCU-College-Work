#!/usr/bin/env python

s = raw_input()
a = []


while s != "end":
   a.append(s)
   s = raw_input()

n = len(a)

i = 0
while i < len(a):
   print i, n, a[i]
   i = i + 1
