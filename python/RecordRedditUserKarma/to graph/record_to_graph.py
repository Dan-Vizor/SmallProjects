#!/usr/bin/python3
# Version 3.0

import time, urllib3
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def GetRedditUserKarma(RedditUsername): # from WebScraper.py version 1.0
	# download html
	http = urllib3.PoolManager()
	response = http.request('GET', "https://www.reddit.com/user/{}".format(RedditUsername))

	# parse html for karma value
	soup = BeautifulSoup(response.data, "html.parser")
	tags = list(soup.find_all("span", {"id": "profile--id-card--highlight-tooltip--karma"}))

	# validate the tag data
	if tags == []:
		#print("Error: karma html tag not found (user may be NSFW)")
		return

	# extract value from tag
	return int(str(tags[0]).replace('<span class="_1hNyZSklmcC7R_IfCUcXmZ" id="profile--id-card--highlight-tooltip--karma">', "").replace("</span>", "").replace(",", ""))

def FileExist(filename):
	try:
		file = open(filename, "r")
		file.close()
		return True
	except:
		return False

karma = []
timestamps = []
user = ""
multiplier = 0.0

# data input from file
if FileExist("meta.txt"):
	print("adding existing data from files")
	MetaFile = open("meta.txt", "r")
	TimestampsFile = open("timestamps.txt", "r")
	DataPointsFile = open("datapoints.txt", "r")
	for line in MetaFile:
		LineList = line.split(": ")
		if len(LineList) == 1:
			print("Error: invalid meta file")
			raise SystemExit

		if LineList[0] == "username":
			user = LineList[1].rstrip()

		if LineList[0] == "sample times":
			multiplier = float(LineList[1].rstrip())

	for line in TimestampsFile:
		timestamps += [line.rstrip()]

	for line in DataPointsFile:
		karma += [line.rstrip()]

	MetaFile.close()
	TimestampsFile.close()
	DataPointsFile.close()

# data input manualy
else:
	# input samples times multiplier
	while True:
		multiplier = input("enter time between datapoints (mins): ")

		if multiplier == "":
			print("using defult (0.1)")
			multiplier = 0.1
			break

		try:
			multiplier = float(multiplier)
			break
		except:
			print("Error: invalid multiplier\n")

	# input Reddit username
	while True:
		user = input("enter Reddit username: ")

		if "u/" in user: user.replace("u/", "")
		if user == "":
			print("using defult (local_meme_dealer45)")
			user = "local_meme_dealer45"
			break

		try:
			user = str(user.rstrip())
			break
		except:
			print("Error: invalid exit value\n")

	MetaFile = open("meta.txt", "w")
	MetaFile.write("username: {}\nsample times: {}\n".format(user, multiplier))
	MetaFile.close()


# recording data to lists
#plt.ion()
plt.xlabel("time")
plt.ylabel("karma")
print("recording data... (CTRL + C to display graph)")

while True:
	# open files
	TimestampsFile = open("timestamps.txt", "a")
	DataPointsFile = open("datapoints.txt", "a")

	# get new data
	KarmaData = GetRedditUserKarma(user)
	TimestampsData = "{}:{}:{}".format(time.localtime(time.time())[3], time.localtime(time.time())[4], time.localtime(time.time())[5])

	# error on invalid data
	if KarmaData == "none":
		print("Error: unable to read profile (check internet connection or profile may be NSFW)")
		raise SystemExit

	# save new data to file
	TimestampsFile.write("{}\n".format(TimestampsData))
	DataPointsFile.write("{}\n".format(KarmaData))

	# add new data to the data lists
	karma += [KarmaData]
	timestamps += [TimestampsData]

	# close files
	TimestampsFile.close()
	DataPointsFile.close()

	plot(timestamps, karma)
	plt.show(block=True)
	print("yeet")

	# sleep
	time.sleep(60 * multiplier)