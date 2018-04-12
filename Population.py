from Player import player

xspeed = 2
yspeed = 5
blocks = []
class Population:
    
    def __init__(self, popsize, b):
        global blocks
        self.totalPop = popsize
        self.peeps = []
        blocks = b
        
        for i in range(self.totalPop):
            self.peeps.append(player(height/2, yspeed, xspeed, 35, height))
        
        self.count = 0
            
    def reset(self):
        for peep in self.peeps:
            # peep.x = 0
            # peep.y = height/2
            # peep.xspeed = 2
            # peep.yspeed = 5
            peep.resetX()
    
    def update(self):
        global blocks
        for peep in self.peeps:
            peep.moveRight()
            peep.display()
            peep.checkBounds()
            if (player.checkCollisions(peep, blocks)):
                player.stopPlayer(peep)
        for x in range(0, len(self.peeps)*30, 30):
            text(self.peeps[x/30].fitness, 100, x)
        self.count += 1
        text(self.count, 500, 500)
        
        if self.count >= self.peeps[0].numCycles:
            self.reset()
            self.count = 0
            