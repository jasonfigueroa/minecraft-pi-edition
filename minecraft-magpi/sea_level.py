import mcpi.minecraft as minecraft
import mcpi.block as block
#import time

mc = minecraft.Minecraft.create()

#testing connection to game
mc.postToChat("adjusting immediate terrain")

air = block.Block(0)
grass = block.Block(2)

xmin = -25
xmax = 25
ymin = 0
ymax = 30 #this value must be a multiple of 10 for updates to be accurate
zmin = -25
zmax = 25

for i in range(ymax, ymin - 1, -1):
    if i == 0:
    	blocktype = grass
    else:
    	blocktype = air
    
    #percentages look strange because this for loop is decrementing
    #maybe change this block to a switch 	
    if i == (ymax / 10):
    	mc.postToChat("90% complete")
    elif i == (ymax / 10) * 2:
    	mc.postToChat("80% complete")
    elif i == (ymax / 10) * 3:
    	mc.postToChat("70% complete")
    elif i == (ymax / 10) * 4:
    	mc.postToChat("60% complete")
    elif i == (ymax / 10) * 5:
    	mc.postToChat("50% complete")
    elif i == (ymax / 10) * 6:
    	mc.postToChat("40% complete")
    elif i == (ymax / 10) * 7:
    	mc.postToChat("30% complete")
    elif i == (ymax / 10) * 8:
    	mc.postToChat("20% complete")
    elif i == (ymax / 10) * 9:
    	mc.postToChat("10% complete")
    	
    #old code for multiples of 4
    #elif i == ymax / 2:
    #	mc.postToChat("50% complete")
    #elif i == (ymax / 4) * 3:
    #	mc.postToChat("25% complete")

    for j in range(xmin, xmax + 1):
        for k in range(zmin, zmax + 1):
            mc.setBlock(j, i, k, blocktype)
            
mc.postToChat("terrain adjustment complete")
