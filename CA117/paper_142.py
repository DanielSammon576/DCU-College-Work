import sys

def main():
	lines = sys.stdin.readlines()
	for line in lines:
		line = line.strip().split()
		#print(line)
		word1 = line[0]
		word2 = line[1]
		if word1 == word2:
			print("Draw")
		if word1 == "paper" and word2 == "rock":
			print("Player 1 wins")
		if word1 == "rock" and word2 == "paper":
			print("Player 2 wins")
		if word1 == "scissors" and word2 == "paper":
			print("Player 1 wins")
		if word1 == "paper" and word2 == "scissors":
			print("Player 2 wins")
		if word1 == "rock" and word2 == "scissors":
			print("Player 1 wins")
		if word1 == "scissors" and word2 == "rock":
			print("Player 2 wins")

if __name__ == '__main__':
	main()
