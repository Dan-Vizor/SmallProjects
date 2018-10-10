#!/usr/bin/python

def readlist(file):
	doc = open(file, "r")
	out = []
	for line in doc:
		out += [line]
	return out

def inlist(list, inp):
	if inp in list:
		return True
	else:
		return False


doc = readlist("quotesDB.txt")
inp = raw_input("input: ")
if inlist(doc, inp):
	