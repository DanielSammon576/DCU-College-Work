#!/usr/bin/env python

import sys

def main():
	print("Enter a name and number, or a name and ? to query (!! to exit)")
	d = {}
	line = sys.stdin.readline()
	#print(line)
	while line != "!!":
		line = line.split()
		if len(line) == 2:
			if line[1] != "?":
				d[line[0]] = line[1]
			elif line[1] == "?" and line[0] not in d:
				print("Sorry there is no " + line[0])
			else:
				print(line[0] + " has number " + d[line[0]])
		line = sys.stdin.readline()

	print("Bye")

if __name__ == '__main__':
	main()
