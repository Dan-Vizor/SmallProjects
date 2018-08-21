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

#main
try: doc = open("currentNo.txt", "r")
except:
	doc = open("currentNo.txt", "w")
	doc.write("1")
doc = open("currentNo.txt", "r")
for line in doc:
	curNo = int(line)
	break
doc.close

stri = str(curNo) + "-" + str(curNo + 100000)
doc = open("output/primes/" + stri + ".txt", "a")
loop = 0
while True:
	if loop == 100000:
		loop = 0
		doc = open("currentNo.txt", "w")
		doc.write(str(curNo))
		stri = str(curNo) + "-" + str(curNo + 100000)
		doc = open("output/primes/" + stri + ".txt", "a")
	
	if isPrime(curNo):
		doc.write(str(curNo) + "\n")
	curNo += 1
	loop += 1
