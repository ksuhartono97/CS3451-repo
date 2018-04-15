# Sample program for the mesh subdivision project

rotate_flag = True    # automatically rotate the model?
time = 0              # time, for automatic rotation of object

# initalize project
def setup():
    size (600, 600, OPENGL)
    noStroke()

# draw the current polygon mesh
def draw():
    global time
    
    background(0)    # clear screen

    perspective (PI*0.333, 1.0, 0.01, 1000.0)
    camera (0, 0, 5, 0, 0, 0, 0, 1, 0)    # place camera in the scene
    scale (1, -1, 1)    # change to using a right-handed coordinate system
    
    # ambient light source
    ambientLight (102, 102, 102)
  
    # two directional light sources
    lightSpecular (204, 204, 204)
    directionalLight (102, 102, 102, -0.7, -0.7, -1)
    directionalLight (152, 152, 152, 0, 0, -1)
    
    pushMatrix();

    fill (50, 50, 200)            # polygon color
    ambient (200, 200, 200)
    specular (0, 0, 0)            # no shiny highlights
    shininess (1.0)
  
    rotate (time, 1.0, 0.0, 0.0)

    # THIS IS WHERE YOU SHOULD DRAW THE MESH
  
    # place-holder polygon
    beginShape()
    normal (0.0, 0.0, 1.0)
    vertex (-1.0, -1.0, 0.0)
    vertex ( 1.0, -1.0, 0.0)
    vertex ( 1.0,  1.0, 0.0)
    vertex (-1.0,  1.0, 0.0)
    endShape(CLOSE)
    
    popMatrix()
    
    # step forward in time (object rotation)
    if rotate_flag:
        time += 0.02

# process a key press
def keyPressed():
    global rotate_flag
    if key == ' ':
        rotate_flag = not rotate_flag
    elif key == '1':
        read_mesh ('tetra.ply')
    elif key == '2':
        read_mesh ('octa.ply')
    elif key == '3':
        read_mesh ('icos.ply')
    elif key == '4':
        read_mesh ('star.ply')
    elif key == '5':
        read_mesh ('torus.ply')
    elif key == 'n':
        pass  # toggle per-vertex shading
    elif key == 's':
        pass  # do Loop subdivision
    elif key == 'q':
        exit() # quit the program

# read in a mesh from a file (YOU NEED TO MODIFY THIS !!!)
def read_mesh(filename):

    fname = "data/" + filename
    # read in the lines of a file
    with open(fname) as f:
        lines = f.readlines()
        
    # determine number of vertices (first line)
    words = lines[0].split()
    num_vertices = int(words[1])
    print "number of vertices =", num_vertices

    # determine number of faces (second line)
    words = lines[1].split()
    num_faces = int(words[1])
    print "number of faces =", num_faces

    # read the vertices
    for i in range(num_vertices):
        words = lines[i+2].split()
        x = float(words[0])
        y = float(words[1])
        z = float(words[2])
        print "vertex = ", x, y, z
    
    # read the faces
    for i in range(num_faces):
        j = i + num_vertices + 2
        words = lines[j].split()
        nverts = int(words[0])
        if nverts != 3:
            print "error: face is not a triangle"
            exit()
        
        index1 = int(words[1])
        index2 = int(words[2])
        index3 = int(words[3])
        print "face =", index1, index2, index3

