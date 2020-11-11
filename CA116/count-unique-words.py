#!/usr/bin/env python

import sys
a = sys.stdin.read().split()

d = {}

count = 0

i = 0
while i < len(a):
   d[a[i]] = count
   i = i + 1

i = 0
while i < len(a):
   d[a[i]] = d[a[i]] + 1
   i = i + 1
print d

for word in d:
   if d[word] == 1:
      print word
