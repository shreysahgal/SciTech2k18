from dna import DNA
class Rocket:
    
    def __init__(self, target, dna, id):
        self.pos = PVector(width/2, height)
        self.vel = PVector()
        self.acc = PVector()
        if dna:
            self.dna = dna
        else:
            self.dna = DNA(None)
        self.count = 0
        self.target = target
        self.fitness = 0
        self.id = id
        
    def applyForce(self, force):
        self.acc.add(force)
    
    def update(self):
        if self.count < self.dna.lifespan:
            self.applyForce(self.dna.genes[self.count])
            self.count += 1
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.mult(0)
        
    def show(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y)
        fill(255, 150)
        rotate(self.vel.heading())
        rectMode(CENTER)
        rect(0, 0, 50, 10)
        # text(self.id, 60, 0)
        popMatrix()
        
    def calcFitness(self):
        d = dist(self.pos.x, self.pos.y, width/2, 50)
        self.fitness = map(d, 0, width, width, 0)
        
