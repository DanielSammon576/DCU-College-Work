#!/usr/bin/env python

import os
files = os.listdir(".")

i = 0
while i < len(files):
    a = files[i].split(".")
    if a[len(a) - 1] == "py":
        with open(files[i]) as f:
            if len(f.read()) != 0:
                print files[i]
    i = i + 1
