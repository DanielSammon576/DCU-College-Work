#!/usr/bin/env python

import sys
a = sys.stdin.readline()

with open("some-file.txt", "w") as f:
   f.write("Hello world\n")
