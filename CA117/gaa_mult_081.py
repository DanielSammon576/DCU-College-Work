#!/usr/bin/env python

import sys

class Score(object):
	def __init__(self, goal=0, point=0):
		self.goal = goal
		self.point = point

	def __eq__(self, other):
		return ((self.goal * 3) + self.point) == (other.goal * 3) + other.point

	def __gt__(self, other):
		return ((self.goal * 3) + self.point) > (other.goal * 3) + other.point

	def __lt__(self, other):
		return ((self.goal * 3) + self.point) < (other.goal * 3) + other.point

	def __mul__(self, other):
		self.goal = self.goal * other
		self.point = self.point * other
		return self

	def __rmul__(self, other):
		self.goal = other * self.goal
		self.point = other * self.point
		return self

	def __imul__(self, other):
		self.goal *= other
		self.point *= other
		return self

	def __str__(self):
		return("{} goal(s) and {} point(s)".format(self.goal, self.point))

def main():

    # Create some instances of Score
    s1 = Score()
    s2 = Score(3, 12)
    s3 = Score(4, 9)
    s4 = Score(2, 11)
    s5 = Score(1, 1)

    # Display
    print('Display...')
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    # Multiplication
    print('Multiplication...')
    s2 = s2 * 2
    print(s2)
    print(s2 > s3)

    # Right multiplication
    print('Right multiplication...')
    s2 = 2 * s2
    print(s2)
    print(s2 > s3)

    # In-place multiplication
    print('In-place multiplication...')
    s2alias = s2
    s2 *= 2
    print(s2)
    print(s2alias)
    print(s2 == s2alias)

if __name__ == '__main__':
    main()