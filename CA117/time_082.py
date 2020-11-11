#!/usr/bin/env python

import sys

class Time(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "The time is {:02d}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __eq__(self, other):
        return (self.hour * 60 * 60) + (self.minute * 60) + self.second == (other.hour * 60 * 60) + (other.minute * 60) + other.second

    def __gt__(self, other):
        return (self.hour * 60 * 60) + (self.minute * 60) + self.second > (other.hour * 60 * 60) + (other.minute * 60) + other.second

    def __lt__(self, other):
        return (self.hour * 60 * 60) + (self.minute * 60) + self.second < (other.hour * 60 * 60) + (other.minute * 60) + other.second

    def __add__(self, other):
        time = (self.hour * 60 * 60) + (self.minute * 60) + self.second + (other.hour * 60 * 60) + (other.minute * 60) + other.second
        minute, second = divmod(time, 60)
        hour, minute = divmod(minute, 60)
        overflow, hour = divmod(hour, 24)
        return Time(hour, minute, second)

    def __iadd__(self, other):
        time = (self.hour * 60 * 60) + (self.minute * 60) + self.second + (other.hour * 60 * 60) + (other.minute * 60) + other.second
        minute, second = divmod(time, 60)
        hour, minute = divmod(minute, 60)
        overflow, hour = divmod(hour, 24)
        self.hour = hour
        self.minute = minute
        self.second = second
        return self

    def seconds_to_time(s):
        minute, second = divmod(s, 60)
        hour, minute = divmod(minute, 60)
        overflow, hour = divmod(hour, 24)
        return Time(hour, minute, second)

def main():

    t1 = Time()
    t2 = Time(9, 35, 16)
    t3 = Time(0, 0, 4)
    t4 = Time(9, 35, 16)

    # Check string representation
    print('Printing times...')
    print(t1)
    print(t2)
    print(t3)

    # Check equality
    print('Checking equality...')
    print(t2 == t4)
    print(t1 == t3)

    # Check greater than/less than
    print('Checking greater than/less than...')
    print(t2 > t3)
    print(t2 < t3)
    print(t4 > t1)
    print(t4 < t1)

    # Check addition
    print('Checking addition...')
    t5 = t2 + t2 + t2
    print(t5)
    print(t5 > t2)

    # Check increment
    print('Checking increment...')
    t33 = t2
    t2 += t2
    t2 += t4
    print(t2)
    print(t33 is t2)
    print(t2 > t3)

    # Check class method
    print('Checking class method...')
    t6 = Time.seconds_to_time(123456)
    print(t6)
    print(t6 > t1)

if __name__ == '__main__':
    main()
