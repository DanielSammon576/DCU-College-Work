#!/usr/bin/env python

import sys
snap = {}
a = []
line = sys.stdin.readline().strip()
while 0 < len(line) and line != "\n" and len(a) == 0:
   if line in snap:
      a.append("snap: " + line)
   else:
      snap[line] = True
   line = sys.stdin.readline().strip()
if len(a) != 0:
   print a[0]
