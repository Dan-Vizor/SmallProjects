#!/usr/bin/python3
import os

def detectOS():
	try:
		os.system("ls")
		return "linux"
	except:
		pass

	try:
		os.system("dir /s")
		return "windows"
	except:
		pass
	return "error"
