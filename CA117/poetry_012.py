#!/usr/bin/env python

import sys

max = 0
lines = sys.stdin.readlines()
for line in lines:
    if len(line) > max:
        max = len(line)
for line in lines:
    print("{:^{}s}".format(line.strip(), max - 1))
