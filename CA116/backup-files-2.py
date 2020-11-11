#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files) and (os.path.isfile(files[i]) != True):
   i = i + 1

if i < len(files):
   with open(files[i]) as f:
      with open(files[i] + ".bak", "w") as f2:
         f2.write(f.read())
