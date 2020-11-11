#!/usr/bin/env python

import sys
args = sys.argv[1]

s = raw_input()

i = 0
j = 0
while j < len(s) and s[j] != ",":
   j = j + 1

p = 0
while s[i:j] != args:
   p = p + 1
   i = j + 1

   j = i
   while j < len(s) and s[j] != ",":
      j = j + 1

print p
