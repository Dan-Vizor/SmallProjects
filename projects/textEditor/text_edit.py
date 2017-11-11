import os
def pHelp():
	print("\n.close = close current file")
	print(".close + .end = close program")
	print(".del = deletes all data in open file")
	print(".del file = deletes open file")
	print(".print = prints open file\n")

while True:
	TFile = raw_input("enter file: ")
	if TFile == ".end":
		break
	elif TFile == ".help":
		pHelp()
	while True:
		inp = raw_input(": ")
		if inp == ".close":
			doc.close()
			break
		elif inp == ".del":
			doc = open(TFile, "w")
			print("file cleared")
		elif inp == ".del file":
			print("do you want to delete ", TFile, " y/n")
			conf = raw_input(": ")
			if conf == "y":
				os.remove(TFile)
				break
		elif inp == ".print":
			doc = open(TFile, "r")
			for line in doc:
				print(line)
		elif inp == ".help":
			pHelp()
		else:
			doc = open(TFile, "a")
			doc.write(inp + "\n")
