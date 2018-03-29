#!/bin/sh
cd /home/pi/SmallProjects
git add .
git commit -m"auto push"
git status
git push
sudo shutdown now
