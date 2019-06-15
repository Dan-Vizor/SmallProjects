#!/usr/bin/python
import time
import mcpi.minecraft as minecraft
from mcpi.block import *
mc = minecraft.Minecraft.create("localhost")

x,y,z = mc.player.getPos()
out = mc.getBlock(x,y-1,z)
print(out)
mc.postToChat(out)
