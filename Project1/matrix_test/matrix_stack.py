# Matrix Stack Library

# you should modify the routines below to complete the assignment
matrixStack = []
ctm = [[0 for i in range(4)] for j in range(4)]

def gtInitialize():
    global ctm
    global matrixStack
    matrixStack = []
    ctm = [[0 for i in range(4)] for j in range(4)]
    ctm[0][0] = 1
    ctm[1][1] = 1
    ctm[2][2] = 1
    ctm[3][3] = 1
    gtPushMatrix()

def gtPushMatrix():
    global matrixStack
    matrixStack.append(ctm)

def gtPopMatrix():
    global matrixStack
    global ctm
    if len(matrixStack) == 1:
       print "cannot pop the matrix stack"
    else:
        ctm = matrixStack.pop()

def gtTranslate(x, y, z):
    global ctm
    transMtx = [[0 for g in range(4)] for h in range(4)]
    transMtx[0][3] = x
    transMtx[1][3] = y
    transMtx[2][3] = z
    transMtx[0][0] = 1
    transMtx[1][1] = 1
    transMtx[2][2] = 1
    transMtx[3][3] = 1
    
    newCtm = [[0 for a in range(4)] for b in range(4)]
    for j in range(len(newCtm[0])): #j is y
        for i in range(len(newCtm)): #i is x
            for k in range(4):
                newCtm[j][i] += ctm[j][k] * transMtx[k][i]            
    ctm = newCtm[:]
    
def gtScale(x, y, z):
    global ctm
    scaleMtx = [[0 for g in range(4)] for h in range(4)]
    scaleMtx[0][0] = x
    scaleMtx[1][1] = y
    scaleMtx[2][2] = z
    scaleMtx[3][3] = 1
    
    newCtm = [[0 for a in range(4)] for b in range(4)]
    for j in range(len(newCtm[0])): #j is y
        for i in range(len(newCtm)): #i is x
            for k in range(4):
                newCtm[j][i] += ctm[j][k] * scaleMtx[k][i]            
    ctm = newCtm[:]


def gtRotateX(theta):
    global ctm
    radTheta = 2*PI*theta/360
    rotMtx = [[0 for g in range(4)] for h in range(4)]
    rotMtx[0][0] = 1
    rotMtx[1][1] = cos(radTheta)
    rotMtx[2][1] = sin(radTheta)
    rotMtx[1][2] = -sin(radTheta)
    rotMtx[2][2] = cos(radTheta)
    rotMtx[3][3] = 1
    
    newCtm = [[0 for a in range(4)] for b in range(4)]
    for j in range(len(newCtm[0])): #j is y
        for i in range(len(newCtm)): #i is x
            for k in range(4):
                newCtm[j][i] += ctm[j][k] * rotMtx[k][i]            
    ctm = newCtm[:]

def gtRotateY(theta):
    global ctm
    radTheta = 2*PI*theta/360
    rotMtx = [[0 for g in range(4)] for h in range(4)]
    rotMtx[0][0] = cos(radTheta)
    rotMtx[2][0] = -sin(radTheta)
    rotMtx[1][1] = 1
    rotMtx[0][2] = sin(radTheta)
    rotMtx[2][2] = cos(radTheta)
    rotMtx[3][3] = 1
    
    newCtm = [[0 for a in range(4)] for b in range(4)]
    for j in range(len(newCtm[0])): #j is y
        for i in range(len(newCtm)): #i is x
            for k in range(4):
                newCtm[j][i] += ctm[j][k] * rotMtx[k][i]            
    ctm = newCtm[:]

def gtRotateZ(theta):
    global ctm
    radTheta = 2*PI*theta/360
    rotMtx = [[0 for g in range(4)] for h in range(4)]
    rotMtx[0][0] = cos(radTheta)
    rotMtx[0][1] = -sin(radTheta)
    rotMtx[1][0] = sin(radTheta)
    rotMtx[1][1] = cos(radTheta)
    rotMtx[2][2] = 1
    rotMtx[3][3] = 1
    
    newCtm = [[0 for a in range(4)] for b in range(4)]
    for j in range(len(newCtm[0])): #j is y
        for i in range(len(newCtm)): #i is x
            for k in range(4):
                newCtm[j][i] += ctm[j][k] * rotMtx[k][i]            
    ctm = newCtm[:]

def gtGetMatrix():
    return ctm

def print_ctm():
    mat =  gtGetMatrix()
    for i in range(len(mat)):
        print mat[i]
    print ""
