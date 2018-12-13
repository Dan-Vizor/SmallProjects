#!/usr/bin/python3
from pyautogui import *
import time, random

try:
        doc = open("settings.txt","r")
except:
        print("Error: no settings file")
        exit()

raw_settings = doc.read().split(",")
try:
        MIN_TIME = int(raw_settings[0])
        MAX_TIME = int(raw_settings[1])
        COOLDOWN = int(raw_settings[2])
except:
        print("Error: bad settings file")
        exit()

# functions ###############################################################

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
			if random.randint(1, 3) < 2:
				out += I.upper()
			else:
				out += I
	return out

def printout(inp):
	typewrite(inp)
	press("return")

def inputblock():
        while True:
                i = input("enter the number of prints: ") 
                try:
                        if int(i) in range(1,99999): break
                        else: print("Error: nuber out of acceptable range\n")
                except: print("Error: input not a number\n")

        while True:
                inp1 = input("enable epic mode (Y/n): ")
                if inp1.lower() == "y":
                        epic_mode = True
                        break
                elif inp1.lower() == "n":
                        epic_mode = False
                        break
                else:
                        print("Error: bad input\n")
        return [i, epic_mode]

# main code ###############################################################

inputFlag = True
while True:
        if inputFlag:
                out = inputblock()
                i = out[0]
                epic_mode = out[1]
        inputFlag = False
        
        go = input("> ")
        if go.lower() == "go":
                break
        elif go.lower() == "abort":
                exit()
        elif go.lower() == "time":
                print("time between prints:\nmin: {}\nmax: {}\n".format(MIN_TIME, MAX_TIME))
        elif go.lower() == "reset":
                print("")
                inputFlag = True
                continue
        else:
                print("Error: invalid command\n")
print("select the target text box and wait for the {} second timer to finish\n".format(COOLDOWN))

inp_main = []
doc = open("input.txt", "r")
for line in doc:
	if line.strip() == "":
		break
	else:
		inp_main += [line.strip()]
if inp_main == "":
        print("Error: input file is blank")
        exit()

time.sleep(COOLDOWN)
for x in range(0, int(i)):
	if epic_mode:
		if random.randint(1, 4) > 1:
			printout(leet(inp_main[random.randint(0, len(inp_main) -1)]))
			time.sleep(random.randint(MIN_TIME, MAX_TIME) / 10)
			continue

	printout(inp_main[random.randint(0, len(inp_main) -1)])
	time.sleep(random.randint(MIN_TIME, MAX_TIME) / 10)
print("done")
