from email import message
import sys
import time
from random import randint
from tkinter import *
from tkinter import messagebox

global words
begin = 0
words = []
words_origin = []
name = "name"


root = Tk()

def help():
	messagebox.showinfo(title = "Rules", message = "Правила: \n Как только вы введёте своё имя и нажмёте на кнопку <Стартуем>, перед вами появится строка с 5 словами(в терминале), которые нужно ввести в красное поле через пробел, после чего нажать на кнопку <Проверка> ")



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
	stats_box = []
	for line in stat:
		s = line.split()
		stats_box.append("{} speed = {} mistakes = {}".format(s[0], s[3], s[6]))
	messagebox.showinfo(title = "Stats", message = stats_box)

		

def start():
	global name
	global begin
	global words_origin
	name = nameInput.get()
	
	if name == "":
		messagebox.showinfo(title = "Ошибка", message = "Ошибка: введите имя")

	word1 = words[randint(0, len(words) - 1)]
	word2 = words[randint(0, len(words) - 1)]
	word3 = words[randint(0, len(words) - 1)]
	word4 = words[randint(0, len(words) - 1)]
	word5 = words[randint(0, len(words) - 1)]
	words_origin = [word1, word2, word3, word4, word5]
	word_str = f"Как можно быстрее введите эти 5 слов в красное поле, а затем нажмите кнопку <Проверка>: \n {word1}, {word2}, {word3}, {word4}, {word5}"

	if name != "":
		print(word_str)
		begin = time.time()

def finish():
	end = time.time()
	error_list = []
	mistakes = 0
	words_str = wordInput.get().split()

	speed = round((end - begin) / 5, 1)

	if len(words_str) == 5:
		for i in range (0, 5):
			if words_str[i] != words_origin[i]:
				mistakes += 1
				error_list.append(words_str[i])
		updateStat(name, speed, mistakes)
		if mistakes != 0:
			messagebox.showinfo(title = "Good", message = f"Вы неправильно написали {error_list}")
		else:
			messagebox.showinfo(title = "Good", message = f"У вас нет ошибок, поздравляю!")
	else:
		messagebox.showinfo(title = "Error", message = "Вы написали не все слова, попытка не будет засчитана")

def extractWords():
	dictionary = open("words.txt")
	dic = []
	for word in dictionary:
		dic.append(word[:-1])
	dictionary.close()
	return dic

words = extractWords()

def clearFile():
	f = open("stat.txt", "w")
	f.close()

def quit():
	exit()

def passing():
	pass



root['bg'] = 'black'
root.title("Тренажёр")
root.geometry("500x300")


canvas = Canvas(root, height = 500, width = 300)
canvas.pack()

frame = Frame(root, bg = "black")
frame.place(relwidth = 1, relheight = 1)

title = Label(frame, text = "Введи своё имя", bg = "black", font = 55)
title.pack()

nameInput = Entry(frame, bg = "black")
nameInput.pack()

title = Label(frame, text = "Ниже надо вводить ваши слова(читай правила)", bg = "red", font = 55)
title.pack()

wordInput = Entry(frame, bg = "red")
wordInput.pack()

btn = Button(frame, text = "Проверка", bg = "red", fg = "red", font = 35, command = finish)
btn.pack()

btn = Button(frame, text = "Стартуем", bg = "black", font = 35, command = start)
btn.pack()

btn = Button(frame, text = "Статистика", bg = "black", font = 35, command = seeStat)
btn.pack()

btn = Button(frame, text = "Правила", bg = "black", font = 35, command = help)
btn.pack()

btn = Button(frame, text = "Отчистить результаты", bg = "black", font = 35, command = clearFile)
btn.pack()

btn = Button(frame, text = "Выход", bg = "black", font = 35, command = quit)
btn.pack()



root.mainloop()