#!/usr/bin/python3
##################################################
def encrypt(data, key, loop):
	for x in range(0,loop):
		if x > 0:
			out = encryptword(olOut, key)
			olOut = out
		else:
			out = encryptword(data, key)
			olOut = out
	return olOut
	
def encryptword(word, key):
	encrypted=""
	for c in word:
		x = ord(c)
		dec = encryptLetter(c, key);
		encrypted += dec
	return encrypted

def encryptLetter(letter, key):
	x = ord(letter)
	if letter == " ":
		enc = ord(" ")
	else:
		enc = x + key
		if enc > ord("z"):
			enc = enc - 26
	return chr(enc)
################################################## tjpm bzoodib bjjy vo ocdn
def decrypt(data, key, loop):
	for x in range(0,loop):
		if x > 0:
			out = decryptWord(olOut, key)
			olOut = out
		else:
			out = decryptWord(data, key)
			olOut = out
	print ("\n" + out)

def decryptLetter(letter, key):
	if letter == " ":
			 return " "
	x = ord(letter)
	enc = x - key
	if enc < ord("a"):
		enc += 26
	return chr(enc)

def decryptWord(word, key):
	decrypted=""
	for c in word:
		x = ord(c)
		dec = decryptLetter(c, key);
		decrypted += dec
	return decrypted
################################################## tqxxa iadxp
def scan_dict(target):
	doc = open("words.txt","r")
	for line in doc:
		if target == line.strip():
			doc.close
			return True
	return False

def test_decrypt(code):
	found = False
	for key in range(1,26):
		if found:
			return key - 1
		end = test_decryptWord(enter, key)
		print(" scaning with " + str(key) + " as a key")
		out = scan_dict(end)
		if out == True:
			print("\nkey is " + str(key))
			found = True
	if not found:
		print("can't find match")
		return False

def test_decryptWord(word, key):
	decrypted=""
	for c in word:
		if c == " ":
			 break
		x = ord(c)
		dec = decryptLetter(c, key);
		decrypted += dec
	return decrypted
##################################################
while True:
	print ("\n1 - incrypt")
	print ("2 - decrypt")
	print ("3 - force decrypt")
	print ("4 - scan dict")
	print ("5 - exit")
	print ("6 - random word")
	mode = int(input("pick mode: "))
	end =""
	print ("")

	if mode == 1:
		key = int(input("enter key(max 25): "))
		data = input("enter text: ")
		out = encryptword(data, key)
		print ("\n" + out)

	if mode == 2:
		data = input("enter code: ")
		key = int(input("enter key(max 25): "))
		decryptWord(data, key)

	if mode == 3:
		enter = input("enter code: ")
		end = test_decrypt(enter)
		if not end:
			print("\nerror decrypting\nthe code maybe using a more advansed cyhper or maybe just junk")
		else:
			decrypt(enter, end, 1)
			
	if mode == 5:
		break
		
	if mode == 4:
		word = input("enter word: ")
		out = scan_dict(word)
		if not out:
			print("can't find " + word)
			print("do you want to add " + word + " to the dictonary y/n")
			a = input(": ")
			if a == "y":
				doc = open("words.txt","a")
				doc.write("\n" + word)
				out = scan_dict(word)
				if not out:
					print("error failed to enter " + word)
				else:
					print(word + " added to dictonary")
		elif out:
			print("\n" + word + " found")

	if mode == 6:
		import random
		doc = open("words.txt","r")
		rand = random.randint(0,1000)
		count = 0
		for line in doc:
			if count == rand:
				print(encrypt(line.strip(), random.randint(2,24), 1))
			count += 1
