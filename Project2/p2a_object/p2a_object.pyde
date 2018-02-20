# Animation Example

time = 0   # use time to move objects from one frame to the next

def setup():
    size (800, 800, P3D)
    perspective (60 * PI / 180, 1, 0.1, 1000)  # 60 degree field of view
    
def draw():
    global time
    time += 0.01

    camera (0, 0, 100, 0, 0, 0, 0,  1, 0)  # position the virtual camera

    background (255, 255, 255)  # clear screen and set background to white
    
    # create a directional light source
    ambientLight(50, 50, 50);
    lightSpecular(255, 255, 255)
    directionalLight (100, 100, 100, -0.3, 0.5, -1)
    
    noStroke()
    specular (180, 180, 180)
    shininess (15.0)
    
    #Main Body
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    scale(1.4, 1.2, 0.9)
    sphereDetail(60)
    sphere(20)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    rotateY(time)
    translate(0, 0, 16)
    scale(1, 1, 1)
    box(5)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    rotateY(time)
    translate(-2.5, -1.5, 15.5)
    scale(0.8, 0.8, 1)
    box(5)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    rotateY(time)
    translate(-6, -3, 15.5)
    scale(0.6, 0.6, 1)
    box(5)
    popMatrix()
    
    pushMatrix()
    rotateY(time)
    translate(2.5, -1.5, 15.5)
    scale(0.8, 0.8, 1)
    box(5)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    rotateY(time)
    translate(6, -3, 15.5)
    scale(0.6, 0.6, 1)
    box(5)
    popMatrix()
    
    #Head
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(0, -10, 0)
    scale(0.9, 1.05, 0.8)
    sphereDetail(60)
    sphere(20)
    popMatrix()
    
    ## Hair
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(-10.5, -12, 15)
    rotateX(radians(35))
    rotateZ(radians(-15))
    scale(0.3, 2, 0.3)
    box(5)
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(-12, -12, 14)
    rotateX(radians(35))
    rotateZ(radians(5))
    scale(0.2, 2, 0.2)
    box(5)
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(10.5, -12, 15)
    rotateX(radians(35))
    rotateZ(radians(15))
    scale(0.3, 2, 0.3)
    box(5)
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(12, -12, 14)
    rotateX(radians(35))
    rotateZ(radians(-5))
    scale(0.2, 2, 0.2)
    box(5)
    popMatrix()
    
    # Mouth
    fill(255,224,189)
    pushMatrix()
    rotateY(time)
    translate(0, -14.5, 12.58)
    scale(10, 3, 3)
    rotateX(radians(10))
    cylinder()
    popMatrix()
    
    fill(255,205,148)
    pushMatrix()
    rotateY(time)
    translate(0, -15, 14.8)
    scale(8, 1, 1)
    rotateX(radians(12))
    cylinder()
    popMatrix()
    
    fill(0,0,0)
    pushMatrix()
    rotateY(time)
    translate(0, -17, 15.3)
    rotateX(radians(12))
    box(1)
    popMatrix()
    
    
    
    ## Eyes
    fill(255, 255, 255)
    pushMatrix()
    rotateY(time)
    translate(-6.5, -19.5, 10.6)
    scale(0.18, 0.15, 0.15)
    sphereDetail(60)
    sphere(24)
    popMatrix()
    
    fill(255, 255, 255)
    pushMatrix()
    rotateY(time)
    translate(6.5, -19.5, 10.6)
    scale(0.18, 0.15, 0.15)
    sphereDetail(60)
    sphere(24)
    popMatrix()
    
    fill(0, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(-7, -20, 12)
    scale(0.1, 0.1, 0.1)
    sphereDetail(60)
    sphere(30)
    popMatrix()
    
    fill(0, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(7, -20, 12)
    scale(0.1, 0.1, 0.1)
    sphereDetail(60)
    sphere(30)
    popMatrix()
    
    #Legs
    pushMatrix()
    fill(255, 0, 0)
    rotateY(time)
    translate(13, 20, 0)
    scale(4, 8, 4)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    pushMatrix()
    fill(255, 0, 0)
    rotateY(time)
    translate(-13, 20, 0)
    scale(4, 8, 4)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    pushMatrix()
    fill(255, 0, 0)
    rotateY(time)
    translate(13, 25, 0)
    scale(2, 8, 2)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    pushMatrix()
    fill(255, 0, 0)
    rotateY(time)
    translate(-13,25, 0)
    scale(2, 8, 2)
    rotateX(radians(90))
    cylinder()
    popMatrix()
    
    
    # Feet
    
    pushMatrix()
    fill(255, 255, 0)
    rotateY(time)
    translate(-13,33, 0.7)
    scale(0.62, 0.62, 0.8)
    box(8)
    popMatrix()
    
    pushMatrix()
    fill(255, 0, 0)
    rotateY(time)
    translate(-13,33, 4)
    scale(0.6, 0.6, 1.6)
    box(8)
    popMatrix()
    
    pushMatrix()
    fill(0, 255, 0)
    rotateY(time)
    translate(-13,31, 0.7)
    scale(0.62, 0.12, 0.8)
    box(8)
    popMatrix()
    
    #Right
    pushMatrix()
    fill(255, 255, 0)
    rotateY(time)
    translate(13,33, 0.7)
    scale(0.62, 0.62, 0.8)
    box(8)
    popMatrix()
    
    pushMatrix()
    fill(255, 0, 0)
    rotateY(time)
    translate(13,33, 4)
    scale(0.6, 0.6, 1.6)
    box(8)
    popMatrix()
    
    pushMatrix()
    fill(0, 255, 0)
    rotateY(time)
    translate(13,31, 0.7)
    scale(0.62, 0.12, 0.8)
    box(8)
    popMatrix()
    
    
    #Arms
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(20, -13, 0)
    rotateY(radians(90))
    scale(3.5, 3.5 ,14)
    cylinder()
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(33.5, -13, 0)
    scale(0.89, 0.89, 0.89)
    sphere(4)
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(37.8, -9.5, 0)
    rotateZ(radians(45))
    rotateY(radians(90))
    scale(2.8, 2.8 ,6)
    cylinder()
    popMatrix()
    
    #Left Arm
    
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(-20, -13, 0)
    rotateY(radians(90))
    scale(3.5, 3.5 ,14)
    cylinder()
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(-33.5, -13, 0)
    scale(0.89, 0.89, 0.89)
    sphere(4)
    popMatrix()
    
    fill(255, 0, 0)
    pushMatrix()
    rotateY(time)
    translate(-37.8, -9.5, 0)
    rotateZ(radians(-45))
    rotateY(radians(90))
    scale(2.8, 2.8 ,6)
    cylinder()
    popMatrix()
    
    ## Hands
    #Left
    fill(255, 255, 255)
    pushMatrix()
    rotateY(time)
    translate(-41.4, -5.8, 0)
    rotateZ(radians(30))
    scale(1.5, 2, 1.5)
    sphere(2)
    popMatrix()
    
    pushMatrix()
    rotateY(time)
    translate(-44, -5.3, 1.2)
    rotateZ(radians(30))
    scale(0.3, 1.5, 0.3)
    box(4)
    popMatrix()
    
    pushMatrix()
    rotateY(time)
    translate(-44, -5.3, -1.2)
    rotateZ(radians(30))
    scale(0.3, 1.5, 0.3)
    box(4)
    popMatrix()
    
    #Right
    fill(255, 255, 255)
    pushMatrix()
    rotateY(time)
    translate(41.4, -5.8, 0)
    rotateZ(radians(-30))
    scale(1.5, 2, 1.5)
    sphere(2)
    popMatrix()
    
    pushMatrix()
    rotateY(time)
    translate(44, -5.3, 1.2)
    rotateZ(radians(-30))
    scale(0.3, 1.5, 0.3)
    box(4)
    popMatrix()
    
    pushMatrix()
    rotateY(time)
    translate(44, -5.3, -1.2)
    rotateZ(radians(-30))
    scale(0.3, 1.5, 0.3)
    box(4)
    popMatrix()
    
    # fill(255, 0, 0)
    # pushMatrix()
    # # rotateY(time)
    # rotateY(90)
    # translate(-20, -10, 0)
    # # scale(3.5, 3.5, 15)
    # cylinder()
    # popMatrix()
    
    
    
    # red box
    # fill (255, 0, 0)
    # pushMatrix()
    # translate (-30, 0, 0)
    # rotateX (time)
    # box(20)
    # popMatrix()

    # green sphere
    # fill (0, 250, 0)
    # pushMatrix()
    # translate (0, 8 * sin(4 * time), 0)  # move up and down
    # sphereDetail(60)  # this controls how many polygons are used to make a sphere
    # sphere(10)
    # popMatrix()

    # blue cylinder
    # fill (0, 0, 255)
    # pushMatrix()
    # translate (30, 0, 0)
    # rotateX (-time)
    # scale (10, 10, 10)
    # cylinder()
    # popMatrix()

# cylinder with radius = 1, z range in [-1,1]
def cylinder(sides = 64):
    # first endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, -1)
    endShape(CLOSE)
    # second endcap
    beginShape()
    for i in range(sides):
        theta = i * 2 * PI / sides
        x = cos(theta)
        y = sin(theta)
        vertex ( x,  y, 1)
    endShape(CLOSE)
    # sides
    x1 = 1
    y1 = 0
    for i in range(sides):
        theta = (i + 1) * 2 * PI / sides
        x2 = cos(theta)
        y2 = sin(theta)
        beginShape()
        normal (x1, y1, 0)
        vertex (x1, y1, 1)
        vertex (x1, y1, -1)
        normal (x2, y2, 0)
        vertex (x2, y2, -1)
        vertex (x2, y2, 1)
        endShape(CLOSE)
        x1 = x2
        y1 = y2