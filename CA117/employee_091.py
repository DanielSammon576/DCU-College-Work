#!/usr/bin/env python

import sys

class Employee(object):
    def __init__(self, name='', number=0):
        self.name = name
        self.number = number

    def wages(self):
        return 0

    def __str__(self):
        return("Name: {}\nNumber: {}\nWages: {:.2f}".format(self.name, self.number, self.wages()))

class Manager(Employee):
    def __init__(self, name='', number=0, salary=0):
        self.name = name
        self.number = number
        self.salary = salary

    def wages(self):
        return self.salary / 52


class AssemblyWorker(Employee):
    def __init__(self, name='', number=0, hourly_rate=0, hours=0):
        self.name = name
        self.number = number
        self.hourly_rate = hourly_rate
        self.hours = hours

    def wages(self):
        return self.hourly_rate * self.hours

def main():

    e1 = Manager('Mary', 1, 50000)
    e2 = AssemblyWorker('Fred', 2, 15.50, 40)
    e3 = Employee('Sean', 3)

    print(e1)
    print(e2)
    print(e3)

if __name__ == '__main__':
    main()
