#!/usr/bin/env python

import sys

def build_dictionary(filename):
    d = {}
    with open(filename, "r") as f:
        wordsandnums = f.read().split()
        i = 0
        while i < len(wordsandnums):
            d[wordsandnums[i]] = wordsandnums[i + 1]
            i = i + 2
        return d
def extract_range(d, low, high):
    nd = {}
    for word in d:
        if low <= int(d[word]) <= high:
            nd[word] = d[word]
    return nd
