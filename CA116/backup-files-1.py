#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
   if files[i][len(files[i]) - 4:] != ".bak":
      with open(files[i]) as f:
         with open(files[i] + ".bak", "w") as f2:
            f2.write(f.read())
   i = i + 1
