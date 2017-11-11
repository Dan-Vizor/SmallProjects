#!/usr/bin/python
import time
import thread
from random import randint
import mcpi.minecraft as minecraft
from mcpi.block import *
mc = minecraft.Minecraft.create("localhost")

def make_death_box():
	mc.setBlocks(-2,59,-2,2,62,2,1)
	mc.setBlocks(-2,61,-2,2,61,2,20)
	mc.setBlock(0,62,0,89)
	mc.setBlocks(-1,61,-1,1,59,1,0)
	mc.setBlock(0,59,0,1)

def makeBot(x,y,z):
	mc.setBlock(x,y+1,z,49)
	mc.setBlock(x-1,y,z,1)
	mc.setBlock(x,y,z+1,1)
	mc.setBlock(x,y,z-1,1)
	mc.setBlock(x+1,y+1,z,89)
	mc.setBlock(x+1,y,z,89)
	mc.setBlock(x,y,z,247)
	time.sleep(2)
	mc.setBlocks(x+2,y+1,z+1,x-1,y,z-1,0)

	mc.setBlock(x,y-1,z,247)
	print 'bot made at:' ,x,y,z
	
def printBot(x,y,z):
	mc.setBlock(x,y,z,247)
	
def delOBot(Ox,Oy,Oz): mc.setBlock(Ox,Oy,Oz,0)
def bot_kill(x,y,z,ou):
	mc.setBlock(x,y,z,0)
	Px,Py,Pz = mc.player.getPos()
	if ou == 1:
		print("bot killed")
		mc.postToChat("killed bot")

def bot_alive(x,y,z):
	if mc.getBlock(x,y,z) == 0:
		return False
	return True

def bot_AI(Iy):
	Px = randint(-30,30)
	Pz = randint(-30,30)
	makeBot(Px,Iy,Pz)
	x = Px
	y = Iy - 1
	z = Pz
	while True:
		if not bot_alive(x,y,z): break
		time.sleep(0.1)
		Plx,Ply,Plz = mc.player.getPos()
		if int(x) in range(int(Plx-2),int(Plx+2)):
			if int(z) in range(int(Plz-2),int(Plz+2)):
				if int(y-1) in range(int(Ply-2),int(Ply+2)):
					bot_kill(x,y,z,0)
					mc.postToChat("you died")
					print("player died")
					make_death_box()
					mc.player.setPos(0,60,0)
					break
		

			if Plx > x:
				if int(Plx) != range(int(x-1),int(x+1)):
					if mc.getBlock(x,y,z) == 0:
						bot_kill(x,y,z,1)
						continue
					
					if mc.getBlock(x+1,y+1,z) != 0:
						printBot(x,y+1,z)
						delOBot(x,y,z)
						y += 1
						
						continue
					if mc.getBlock(x+1,y,z) != 0:
						printBot(x+1,y+1,z)
						delOBot(x,y,z)
						y += 1
						x += 1
						
						continue
						
					if mc.getBlock(x,y-2,z) == 0:
						printBot(x,y-1,z)
						delOBot(x,y,z)
						y -= 1
						
						continue
							
					if mc.getBlock(x,y-1,z) != 0:
						printBot(x,y+1,z)
						delOBot(x,y,z)
						y += 1
						
						continue

					printBot(x+1,y,z)
					delOBot(x,y,z)
					x += 1
					if mc.getBlock(x,y,z) == 0:
						bot_kill(x,y,z,1)
						continue
			
		
		if Plx < x:
			if int(Plx) != range(int(x-1),int(x+1)):
				if mc.getBlock(x,y,z) == 0:
						bot_kill(x,y,z,1)
						continue
					
				if mc.getBlock(x-1,y+1,z) != 0:
					printBot(x,y+1,z)
					delOBot(x,y,z)
					y += 1
					
					continue
				if mc.getBlock(x-1,y,z) != 0:
					printBot(x-1,y+1,z)
					delOBot(x,y,z)
					y += 1
					x -= 1
					
					continue
					
				if mc.getBlock(x,y-2,z) == 0:
					printBot(x,y-1,z)
					delOBot(x,y,z)
					y -= 1
					
					continue
						
				if mc.getBlock(x,y-1,z) != 0:
					printBot(x,y+1,z)
					delOBot(x,y,z)
					y += 1
					
					continue

				printBot(x-1,y,z)
				delOBot(x,y,z)
				x -= 1
				if mc.getBlock(x,y,z) == 0:
					bot_kill(x,y,z,1)
					continue
		
		
		if Plz > z: 
			if int(Plz) != range(int(z-1),int(z+1)):
				if mc.getBlock(x,y,z) == 0:
						bot_kill(x,y,z,1)
						continue
					
				if mc.getBlock(x,y+1,z+1) != 0:
					printBot(x,y+1,z)
					delOBot(x,y,z)
					y += 1
					
					continue
				if mc.getBlock(x,y,z+1) != 0:
					printBot(x,y+1,z+1)
					delOBot(x,y,z)
					y += 1
					z += 1
					
					continue
					
				if mc.getBlock(x,y-2,z) == 0:
					printBot(x,y-1,z)
					delOBot(x,y,z)
					y -= 1
					
					continue
						
				if mc.getBlock(x,y-1,z) != 0:
					printBot(x,y+1,z)
					delOBot(x,y,z)
					y += 1
					continue

				printBot(x,y,z+1,)
				delOBot(x,y,z)
				z += 1
				if mc.getBlock(x,y,z) == 0:
					bot_kill(x,y,z,1)
					continue
	

		if Plz < z:
			if int(Plz) != range(int(z-1),int(z+1)):
				if mc.getBlock(x,y,z) == 0:
						bot_kill(x,y,z,1)
						continue
					
				if mc.getBlock(x,y+1,z-1) != 0:
					printBot(x,y+1,z)
					delOBot(x,y,z)
					y += 1
			
					continue
				if mc.getBlock(x,y,z-1) != 0:
					printBot(x,y+1,z-1)
					delOBot(x,y,z)
					y += 1
					z -= 1
				
					continue
					
				if mc.getBlock(x,y-2,z) == 0:
					printBot(x,y-1,z)
					delOBot(x,y,z)
					y -= 1
					continue
						
				if mc.getBlock(x,y-1,z) != 0:
					printBot(x,y+1,z)
					delOBot(x,y,z)
					y += 1
					continue

				printBot(x,y,z-1)
				delOBot(x,y,z)
				z -= 1
				if mc.getBlock(x,y,z) == 0:
					bot_kill(x,y,z,1)
					continue

make_death_box()
mc.player.setPos(0,60,0)
while True:
	time.sleep(3)
	Plx,Ply,Plz = mc.player.getPos()
	if Ply < 40:
		#thread.start_new_thread ( bot_AI,(10,))
		#thread.start_new_thread ( bot_AI,(10,))
		bot_AI(10)
