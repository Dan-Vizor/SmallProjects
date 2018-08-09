#!/usr/bin/python

try:
	doc = open("/home/daniel/SmallProjects/projects/alex_counter/data.txt","r")

except:
	print("error: no data file")
	exit()

data = []
for x in doc:
	data += [x]
doc.close()

file = open("/home/daniel/SmallProjects/projects/alex_counter/data.txt","w")
out = str(data[0])
file.write(str(int(out) + 1))
print(out + " stupid things said sinse 9/8/18")
file.close()