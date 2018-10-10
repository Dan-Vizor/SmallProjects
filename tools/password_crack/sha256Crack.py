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
tar_hash = tar_hash.strip()
dict_list = import_file("pass_list.txt")

print("\nstarting dict scan...")

for line in range(0,len(dict_list)):
	if sha256(dict_list[line].strip()) == tar_hash:
		print("password is {}.".format(dict_list[line].strip()))
		exit()

# dict scan finished, no match found
# starting brute force attack

chars = string.ascii_lowercase + string.digits + string.punctuation
attempts = 0
for password_length in range(1, 9):
    for guess in itertools.product(chars, repeat=password_length):
    	#sleep(0.001)
        attempts += 1
        guess = ''.join(guess)
        if sha256(guess) == tar_hash:
            print('password is {}. found in {} guesses.'.format(guess, attempts))
            exit()
        print(guess, attempts)
