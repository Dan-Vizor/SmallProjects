#!/bin/sh

###
#cd
#cd /media/pi/USB
###

###
dc usb_drive_data
###

python3 ./main_script.py
python3 ./robo_stop.py
