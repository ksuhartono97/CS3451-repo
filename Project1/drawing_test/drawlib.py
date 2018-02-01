# Drawing Routines, like OpenGL

from matlib import *

vertexList = []
allowDraw = False

def gtOrtho(left, right, bottom, top, near, far):
    
    pass

def gtPerspective(fov, near, far):
    
    pass

def gtBeginShape():
    global vertexList
    vertexList = []
    global allowDraw
    allowDraw = True
    
def gtEndShape():
    global vertexList
    print vertexList
    
    for i in range(0, len(vertexList), 2):
        point1 = vertexList[i]
        point2 = vertexList[i+1]
        line(point1[0], point1[1], point2[2], point2[0], point2[1], point2[2])
        # print point1,
        # print " ",
        # print point2
    
    vertexList = []
    global allowDraw
    allowDraw = False
    print vertexList

def gtVertex(x, y, z):
    global vertexList
    if allowDraw == True: 
        vertexList.append((x, y, z))