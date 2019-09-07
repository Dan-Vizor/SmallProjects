#!/usr/bin/python3
# Version 2.1

import random, time
from custom import custom

def PrintGame(GameData):
	OutString = "-------------\n"
	OutString += "| {} | {} | {} |\n".format(GameData[0], GameData[1], GameData[2])
	OutString += "-------------\n"
	OutString += "| {} | {} | {} |\n".format(GameData[3], GameData[4], GameData[5])
	OutString += "-------------\n"
	OutString += "| {} | {} | {} |\n".format(GameData[6], GameData[7], GameData[8])
	OutString += "-------------\n"
	print(OutString)

def SecInput(InputMessage, InputType):
	while True:
		OutData = input(InputMessage)
		try:
			if InputType == "string".lower(): str(OutData)
			elif InputType == "int".lower(): int(OutData)
			elif InputType == "float".lower(): float(OutData)
			return OutData

		except:
			print("Error: invalid input '{}'",format(OutData))
			raise SystemExit
	return OutString

def TestWin(GameData):
	if len(GameData) != 9:
		print("Error: invalid data given to TestWin()")
		raise SystemExit

	# X
	# horisontal
	if GameData[0] == "X" and GameData[1] == "X" and GameData[2] == "X": return "X" # top
	if GameData[3] == "X" and GameData[4] == "X" and GameData[5] == "X": return "X" # middle
	if GameData[6] == "X" and GameData[7] == "X" and GameData[8] == "X": return "X" # bottom
	# vertical
	if GameData[0] == "X" and GameData[3] == "X" and GameData[6] == "X": return "X" # left
	if GameData[1] == "X" and GameData[4] == "X" and GameData[7] == "X": return "X" # middle
	if GameData[2] == "X" and GameData[5] == "X" and GameData[8] == "X": return "X" # right
	# diagonal
	if GameData[0] == "X" and GameData[4] == "X" and GameData[8] == "X": return "X" # back
	if GameData[2] == "X" and GameData[4] == "X" and GameData[6] == "X": return "X" # forward

	# O
	# horisontal
	if GameData[0] == "O" and GameData[1] == "O" and GameData[2] == "O": return "O" # top
	if GameData[3] == "O" and GameData[4] == "O" and GameData[5] == "O": return "O" # middle
	if GameData[6] == "O" and GameData[7] == "O" and GameData[8] == "O": return "O" # bottom
	# vertical
	if GameData[0] == "O" and GameData[3] == "O" and GameData[6] == "O": return "O" # left
	if GameData[1] == "O" and GameData[4] == "O" and GameData[7] == "O": return "O" # middle
	if GameData[2] == "O" and GameData[5] == "O" and GameData[8] == "O": return "O" # right
	# diagonal
	if GameData[0] == "O" and GameData[4] == "O" and GameData[8] == "O": return "O" # back
	if GameData[2] == "O" and GameData[4] == "O" and GameData[6] == "O": return "O" # forward

### built-in game AIs ###
def manual(GameData, side):
	while True:
		PrintGame(GameData)
		PlayerInput = SecInput("enter position: ", "string")
		if PlayerInput == "": continue

		# special commands
		if PlayerInput == "help".lower():
			print("position numbers:")
			PrintGame(["1", "2", "3",
				"4", "5", "6",
				"7", "8", "9"])
			continue

		if PlayerInput == "exit".lower():
			print("exiting game...")
			raise SystemExit

		if int(PlayerInput) in range(1,10):
			if GameData[int(PlayerInput) -1] == " ":
				return int(PlayerInput)
			else:
				print("Error: slot taken")
				continue
		else:
			print("Error: invalid input")

def AI_random(GameData, side):
	EmptySlots = []
	i = 1
	for each in GameData:
		if each == " ": EmptySlots += [i]
		i += 1

	RandomSlot = random.choice(EmptySlots)
	#time.sleep(0.05)
	return RandomSlot

def AI_offensive(GameData, side):
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

