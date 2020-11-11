#!/usr/bin/env python

a = []
s = raw_input()
while s != "end":
   a.append(int(s))
   s = raw_input()

total = 0
j = 0
while j < len(a):
   total = total + a[j]
   j = j + 1

i = 0
while i < len(a):
   if a[i] > total / len(a):
      print a[i]
   i = i + 1
