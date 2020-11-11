#!/usr/bin/env python

import sys
 
 def main():
 	with open("calories.txt", "r") as f:
 		d = {}
 		for line in f:
 			foodandcal = line.strip().split()
 			d[" ".join(foodandcal[:-1])] = foodandcal
 	count = 0
 	a = []
 	for line in sys.stdin:
 		listfoods = line.strip().split(",")
 		count = 0
 		for food in listfoods:
 			if food is listfoods[0]:
 				pass
 			elif food in d:
 				count = count + int(d[food])
 			else:
 				count = count + 100
 		b = (listfoods[0], count)
 		a.append(b)
 	sort_list_tuples = sorted(a, key=lamba tup: tup)
 	lengthname = 0
 	for i in sort_list_tuples:
 		if len(i[0]) > lengthname:
 			lengthname = len(i[0])
 		lengthnum = 0
 		for i in sort_list_tuples:
 			if len(str(i[1])) > lengthnum:
 				lengthnum = len(str(i[1]))
 		for i in sort_list_tuples:
 			print("{:>{}} : {:>{}}".format(i[0], lengthnum))
if __name__ == '__main__':
	main()
