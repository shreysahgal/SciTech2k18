<<<<<<< HEAD
class player(object):
    x = 0
    y = 0
    xspeed = 0
    yspeed = 0
    radius = 0

    def __init__(self, y, yspeed, xspeed, radius):
        self.y = y
        self.yspeed = yspeed
        self.xspeed = xspeed
        self.radius = radius

    def display():
        ellipse(x, y, radius, radius)

    def moveUp():
        self.y -= self.yspeed

    def moveDown():
        self.y += self.yspeed

    def moveRight():
        self.x += self.xspeed


def setup():
    size(600, 600)
    playerObj = player(displayHeight / 2, 5, 3, 10)


def draw():
    playerObj.moveRight()
    playerObj.display()


def keyPressed():
    if key == CODED:
        if keyCode == UP:
            playerObj.moveUp()
        elif keyCode == DOWN:
            playerObj.moveDown()
=======
>>>>>>> df8dfbefab7d5ccb4f3d610252fe427ffbbee93c
