#!/usr/bin/python
import time
import mcpi.minecraft as minecraft
from mcpi.block import *
mc = minecraft.Minecraft.create("localhost")

#0.003 setblock
#0.049 getblock

x,y,z = mc.player.getPos()
startT = time.time()

###
#mc.setBlock(x,y,z,1)
X = mc.getBlock(x,y,z)
###

endT = time.time()
print(endT - startT)
