#!/usr/bin/python
import hashlib, itertools, string, time

def sha256(inp):
	hash_object = hashlib.sha256(inp)
	hex_dig = hash_object.hexdigest()
	return hex_dig

tar_hash = raw_input("enter target hash(sha256): ")
tar_hash = tar_hash.strip()

start_time = time.time()
chars = string.ascii_lowercase + string.digits + string.punctuation
attempts = 0
for password_length in range(1, 9):
    for guess in itertools.product(chars, repeat=password_length):
    	time.sleep(0.0005)
        attempts += 1
        guess = ''.join(guess)
        guess_hash = sha256(guess)
        if guess_hash in tar_hash:
        	doc = open("out.txt","w")
        	doc.write("password is " + str(guess) + ". found in " + str(attempts) + "guesses.\ncompleted in " + str(time.time() - start_time) + "seconds.\n")
        	exit()