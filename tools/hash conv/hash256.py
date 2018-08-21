#!/usr/bin/python
import hashlib

# functions #
def sha256(inp):
	hash_object = hashlib.sha256(inp)
	hex_dig = hash_object.hexdigest()
	return hex_dig

# main #
chash = "sha256"
while True:
	pass
	fName = raw_input("enter password list file name (in same folder): ")
	try:
		file = open(fName,"r")
		print("file found")
		break
	except: print("error file '" + fName + "' not found\n")

while True:
	outFile = raw_input("enter output file name (will overite old files): ")
	x = raw_input("\n" + fName + " will be hashed using " + chash + " (y/n): ")
	if x == "y":
		break
	elif x == "n":
		continue
	else:
		print("error invalid input\n")

print("running\n")
out = open(outFile,"w")
main = open("main.txt","a")
for line in file:
	x = sha256(line)
	out.write(x + "\n")
	main.write(x + "\n")

print("done")