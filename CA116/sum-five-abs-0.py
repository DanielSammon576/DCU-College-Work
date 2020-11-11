#!/usr/bin/env python

total = 0

n = input()
while n != 0:
   if n < 0:
      n = - n
      total = total + n
   else:
      total = total + n
   n = input()

print total
