#!/usr/bin/env python

import sys
import os
import re

args = sys.argv[1]

#print(args)

with open(args, 'r') as f:
    p = f.read().splitlines()

print(p)
