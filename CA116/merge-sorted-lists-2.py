#!/usr/bin/env python

a = []
b = []

line = raw_input()
while line != "end":
   a.append(int(line))
   line = raw_input()

line = raw_input()
while line != "end":
   b.append(int(line))
   line = raw_input()

i = 0
j = 0
while i < len(a) or len(b):
   if len(a) <= i or b[j] <= a[i]:
      print b[j]
      j = j + 1
   elif len(b) <= j or a[i] <= b[j]:
      print a[i]
      i = i + 1
