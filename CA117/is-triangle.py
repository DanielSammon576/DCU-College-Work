#!/usr/bin/env python

a = input()
b = input()
c = input()

if a + b > c and b + c > a and a + c > b:
	print("Yes")
else:
	print("No")
