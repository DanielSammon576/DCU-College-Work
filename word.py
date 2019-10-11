import sys

def get_plural(word):
	if word[-2:] in ["ch", "sh"]:
		return word + "es"
	elif word[-1] in ["x", "s", "z"]:
		return word + "es"
	elif word[-1] == "y" and word[-2] == "aeiou":
		return word + "es"
	elif word[-1] == "y" and word[-2] not in ["a","i","e","o","u"]:
		return word[:-1] + "ies"
	elif word[-1] == "f":
		return word[:-1] + "ves"
	elif word[-2:] == "fe":
		return word[:-2] + "ves"
	elif word[-1] == "o":
		return word + "es"
	else:
		return word + "s"