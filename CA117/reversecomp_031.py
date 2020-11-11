#!/usr/bin/env python

import sys

def main():
	list = [word.strip() for word in sys.stdin if len(word.strip()) >= 5]
	reverselist = []
	for word in list:
		if word[::-1] in list:
			reverselist.append(word)
	print(reverselist)

if __name__ == '__main__':
	main()
