#!/usr/bin/python
from mcpi.minecraft import minecraft
size = 10
mc = minecraft.create()
x,y,z = mc.player.getTilepos()
print ("Making Steps at: " + str (x + 2) + ", " + str (z)

for step in range(size)
	 mc.setBlock(x+2, y,  z,  block.STAIRS_WOOD.id,0)
	 mc.setBlock(x+3, y, z, block.WOOD.id)      
	 
