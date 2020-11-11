#!/usr/bin/env python

import sys

class Employee(object):

    next_employee_number = 0

    def __init__(self, name, employee_number=0, hours_worked=0, hourly_rate=9.25, number=0):
        self.name = name
        self.employee_number = employee_number
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        self.number = Employee.next_employee_number
        Employee.next_employee_number += 1

    def add_hours(self, number):
        self.hours_worked += number

    def __str__(self):
        return "Name: {}\nID: {}\nHours: {:.2f}\nRate: {:.2f}\nWages: {:.2f}".format(self.name, self.number, self.hours_worked, self.hourly_rate, (self.hours_worked * self.hourly_rate))

def main():

    # Check class attributes
    print('Checking class attributes...')
    print(Employee.next_employee_number)

    # Create two employees
    e1 = Employee('Jimmy')
    e2 = Employee('Mary', hours_worked=12, hourly_rate=12.40)

    # Check string representation
    print('Printing employees...')
    print(e1)
    print(e2)

    # Check adding hours
    print('Checking adding hours...')
    e1.add_hours(10.5)
    e2.add_hours(30)
    print(e1)
    print(e2)

    # Check class attributes
    print('Checking class attributes...')
    print(Employee.next_employee_number)

if __name__ == '__main__':
    main()
