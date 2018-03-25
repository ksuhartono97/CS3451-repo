# This is the starter code for the CS 3451 Ray Tracing project.
#
# Kristian Suhartono
#
# The most important part of this code is the interpreter, which will
# help you parse the scene description (.cli) files.

def setup():
    size(300, 300) 
    noStroke()
    colorMode(RGB, 1.0)  # Processing color values will be in [0, 1]  (not 255)
    background(0, 0, 0)

class Scene:
    backgroundR = 0
    backgroundG = 0
    backgroundB = 0
    fovAngle = 0
    def __init__(self, r, g, b, a):
        self.backgroundR = r
        self.backgroundG = g
        self.backgroundB = b
        self.fovAngle = a
        
    def setBackgroundRGB(self, r, g, b):
        self.backgroundR = r
        self.backgroundG = g
        self.backgroundB = b
        print str(self.backgroundR) + "  " + str(self.backgroundG) + " " + str(self.backgroundB)
        
    def setFovAngle(self, a):
        self.fovAngle = a
        print self.fovAngle
    
class Light:
    lightSources = []
    def __init__(self):
        self.lightSources = []
        
    def addLightSource(self, r, g, b ,x, y, z):
        light = [r, g, b ,x, y, z]
        self.lightSources.append(light)
        print light
        print len(self.lightSources)
        
class Surface:
    Car = 0
    Cag = 0
    Cab = 0
    Cdr = 0
    Cdg = 0
    Cdb = 0
    Csr = 0
    Csg = 0
    Csb = 0
    P = 0
    Krefl = 0
    
    def __init__(self, Car, Cag, Cab, Cdr, Cdg, Cdb, Csr, Csg, Csb, P, Krefl):
        self.Car = Car
        self.Cag = Cag
        self.Cab = Cab
        self.Cdr = Cdr
        self.Cdg = Cdg
        self.Cdb = Cdb
        self.Csr = Csr
        self.Csg = Csg
        self.Csb = Csb
        self.P = P
        self.Krefl = Krefl
        print "surface object created"
        
class Sphere:
    x = 0
    y = 0
    z = 0
    radius = 0
    surface = None
    def __init__(self, x, y, z, radius):
        self.x = x
        self.y = y
        self.z = z
        self.radius = radius
        self.surface = None
        # print "sphere created"
    
    def assignSurface(self, surface):
 
        self.surface = surface
    
class Ray:
    origin = None
    direction = None
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction
    
class Hit:
    t = 0
    position = None
    object = None
    def __init__(self, t, position, object):
        self.t = t
        self.position = position
        self.object = object
    
scene = None
light = None
surfaces = None
latestSurfaceIndex = -1 
objects = None

def checkSphereIntersection(ray, s):
    dx = ray.direction.x - ray.origin.x
    dy = ray.direction.y - ray.origin.y
    dz = ray.direction.z - ray.origin.z
    
    a = dx*dx + dy*dy + dz*dz
    b = 2*dx*(ray.origin.x - s.x) + 2*dy*(ray.origin.y - s.y) + 2*dz*(ray.origin.z - s.z)
    c = s.x*s.x + s.y*s.y + s.z*s.z + ray.origin.x*ray.origin.x + ray.origin.y*ray.origin.y + ray.origin.z*ray.origin.z + (-2)*(s.x*ray.origin.x + s.y*ray.origin.y + s.z*ray.origin.z) - s.radius*s.radius
    
    d = (b*b) - (4*a*c)
    
    if d < 0:
        return None
    else:
        t = (-b - sqrt((b*b) - (4*a*c))) / 2 * a
        intX = ray.origin.x + t * dx
        intY = ray.origin.y + t * dy
        intZ = ray.origin.z + t * dz
        
        intersectionPoint = PVector(intX, intY, intZ)
        
        hitObj = Hit(t, intersectionPoint, s)
        return hitObj

# read and interpret the appropriate scene description .cli file based on key press
def keyPressed():
    if key == '1':
        interpreter("i1.cli")
    elif key == '2':
        interpreter("i2.cli")
    elif key == '3':
        interpreter("i3.cli")
    elif key == '4':
        interpreter("i4.cli")
    elif key == '5':
        interpreter("i5.cli")
    elif key == '6':
        interpreter("i6.cli")
    elif key == '7':
        interpreter("i7.cli")
    elif key == '8':
        interpreter("i8.cli")
    elif key == '9':
        interpreter("i9.cli")
    elif key == '0':
        interpreter("i10.cli")

