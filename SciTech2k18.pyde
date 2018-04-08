from Block import Block
from Player import player
import random

blocks = []

def spawnRandomBlocks(n):
    global blocks
    
    for i in range(n):
        blocks.append(Block(random.randint(0, width-99), height*random.randint(0, 1), random.randint(50, 120), random.randint(0, int(height/1.1))))
    
def setup():
    size(displayWidth,displayHeight)
    global playerObj
    playerObj = player(height/2,10,8,100)
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
    if playerObj.checkCollisions(blocks):
        noLoop()
        print(playerObj.x, playerObj.y, playerObj.radius)

def keyPressed():
     global playerObj
     if key == CODED:
         if keyCode == UP:
             playerObj.moveUp()
         elif keyCode == DOWN:
             playerObj.moveDown()