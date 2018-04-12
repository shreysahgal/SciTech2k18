from Block import Block
from Player import player
from Population import Population

import random

blocks = []
def spawnRandomBlocks(n):
    global blocks
 
    for x in range(100, width-100, 250):
        blocks.append(Block(x, random.randint(0, height-99), random.randint(40, 90), random.randint(0, int(height/1.1))))
def setup():
    size(displayWidth, displayHeight)
    global playerObj
    playerObj = player(height/2,10,2,40, width/2)
    global blocks
    
    spawnRandomBlocks(6)
        
def draw():
    global blocks
    background(255)
    strokeWeight(1)
    global playerObj
    playerObj.moveRight()
    playerObj.checkBounds()
    playerObj.display()
    for block in blocks:
        block.show()
    if (playerObj.checkCollisions(blocks)):
        playerObj.stopPlayer()
    
    strokeWeight(5)
    topDist = playerRayCastb30()
    line(playerObj.x,playerObj.y,playerObj.x+cos(PI/6)*topDist,playerObj.y+sin(PI/6)*topDist)
    
    midDist = playerRayCast0()
    line(playerObj.x,playerObj.y,playerObj.x+midDist,playerObj.y)
    
    bottomDist = playerRayCast30()
    line(playerObj.x,playerObj.y,playerObj.x+cos(-PI/6)*bottomDist,playerObj.y+sin(-PI/6)*bottomDist)
    
# dumb comment
def keyPressed():
     global playerObj
     if key == CODED:
         if keyCode == UP:
             playerObj.moveUp()
         elif keyCode == DOWN:
             playerObj.moveDown()

def playerRayCast0(): # ray cast forward
    global playerObj
    global blocks
    dists = [width]
    for i in blocks:
        if i.y<=playerObj.y and i.y+i.h>=playerObj.y and i.x >= playerObj.x:
            dists.append(i.x-playerObj.x)
    return min(dists)

def playerRayCast30(): # ray cast 30 degrees up
    global playerObj
    global blocks
    dists=[width*2]
    m = -1/sqrt(3) # negative because computer y axis is flipped
    for i in blocks:
        if i.x<playerObj.x:
            continue
        if i.y>=playerObj.y: # player is above; no way for ray 30 degrees above to hit
            continue
        elif i.y+i.h<=playerObj.y: # player is below
            # check against rect's bottom edge
            testx = (m*playerObj.x+i.y+i.h-playerObj.y)/m # using point-slope equation to find the x loc
            if testx>=i.x and testx<=i.x+i.w:
                dists.append(dist(playerObj.x,playerObj.y,testx,i.y))
            # check against rect's left edge
            testy = m*(i.x-playerObj.x)+playerObj.y
            if testy>=i.y and testy<=i.y+i.h:
                dists.append(dist(playerObj.x,playerObj.y,i.x,testy))
        else: # player is somewhere in 'front'; ray can only possibly hit left side
            # check against rect's left edge
            testy = m*(i.x-playerObj.x)+playerObj.y
            if testy>=i.y and testy<=i.y+i.h:
                dists.append(dist(playerObj.x,playerObj.y,i.x,testy))
    return min(dists)

def playerRayCastb30(): # ray cast 30 degrees down
    global playerObj
    global blocks
    dists=[width*2]
    m = 1/sqrt(3) # positive because computer y axis is flipped
    for i in blocks:
        if i.x<playerObj.x:
            continue
        if i.y>=playerObj.y: # player is above            
            # check against rect's top edge
            testx = (m*playerObj.x+i.y-playerObj.y)/m # using point-slope equation to find the x loc
            if testx>=i.x and testx<=i.x+i.w:
                dists.append(dist(playerObj.x,playerObj.y,testx,i.y))
            # check against rect's left edge
            testy = m*(i.x-playerObj.x)+playerObj.y
            if testy>=i.y and testy<=i.y+i.h:
                dists.append(dist(playerObj.x,playerObj.y,i.x,testy))
        elif i.y+i.h<=playerObj.y: # player is below; cannot possibly hit
            continue
        else: # player is somewhere in 'front'; ray can only possibly hit left side
            # check against rect's left edge
            testy = m*(i.x-playerObj.x)+playerObj.y
            if testy>=i.y and testy<=i.y+i.h:
                dists.append(dist(playerObj.x,playerObj.y,i.x,testy))
    return min(dists)