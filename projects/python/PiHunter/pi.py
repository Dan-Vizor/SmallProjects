#!/usr/bin/env python
import math

def floatlen(x):
	out = []
	for ch in str(x):
		out += [ch]
	return len(out)
	
def devFra(n1,d1,n2,d2):
	outN = n1 * d2
	outD = d1 * n2
	return outN, outD

def progress(run, no):
	if int(run) / 4 < floatlen(no):
		print("25%")
	if int(run) / 2 < floatlen(no):
		print("50%")
	if (int(run) / 4) * 3 < floatlen(no):
		print("75%") 

while True:
	runtime = raw_input("no of chrs: ")
	try:
		int(runtime)
		break
	except:
		print("error invalid input\n")

Nn, Dn = devFra(2,1,3,1)
de = 5.0
flip = False
while int(runtime) > floatlen(Nn/Dn):
	if flip == True:
		#a, b = devFra(Nn,Dn,1,de)
		Nn -= 1
		Dn -= de
		flip = False
	else:
		#a, b = devFra(Nn,Dn,1,de)
		Nn += 1
		Dn += de
		flip = True
	de += 2.0
	print(Nn/Dn*4)
	progress(runtime, Nn/Dn)
doc = open("output.txt","w")
doc.write(str(Nn/Dn * 4))
print("done\noutput in output.txt")
