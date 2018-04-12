from Block import Block
import random

def upOrDown():
    if random.randint(0, 1) == 0:
        return 0
    return 1

class player:
    
    def __init__(self, y, yspeed, xspeed, radius, dnalen):
        self.x = 0
        self.y = y
        self.yspeed = yspeed
        self.xspeed = xspeed
        self.radius = radius
        self.moves = []
        self.counter = 0
        self.numCycles = dnalen
        self.fiss = 1/(dist(self.x, self.y, width, height/2))

        for i in range(dnalen):
            self.moves.append(upOrDown())
    
    def display(self):
        fill(0,255,0)
        ellipse(self.x,self.y,self.radius,self.radius)
    
    def moveUp(self):
        self.y -= self.yspeed
    
    def moveDown(self):
        self.y += self.yspeed

    def moveRight(self):
        self.x += self.xspeed
        if self.counter < len(self.moves):
            if self.moves[self.counter] == 0:
                self.moveUp()
            else:
                self.moveDown()
        self.counter += 1
        self.fitness = 100/(dist(self.x, self.y, width, self.y)+1)
        line(self.x, self.y, width, self.y)
        
    def checkBounds(self):
        if self.y>height:
            self.y=height
        if self.y<0:
            self.y=0
        if self.x>width:
            self.x=width # later on this is the end of the screen so win
                
    def checkCollisions(self, blocks):

        for block in blocks: # test variables are the perpendicular intersections
            testX = self.x
            if self.x<block.x: # left of the rect
                testX = block.x
            elif self.x>block.x+block.w:# right; this is probably never gonna happen but it is necessary if you are passed the box and want to get a false
                testX = block.x+block.w
            testY = self.y
            if self.y < block.y:# above the rect
                testY = block.y # 
            elif self.y > block.y+block.h:
                testY = block.y+block.h # bottom edge
<<<<<<< HEAD
            
            dX = self.x - testX
            dY = self.y - testY
            d = sqrt( (dX*dX) + (dY*dY) )
            
            if d <= self.radius/2:
                return True            
=======

            dX = self.x - testX
            dY = self.y - testY
            d = sqrt( (dX*dX) + (dY*dY) )

            if d <= self.radius/2:
                return True
>>>>>>> 4abda537b3daad230e43ac874b4a17b519e85ded
        return False
    
    def stopPlayer(self):
        self.xspeed = 0
        self.yspeed = 0
        
    def resetX(self):
        self.x = 0
        self.xspeed = 2
        self.yspeed = 5
        