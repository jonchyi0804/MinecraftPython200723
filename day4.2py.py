# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 10:43:29 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random
x,y,z = mc.player.getTilePos()
for i in range(20):
    r = random.randrange(1,7)
    
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,57)
        x = x+4
    elif r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,41)
        x = x-4
    elif r == 3:
        mc.setBlocks(x,y,z,x,y,z+4,47)
        z = z+4
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z-4,155) 
        z = z-4
    elif r == 5:
        mc.setBlocks(x,y,z,x,y+4,z,423) 
        y = y+4
    elif r == 6:
        mc.setBlocks(x,y,z,x,y-4,z,97) 
        y = y-4    
    
    
    
    
    
    
    
    