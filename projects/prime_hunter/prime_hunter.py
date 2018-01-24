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
	doc.write(stand_form(No) + "\n")
	doc.close
	doc = open("currentNo.txt", "w")
	doc.write(str(No))
	doc.close

def stand_form(No):
	power = 0
	if No > 0:
		while No != range(0,9):
			No /= 10
			power += 1
		return str(No) + " x 10^" + power
	else:
		while No != range(0,9):
			No *= 10
			power -= 1
		return str(No) + " x 10^-" + power

#main
doc = open("currentNo.txt", "r")
for line in doc:
	curNo = int(line)
	break
doc.close

while True:
	if isPrime(curNo): doc_write(curNo)
	curNo += 1
