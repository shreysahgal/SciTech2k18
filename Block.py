class Block:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        
    def show(self):
        rectMode(CORNER)
        fill(255, 211, 249)
        rect(self.x, self.y, self.w, self.h)
