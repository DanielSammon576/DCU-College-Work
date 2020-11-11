#!/usr/bin/env python

a = input()
b = input()
c = input()
d = []

smallest = 0
middle = 0
biggest = 0

d = [a, b, c]

if a <= b <= c:
   smallest = a
   middle = b
   biggest = c
elif b <= a <= c:
   smallest = b
   middle = a
   biggest = c
elif c <= a <= b:
   smallest = c
   middle = a
   biggest = b
elif a <= c <= b:
   smallest = a
   middle = c
   biggest = b
elif b <= c <= a:
   smallest = b
   middle = c
   biggest = a
else:
   smallest = c
   middle = b
   biggest = a
print smallest
print middle
print biggest
