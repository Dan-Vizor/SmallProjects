#!/usr/bin/python
from math import sqrt
from itertools import count, islice
#functions
def isPrime(No):
	if No < 2: return False
	for number in islice(count(2), int(sqrt(No)-1)):
		if not No%number:
			return False
	return True
		
def doc_write(No):
	doc = open("primes.txt", "a")
	doc.write(str(No) + "\n")
	doc.close

def stand_form(No):
	No = float(No)
	power = 0
	while True:
		No /= 10
		power += 1
		if No in range(0,9): break
	return str(No) + "x10^" + str(power)

#main
doc = open("currentNo.txt", "r")
for line in doc:
	curNo = int(line)
	break
doc.close

doc = open("currentNo.txt", "w")
while True:
	if isPrime(curNo): doc_write(curNo)
	doc.write(str(curNo))
	doc.close
	curNo += 1
