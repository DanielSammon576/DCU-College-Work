#!/usr/bin/env python

import sys


a = []
s = sys.stdin.readline()
while s != -1:
	a.append(s)
	s = sys.stdin.readline()

print(a)
