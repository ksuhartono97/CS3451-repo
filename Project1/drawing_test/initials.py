# In the routine below, you should draw your initials in perspective

from matlib import *
from drawlib import *

def persp_initials():
    gtInitialize()
    gtPerspective (60, -100, 100)
    gtPushMatrix()
    gtTranslate(0, 0, -4)
    gtRotateX(-60)
    ### 
    gtBeginShape()
    #K
    gtVertex (-1.0, -1.0,  0.0)
    gtVertex (-1.0,  1.0,  0.0)
    
    gtVertex (-1.0, 0.0,  0.0)
    gtVertex (0.0, 1.0,  0.0)
    
    gtVertex (-1.0, 0.0,  0.0)
    gtVertex (0.0, -1.0,  0.0)
    
    #S
    gtVertex(1.0, 1.0, 0.0)
    gtVertex(0.0, 1.0, 0.0)
    
    gtVertex(0.0, 1.0, 0.0)
    gtVertex(0.0, 0.0, 0.0)
    
    gtVertex(0.0, 0.0, 0.0)
    gtVertex(1.0, 0.0, 0.0)
    
    gtVertex(1.0, 0.0, 0.0)
    gtVertex(1.0, -1.0, 0.0)
    
    gtVertex(1.0, -1.0, 0.0)
    gtVertex(0.0, -1.0, 0.0)
    
    gtEndShape()
    ### 
    gtPopMatrix()