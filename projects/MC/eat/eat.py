#!/usr/bin/python
import time
import mcpi.minecraft as minecraft
from mcpi.block import *
mc = minecraft.Minecraft.create("localhost")
bl = 20

def toArray(x,y,z): return str(x) + "," + str(y) + "," + str(z) + ","

def fromArray(array, place):
	data = array[place]
	sep = 0
	con = ""
	for let in data:
		if let == ",":
			if sep == 0:
				x = con
				con = ""
			if sep == 1:
				y = con
				con = ""
			if sep == 2:
				z = con
				break

			sep += 1
		else: con += let
	return int(x),int(y),int(z)

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

acBlocks = [toArray(int(ox),int(oy),int(oz))]
NacBlocks = acBlocks
while True:
#	for ita in range(0,len(acBlocks)):
#		x,y,z = fromArray(acBlocks,ita)
#		mc.setBlock(x,y,z,0)
	
	acBlocks = NacBlocks
	NacBlocks = []
	for ita in range(0,len(acBlocks)):
		cx,cy,cz = fromArray(acBlocks,ita)
		ax,ay,az = cx,cy,cz
		if mc.getBlock(cx+1,cy,cz) in BTD:
			mc.setBlock(cx+1,cy,cz,bl)
			mc.setBlock(cx,cy,cz,0)
			NacBlocks += [toArray(cx+1,cy,cz)]

		if mc.getBlock(cx-1,cy,cz) in BTD:
			mc.setBlock(cx-1,cy,cz,bl)
			mc.setBlock(cx,cy,cz,0)
			NacBlocks += [toArray(cx-1,cy,cz)]
			
		if mc.getBlock(cx,cy,cz-1) in BTD:
			mc.setBlock(cx,cy,cz-1,bl)
			mc.setBlock(cx,cy,cz,0)
			NacBlocks += [toArray(cx,cy,cz-1)]

		if mc.getBlock(cx,cy,cz+1) in BTD:
			mc.setBlock(cx,cy,cz+1,bl)
			mc.setBlock(cx,cy,cz,0)
			NacBlocks += [toArray(cx,cy,cz+1)]

		if mc.getBlock(cx,cy-1,cz) in BTD:
			mc.setBlock(cx,cy-1,cz,bl)
			mc.setBlock(cx,cy,cz,0)
			NacBlocks += [toArray(cx,cy-1,cz)]

		if mc.getBlock(cx,cy+1,cz) in BTD:
			mc.setBlock(cx,cy+1,cz,bl)
			mc.setBlock(cx,cy,cz,0)
			NacBlocks += [toArray(cx,cy+1,cz)]
		acBlocks += NacBlocks
