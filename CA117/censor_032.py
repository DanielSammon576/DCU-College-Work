#!/usr/bin/env python

import sys

def censor():
    with open(sys.argv[1], 'r') as f:
        a = f.read().split()
    words = sys.stdin.read().split(" ")
    #print(words)
    for censor in a:
        i = 0
        for word in words:
            if censor in word:
                word = word.replace(censor, "@" * len(censor))
                words[i] = word
            i += 1
    words = " ".join(words)
    print(words.strip())

def main():
    censor()

if __name__ == '__main__':
    main()
