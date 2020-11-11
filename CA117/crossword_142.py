import sys

def letters(line):
	word1 = line[0]
	word2 = line[1]
	for letter in word1:
		if letter in word2:
			x = letter
			break
	return(x)

def main():
	line = sys.stdin.readline()
	line = line.strip().split()

	print(letters(line))
if __name__ == '__main__':
	main()
