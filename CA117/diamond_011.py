#!/usr/bin/env python

import sys

args = int(sys.argv[1])

i = 0
lines = 1
while lines < 2 * args:
    spaces = abs(args - lines)
    dots = abs(args - spaces)
    print((spaces * " " + dots * "* ").rstrip())
    lines = lines + 1
