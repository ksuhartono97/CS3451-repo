import random

circleSize = 0.7
circleRot = 0.0
colorArr = [color(148, 0, 211), color(75, 0, 130), color(0, 0, 255), color(0, 255, 0), color(255, 255, 0), color(255, 127, 0), color(255, 0 , 0)]

def setup():
    size(500, 500)
    
def draw():
    background(255, 255, 255)
    noStroke()  
    noFill()
    circleSize = (1 - (mouseY+1) / float(height)) * 0.7
    circleRot = (mouseX + 1) / float(width)
    drawEllipse(width/2, height/2, width, height, 0, circleSize, circleRot)
        
def drawEllipse(w, h, rw, rh, depth, radiusMultiplier, rotationMultiplier):
    if depth==7:
        return
        
    fill(colorArr[depth])
    ellipse(w, h, rw, rh)   
    if rw > 1 or rh > 1:
        for i in range(3):
            theta = 2*PI*i/float(3) + PI/float(6) + 2*PI*rotationMultiplier
            newX = w + (1 - radiusMultiplier)*rw/2*cos(theta)
            newY = h + (1 - radiusMultiplier)*rh/2*sin(theta)
            theta = 2*PI*i/float(3)
            drawEllipse(newX, newY, rw*(radiusMultiplier), rh * (radiusMultiplier), depth+1, radiusMultiplier, rotationMultiplier)