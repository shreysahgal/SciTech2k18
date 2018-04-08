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
        if isinstance(self.counter, int):
            if self.moves[self.counter] == 0:
                self.moveUp()
            elif self.moves[self.counter] == 1:
                self.moveDown()
        self.counter += 0.5
        
        
    def checkBounds(self):
        if self.y>height:
            self.y=height
        if self.y<0:
            self.y=0
        if self.x>width:
            self.x=width # later on this is the end of the screen so win
                
    def checkCollisions(self, blocks):

        for block in blocks:
            if self.x<block.x:
                testX = block.x
            else:
                testX = self.x
            testY = self.y
            if self.y < block.y:
                testY = block.y # top edge
            elif self.y > block.y+block.h:
                testY = block.y+block.h # bottom edge
            
            dX = self.x-self.radius/2 - testX
            dY = self.y - testY
            d = sqrt( (dX*dX) + (dY*dY) )
            
            if d <= self.radius:
                return True
            
        return False
    
    def stopPlayer(self):
        self.xspeed = 0
        self.yspeed = 0