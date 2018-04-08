
class Block:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.tag = None
        if y == 0:
            self.tag = True
        else:
            self.tag = False
            
    def show(self):
        rectMode(CENTER)
        fill(0,0,255)
        rect(self.x, self.y, self.w, self.h)
    
    def info(self):
        print(self.x, self.y, self.tag)