#!/usr/bin/python3
# Version 1.2

import time, urllib3
from bs4 import BeautifulSoup

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

while True:
	try:
		multiplier = float(input("enter sample time (mins): "))
		break
	except:
		print("invalid input")

SAMPLE_TIME = 60 * multiplier
OUTPUT_PATH = ""

# input usernames
users = []
GotUsernames = False
if FileExist("input.txt"):
	InputFile = open("input.txt", "r")
	for line in InputFile:
		users += [line.rstrip()]
	if len(users) > 0: GotUsernames = True

if not GotUsernames:
	while True:
		user = input("enter Reddit username: ")
		if user == "done": break
		if "u/" in user: user.replace("u/", "")
		users += [user]

# write file header
filename = "{}{}.csv".format(OUTPUT_PATH, round(time.time()))
file = open(filename, "w") 
header = "timestamp"
for user in users: header += ", {}".format(user)
file.write("{}\n".format(header))
file.close()

# begin recording
while True:
	if FileExist(filename): file = open(filename, "a")
	else: file = open(filename, "w")

	data = ""
	for user in users: data += ", {}".format(GetRedditUserKarma(user))
	file.write("{}{}\n".format(round(time.time()), data))
	file.close()
	
	time.sleep(SAMPLE_TIME)

# csv legend:
# username, karma, timestamp