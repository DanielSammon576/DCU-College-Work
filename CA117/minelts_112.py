#!/usr/bin/env python
from priority_queue_112 import PQ
import sys

def main():
    s = PQ()
    m = int(sys.argv[1])
    for line in sys.stdin:
        n = int(line.strip())
        if s.size() < m:
            s.insert(n)
        else:
            if n < s.getMax():
                s.insert(n)
                s.delMax()
    while s.size() > 0:
        print(s.delMax())

if __name__ == '__main__':
    main()
