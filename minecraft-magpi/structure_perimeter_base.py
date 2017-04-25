import mcpi.minecraft as minecraft
import mcpi.block as block
#import time

mc = minecraft.Minecraft.create()

#testing connection to game
mc.postToChat("building structure perimeter base and flooring")

#assign desired block ids for structure and floor
structureBlockId = 45 #brick block
floorBlockId = 5

structureBlock = block.Block(structureBlockId)
floorBlock = block.Block(floorBlockId)

xmin = -10
xmax = 10

groundlevel = 1
ceiling = groundlevel + 5

zmin = -10
zmax = 10


for y in range(groundlevel, ceiling + 1):
	for x in range(xmin, xmax + 1):
    		for z in range(zmin, zmax + 1):
            		if (x == xmin or x == xmax) or (z == zmin or z == zmax):
                		mc.setBlock(x, y, z, structureBlock)
            		elif (y == groundlevel):
                		mc.setBlock(x, y - 1, z, floorBlock)
                	elif (y == ceiling):
                		mc.setBlock(x, y, z, floorBlock)
            
mc.postToChat("structure perimeter base and flooring complete")
