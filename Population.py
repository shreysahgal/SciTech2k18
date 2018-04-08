from Player import player

xspeed = 2
yspeed = 5
class Population: 
    
    peeps = []
    
    def __init__(self, popsize):
        self.totalPop = popsize
        
        for i in range(self.totalPop):
            peeps.append(player(height/2, yspeed, xspeed, 35))
            