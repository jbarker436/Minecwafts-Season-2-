from mcpi.minecraft import Minecraft

mc = Minecraft.create()

position = mc.player.getTilePos()

x = position.x
y = position.y
z = position.z

y = y + y + y
mc.player.setTilePos(x, y, z)
