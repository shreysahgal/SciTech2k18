import random
class DNA:
    def __init__(self, genes):
        self.lifespan = 200
        if genes:
            self.genes = genes
        else:
            self.genes = []
            for i in range(self.lifespan+1):
                self.genes.append(PVector.random2D().setMag(0.6))

            
    def crossover(self, partner):
        newgenes = []
        i = random.randint(0, len(self.genes))
        newgenes = self.genes[:i] + partner.genes[i:]
        return DNA(newgenes)
    
    def mutate(self):
        for i in self.genes:
            if random(1) < 0.05:
                i = PVector.random2D.setMag(0.6)
