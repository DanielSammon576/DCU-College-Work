#!/usr/bin/env python

import sys

def main():
	for line in sys.stdin:
		n,base = line.split()
		tot = 0
		i = 0
		while i < len(n):
			tot = tot + (int(base) ** i) * int(n[-1-i])
			i = i + 1
		print(tot)

if __name__ == '__main__':
	main()
