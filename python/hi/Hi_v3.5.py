#!/usr/bin/python3

import webbrowser, time, os
URL = 'https://www.google.co.uk/search?q=where+is+Paul+Ramage?'
MAX = 31
OS = "linux"

def killTask(OS):
	if OS == "linux":
		os.system("pkill firefox")
	elif OS == "windows":
		os.system("taskkill /im chrome.exe")
	time.sleep(2)

def spam(loop):
    for x in range(0,loop):
        webbrowser.open(URL)
        time.sleep(0.5)
def menu():
    print("run = run program")
    print("inf = run program forever")
    print("clear = closes the chrome window")
    print("autoclear on = closes the chrome tab after the 'run' command")
    print ("autoclear off = disables the autoclear function")
    print("change no = lets you edit the loop number")
    print("exit = close this program and chrome\n")

webbrowser.open(URL)
print("solve CAPTCHA then press enter")
x = input()
killTask(OS)

while True:
    loop = input("enter number of tabs per loop: ")
    try:
        loop = int(loop)
        if loop > MAX: print("error: don't be stupid\n")
        else: break
    except: print("error: invalid input (enter a number)\n")

inf = False
autoclear = False
while True:
    if inf:
        spam(loop)
        time.sleep(loop /2)
        killTask(OS)
        time.sleep(inf_break)
    else:
        inp = input(": ")
        if inp == "exit":
            killTask(OS)
            exit()
            
        elif inp == "inf":
            inf = True
            while True:
                inf_break = input("\nenter break time between runs: ")
                try:
                    inf_break = int(inf_break)
                    if loop < 1: print("error: input number to low\n")
                    else: break
                except: print("error: invalid input (enter a number)\n")
            
        elif inp == "autoclear on" or inp == "autoclear":
            autoclear = True
            print("autoclear set to: ON")

        elif inp == "autoclear off":
            autoclear = False
            print("autoclear set to: OFF")

        elif inp == "clear": killTask(OS)
            
        elif inp == "run":
            if autoclear:
                spam(loop)
                time.sleep(loop /2)
                killTask(OS)
            else:
                spam(loop)
            
        elif inp == "change no":
            while True:
                loop = input("enter number of tabs per loop: ")
                try:
                    loop = int(loop)
                    if loop > MAX: print("error: don't be stupid\n")
                    else: break
                except: print("error: invalid input (enter a number)\n")
                
        elif inp == "help": menu()
            
        else: print("error: invalid command (enter 'help' for list of commands)\n")