def interpreter(fname):
    global scene
    global light
    global objects
    global latestSurfaceIndex
    global surfaces
    scene = Scene(0, 0, 0, 0)
    light = Light()
    objects = []
    latestSurfaceIndex = -1
    surfaces = []
    
    fname = "data/" + fname
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()

    # parse each line in the file in turn
    for line in lines:
        words = line.split()  # split the line into individual tokens
        if len(words) == 0:   # skip empty lines
            continue
        if words[0] == 'sphere':
            x = float(words[1])
            y = float(words[2])
            z = float(words[3])
            radius = float(words[4])
            global latestSurfaceIndex
            global surfaces
            global objects
            newS = Sphere(x, y, z, radius)
            newS.assignSurface(surfaces[latestSurfaceIndex])
            objects.append(newS)
            print objects
            # call your sphere creation routine here
            # for example: create_sphere(x,y,z,radius)
        elif words[0] == 'fov':
            angle = float(words[1])
            global scene
            scene.setFovAngle(angle)
        elif words[0] == 'background':
            r = float(words[1])
            g = float(words[2])
            b = float(words[3])
            scene.setBackgroundRGB(r, g, b)
        elif words[0] == 'light':
            r = float(words[1])
            g = float(words[2])
            b = float(words[3])
            x = float(words[4])
            y = float(words[5])
            z = float(words[6])
            global light
            light.addLightSource(r, g, b, x, y, z)
        elif words[0] == 'surface':
            Car = float(words[1])
            Cag = float(words[2])
            Cab = float(words[3])
            Cdr = float(words[4])
            Cdg = float(words[5])
            Cdb = float(words[6])
            Csr = float(words[7])
            Csg = float(words[8])
            Csb = float(words[9])
            P = float(words[10])
            Krefl = float(words[11])
            
            global surfaces
            surfaces.append(Surface(Car, Cag, Cab, Cdr, Cdg, Cdb, Csr, Csg, Csb, P, Krefl))
            latestSurfaceIndex = latestSurfaceIndex + 1
        elif words[0] == 'cylinder':
            pass
        elif words[0] == 'write':
            render_scene()    # render the scene
            save(words[1])    # write the image to a file
            pass

# render the ray tracing scene
def render_scene():
    for j in range(height):
        for i in range(width):
            # Conversion to 3D Perspective Point
            global scene
            
            theta = 2*PI*scene.fovAngle/float(360)
            k = tan(theta/2)
            
            x3d = ((i * (2*k) / width) - k) * abs(-1)
            y3d = (((height - j) * (2*k) / height) - k) * abs(-1)
            
            eyeRayDir = PVector(x3d, y3d, -1)
            eyeRayDir = eyeRayDir.normalize()
            ray = Ray(PVector(0, 0, 0), eyeRayDir)
            
            # Detect Intersection
            global objects
            hitArr = []
            for object in objects:
                hitArr.append(checkSphereIntersection(ray, object))
            
            t = sys.maxint
            finalHit = None
            # print hitArr
            for item in hitArr:
                if item != None:
                    if item.t < t and item.t >= 0:
                        finalHit = item
            
            pixCol = PVector(0, 0, 0)
            if finalHit != None:
                surfaceCol = PVector(finalHit.object.surface.Cdr, finalHit.object.surface.Cdg, finalHit.object.surface.Cdb)
                pixCol = surfaceCol
                N = PVector((finalHit.position.x - finalHit.object.x)/finalHit.object.radius, (finalHit.position.y - finalHit.object.y)/finalHit.object.radius, (finalHit.position.z - finalHit.object.z)/finalHit.object.radius)
                global light
                lvecs = PVector(0.0, 0.0, 0.0)
                for l in light.lightSources:
                    lPos = PVector(l[3], l[4], l[5])
                    lVec = (lPos - finalHit.position).normalize()
                    lCol = PVector(l[0], l[1], l[2])
                    lVecContrib = lCol * max(0, N.dot(lVec))
                    lvecs = lvecs + lVecContrib
                
                pixCol = PVector(surfaceCol.x * lvecs.x, surfaceCol.y * lvecs.y, surfaceCol.z * lvecs.z)
            else:
                global scene
                pixCol = PVector(scene.backgroundR, scene.backgroundG, scene.backgroundB)
            
            # print pixCol
            
            # create an eye ray for pixel (i,j) and cast it into the scene
            pix_color = color(pixCol.x, pixCol.y, pixCol.z)  # you should calculate the correct pixel color here
            set (i, j, pix_color)         # fill the pixel with the calculated color
    print "done"

# should remain empty for this assignment
def draw():
    pass
    