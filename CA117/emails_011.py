#!/usr/bin/env python

import sys

#def search(s):
#	i = 0
#	while i < len(s) and (s[i] < "0" and s[i] > "9"):
#		i = i + 1
#
#	if i < len(s):
#		return s[:i]
#
#def capital(s):
#	f_name = s[0].strip()
#	print(f_name)
#	l_name = s[1].strip()
#	print(l_name)
#	l_name = search(s[1])
#	return l_name
#
#def main():
#	lines = sys.stdin.readlines()
#	i = 0
#	while i < len(lines):
#		line = lines[i].strip().split(".")
#		print(capital(line))
#		i = i + 1
#
#if __name__ == '__main__':
#	main()

def fname(b):
	fname = b[0].capitalize()
	return fname

def lname(c):
	part = c[1].split("0")[0]
	s = ""
	for letter in part:
		if letter >= "0" and letter <= "9":
			return s.capitalize()
		else:
			s = s + letter

def main():
	for line in sys.stdin:
		a = line.split(".")
		print(fname(a), lname(a))

if __name__ == '__main__':
	main()
