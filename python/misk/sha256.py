#!/usr/bin/python
import hashlib

def sha256(inp):
	hash_object = hashlib.sha256(inp)
	hex_dig = hash_object.hexdigest()
	return hex_dig

inp = raw_input("enter string: ")
print(sha256(inp))