#!/usr/bin/env python

import sys
words = sys.stdin.read().split()

end_markers = {
   ".": True,
   "!": True,
   "?": True,
}

def end_of_sentence(a):
   punctuation = a[-1]
   return punctuation in end_markers

i = 0
while i < len(words):
   j = i
   while j < len(words) and not end_of_sentence(words[j]):
      j = j + 1
   print ' '.join(words[i:j + 1])
   i = j + 1
