#!/usr/bin/python

try:
	doc = open("/home/daniel/SmallProjects/projects/alex_counter/data.txt","r")

except:
	print("error: no data file")
	exit()

#data = []
#for x in doc:
#	data += [x]
data = doc.read(1)
doc.close()
print(data)

rdata = str(data[0])
print("alex is on " + rdata.rstrip())

while True:
	menu = raw_input(": ")

	split = []
	for x in menu:
		split += [x]

	if split[0] == "+":
		file = open("/home/daniel/SmallProjects/projects/alex_counter/data.txt","w")
		file.write(str(int(rdata) + int(split[1])))
		print(rdata + " stupid things said sinse 9/8/18")
		file.close()
		break

	elif split[0] == "-":
		file = open("/home/daniel/SmallProjects/projects/alex_counter/data.txt","w")
		file.write(str(int(rdata) - int(split[1])))
		print(rdata + " stupid things said sinse 9/8/18")
		file.close()
		break

	elif menu == "exit":
		break

	else:
		print("error: invalid command")