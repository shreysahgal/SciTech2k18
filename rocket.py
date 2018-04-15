from dna import DNA
class Rocket:
    
    def __init__(self, target, dna, id):
        self.pos = PVector(width/2, height)
        self.vel = PVector()
        self.acc = PVector()
        self.reached = False
        self.isCollided = False
        self.rotMod = 0
        self.fitMod = 0
        if dna:
            self.dna = dna
        else:
            self.dna = DNA(None)
        self.count = 0
        self.target = target
        self.fitness = 0
        self.id = id
        self.col = color(0)
        
    def applyForce(self, force):
        self.acc.add(force)
    
    def update(self):
        if not self.reached and not self.isCollided:
            self.vel.add(self.acc)
            self.pos.add(self.vel)
            self.acc.mult(0)
        
        if self.count < self.dna.lifespan and not self.isCollided:
            self.applyForce(self.dna.genes[self.count])
            self.count += 1
        
            
        if dist(self.pos.x, self.pos.y, width/2, 50) <= 20:
           self.reached = True
           
        if self.reached or self.isCollided:
            self.halt()
            print("isCOllided")
            self.col = color(255)
        
    def show(self):
        fill(self.col)
        
        ellipseMode(CENTER)
        ellipse(self.pos.x, self.pos.y, 25, 25)
        
    def calcFitness(self):
        d = dist(self.pos.x, self.pos.y, width/2, 50)
        self.fitness = map(d, 0, width, width, 0)
        if self.reached:
            self.fitness *= 5
        elif self.isCollided:
            self.fitness /= 5
        
    def halt(self):
        self.vel = PVector()
        self.acc = PVector()
    
    def checkColls(self, blocks):
        for i in blocks: 
            testX = self.pos.x
            if self.pos.x < i.x:
                testX = i.x
            elif self.pos.x > i.x + i.w:
                testX = i.x + i.w
            
            testY = self.pos.y
            if self.pos.y < i.y:
                testY = i.y
            elif self.pos.y > i.y + i.h:
                testY = i.y + i.h
            
            dX = self.pos.x - testX
            dY = self.pos.y - testY
            
            d = sqrt( (dX*dX) + (dY*dY) )
            
            if d <= 25/2:
                return True
        return False
            
