#!/usr/bin/python
import hashlib, itertools, string, time

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

start_time = time.time()
# dict scan
for line in range(0,len(dict_list)):
	if sha256(dict_list[line].strip()) == tar_hash:
		print("password is {}. found in dict scan.".format(dict_list[line].strip()))
		exit()

#brute force scan
print("running brute force scan...\ntesting length 1...")
scan_len = 1
chars = string.ascii_lowercase + string.digits + string.punctuation
attempts = 0
for password_length in range(1, 9):
    for guess in itertools.product(chars, repeat=password_length):
        attempts += 1
        guess = ''.join(guess)
        guess_hash = sha256(guess)
        if guess_hash in tar_hash:
            print('password is {}. found in {} guesses.'.format(guess, attempts))
            print("completed in {} seconds.".format(time.time() - start_time))
            exit()
        if password_length > scan_len:
        	scan_len += 1
	        print("testing length {}...".format(password_length))