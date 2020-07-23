# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 09:55:19 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
x,y,z = mc.player.getTilePos()

nuber = 1

for i in range(8):
    for j in range(nuber):
        mc.spawnEntity(x,y,z,61e)
    
    nuber = nuber * 2
    mc.postToChat("你生成了"+str(nuber)+"隻蠹魚")