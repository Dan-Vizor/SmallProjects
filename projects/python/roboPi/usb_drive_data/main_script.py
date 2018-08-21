#!/usr/bin/python3
import roboPi_test_mod, time
mo = roboPi_test_mod
x = mo.lsen()
print(x)
while True:
	if mo.Msen():
		mo.lights(1)
		mo.speed(-15)
		if mo.Lsen():
			if mo.Rsen:
				mo.turn(45)
				time.sleep(1)
				continue
		while mo.Msen:
			if mo.Lsen(): mo.turn(45)
			if mo.Rsen(): mo.turn(-45)
	else:
		mo.lights(0)
		mo.speed(45)
		mo.turn(0)
