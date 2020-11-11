#!/usr/bin/env python

import sys

class Queue(object):
    def __init__(self):
        self.d = []

    def enqueue(self, other):
        self.d.append(other)

    def dequeue(self):
        return self.d.pop(0)

    def first(self):
        return self.d[0]

    def is_empty(self):
        return len(self.d) == 0

    def __len__(self):
        return len(self.d)

def main():

    q = Queue()

    print(len(q))
    q.enqueue(1)
    print(q.first())
    print(q.is_empty())
    print(q.dequeue())
    print(q.is_empty())
    try:
        print(q.dequeue())
    except IndexError:
        print('Error')
    try:
        print(q.first())
    except IndexError:
        print('Error')
    q.enqueue('cat')
    q.enqueue('dog')
    q.enqueue('fish')
    print(len(q))
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())

if __name__ == '__main__':
    main()
