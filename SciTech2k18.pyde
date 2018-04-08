from Block import Block
from Player import player

playerObj = None

def setup():
    size(600,600)
    global playerObj
    playerObj = player(height/2,10,1,100)
    
def draw():
    background(255)
    global playerObj
    playerObj.moveRight()
    playerObj.display()

def keyPressed():
    global playerObj
    if key == CODED:
        if keyCode == UP:
            playerObj.moveUp()
        elif keyCode == DOWN:
            playerObj.moveDown()