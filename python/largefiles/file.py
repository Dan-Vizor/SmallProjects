#!/usr/bin/python

size = input("size(kB): ")
size = size * 1000
print("start")
doc = open("u.txt","w")
out = ""
y = 0
while y < size:
	out += "A"
	
	if y == size / 4: print("25%")
	if y == size / 2: print("50%")
	if y == size / 4 * 3: print("75%")
	y += 1
	
doc.write(out)
doc.close()
print("end")
