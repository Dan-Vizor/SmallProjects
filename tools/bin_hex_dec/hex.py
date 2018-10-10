#!/usr/bin/python

def valid(inp):
	if inp == "q":
		exit(0)
	elif inp == "d":
		return True
	elif inp == "b":
		return True
	elif inp == "h":
		return True
	else:
		return False

def DtoB(inp):
	split = []
	for x in inp:
		split += [x]

	if split[0] in range(49,57):
		pass

	else:
		pass

def DBcov(inp):
	twos = [128,64,32,16,8,4,2,1]
	count = 8
	out = ""
	if inp > twos[count]:
		pass

#twos = [128,64,32,16,8,4,2,1]
# hex WIP h = hex, 
print("d = decimal, b = binary")
while True:
	while True:
		mode = raw_input("enter input mode(h,d,b):\n> ")
		if mode == "q":
			exit(0)
		elif valid(mode) == True:
			break
		else:
			print("Error. Invalid input\n")

	data = raw_input("enter data:\n> ")

	while True:
		outMode = raw_input("enter output mode(h,d,b):\n> ")
		if valid(mode) == True:
			break
		else:
			print("Error. Invalid output\n")


	if mode == "d" and outMode == "b":
		splitData = []
		for x in data:
			splitData += [x]

		if splitData[1] not in range(49,57):
			ordData = []
			for each in splitData:
				ordData += [ord(each)]
			splitData = ordData

		output = ""
		count = 0
		for each in splitData:
			ins = each
			for x in range(0,7):
				if ins > twos[count]:
					print(count)
					ins -= twos[count]
					count += 1
					output += "1"

				else:
					output += "0"
					count += 1

		print(output)