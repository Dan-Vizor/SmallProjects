#!/usr/bin/python3

def speed(speed):
	print("set moters to " + str(speed) + "%")

def turn(turn):
	print("set turning moter to " + str(turn))

def stop():
	speed(0)
	turn(0)
	print("bot stoped")
	
def lights(t):
	if t == 1:
		print("lights set to on")
		return
	if t == 0:
		print("lights set to off")
		return
	print("error: invaid input for .lights")


def Lsen():
	sen = input("Lsen output [y/n]: ")
	if sen == "y": return True
	return False
def Msen():
	sen = input("Msen output [y/n]: ")
	if sen == "y": return True
	return False
def Rsen():
	sen = input("Rsen output [y/n]: ")
	if sen == "y": return True
	return False
