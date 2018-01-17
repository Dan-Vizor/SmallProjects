#!/usr/bin/python3

def speed(speed):
	if speed < -100:
		print("error: invalid input for .speed (to low)")
		return
	if speed > 100:
		print("error: invalid input for .speed (to high)")
		return
	# set moters to go (speed)%

def turn(turn):
	if turn < -45:
		print("error: invalid input for .turn (to low)")
		return
	if speed > 45:
		print("error: invalid input for .speed (to high)")
		return
	# set turning moter to (turn)

def stop():
	speed(0)
	turn(0)
	print("bot stoped")
	
def lights(t):
	if t == 1:
		#lights set to on
		return
	if t == 0:
		#lights set to off
		return
	print("error: invaid input for .lights")
	

def Lsen():
	sen = False
	#sen = left_sensor_output()
	return sen
def Msen():
	sen = False
	#sen = mid_sensor_output()
	return sen
def Rsen():
	sen = False
	#sen = right_sensor_output()
	return sen
