#!/usr/bin/python3
# Version 1.3

import time, sys, praw
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

def FileExist(filename):
	try:
		file = open(filename, "r")
		file.close()
		return True
	except:
		return False

def get_Reddit_meta_data():
	# checking file exists
	if not FileExist("RedditMeta.txt"):
		print("Error: no 'RedditMeta.txt' file found")
		raise SystemExit

	client_id = ""
	user_agent = ""
	client_secret = ""
	username = ""
	password = ""
	# scanning file
	file = open("RedditMeta.txt", "r")
	for line in file:
		LineData = line.split(": ")
		if len(LineData) == 1: continue

		if LineData[0] == "client ID":
			client_id = LineData[1].rstrip()

		if LineData[0] == "client secret":
			client_secret = LineData[1].rstrip()

		if LineData[0] == "user agent":
			user_agent = LineData[1].rstrip()

		if LineData[0] == "username":
			username = LineData[1].rstrip()

		if LineData[0] == "password":
			password = LineData[1].rstrip()

	# checking all fields are filled
	if client_id == "":
		print("Error: no 'client ID' found in 'RedditMeta.txt'")
		raise SystemExit

	if user_agent == "":
		print("Error: no 'user_agent' found in 'RedditMeta.txt'")
		raise SystemExit

	if client_secret == "":
		print("Error: no 'client_secret' found in 'RedditMeta.txt'")
		raise SystemExit

	if username == "":
		print("Error: no 'username' found in 'RedditMeta.txt'")
		raise SystemExit

	if password == "":
		print("Error: no 'password' found in 'RedditMeta.txt'")
		raise SystemExit

	return client_id, user_agent, client_secret, username, password

def PRAW_get_karma(user):
	client_id, user_agent, client_secret, username, password = get_Reddit_meta_data()
	r = praw.Reddit(
		user_agent=user_agent,
		client_id=client_id,
		client_secret=client_secret,
		username=username,
		password=password)
	UserData = r.redditor(user)
	return UserData.link_karma + UserData.comment_karma

# input SAMPLE_TIME multiplier
if len(sys.argv) > 1:
	multiplier = float(sys.argv[1])
else:
	print("Error: no sample time multiplier found")
	raise SystemExit

SAMPLE_TIME = 60 * multiplier
OUTPUT_PATH = ""

# input usernames
users = []
GotUsernames = False
if FileExist("input.txt"):
	InputFile = open("input.txt", "r")
	for line in InputFile:
		if line.rstrip() != "": users += [line.rstrip()]
	if len(users) > 0: GotUsernames = True

if not GotUsernames:
	print("Error: no 'input.txt' file found")
	raise SystemExit

filename = "{}output.csv".format(OUTPUT_PATH)
if not FileExist(filename):
	file = open(filename, "w")
	header = "timestamp"
	for user in users: header += ", {}".format(user)
	file.write("{}\n".format(header))
	file.close()

# begin recording
try:
	while True:
		if FileExist(filename): file = open(filename, "a")
		else: file = open(filename, "w")

		data = ""
		for user in users: data += ", {}".format(PRAW_get_karma(user))
		file.write("{}{}\n".format(round(time.time()), data))
		file.close()

		print(data)
		time.sleep(SAMPLE_TIME)
except KeyboardInterrupt:
	raise SystemExit
	
	plt.xlabel("time")
	plt.ylabel("karma")
	plt.plot(timestamps, karma)
	plt.show(block=True)