
class Block:
    def __init__(self, x, y, w, h):
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.tag = None
        if y == 0:
            self.tag = True
        else:
            self.tag = False
<<<<<<< HEAD
            
=======
        self.upperBound = self.y
        self.lowerBound = self.y + self.h
>>>>>>> 92a05658bb8675dc8741e42d67825bde9bc3634f
    def show(self):
        fill(0,0,255)
        rect(self.x, self.y, self.w, self.h)
    
    def info(self):
        print(self.x, self.y, self.tag)