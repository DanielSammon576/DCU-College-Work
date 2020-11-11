#!/usr/bin/env python

import sys
from math import pi
args = sys.argv[1]

print('{:.{}f}'.format(pi, args))
