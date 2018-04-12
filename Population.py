from Player import player

xspeed = 2
yspeed = 5
class Population:
    
    def __init__(self, popsize):
        self.totalPop = popsize
        self.peeps = []
        
        for i in range(self.totalPop):
            self.peeps.append(player(height/2, yspeed, xspeed, 35, height))
        
        self.count = 0
            
    def reset(self):
        for peep in self.peeps:
            peep.x = 0
    
    def update(self):
        for peep in self.peeps:
            peep.moveRight()
            peep.display()
            peep.checkBounds()
        for x in range(0, len(self.peeps)*30, 30):
            text(self.peeps[x/30].fitness, 100, x)
        self.count += 1
        
        if self.count >= self.peeps[0].numCycles:
            self.reset()
            