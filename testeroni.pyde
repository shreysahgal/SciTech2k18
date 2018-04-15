from rocket import Rocket
from population import Population
from block import Block
import random

p = None # population
lifespan = 200
target = None
gen = 0

numblocks = 5
blocks = []

def setup():
    global p, target, numblocks, blocks
    p = Population(target)
    size(1000, 700)
    target = PVector(width/2, 50)
    
    for i in range(numblocks+1):
        blocks.append(Block(random.randint(50, width), random.randint(50, height-50), random.randint(25, 60), random.randint(30, 70)))
    
def draw():
    global p, gen, target, blocks
    
    background(192, 147, 255, 150)
    
    p.run()
    p.checkColls(blocks)
    
    fill(255)
    text(p.rockets[0].count, 100, 100)
    text(gen, 150, 150)
    
    if p.rockets[-1].count == lifespan:
        p.resetCount()
        p.evaluate()
        # p.stopAll()
        p.selection()
        # p.printFit()
        gen += 1
    
    ellipse(target.x, target.y, 20, 20)
    
    for b in blocks:
        b.show()
