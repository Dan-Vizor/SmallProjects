#!/usr/bin/env python
import os

def comp(array,low,high):
	loop = 0
	out = ""
	for cy in range(low,high):
		out += array[cy]
	return out

while True:
	### main input
	Rinp = raw_input("> ")
	###
	Aimp = Rinp.split()
	
	if lower(Aimp[0]) == "find":
		os.system("find " + comp(Aimp,1,len(Aimp)))
