#!/usr/bin/env python

import sys

def capital(s):
	newline = ''
	for word in s:
		newline = newline + ' ' + word.capitalize()
	return newline.strip()

def main():
	lines = sys.stdin.readlines()
	i = 0
	while i < len(lines):
		line = lines[i].strip().split()
		print(capital(line))
		i = i + 1


if __name__ == '__main__':
	main()
