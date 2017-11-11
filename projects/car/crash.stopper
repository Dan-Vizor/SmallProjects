#!/usr/bin/python3
link = False
thr = 50
# artificial testing input ##################################################
sen1 = raw_input("enter input for sensor 1 (left) (y/n): ")
sen2 = raw_input("enter input for sensor 2 (right) (y/n): ")
rev = raw_input("is rev active (y/n): ")
con = input("enter input from controler:\n1 - left\n2 - nothing\n3 - right\n: ")
print("")

if sen1 == "y": sen1 = 1
else: sen1 = 0

if sen2 == "y": sen2 = 1
else: sen2 = 0
if rev == "y": rev = 1
else: rev = 0
#############################################################################
while True:
    break

fir = True
while not link:
    if fir:
        # start quick_stop in new thread
    #####################
		link = True
		continue
    #####################
    if thr > 0:
        if sen1 == sen2:
            if sen1 == 1:
                print ("the car stoped")
            else:
                print ("the car went straight on11")
        else:
            if sen1 == 1:
                print ("the car turned right")
            if sen2 == 1:
                print ("the car turned left")
    else:
        print ("the car is reversing")

while link:
    if thr > 0:
        if sen1 == sen2:
            if sen1 == 1:
                print ("the car stoped")
            else:
                if con == int("1"):
                    print ("the car turned left")
                if con == int("2"):
                    print ("the car went straight on")
                if con == int("3"):
                    print ("the car turned right")
        else:
            if sen1 == 1:
                if con == int("1"):
                    print ("the car turned left and crashed (user input override")
                else:
                    print ("the car turned right")
            if sen2 == 1:
                if con == int("3"):
                    print ("the car turned right and crashed (user input override)")
                else:
                    print ("the car turned left")
    else:
        print ("the car is reversing")
    #####
    break
    #####
