#!/usr/bin/env python

import sys

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        return ((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5

class Shape(object):
    def __init__(self, list1):
        self.points = list1

    def sides(self):
        if len(self.points) == 4:
            point1 = self.points[0]
            point2 = self.points[1]
            point3 = self.points[2]
            point4 = self.points[3]
            side1 = Point.distance(point1, point2)
            side2 = Point.distance(point2, point3)
            side3 = Point.distance(point3, point4)
            side4 = Point.distance(point4, point1)
            return [side1, side2, side3, side4]
        else:
            point1 = self.points[0]
            point2 = self.points[1]
            point3 = self.points[2]
            side1 = Point.distance(point1, point2)
            side2 = Point.distance(point2, point3)
            side3 = Point.distance(point3, point1)
            return [side1, side2, side3]

    def perimeter(self):
        if len(self.points) == 4:
            point1 = self.points[0]
            point2 = self.points[1]
            point3 = self.points[2]
            point4 = self.points[3]
            side1 = Point.distance(point1, point2)
            side2 = Point.distance(point2, point3)
            side3 = Point.distance(point3, point4)
            side4 = Point.distance(point4, point1)
            perimeter = side1 + side2 + side3 + side4
            return perimeter
        else:
            point1 = self.points[0]
            point2 = self.points[1]
            point3 = self.points[2]
            side1 = Point.distance(point1, point2)
            side2 = Point.distance(point2, point3)
            side3 = Point.distance(point3, point1)
            perimeter = side1 + side2 + side3
            return perimeter

class Triangle(Shape):
    def area(self):
        point1 = self.points[0]
        point2 = self.points[1]
        point3 = self.points[2]
        side1 = Point.distance(point1, point2)
        side2 = Point.distance(point2, point3)
        side3 = Point.distance(point3, point1)
        s1 = (side1 + side2 + side3) / 2
        A = (s1 * (s1 - side1) * (s1 - side2) * (s1 - side3)) ** (1 / 2)
        return A

class Square(Shape):
    def area(self):
        point1 = self.points[0]
        point2 = self.points[1]
        point3 = self.points[2]
        point4 = self.points[3]
        side1 = Point.distance(point1, point2)
        side2 = Point.distance(point2, point3)
        side3 = Point.distance(point3, point4)
        side4 = Point.distance(point4, point1)
        A = side1 * side2
        return A
