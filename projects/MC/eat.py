#!/usr/bin/python3
import time
import mcpi.minecraft as minecraft
from mcpi.block import *
mc = minecraft.Minecraft.create("localhost")
bl = 247

ox,oy,oz = mc.player.getPos()
mc.setBlock(ox+2,oy,oz,bl)
ox += 2

while True:
	if mc.events.pollBlockHits(): break
	else: time.sleep(0.1)

up = 1
BTD = []
while True:
	if mc.getBlock(ox,oy+up,oz) != 0:
		BTD += [mc.getBlock(ox,oy+up,oz)]
		up += 1
	else: break
print (BTD)

cx,cy,cz = ox,oy,oz
while True:
	#time.sleep(0.3)
	ax,ay,az = cx,cy,cz
	if mc.getBlock(cx+1,cy,cz) in BTD:
		mc.setBlock(cx+1,cy,cz,bl)
		cx += 1
		mc.setBlock(ax,ay,az,0)
		continue
	if mc.getBlock(cx-1,cy,cz) in BTD:
		mc.setBlock(cx-1,cy,cz,bl)
		cx -= 1
		mc.setBlock(ax,ay,az,0)
		continue
	if mc.getBlock(cx,cy,cz-1) in BTD:
		mc.setBlock(cx,cy,cz-1,bl)
		cz -= 1
		mc.setBlock(ax,ay,az,0)
		continue
	if mc.getBlock(cx,cy,cz+1) in BTD:
		mc.setBlock(cx,cy,cz+1,bl)
		cz += 1
		mc.setBlock(ax,ay,az,0)
		continue
	if mc.getBlock(cx,cy-1,cz) in BTD:
		mc.setBlock(cx,cy-1,cz,bl)
		cy -= 1
		mc.setBlock(ax,ay,az,0)
		continue
	if mc.getBlock(cx,cy+1,cz) in BTD:
		mc.setBlock(cx,cy+1,cz,bl)
		cy += 1
		mc.setBlock(ax,ay,az,0)
		continue
