#!/usr/bin/python
import hashlib, itertools, string
from time import sleep

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
#tar_hash += tar_hash.strip()
dict_list = import_file("pass_list.txt")

# dict scan
for line in range(0,len(dict_list)):
	print(dict_list[line].strip())
#	if sha256(dict_list[line].strip()) == tar_hash:
#		print("password is {}. found in dict scan.".format(dict_list[line].strip()))
	if dict_list[line].strip() == tar_hash.strip():
		print("password is {}. found in dict scan.".format(dict_list[line].strip()))
print("no match found")