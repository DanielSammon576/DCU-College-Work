#!/usr/bin/env python

import sys
args = int(sys.argv[1])

s = raw_input()

i = 0
num_commas = 0
while i < len(s) and num_commas < args:
   if s[i] == ',':
      num_commas = num_commas + 1
   i = i + 1

if i < len(s):
   j = i
   while j < len(s) and s[j] != ',':
      j = j + 1
print s[i:j]