def AI_defensive(GameData, side):
	if GameData[4] == " ": return 5

	if side == "X": NotSide = "O"
	else: NotSide = "X"

	i = 1
	for each in GameData:
		if each != NotSide: continue
		if i == 1:
			if GameData[3] == NotSide and GameData[6] == " ": return 7 # left vertical
			if GameData[1] == NotSide and GameData[2] == " ": return 3 # top horasontal
			if GameData[4] == NotSide and GameData[8] == " ": return 9 # back diagonal

		if i == 2:
			if GameData[2] == NotSide and GameData[0] == " ": return 1 # top horasontal
			if GameData[4] == NotSide and GameData[7] == " ": return 8 # middle vertical

		if i == 3:
			if GameData[2] == NotSide and GameData[0] == " ": return 1 # right vertical
			if GameData[4] == NotSide and GameData[6] == " ": return 7 # forward diagonal

		if i == 4:
			if GameData[6] == NotSide and GameData[0] == " ": return 1 # back diagonal
			if GameData[4] == NotSide and GameData[5] == " ": return 6 # middle horasontal

		if i == 5:
			if GameData[7] == NotSide and GameData[1] == " ": return 2 # middle vertical
			if GameData[5] == NotSide and GameData[3] == " ": return 4 # middle horasontal

		if i == 6:
			if GameData[8] == NotSide and GameData[1] == " ": return 2 # right vertical
			if GameData[4] == NotSide and GameData[3] == " ": return 4 # forward diagonal

		if i == 7:
			if GameData[7] == NotSide and GameData[8] == " ": return 9 # bottom horisontal

		if i == 8:
			if GameData[4] == NotSide and GameData[1] == " ": return 2 # middle vertical
			if GameData[7] == NotSide and GameData[6] == " ": return 7 # bottom horisontal

		if i == 10: break
		i += 1


	EmptySlots = []
	i = 1
	for each in GameData:
		if each == " ": EmptySlots += [i]
		i += 1

	RandomSlot = random.choice(EmptySlots)
	return RandomSlot
################

def game(Player1Mode, Player2Mode):
	GameData = []
	for i in range(1,10): GameData += [" "]

	while True:
		# test for draw
		EmptySlots = 0
		for each in GameData:
			if each == " ": EmptySlots += 1
		if EmptySlots < 3:
			return "draw", GameData

		# player 1's turn
		if Player1Mode == "manual": SelectedSlot = manual(GameData, "X")
		if Player1Mode == "random": SelectedSlot = AI_random(GameData, "X")
		if Player1Mode == "offensive": SelectedSlot = AI_offensive(GameData, "X")
		if Player1Mode == "defensive": SelectedSlot = AI_defensive(GameData, "X")
		if Player1Mode == "custom": SelectedSlot = custom(GameData, "X")

		SelectedSlot = int(SelectedSlot)
		if GameData[SelectedSlot -1] != " " or SelectedSlot not in range(1,10):
			print("Error: illigal move by player 1")
			raise SystemExit
		GameData[SelectedSlot -1] = "X"

		# test player 1's win condison
		if TestWin(GameData) == "X":
			return "X", GameData

		# player 2's turn
		if Player2Mode == "manual": SelectedSlot = manual(GameData, "O")
		if Player2Mode == "random": SelectedSlot = AI_random(GameData, "O")
		if Player2Mode == "offensive": SelectedSlot = AI_offensive(GameData, "O")
		if Player2Mode == "defensive": SelectedSlot = AI_defensive(GameData, "O")
		if Player2Mode == "custom": SelectedSlot = custom(GameData, "O")

		SelectedSlot = int(SelectedSlot)
		if GameData[SelectedSlot -1] != " " or SelectedSlot not in range(1,10):
			print("Error: illigal move by player 2")
			raise SystemExit
		GameData[SelectedSlot -1] = "O"

		# test player 1's win condison
		if TestWin(GameData) == "O":
			return "O", GameData

Xwins = 0
Owins = 0
draws = 0
GamesNo = int(input("number of games: "))
for x in range(GamesNo):
	out, GameData = game("random", "random")
	if GamesNo < 11: PrintGame(GameData)
	if out == "X": Xwins += 1
	if out == "O": Owins += 1
	if out == "draw": draws += 1
print("\nX wins: {}\nO wins: {}\ndraws: {}".format(str(Xwins), str(Owins), str(draws)))
