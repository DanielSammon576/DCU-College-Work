#!/usr/bin/env python

import sys

def pluralise(s):
	a = ["ch", "sh", "x", "s", "z"]
	b = ["a", "e", "i", "o", "u"]
	i = 0
	while i < len(s):
		if s[len(s) - 2:] in a:
		   s = s + "es"
		elif s[len(s) - 1:] in a:
			s = s + "es"
		elif s[len(s) - 1:] == "y" and s[len(s) - 2:len(s) - 1] not in b:
			s = s[:len(s) - 1] + "ies"
		elif s[len(s) - 1:] == "f":
			s = s[:len(s) - 1] + "ves"
		elif s[len(s) - 1:] == "o":
			s = s + "es"
		elif s[len(s) - 2:] == "fe":
			s = s[:len(s) - 2] + "ves"
		else:
			s = s + "s"
		return s

def main():
	lines = sys.stdin.readlines()
	i = 0
	while i < len(lines):
		line = lines[i].strip()
		print(pluralise(line))
		i = i + 1

if __name__ == '__main__':
	main()
