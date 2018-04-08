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