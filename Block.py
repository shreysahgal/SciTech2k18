
class Block:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def show(self):
        rectMode(CENTER)
        rect(x, y, w, h)