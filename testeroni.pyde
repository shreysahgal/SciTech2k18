from rocket import Rocket
from population import Population

p = None
lifespan = 200
target = None
gen = 0

def setup():
    global p, target
    p = Population(target)
    size(1000, 700)
    target = PVector(width/2, 50)
    
def draw():
    global p, gen, target
    background(192, 147, 255, 150)
    p.run()
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
