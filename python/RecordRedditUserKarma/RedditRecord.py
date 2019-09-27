#!/usr/bin/python3
__version__ = 0.1
import time, praw, os, sys

def GetKarma(user, r):
	try:
		UserData = r.redditor(user)
	except:
		print("Error: user 'u/{}' does not exist or can't be found")
		raise SystemExit
	return UserData.link_karma + UserData.comment_karma

def PlaceValue(number): return "{:,}".format(int(number))

def main():
	PauseTime = 5

	# reading account names from input.txt file
	accounts = []
	try:
		for line in open("input.txt", "r"):
			if line == "\n" or line == "\n": continue
			accounts += [line.rstrip()]
	except:
		print("Error: can't locate 'input.txt'")
		raise SystemExit

	# setting up Reddit login info
	RedditInfo = []
	try:
		for line in open("meta.txt", "r"):
			if line == "\n" or line == "\n": continue
			RedditInfo += [line.rstrip()]
	except:
		print("Error: can't locate 'meta.txt'")
		raise SystemExit

	if len(RedditInfo) != 5:
		print("Error: invalid 'meta.txt' file")
		raise SystemExit

	# correct meta.txt format:
	# user_agent
	# client_id
	# client_secret
	# username
	# password

	# creating Reddit object (r)
	r = praw.Reddit(
		user_agent = RedditInfo[0],
		client_id = RedditInfo[1],
		client_secret = RedditInfo[2],
		username = RedditInfo[3],
		password = RedditInfo[4])

	print("loading...", end="\r")

	# command line arguments
	QuietMode = False
	NoFile = False
	KarmaFileTF = False

	if sys.argv[0] == "./RedditRecord.py":
		for i in range(len(sys.argv)):
			if i == 0: continue # skip first argument
			if "-" not in sys.argv[i]: continue

			# quiet mode
			if sys.argv[i].lower() == "-Q":
				QuietMode = True
				print("running in quiet mode")
				continue

			# no output file
			if sys.argv[i] == "-N":
				NoFile = True
				continue

			# input karma values from file
			if sys.argv[i] == "-k":
				KarmaFileTF = True
				KarmaFile = sys.argv[i+1]
				continue

			# manual pause time
			if sys.argv[i] == "-t":
				try:
					PauseTime = int(sys.argv[i+1])
				except:
					print("Error: no value given")
					raise SystemExit
				continue

			print("Error: {} is not a valid argument".format(sys.argv[i]))
			raise SystemExit

	# saving staring data
	StartKarma = []
	if KarmaFileTF:
		for each in open(KarmaFile, "r"): StartKarma += [each]
		if len(accounts) != len(StartKarma): print("Error: invalid karma file")
	else:
		for each in accounts: StartKarma += [GetKarma(each, r)]

	# setting up output info
	if not NoFile:
		OutFile = open("output.csv", "w")
		header = "time,"
		for each in accounts: header += "u/{},".format(each)
		OutFile.write(header + "\n")
		OutFile.close()

	# set QuietMode override
	if not QuietMode:
		rows, columns = os.popen('stty size', 'r').read().split()
		if int(rows) >= len(accounts) * 25:
			QuietMode = True
			print("to many accounts to display. running in quiet mode")
		else:
			QuietMode = False

	# running scanning loop
	while True:
		OutString = ""
		FileString = str(round(time.time())) + ","

		for i in range(0, len(accounts)):
			karma = GetKarma(accounts[i], r)
			OutString += "u/{}: {} : {} | ".format(accounts[i], PlaceValue(karma), PlaceValue(str(round(karma - StartKarma[i]))))
			if not NoFile: FileString += str(karma) + ","

		if not QuietMode:
			rows, columns = os.popen('stty size', 'r').read().split()
			if int(rows) > len(OutString): QuietMode = True
			else: print(OutString[:-3], end="\r")
		else: print(" ", end="\r")

		if not NoFile:
			OutFile = open("output.csv", "a")
			OutFile.write(FileString + "\n")
			OutFile.close()

		time.sleep(PauseTime)


StartTime = time.time()
try:
	main()
except KeyboardInterrupt:
		print('\ntime eclipsed: {}s'.format(str(round(time.time() - StartTime))))