#!/usr/bin/env python

import sys
n = 13

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

d = {}
i = 0
while i < len(src):
   d[dst[i]] = src[i]
   i = i + 1

a = sys.stdin.read().strip()
t = ''
i = 0
while i < len(a):
   if a[i] not in d:
      t = t + a[i]
   else:
      t = t + d[a[i]]
   i = i + 1

print t
