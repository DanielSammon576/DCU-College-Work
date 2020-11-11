#!/usr/bin/env python

import sys
args = sys.argv[1]

with open(args, "w") as f:
   f.write("Hello world.\n")
