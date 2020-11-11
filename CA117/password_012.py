#!/usr/bin/env python

import sys

def charachter(s):
	digit = 0
	upper = 0
	charachter = 0
	symbol = 0
	for chars in s:
		if chars.isupper():
			upper = 1
		elif chars.isdigit():
			digit = 1
		elif chars.islower():
			charachter = 1
		else:
			symbol = 1
	result = digit + upper + charachter + symbol
	return result


def main():
	lines = sys.stdin.readlines()
	i = 0
	while i < len(lines):
		line = lines[i].strip()
		print(charachter(line))
		i = i + 1

if __name__ == '__main__':
	main()
