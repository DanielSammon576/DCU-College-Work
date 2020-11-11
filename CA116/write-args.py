#!/usr/bin/env python

import sys
args = sys.argv[1]

words = sys.argv[2:]

with open(args, "w") as f:
   i = 0
   while i < len(words):
      f.write(words[i] + "\n")
      i = i + 1
