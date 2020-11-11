#!/usr/bin/env python

import sys
args = sys.argv[1]

total = 0

with open(args, "r") as f:
   a = f.read().split()
   i = 0
   while i < len(a):
      total = total + int(a[i])
      i = i + 1

print total
