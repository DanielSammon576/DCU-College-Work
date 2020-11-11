#!/usr/bin/env python

def topscore(students):
    with open(students, "r") as f:
        f = f.readlines()
        newhigh = 0
        for c in f:
            mark = c.strip().split()
            if newhigh < int(mark[0]):
                newhigh = int(mark[0])
                newstudent = mark[1:]
        count = 0
        highstudents = ""
        for c in f:
            mark = c.strip().split()
            if int(mark[0]) == newhigh and count == 0:
                count = count + 1
                highstudents = "Best student(s): " + " ".join(mark[1:])
            elif int(mark[0]) == newhigh and count >= 1:
                highstudents = highstudents + "," + " " + " ".join(mark[1:])
        return highstudents + "\n" + "Best mark: " + str(newhigh)

def main():
    import sys
    students = sys.argv[1]
    print(topscore(students))

if __name__ == '__main__':
    main()
