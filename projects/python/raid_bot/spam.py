#!/usr/bin/python3
from pyautogui import *
import time, random

MIN_TIME = 50
MAX_TIME = 120

#################################################################

def leet(inp):
	out = ""
	for I in inp:
		if I.lower() == "e": out += "3"
		elif I.lower() == "a": out += "4"
		elif I.lower() == "o": out += "0"
		elif I.lower() == "s": out += "z"
		elif I.lower() == "z": out += "2"
		elif I.lower() == "g": out += "9"
		else:
			if random.randint(0, 1) > 0:
				out += I.upper()
			else:
				out += I
	return out

def printout(inp):
	typewrite(inp)
	press("return")

#################################################################

while True:
	i = input("enter the number spams: ")

	while True:
		inp1 = input("enable leet-speek mode (Y/n): ")
		if inp1.lower() == "y":
			epic_mode = True
			break
		elif inp1.lower() == "n":
			epic_mode = False
			break
		else:
			print("Error: bad input")

	go = input("> ")
	if go.lower() == "go":
		break
	elif go.lower() == "abort":
		exit()
	elif go.lower() == "reset":
		print("")
		continue
	else:
		print("Error: invalid command\n")
print("select the text box of the target and wait for the 5 second timer to finish\n")

inp_main = []
doc = open("input.txt", "r")
for line in doc:
	if line == "\n":
		break
	else:
		inp_main += [line.strip()]

time.sleep(5)
for x in range(0, int(i)):
	if epic_mode:
		if random.randint(0, 1) > 0:
			printout(leet(inp_main[random.randint(0, len(inp_main) -1)]))
			continue

	printout(inp_main[random.randint(0, len(inp_main) -1)])
	time.sleep(random.randint(MIN_TIME, MAX_TIME) / 10)