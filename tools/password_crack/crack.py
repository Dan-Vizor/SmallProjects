#!/usr/bin/python
import hashlib, time

def sha256(inp):
	hash_object = hashlib.sha256(inp)
	hex_dig = hash_object.hexdigest()
	return hex_dig

def import_file(file):
	doc = open(file,"r")
	out = []
	for line in doc:
		out += [line]
	return out

tar_hash = raw_input("enter target hash(sha256): ")
tar_hash = tar_hash.strip()
dict_list = import_file("pass_list.txt")

print("\nstarting dict attack")

for line in range(0,len(dict_list)):
	if sha256(dict_list[line].strip()) == tar_hash:
		print("'" + dict_list[line].strip() + "' is the password")
		exit()

print("dict attack finished, no match found\n\nstarting brute force attack")

last_try = ""
test = " "
while True:
	if sha256(test) == tar_hash:
		print("'" + test + "' is the password")
		exit()
