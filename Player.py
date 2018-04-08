class player:
    x = 0
    y = 0
    xspeed = 0
    yspeed = 0
    radius = 0
    def __init__(self, y, yspeed, xspeed, radius):
        self.y = y
        self.yspeed = yspeed
        self.xspeed = xspeed
        self.radius = radius
    
    def display(self):
        fill(0,255,0)
        ellipse(self.x,self.y,self.radius,self.radius)
    
    def moveUp(self):
        self.y -= self.yspeed
    
    def moveDown(self):
        self.y += self.yspeed
    
    def moveRight(self):
        self.x += self.xspeed
        
    def checkBounds(self):
        if self.y>height:
            self.y=height
        if self.y<0:
            self.y=0
        if self.x>width:
            self.x=width # later on this is the end of the screen so win