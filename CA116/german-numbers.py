#!/usr/bin/env python

import sys
a = sys.stdin.read().split()

numbers = {
   "one": "eins",
   "two": "zwei",
   "three": "drei",
   "four": "vier",
   "five": "funf",
   "six": "sechs",
   "seven": "sieben",
   "eight": "acht",
   "nine": "neun",
   "ten": "zehn",
}

i = 0
while i < len(a):
   if a[i] in numbers:
      print numbers[a[i]]
   i = i + 1
