#!/bin/sh
sudo ifconfig wlan0 up
echo pulling git repos
sleep 10
#
cd /home/pi/SmallProjects
git pull
#
#cd /home/pi/
#git pull
#
