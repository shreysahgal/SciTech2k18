<<<<<<< HEAD
from Block import Block
from Player import player
import random

blocks = []

def spawnRandomBlocks(n):
    global blocks
    
    for i in range(n):
        blocks.append(Block(random.randint(0, width-99), height*random.randint(0, 2), random.randint(50, 120), random.randint(600, 800)))
    
def setup():
    size(600, 600)
    global blocks
    
    spawnRandomBlocks(5)
        
def draw():
    global blocks
    
    for block in blocks:
        block.show()
=======
<<<<<<< HEAD
#blah
=======
>>>>>>> 102ef5465a735d01c6b83bc399db83fe6f097405
>>>>>>> df8dfbefab7d5ccb4f3d610252fe427ffbbee93c
