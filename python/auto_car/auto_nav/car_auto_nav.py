#!/usr/bin/python3
def midSen():
	return True

def optSetUp():
	doc = open("turnBi.txt","w")
	doc.write("0")

try:
	doc = open("turnBi.txt","r")
	for line in doc:
		turnBi = int(line)
		break
except:
	optSetUp()
	turnBi = 0

speed = 20
while True:
	if midSen:
		speed = 0
		while midSen:
			if turnBi == 0: pass # will turn right 1 degree
			else: pass # will turn left 1 degree
			#####
			break
			#####
		speed = 20
