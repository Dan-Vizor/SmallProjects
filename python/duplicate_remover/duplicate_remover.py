#!/usr/bin/python3
import hashlib, os

def MD5_hash(path):
	m=hashlib.md5()
	m.update(open(path, "br").read())
	a=m.hexdigest()
	return a

while True:
	path = input("enter absolute path for target folder: ")
	if os.path.isdir(path):
		break
	else:
		print("Error: folder dosn't exist,\nplease check the path\n")

files = [ f for f in os.listdir(path) if os.path.isfile(os.path.join(path,f)) ]

for staticFile in files:
	for eachFile in files:
		if not staticFile == eachFile:
			if MD5_hash(path + "/" + eachFile) == MD5_hash(path + "/" + staticFile):
				print(eachFile + " is the same as " + staticFile)
				try: os.remove(eachFile)
				except: print("Error: failed to remove " + eachFile)
				files.remove(eachFile)