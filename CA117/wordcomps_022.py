#!/usr/bin/env python

import sys

lines = sys.stdin.read().split("\n")

def letters17(s):
	return[word for word in s if len(word) == 17]

def letters18(s):
	return[word for word in s if len(word) > 17]

def vowels2(w):
	return 'a' in w and 'i' in w and 'e' in w and 'o' in w and 'u' in w
def vowels(s):
	return [word for word in s if vowels2(word) == True]

def a4(s):
	return[word for word in s if aaaa(word)]
def aaaa(word):
	count = 0
	for c in word:
		if c.lower() == 'a':
			count = count + 1

	if count == 4:
		return word

def q2(s):
	return[word for word in s if qq(word)]
def qq(word):
	count = 0
	for c in word:
		if c.lower() == 'q':
			count = count + 1

	if count >= 2:
		return word

def cie(s):
	return[word for word in s if 'cie' in word]

def anagramT(w):
	return 'a' in w and 'n' in w and 'g' in w and 'l' in w and 'e' in w and len(w) == 5 and w != 'angle'
def anagram(s):
	return[word for word in s if anagramT(word.lower()) == True]

def iaryT(w):
	return w[-4:] == "iary"
def iary(s):
	return[word for word in s if iaryT(word) == True]

def countes(s):
	a = []
	a.append(s[0])
	for word in s:
		if word.count('e') > a[0].count('e'):
			a = []
			a.append(word)
		elif word.count('e') == a[0].count('e'):
			a.append(word)
	if a[0].count('e') != 0:
		return a

'''
def es(s):
	return max([word for word in s], key=count)
def count(w):
	return w.count('e')
'''

print("Words containing 17 letters:" + " " + str(letters17(lines)))
print("Words containing 18+ letters:" " " + str(letters18(lines)))
print("Shortest word containing all vowels:" + " " + str(sorted(vowels(lines), key=len)[0]))
print("Words with 4 a's:" " " + str(a4(lines)))
print("Words with 2+ q's:" + " " + str(q2(lines)))
print("Words containing cie:" + " " + str(cie(lines)))
print("Anagrams of angle:" " " + str(anagram(lines)))
print("Words ending in iary:" + " " + str(len(iary(lines))))
print("Words with most e's:" + " " + str(countes(lines)))
