#!/usr/bin/env python

import sys

def main():
    dist = sys.stdin.readline()
    dist = int(dist)
    #print(dist)

    t = 0
    second_d = 0
    dif = 0
    for line in sys.stdin:
        line = line.strip().split()
        second_d, r, g = int(line[0]), int(line[1]), int(line[2])
        #print(second_d, r, g)
        t = t + (second_d - dif)
        stopping = t - ((r + g) * (t // (r + g)))
        if stopping < r:
            other = (r - stopping)
            t = t + other
            #print(t)
        dif = second_d
    t = t + (dist - second_d)
    print(t)

if __name__ == '__main__':
    main()
