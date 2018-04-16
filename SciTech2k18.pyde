from rocket import Rocket
from population import Population
from block import Block
import random

p = None # population
lifespan = 200
target = None
gen = 0

numblocks = 15
blocks = []

asdf = None            

ready = False

w = 0

def setup():
    global p, target, numblocks, blocks
    p = Population(target)
    size(1000, 700)
    target = PVector(width/2, 50)
    
    # for i in range(numblocks+1):
    #     blocks.append(Block(random.randint(50, width), random.randint(50, height-50), random.randint(25, 60), random.randint(30, 70)))
    
def draw():
    global ready
    
    background(192, 147, 255, 150)
    if ready:
        textSize(20)
        doThings()
    else:
        textAlign(CENTER)
        fill(0, 90)
        textSize(30)
        text("press any key to start the training", width/2, height/2 - 100)
        textSize(60)
        fill(255, 211, 249)
        text("Start!", width/2, height/2)
        prepare()
        for b in blocks:
            b.show()
        
        if keyPressed == True:
            ready = True

def prepare():
    global blocks
    if mousePressed and mouseButton == LEFT:
        blocks.append(Block(mouseX, mouseY, 50, 50))
        
    
def doThings():
    global p, gen, target, blocks, asdf
    
    background(192, 147, 255, 150)
    
    
    p.checkColls(blocks)
    p.run()
    
    fill(255)
    text("gen: " + str(gen), 100, 100)
    text("max fitness: " + p.maxfit[:5], 100, 150)
    
    # if any(p.rockets[-1].count == lifespan:
    if any([r.count >= lifespan for r in p.rockets]):
        p.resetCount()
        p.evaluate()
        # p.stopAll()
        p.selection()
        # p.printFit()
        gen += 1
    
    ellipse(target.x, target.y, 20, 20)
    
    for b in blocks:
        b.show()
