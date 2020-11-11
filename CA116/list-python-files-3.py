#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
   with open(files[i]) as file:
      firstline = file.readline().rstrip()
   if len(firstline) != 0:
      if files[i][len(files[i]) - 3:] == ".py":
         print files[i]
      if firstline == "#!/usr/bin/env python":
         print files[i]
   i = i + 1
