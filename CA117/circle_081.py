#!/usr/bin/env python

import sys

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return 'Point: ({}, {}'.format(self.x, self.y)

    def midpoint(self, other):
        return (self.x + other.x) / 2, (self.y + other.y) / 2

class Circle(object):

    def __init__(self, p=Point(0, 0), r=0):
        self.r = int(r)
        self.p = p

    def __str__(self):
        return 'Centre: ({:.1f}, {:.1f})\nRadius: {}'.format(self.p.x, self.p.y, self.r)

    def __add__(self, other):
        tr = self.r + other.r
        tx, ty = Point.midpoint(self.p, other.p)

        return Circle(Point(tx, ty), tr)

def main():
    p1 = Point()
    p2 = Point(4, 6)
    c1 = Circle(p1, 10)
    c2 = Circle(p2, 5)
    c3 = c1 + c2
    print(c3)

    p3 = Point(10, 10)
    c4 = Circle(p3, 15)
    c5 = c2 + c4
    print(c5)

if __name__ == '__main__':
    main()
