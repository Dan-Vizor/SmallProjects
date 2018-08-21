#!/usr/bin/python
import mcpi.minecraft as minecraft
from mcpi.block import *
mc = minecraft.Minecraft.create("localhost")

def build():
	size = raw_input("enter size: ")
	size = int(size)
	x,y,z = mc.player.getPos()
	mc.setBlocks(x-size+2,y-10,z-size+2,x+size+2,y+30,z+size+2,0)
	mc.setBlocks(x-30,y+5,z-30,x+30,y,z+30,0)
	mc.setBlocks(x-size+2,y-10,z-size+2,x+size+2,y-1,z+size+2,2)
	
	mc.setBlocks(x-size+1,y,z-size+1,x+size+2,y+6,z+size+2,4)
	mc.setBlocks(x-size+1,y,z-size+1,x+size,y+6,z+size,0)
build()
