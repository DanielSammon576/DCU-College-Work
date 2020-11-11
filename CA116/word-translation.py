#!/usr/bin/env python

import sys

with open("translation.txt", "r") as f:
   a = f.read().split()

dick = {}

i = 0
while i < len(a):
   dick[a[i]] = a[i + 1]
   i = i + 2

b = sys.stdin.read().split()

i = 0
while i < len(b):
   if b[i] in dick:
      print dick[b[i]]
   i = i + 1
