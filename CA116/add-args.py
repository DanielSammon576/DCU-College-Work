#!/usr/bin/env python

import sys
args = sys.argv[1:]


total = 0
i = 0
while i < len(args):
   total = int(args[i]) + total
   i = i + 1

print total
