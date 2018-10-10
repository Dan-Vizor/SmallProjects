#!/usr/bin/python
import hashlib, time

# functions #
def sha256(inp):
	hash_object = hashlib.sha256(inp)
	hex_dig = hash_object.hexdigest()
	return hex_dig

# main #
while True:
	pass
	fName = raw_input("enter password list file name (in same folder): ")
	try:
		file = open(fName,"r")
		print("file found")
		break
	except: print("error file '" + fName + "' not found\n")

print("running...\n")
out = open("out","w")
main = open("sha256_main.txt","a")
for line in file:
	x = sha256(line)
	out.write(x + "\n")
	main.write(x + "\n")
	time.sleep(0.002)

print("done")

# knowledge is power