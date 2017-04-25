#should try altering this program to loop y values backwards and fill with air 
#blocks until desired elevation level

import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

#testing connection to game
mc.postToChat("hi")

xmin = -50
xmax = 50
ymin = 0
ymax = 20
zmin = -50
zmax = 50
for i in range(ymin, ymax + 1):
    for j in range(xmin, xmax + 1):
        for k in range(zmin, zmax + 1):
            mc.setBlock(j, i, k, grass)
