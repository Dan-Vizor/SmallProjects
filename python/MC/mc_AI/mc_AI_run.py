#!/usr/bin/python
import mcpi.minecraft as minecraft
from mcpi.block import *
mc = minecraft.Minecraft.create("localhost")
import os

mc.setBlocks(-2,59,-2,2,62,2,1)
mc.setBlocks(-2,61,-2,2,61,2,20)
mc.setBlock(0,62,0,89)
mc.setBlocks(-1,61,-1,1,59,1,0)
mc.setBlock(0,59,0,20)

mc.player.setPos(0.5,60,0.5)
os.system("./mc_AI.py")
