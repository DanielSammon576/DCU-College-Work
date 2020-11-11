#!/usr/bin/env python

n = 20
import sys

lines = sys.stdin.readlines()
plot = {}

i = 0
while i < len(lines):
   tokens = lines[i].split()
   key = tokens[0] + "-" + tokens[1]
   plot[key] = True
   i = i + 1
print plot

print " " + "-" * n

i = 0
while i < n:
   y = n - i - 1
   output = []

   x = 0
   while x < n:
      key = str(x) + "-" + str(y)
      if key in plot:
         output.append("*")
      else:
         output.append(" ")
      x = x + 1

   print "|" + "".join(output) + "|"
   i = i + 1

print " " + "-" * n
