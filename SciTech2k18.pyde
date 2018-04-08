from Block import Block
from Player import player
import random

blocks = []

def spawnRandomBlocks(n):
    global blocks
    
    for i in range(n):
<<<<<<< HEAD
        blocks.append(Block(random.randint(0, width-99), height*random.randint(0, 1), random.randint(50, 120), random.randint(0, int(height/1.1))))
=======
        blocks.append(Block(random.randint(0, width-99), random.randint(0, height-99), random.randint(50, 120), random.randint(0, int(height/1.1))))
>>>>>>> 92a05658bb8675dc8741e42d67825bde9bc3634f
    
def setup():
    size(displayWidth,displayHeight)
    global playerObj
<<<<<<< HEAD
    playerObj = player(height/2,10,8,100)
=======
    playerObj = player(height/2,10,3,40)
>>>>>>> 92a05658bb8675dc8741e42d67825bde9bc3634f
    global blocks
    
    spawnRandomBlocks(8)
        
def draw():
    global blocks
    background(255)
    global playerObj
    playerObj.moveRight()
    playerObj.checkBounds()
    playerObj.display()
    for block in blocks:
        block.show()
<<<<<<< HEAD
    if playerObj.checkCollisions(blocks):
        noLoop()
        print(playerObj.x, playerObj.y, playerObj.radius)
=======
    if (playerObj.checkCollisions(blocks)):
        playerObj.stopPlayer()
>>>>>>> 92a05658bb8675dc8741e42d67825bde9bc3634f

def keyPressed():
     global playerObj
     if key == CODED:
         if keyCode == UP:
             playerObj.moveUp()
         elif keyCode == DOWN:
             playerObj.moveDown()