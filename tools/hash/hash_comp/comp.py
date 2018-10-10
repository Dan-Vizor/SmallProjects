#!/usr/bin/python
import hashlib, time

def sha256(inp):
	hash_object = hashlib.sha256(inp)
	hex_dig = hash_object.hexdigest()
	return hex_dig

inp = raw_input("enter target hash: ")
hasha = raw_input("enter hash algorithm: ")

if hasha == "sha256":
	pass
elif hasha == "md5":
	print("WIP")
	exit()
else:
	print("error invalid input")
	exit()

print("scaning...\n")
file = open("pass_plain.txt","r")
for line in file:
	time.sleep(0.001)
	if sha256(inp) == line.rstrip():
		print("match found!\npassword: " + line)
		found = True
		exit()
print("no match found")