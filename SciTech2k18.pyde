from Block import Block
from Player import player
import random

blocks = []

def spawnRandomBlocks(n):
    global blocks
    
    for i in range(n):
        blocks.append(Block(random.randint(0, width-99), random.randint(0, height-99), random.randint(50, 120), random.randint(0, int(height/1.1))))
    
def setup():
    size(displayWidth,displayHeight)
    global playerObj
    playerObj = player(height/2,10,3,40)
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
    if (playerObj.checkCollisions(blocks)):
        playerObj.stopPlayer()
# dumb comment
def keyPressed():
     global playerObj
     if key == CODED:
         if keyCode == UP:
             playerObj.moveUp()
         elif keyCode == DOWN:
             playerObj.moveDown()