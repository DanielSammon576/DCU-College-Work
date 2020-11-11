#!/usr/bin/env python

curr = input()

while curr != 0:
   prev = curr
   curr = input()
   if prev < curr:
      print "higher"
   elif prev == curr:
      print "equal"
   else:
      print "lower"
   curr = prev
   curr = input()
