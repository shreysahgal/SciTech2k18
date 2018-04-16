from rocket import Rocket
import random

class Population:
    
    def __init__(self, target):
        self.rockets = []
        self.popsize = 25
        self.matingpool = []
        self.target = target
        self.maxfit = "n/a"
        
        for i in range(self.popsize):
            self.rockets.append(Rocket(self.target, None, i))
    
    def run(self):
        for i in self.rockets:
            i.update()
            i.show()
            
    def resetCount(self):
        for i in self.rockets:
            i.count = 1000
    
    def evaluate(self):
        maxfit = 0
        
        for i in self.rockets:
            i.calcFitness()
            if i.fitness > maxfit:
                maxfit = i.fitness
        
        self.maxfit = str(maxfit)

        for i in self.rockets:
            i.fitness /= maxfit
        
        self.matingpool = []
         
        for i in self.rockets:
            n = int(i.fitness*100)
            # print(n)
            if (n > 0):
                for j in range(n):
                    self.matingpool.append(i)
        # for i in self.matingpool:
            # print(i.fitness)
        
       
    
    def selection(self):
        newrockets = []
        for i in self.rockets:
            parentA = random.choice(self.matingpool).dna
            parentB = random.choice(self.matingpool).dna
            child =  parentA.crossover(parentB)
            child.mutate()
            # print(i.fitness)
            newrockets.append(Rocket(self.target, child, None))
        
        self.rockets = newrockets
    
    def printFit(self):
        for i in self.rockets:
            print(str(i.id) + ": " + str(int(i.fitness*100)))
            
    def stopAll(self):
        for i in self.rockets:
            i.halt()
            
    def checkColls(self, blocks):
        for i in self.rockets:
            if i.checkColls(blocks):
                i.isCollided = True
