#!/usr/bin/env python

import secret_number
n = 1000

def play()
   i = 500
   hi = 1000
   low = 0
   z = seret_number.guess(i)
   while i < n and z != "correct":
      if z == "too-low":
         low = i
         i = low + ((hi - low) / 2)
      elif z == "too-high":
         hi = i
         i = hi - ((hi - low) / 2)
      z = secret_number.guess(i)
