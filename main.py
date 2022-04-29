import sys
import time
from random import randint

words = []

def help():
	print("Write \'start\' to start training")
	print("Write \'stat\' to see your's full statistic")
	print("Write \'add\' to add new word in dictionary")
	print("Write \'clear\' to clear stat")
	print("Write \'quit\' to quit from program")


def extractStats():
	f = open("stat.txt", "r")
	stats = []
	for line in f:
		s = line.split()
		stats.append([s[0], s[3], s[6]])
	f.close()
	return stats

def updateStat(name, score, mistakes):
	stats = extractStats()
	stats.append([name, score, mistakes])
	stat = open("stat.txt", "w")
	for line in stats:
		stat.write(line[0] + " speed = " + str(line[1]) + " mistakes = " + str(line[2]) + '\n')

def seeStat():
	stat = open("stat.txt", "r")
	for line in stat:
		s = line.split()
		print("{} speed = {} mistakes = {}".format(s[0], s[3], s[6]))

def start():
	print("What is your name?")
	name = input()
	score = 0
	mistakes = 0
	wordsWhereWasMistake = []
	wrongWords = []
	begin = time.time()
	gameTime = 10
	while time.time() - begin < gameTime:
		word = words[randint(0, len(words) - 1)]
		print(word)
		s = input()
		if s == word:
			score += len(word)
		else:
			mistakes += 1
			wordsWhereWasMistake.append(word)
			wrongWords.append(s)
	print("Your speed is {} characters per minute".format(score / gameTime))
	if (mistakes != 0):
		print("Your mistakes was:")
		for i in range(mistakes):
			print("The word was: " + wordsWhereWasMistake[i] + ", you wrote: " + wrongWords[i])
		print()
	else:
		print("You made 0 mistakes, great!")
	updateStat(name, score / gameTime, mistakes)

def extractWords():
	dictionary = open("words.txt")
	dic = []
	for word in dictionary:
		dic.append(word[:-1])
	dictionary.close()
	return dic

def clearFile():
	f = open("stat.txt", "w")
	f.close()

def addNewWord():
	print("Write your's new word")
	word = input()
	words.append(word)

	dictionary = open("words.txt", "w")
	for word in words:
		dictionary.write(word + '\n')
	dictionary.close()

	print("Your word successfully added")


def main():
	global words
	words = extractWords()

	print("Welcome to keyboard training")
	print("Write help to see all commands")

	while True:
		s = input()
		if s == "help":
			help()
		if s == "start":
			start()
		if s == "stat":
			seeStat()
		if s == "add":
			addNewWord()
		if s == "clear":
			clearFile()
		if s == "quit":
			break

if __name__ == "__main__":
	main()
