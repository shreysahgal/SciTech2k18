
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
        self.upperBound = self.y
        self.lowerBound = self.y + self.h
    def show(self):
        fill(0,0,255)
        rect(self.x, self.y, self.w, self.h)