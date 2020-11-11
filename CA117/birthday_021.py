#!/usr/bin/env python

import sys

import calendar

def poems(s):
    if s == 0:
        return "You were born on a Monday and Monday's child is fair of face."
    elif s == 1:
        return "You were born on a Tuesday and Tuesday's child is full of grace."
    elif s == 2:
        return "You were born on a Wednesday and Wednesdays's child is full of woe."
    elif s == 3:
        return "You were born on a Thursday and Thursday's child has far to go."
    elif s == 4:
        return "You were born on a Friday and Friday's child is loving and giving."
    elif s == 5:
        return "You were born on a Saturday and Saturday's child works hard for a living."
    elif s == 6:
        return "You were born on a Sunday and Sunday's child is fair and wise and good in every way."

def main():
    year = int(sys.argv[3])
    month = int(sys.argv[2])
    day = int(sys.argv[1])
    bday = calendar.weekday(year, month, day)
    day = poems(bday)
    print(day)

if __name__ == '__main__':
    main()
