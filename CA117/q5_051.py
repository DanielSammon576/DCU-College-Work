#!/usr/bin/env python

import sys

def converter(t):
	 mins, seconds = t.split(":")
	 total = 0
	 total = int(mins) * 60 + int(seconds)
	 return total

def sorter(l):
	return converter(l[1])

def main():
	d = {}
	for line in sys.stdin:
		try:
			line = line.strip()
			tokens = line.split()
			d[tokens[0]] = min(tokens[1:], key=converter)
		except ValueError:
			continue
	sa = (min(d.items(), key=sorter))
	print(sa[0] + " : " * sa[1])
if __name__ == '__main__':
	main()
