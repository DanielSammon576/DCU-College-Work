#!/usr/bin/env python

import sys
args = sys.argv[1:]

total = 0

i = 0
while i < len(args):
   with open(args[i], "r") as f:
   	  print f
      a = f.read().split()
      j = 0
      while j < len(a):
         total = total + int(a[j])
         j = j + 1
   i = i + 1

print total
