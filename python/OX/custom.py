#!/usr/bin/python3
import random

def custom(GameData, side):
	if GameData[4] == " ": return 5

	i = 1
	for each in GameData:
		if each != side: continue
		if i == 1:
			if GameData[3] == side and GameData[6] == " ": return 7 # left vertical
			if GameData[1] == side and GameData[2] == " ": return 3 # top horasontal
			if GameData[4] == side and GameData[8] == " ": return 9 # back diagonal

		if i == 2:
			if GameData[2] == side and GameData[0] == " ": return 1 # top horasontal
			if GameData[4] == side and GameData[7] == " ": return 8 # middle vertical

		if i == 3:
			if GameData[2] == side and GameData[0] == " ": return 1 # right vertical
			if GameData[4] == side and GameData[6] == " ": return 7 # forward diagonal

		if i == 4:
			if GameData[6] == side and GameData[0] == " ": return 1 # back diagonal
			if GameData[4] == side and GameData[5] == " ": return 6 # middle horasontal

		if i == 5:
			if GameData[7] == side and GameData[1] == " ": return 2 # middle vertical

		if i == 6:
			if GameData[8] == side and GameData[1] == " ": return 2 # right vertical
			if GameData[4] == side and GameData[3] == " ": return 4 # forward diagonal

		if i == 7:
			if GameData[7] == side and GameData[8] == " ": return 9 # bottom horisontal

		if i == 8:
			if GameData[4] == side and GameData[1] == " ": return 2 # middle vertical
			if GameData[7] == side and GameData[6] == " ": return 7 # bottom horisontal

		if i == 10: break
		i += 1


	EmptySlots = []
	i = 1
	for each in GameData:
		if each == " ": EmptySlots += [i]
		i += 1

	RandomSlot = random.choice(EmptySlots)
	return RandomSlot