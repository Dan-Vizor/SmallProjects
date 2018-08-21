#!/usr/bin/python3
import roboPi_test_mod
mo = roboPi_test_mod

mo.speed(20) # bettwen 0 ~ 100
mo.turn(10) # bettwen -90 ~ 90
mo.lights(1) # 1/0 = on/off
mo.stop()
