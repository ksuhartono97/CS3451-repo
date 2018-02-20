# Drawing Routines, like OpenGL

from matlib import *

vertexList = []
allowDraw = False
xModifierFunction = None
yModifierFunction = None
orthoDict = {}
perspDict = {}
projFlag = None 
#False for ortho

def coordinateTransformer(x, y, z):
    ctm = gtGetMatrix()
    # print ctm
    
    coordinateMat = [[0 for g in range(4)] for h in range(4)]
    coordinateMat[0][0] = x
    coordinateMat[1][0] = y
    coordinateMat[2][0] = z
    coordinateMat[3][0] = 1
    res = [[0 for a in range(4)] for b in range(4)]
    
    for j in range(len(res[0])): #j is y
        for i in range(len(res)): #i is x
            for k in range(4):
                res[j][i] += ctm[j][k] * coordinateMat[k][i]    
                
    return [res[0][0], res[1][0], res[2][0]]        
        

def xOrthoModifier(x, left, right):
    newX = (x - left) / float(right - left) * width
    return newX
    
def yOrthoModifier(y, bottom, top):
    newY = (y - bottom) / float(top - bottom) * height
    return (height - newY)
    
def xPerspModifier(x, z, fov):
    theta = 2*PI*fov/float(360)
    k = tan(theta/2)
    firstX = x / abs(z)
    newX = (firstX + k) * width / (2 * k)
    return newX

def yPerspModifier(y, z, fov):
    theta = 2*PI*fov/float(360)
    k = tan(theta/2)
    firstY = y / abs(z)
    newY = (firstY + k) * height / (2 * k)
    return (height - newY)

def gtOrtho(left, right, bottom, top, near, far):
    xModifierFunction = xOrthoModifier
    yModifierFunction = yOrthoModifier
    global orthoDict
    orthoDict = {'left':left, 'right':right, 'bottom':bottom, 'top': top, 'near': near, 'far':far}
    global projFlag
    projFlag = False

def gtPerspective(fov, near, far):
    xModifierFunction = xPerspModifier
    yModifierFunction = yPerspModifier
    global perspDict
    perspDict = {'fov':fov, 'near':near, 'far':far}
    global projFlag
    projFlag = True

def gtBeginShape():
    global vertexList
    vertexList = []
    global allowDraw
    allowDraw = True
    
def gtEndShape():
    global vertexList
    print vertexList
    
    if allowDraw == False:
        return
    
    for i in range(0, len(vertexList), 2):
        # point1 = vertexList[i]
        # point2 = vertexList[i+1]
        p1X = vertexList[i][0]
        p1Y = vertexList[i][1]
        p1Z = vertexList[i][2]
        p2X = vertexList[i+1][0]
        p2Y = vertexList[i+1][1]
        p2Z = vertexList[i+1][2]
        
        p1trans = coordinateTransformer(p1X, p1Y, p1Z)
        p2trans = coordinateTransformer(p2X, p2Y, p2Z)
        
        p1X = p1trans[0]
        p1Y = p1trans[1]
        p1Z = p1trans[2]
        p2X = p2trans[0]
        p2Y = p2trans[1]
        p2Z = p2trans[2]
        
        if projFlag == False:
            # print "(" + str(p1X) + ", " + str(p1Y) + ") (" + str(p2X) + ", " + str(p2Y) + ")"
            p1X = xOrthoModifier(p1X, orthoDict['left'], orthoDict['right'])
            p1Y = yOrthoModifier(p1Y, orthoDict['bottom'], orthoDict['top'])
            p2X = xOrthoModifier(p2X, orthoDict['left'], orthoDict['right'])
            p2Y = yOrthoModifier(p2Y, orthoDict['bottom'], orthoDict['top'])
            # print "(" + str(p1X) + ", " + str(p1Y) + ") (" + str(p2X) + ", " + str(p2Y) + ")"
            line(p1X, p1Y, p2X, p2Y)
        elif projFlag == True:
            p1X = xPerspModifier(p1X, p1Z, perspDict['fov'])
            p1Y = yPerspModifier(p1Y, p1Z, perspDict['fov'])
            p2X = xPerspModifier(p2X, p2Z, perspDict['fov'])
            p2Y = yPerspModifier(p2Y, p2Z, perspDict['fov'])
            print "(" + str(p1X) + ", " + str(p1Y) + ") (" + str(p2X) + ", " + str(p2Y) + ")"
            line(p1X, p1Y, p2X, p2Y)
    
    vertexList = []
    global allowDraw
    allowDraw = False
    print vertexList

def gtVertex(x, y, z):
    global vertexList
    if allowDraw == True: 
        vertexList.append((x, y, z))