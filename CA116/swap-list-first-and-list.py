#!/usr/bin/env python

if __name__ == "__main__":
   a = [8, 9, 4, 7, 2, 11, 11, 12]

tmp = a[0]
a[0] = a[len(a) - 1]
a[len(a) - 1] = tmp
