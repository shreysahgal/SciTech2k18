
class Block:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def show(self):
        rectMode(CENTER)
        fill(0,0,255)
        rect(self.x, self.y, self.w, self.h)