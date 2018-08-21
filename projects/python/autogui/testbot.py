#!/usr/bin/python
import pyautogui, time
pyautogui.PAUSE = 1

def sep(inp):
	x = ""
	y = x
	flip = False
	for c in str(inp):
		if c == ",":
			flip = True
			continue
		if c == " ":
			continue 

		if flip == False:
			x += c
		else:
			y += c
	return x,y

time.sleep(1)
#pyautogui.typewrite('Hello world!\n', interval=0.25)

tlist = []
for i in pyautogui.locateCenterOnScreen('ref/bin.png'):
	#x,y = sep(i)
	#print(str(x) + " | " + str(y))
	tlist += [i]

pyautogui.moveTo(tlist[0], 0)
pyautogui.click()

print(tlist)
if tlist != []:
	print("good")
else: print("can't find target")