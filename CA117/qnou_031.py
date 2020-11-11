#!/usr/bin/env python

import sys

def main():
    list = []
    for word in sys.stdin:
        if 'q' in word.lower():
            if word.lower().count('qu') != word.lower().count('q'):
                list.append(word.strip())
    print("Words with q but no u:", list)

if __name__ == '__main__':
    main()
