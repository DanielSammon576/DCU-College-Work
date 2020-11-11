#!/usr/bin/env python

import sys

line = sys.stdin.readline()
total = 0
while 0 < len(line) and line != "\n":
   total = total + int(line)
   line = sys.stdin.readline()
sys.stdout.write(str(total) + "\n")
