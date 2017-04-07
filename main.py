"""
##########################################
Rosie Sun
15-112
Term Project - Starry Night

Module: 
Processing
###########################################

"""

add_library('beads')
add_library('sound')

from cluster import UpperWaves, LowerWaves
from vfield import VectorField, VF2
from dots import Dot
from plant import Plant
from piece import Piece
from splashElement import Element
from pen import Pen
from smoke import Smoke
from button import Button
from star import Star

"""
MAIN FUNCTIONS:
    
"""

def setup():
    #init splash screen
    size(640, 440, P3D)
    colorMode(RGB, 255)
    smooth()
    noStroke()
    global bg, paintmode
    paintmode = "Stroke"
    #load sound and backgdround image
    song = SoundFile(this, "music.mp3")
    ###########################################
    """
    background music:
    https://www.youtube.com/watch?v=se6LI8e9DAU    
    """
    ###########################################
    bg =  loadImage("bg2.jpg")
    song.play()
    initSplash()
    initPosList()

def initPosList():
    #initial positions to store for later to animate the painting mode
    global poslist
    global firstpos, secondpos, lines
    firstpos = []
    secondpos = []
    lines = []
    poslist = []
    
def draw(): 
    global mode
    #similar to redrawall(), constantly redraw every frame
    if mode == "puzzle":
        pushMatrix()
        drawPuzzle()
        popMatrix()
    elif mode == "splash":
        pushMatrix()
        drawSplash()
        popMatrix()
    elif mode == "animation":
        pushMatrix()
        drawAnimation()
        #drawSphere()
        popMatrix()
    elif mode == "paint":
        pushMatrix()
        drawPaint()
        popMatrix()
    elif mode == "move":
        pushMatrix()
        strokeWeight(1)
        background(0)
        #initbackground()
        initCanvas()
        drawMove()
        popMatrix()

"""
CONTROLLS
"""

def keyPressed():
    #key control for changing scenes, and animation
    global mode
    #initbackground()
    if mode == "paint":
        if key == ENTER:
            initCurve()
            initStarObject()
            mode = "move"
    elif mode == "animation":
        if key == ENTER:
            resetP()
            mode = "splash"
    if mode == "move":
        if key == BACKSPACE:
            background(0)
            initSplash()
            mode = "splash"

def mouseClicked():
    global mode, ctYellow, ctUpper, ctLower
    #control to animate stars
    if mode == "animation":
        yellowBound = (0, 290, width, 375)
        upperBound = (0, 0, width, 290)
        lowerBound= (0, 290, width, height)
        mousePos = mouseX, mouseY
        if inboundRec(mousePos, yellowBound):
            ctYellow = True
        if inboundRec(mousePos, upperBound):
            ctUpper = True
        if inboundRec(mousePos, lowerBound):
            ctLower = True
    elif mode == "move" or mode == "paint":
        pos = mouseX, mouseY
        updatescreen(pos)
            
def mousePressed():
    global mode, paintmode
    if mode =="puzzle":
        #use reversed so we click the one on top
        for piece in reversed(unsolved):
            if piece.containspoint(mouseX, mouseY):
                piece.locked = True
                piece.xoffset = mouseX - piece.pos[0]
                piece.yoffset = mouseY - piece.pos[1]
                break
    if mode == "splash":
        #check the first button
        cx, cy = 200, 300
        x0, y0, x1, y1 = cx-30, cy-30, cx+30, cy+30
        if x0 < mouseX < x1 and y0 < mouseY < y1:
            mode = "puzzle"
            initPuzzle()
        #2nd button
        cx2, cy2 = 420, 300
        x00, y00, x11, y11 = cx2-30, cy2-30, cx2+30, cy2+30
        if x00 < mouseX < x11 and y00 < mouseY < y11:
            mode = "paint"
            background(0)
            initCanvas()
        else:
            pass
    elif mode == "paint":
        global firstpos, secondpos, lines
        x, y = mouseX, mouseY
        #updatecolors((x, y))
        pos = (x,y)
        updates(pos)
        if paintmode == "Line":
            firstpos.append((x, y))

def mouseReleased():
    global mode, strokecolor, weight, paintmode
    if mode == "puzzle":
        for piece in unsolved:
            if piece.locked:
                piece.locked = False
                piece.xoffset, piece.yoffset = None, None
        #offsets = relative position from edge to mouse
    #lalala
    if mode == "paint":
        global secondpos, firstpos, lines
        if len(firstpos) != 0 and paintmode == "Line":
            (x, y)= mouseX, mouseY
            secondpos.append((x, y))
            (initx, inity) = firstpos[-1]
            (thisx, thisy) = secondpos[-1]
            #store the value of lines so we can move them later
            pos = (initx, inity, thisx, thisy)
            thiscol = strokecolor
            thisweight = weight
            addLine(pos, thiscol, thisweight*1.4)

def addLine(thispos, thiscol, thisweight):
    global lines
    newLine = LineSeg(thispos, thiscol, thisweight)
    lines.append(newLine)

def mouseDragged():
    #detect mouse motion for puzzle movement
    global unsolved, mode, solved, firstpos
    if mode == "puzzle":
        for piece in unsolved:
            if piece.locked:
                piece.update()
                updateScene(unsolved, solved)
            
def inboundRec(mousePos, bound):
    #helper function that determine the position of mouse
    (x0, y0, x1, y1) = bound
    mouseposX, mouseposY = mousePos
    if x0 < mouseposX < x1 and y0 < mouseposY < y1:
        return True  

def initCurve():
    global step, frames, edge, maxY, theta
    maxY = 20
    frames = 120
    edge = -80
    step = 1
    theta = 0.0

def resetP():
    #change of perspective to standard view
    #reference see https://github.com/processing/processing-docs/issues/71
    aspect = float(width)/float(height)
    fov = PI/3.0;
    cameraZ = (height/2.0) / tan(PI*60.0/360.0);
    perspective(fov, aspect, cameraZ/10.0, cameraZ*10.0)

"""
1. SPLASH SCREEN 
"""

def initSplash():
    #starting function to set splash screen
    global mode, bg
    mode = "splash"
    noStroke()
    global elems
    lenOfelems = 40
    elems = []
    for i in range(lenOfelems):
        x = random(0, width)
        y = random(0, height)
        loc = (x, y)
        elemSize = random(12, 24)
        col = setInitColor()
        angle = random(PI*2)
        #element is the circular particles that animate at the background
        new = Element(col, loc, elemSize, angle)
        elems.append(new)
    #create titles and buttons
    initFont()
    initButton()

def initStarObject():
    global stars
    stars = []
    num = 10 
    for i in range(num):
        #light blue colors
        r = random(240, 255)
        g = random(210, 230)
        b = random(235, 255)
        a = random(10, 255)
        col = color(r, g, b, a)
        bx0, by0, bx1, by1 =  100, 40, 600, 400
        posx = random(bx0, bx1)
        posy = random(by0, by1/2)
        new = Star((posx, posy), col)
        stars.append(new)

def initFont():
    #set fonts
    global f1, f2, f3, f4
    f1 = createFont("Silom", 70)
    f2 = createFont("SignPainter-HouseScript", 25)
    f3 = createFont("Silom", 40)
    f4 = createFont("Optima", 18)
    
def initButton():
    #set buttons, pretty straight forward
    global button1, button2
    pos1 = (200, 300)
    pos2 = (420, 300)
    button1 = Button(pos1)
    button2 =  Button(pos2)
    
def drawMove():
    global poslist, mod, lines, stars
    if mode == "move":
        #detect shapes and animate accordingly
        noStroke()
        initCanvas()
        for i in range(len(poslist)):
            pos = poslist[i]
            pos.move()
            pos.display()
        for lineSeg in lines:
            lineSeg.move()
            lineSeg.display()
        drawMode()
        drawCurve()

def drawMode():
    global f4
    db2 = color(52, 86, 163)
    fill(color(255))
    textFont(f4)
    textAlign(CENTER, CENTER)
    posx, posy = width-100, height-20
    text("Strokes", posx, posy)
    #610-640, 420, 440
    #610-640, 420-440
    posx2, posy2 = width-30, height-20
    text("Lines", posx2, posy2)
    
def drawCurve():
    global step, frames, edge, maxY, theta, strokecolor
    fill(color(255, 250, 194))
    boardbound = 100, 40, 600, 400
    boardStart = x0, y0 = 100, 40
    noStroke()
    angle = 0
    offset = 10
    for i in range(boardStart[0]+offset, boardbound[2]-offset, step):
        y = 250 + map(sin(theta+angle), -1, 1, -maxY, maxY)
        sz= map(sin(theta+angle*2), -1, 1, 2, 4)
        rx = map(sin(theta+angle*3), -1, 1, -20, 40)
        r = map(sin(angle*2), -1, 1, PI/4, PI/2)
        pushMatrix();
        translate(i,y)
        rotate(r)
        ellipse(rx, 0, sz*2, sz*2)
        popMatrix()
        angle += (2*PI/width*step)
    theta -= PI*2 / frames

def cleanScreen():
    noStroke()
    boardbound = 100, 40, 600, 400
    boardStart = x0, y0 = 100, 40
    boardWid, boardHei = 500, 360
    bgcolor = color(22, 24, 70, 255)
    fill(bgcolor)
    h = 290
    rect(x0, y0, boardWid, h)
    
def drawSphere():
    #sphere objects
    global time, starSphere
    if mode == "animation":
        pushMatrix()
        rectMode(RADIUS)
        ellipseMode(RADIUS)
        strokeCap(ROUND)
        strokeWeight(2)
        rightHanded()
        with pushMatrix():
            noStroke()
            translate(0, 0, SphereRadius)
            rect(0, 0, width, height)
        time += timecount
        for t in starSphere:
            t.update(time, timecount, SphereRadius)
        popMatrix()
        
def rightHanded():
    #reset center pos
    rotateX(TAU / 2) 
    x,  y = 200, -100 
    translate(x, y, 0) 

def drawSmoke():
    #creating smoke objects in the puzzle scene
    global smokes
    for smoke in smokes:
        smoke.move()
        smoke.display()    

def drawSplash():
    pushMatrix()
    noStroke()
    global elems, button1, button2
    fill(94, 184, 219, 7)
    rect(0, 0, width, height)
    #display circular objects
    for elem in elems:
        elem.display()
    drawFont()
    button1.display()
    button2.display()
    popMatrix()

def drawFont():
    #draw titles on splash screen
    fill(255, 255, 255, 80)
    textFont(f1)
    textAlign(CENTER, CENTER)
    text("Starry Night", width/2, 150)
    textFont(f2)
    textAlign(CENTER, CENTER)
    text("by Rosie Sun", 500, 120)
    fill(255, 255, 255, 150)
    textFont(f3)
    textAlign(CENTER, CENTER)
    text("Create", 420, 350)
    textFont(f3)
    textAlign(CENTER, CENTER)
    text("Interact", 200, 350)


"""
2. PUZZLE PROGRAM
"""

def loadPuzzles():
    global images
    p1 = loadImage("p1.png")
    p2 = loadImage("p2.png")
    p3 = loadImage("p3.png")
    p4 = loadImage("p4.png")
    p5 = loadImage("p5.png")
    p6 = loadImage("p6.png")
    p7 = loadImage("p7.png")
    p8 = loadImage("p8.png")
    bg = loadImage("bg2.jpg")
    images = [p1,p2,p3,p4,p5,p6,p7,p8]

def initPuzzle():
    global unsolved, mode, solved, bg, images
    unsolved = []
    solved = []
    solvedcount = 0
    correctpos = []
    surface = p1
    boxsize = (width/4, height/2)
    for row in range(2):
        for col in range(4):
            wid = boxsize[0]*col
            hei = boxsize[1]*row
            correctpos.append((wid, hei))
    for i in range(8):
        posx = random(100, 200)
        posy = random(100, 200)
        initpos = (posx, posy)
        targetpos = correctpos[i]
        surface = images[i]
        #init pos: if pos= targetpos, this is solved!
        piece = Piece(initpos, targetpos, boxsize, surface)
        #first: all pieces are unsolved
        unsolved.append(piece)
    initSmoke()

def initSmoke():
    global smokes
    smokes = []
    for i in range(1000):
        vec = PVector(0, 0)
        velo = PVector(0, 0)
        siz = random(20, 30)
        #smoke has a velocity, size and direction
        smokes.append(Smoke(vec, velo, siz))

def updateScene(unsolved, solved):
    global mode
    for piece in unsolved:
        if piece.solved:
            solved.append(piece)
            i = unsolved.index(piece)
            unsolved.pop(i)
            if len(unsolved)== 0:
                #if we have solved all, jump to the next screen
                initAnimation()
                mode = "animation"

def drawPuzzle():
    global mode, solved, unsolved, bg
    if mode == "puzzle":
        pushMatrix()
        image(bg, 0, 0, width, height)
        for piece in solved:
            piece.display()
        for piece in unsolved:
            piece.move()
            piece.display()
        drawSmoke()
        popMatrix()


"""
4. ANIMATION PROGRAM
"""

def initAnimation():
    #set different parts of animation
    global bg, dotslist, yellowWaves, top, mid, plants
    global ctYellow, ctUpper, ctLower
    global rx1, rx2, rx3, ry1, ry2, ry3
    rx1, rx2, rx3, ry1, ry2, ry3 = 0, 0, 0, 0, 0, 0
    ctYellow, ctUpper, ctLower = False,False, False
    yellowWaves = initYellowWave()
    top, mid = initvecs()
    dotslist = initdots()
    plants = []
    plants = initplants(plants)
    #initStars()

def initStars():
    global starSphere, time, timecount, SphereRadius
    starSphere = []
    for i in range(80):
        y1 = color(229, 226, 173)
        y2 = color(234, 234, 226)
        y3 = color(255, 250, 194)
        y4 = color(240, 229, 163)
        colors = [y1,y2,y3,y4]
        colindex = int(random(4))
        thiscolor = colors[colindex]
        starSphere.append(Sphere(i * -100, thiscolor))
    time = 0
    timecount = 0.6 / 100.0  
    SphereRadius = 30
    
def drawAnimation():
    global mode,f4
    global ry, rx, dotslist, plants, yellowWaves, top, mid
    global ctYellow, ctUpper, ctLower
    if mode == "animation":
        strokeWeight(0 )
        pushMatrix()
        lights()
        #######################################################
        #change persepctive, see reference
        #https://processing.org/reference/perspective_.html
        cameraY = height / 2
        fov = mouseX / float(width) * PI / 2 
        if fov == 0:
            fov = .000001
        cameraZ = cameraY / tan(fov / 2)
        aspect = float(width) / float(height)
        perspective(fov, aspect, cameraZ / 2.0, cameraZ * 1.00001)
        #######################################################
        fill(10, 12, 57, 10)
        rect(0, 0, width, height)
        if ctUpper:
            displayVector(mid)
            displayVector(top)
        if ctUpper:
            displayDots(dotslist)
        if ctYellow:
            displayYellow(yellowWaves)
        displayMountains()
        displayPlants(plants)
        popMatrix() 

def initdots():
    # center circle, this is the sky
    dots1 = []
    for i in range(500):
        col = setcolor("lb")
        new = Dot(col, random(TWO_PI), random(TWO_PI), random(30, 140))
        dots1.append(new)
    dots2 = []
    for i in range(400):
        col = setcolor("db")
        new = Dot(col, random(TWO_PI), random(TWO_PI), random(30, 120))
        dots2.append(new)
    dots3 = []
    for i in range(200):
        col = setcolor("lb")
        new = Dot(col, random(TWO_PI), random(TWO_PI), random(30, 90))
        dots3.append(new)
    dotslist = [dots1, dots2, dots3]
    return dotslist
                
def initplants(plants):
    # init three groups of plants with different sizes
    for i in range(3):
        loc = PVector(random(170, 220), height)
        tall = int(random(80, 130))
        plants.append(Plant(loc, tall))
    for j in range(3):
        loc = PVector(random(120, 150), height)
        tall = int(random(40, 80))
        plants.append(Plant(loc, tall))
    for k in range(2):
        loc = PVector(random(220, 240), height)
        tall = int(random(40, 60))
        plants.append(Plant(loc, tall))
    return plants
    

def initYellowWave():
    #range, bound, angle, slope, num, colorange
    #fix yellow waves at the bottom
    #yellow wave bound(0, 290, width, 375)
    c1 = LowerWaves((-40, 330, 230, 370), (240, 375), PI / 20, 1.5, 130, "y")
    c2 = UpperWaves(
        (200, 300, width, 360), (width + 20, 290), -PI / 15, 2, 130, "y")
    return [c1, c2]

#display individual parts
def displayPlants(plants):
    for plant in plants:
        plant.display()

def displayVector(vectorlist):
    for vec in vectorlist:
        vec.display()
    
def displayYellow(yellowWaves):
    for yellowwave in yellowWaves:
        yellowwave.display()

def displayDots(dotslist):
    global rx1, rx2, rx3, ry1, ry2, ry3
    [dots1, dots2, dots3] = dotslist
    pushMatrix()
    ry1 -= 0.01
    rx1 -= 0.005
    r = 200
    translate(300, 180)
    rotateX(rx1)
    rotateY(ry1)
    for dotobject in dots1:
        dotobject.display()
    popMatrix()
    pushMatrix()
    ry2 -= 0.005
    rx2 -= 0.004
    r = 200
    translate(500, 90)
    rotateX(rx2)
    rotateY(ry2)
    for dotobject in dots2:
        dotobject.display()
    popMatrix()
    pushMatrix()
    ry3 -= 0.008
    rx3 -= 0.004
    r = 100
    translate(500, 220)
    rotateX(rx3)
    rotateY(ry3)
    for dotobject in dots3:
        dotobject.display()
    popMatrix()

def initvecs():
    #this is the flow of vectors
    # init blues
    v1 = (-0.5, -0.04)
    v0 = (0.4, -0.035)
    bound = (0, 200, 0, 150)
    top1 = VectorField(bound, 140, "db", v1)
    top2 = VectorField(bound, 140, "db", v0)
    bound2 = (100, 450, 5, 80)
    bound3 = (100, 450, 5, 60)
    top3 = VF2(bound2, 100, "db", v0)
    top4 = VF2(bound2, 40, "db", v1)
    # middlebound1
    vmid1 = (0.4, -0.1)
    mid1 = VectorField((0, 200, 150, 330), 150, "lb", vmid1)
    mid2 = VectorField((0, 200, 150, 330), 150, "lb", (-0.4, 0.1))
    top = [top1, top2, top3, top4]
    mid = [mid1, mid2]
    return top, mid

def displayMountains():
    # tutorial about drawing sin waves in processing:
    # https://www.youtube.com/watch?v=4v2NkbUJEks
    pushMatrix()
    maxnumber = 3
    for i in range(maxnumber):
        y = 30 * i
        fill(map(i, 0, 10, 20, 10), map(
            i, 0, 5, 20, 80), map(i, 0, 5, 100, 150))
        strokeWeight(0)
        stroke(0, map(i, 0, 5, 20, 150), map(i, 0, 5, 255, 150))
        beginShape()
        vertex(0, 200 + y)
        for j in range(0, width, 10):
            y2 = (350 + y + abs(sin(radians(j) + i)) *
                  cos(radians(i + j / 2)) * map(i, 7, 180, 40, 30))
            vertex(j, y2)
        v1, v2 = 800, 500
        vertex(v1, v2)
        v3, v4 = 0, 500
        vertex( v3, v4)
        endShape()
    popMatrix()

def setcolor(colorrange):
    # color selecting functions
    # darkblues
    db1 = color(40, 70, 140)
    db2 = color(52, 86, 163)
    db3 = color(70, 130, 180)
    db4 = color(65, 105, 225)
    db = [db1, db2, db3, db4]
    # lightblues
    lb1 = color(94, 184, 219)
    lb2 = color(93, 153, 187)
    lb3 = color(72, 92, 151)
    lb4 = color(117, 143, 170)
    lb = [lb1, lb2, lb3, lb4]
    # yellows
    y1 = color(229, 226, 173)
    y2 = color(234, 234, 226)
    y3 = color(255, 250, 194)
    y4 = color(240, 229, 163)
    y = [y1, y2, y3, y4]
    if colorrange == "db":
        listOfColor = db
    if colorrange == "lb":
        listOfColor = lb
    if colorrange == "y":
        listOfColor = y
    colind = int(random(4))
    thiscolor = listOfColor[colind]
    return thiscolor

"""
3. PAINT PROGRAM

"""

def initCanvas():
    #draw the canvas setting
    global weight, strokecolor, buttonSize, mode
    global boardbound, buttonSize, bStartX, bStartY
    if mode == "paint" or mode == "move":
        buttonSize = 30
        weight = 3
        strokecolor = color(22, 24, 70)
        boardbound = 100, 40, 600, 400
        boardStart = x0, y0 = 100, 40
        boardWid, boardHei = 500, 360
        fill(22, 24, 70, 255)
        rect(x0, y0, boardWid, boardHei)
        bottonSize = 30
        bStartX, bStartY = 40, 40
        db1 =color(40, 70, 140)
        fill(db1)
        rect(bStartX, bStartY, bottonSize, bottonSize)
        db2 = color(70, 130, 180)
        fill(db2)
        rect(bStartY, bStartY+bottonSize*1, bottonSize, bottonSize)
        lb1 = color(94, 184, 219)
        fill(lb1)
        rect(40, bStartY+bottonSize*2, bottonSize, bottonSize)
        lb2 = color(93, 153, 187)
        fill(lb2)
        rect(40, bStartY+bottonSize*3, bottonSize, bottonSize)
        lb3 = color(72, 92, 151)
        fill(lb3)
        rect(40, bStartY+bottonSize*4, bottonSize, bottonSize)
        lb4 = color(117, 143, 170)
        fill(lb4)
        rect(40, bStartY+bottonSize*5, bottonSize, bottonSize)
        y1 = color(229, 226, 173)
        fill(y1)
        rect(40, bStartY+bottonSize*6, bottonSize, bottonSize)
        y2 = color(234, 234, 226)
        fill(y2)
        rect(40, bStartY+bottonSize*7, bottonSize, bottonSize)
        y3 = color(255, 250, 194)
        fill(y3)
        rect(40, bStartY+bottonSize*8, bottonSize, bottonSize)
        fill(200)
        global colors
        colors = [db1,db2,lb1,lb2,lb3,lb4,y1,y2,y3]
        drawStrokeSelection()
        drawIcons()
    
def initbackground():
    global mode 
    global positions
    if mode == "paint":
        positions = []
        background(0)
        noStroke()
        particlenum = 1000
        for i in range(particlenum):
            #this draws the galaxy in the background
            stroke(255, 255, 255, random(10, 255))
            x = int(random(0, width))
            y = int(random(0, height))
            positions.append((x, y))
            point(x, y)

def updatecolors(pos):
    #this selects colors from the mouse motion
    global colors, buttonSize, bStartX, bStartY, strokecolor
    x, y  = pos
    if bStartX < x < bStartX + buttonSize:
        if bStartY < y < bStartY + buttonSize*1:
            strokecolor = colors[0]
        if bStartY+buttonSize*1 < y < bStartY + buttonSize*2:
            strokecolor = colors[1]
        if bStartY+buttonSize*2 < y < bStartY + buttonSize*3:
            strokecolor = colors[2]
        if bStartY+buttonSize*3 < y < bStartY + buttonSize*4:
            strokecolor = colors[3]
        if bStartY+buttonSize*4 < y < bStartY + buttonSize*5:
            strokecolor = colors[4]
        if bStartY+buttonSize*5 < y < bStartY + buttonSize*6:
            strokecolor = colors[5]
        if bStartY+buttonSize*6 < y < bStartY + buttonSize*7:
            strokecolor = colors[6]
        if bStartY+buttonSize*7 < y < bStartY + buttonSize*8:
            strokecolor = colors[7]
        if bStartY+buttonSize*8 < y < bStartY + buttonSize*9:
            strokecolor = colors[8]

def updateweight(pos):
    # strokeweight update function
    global weight
    (x, y) = pos
    r1 = 8
    r2 = 12
    r3 = 16
    cx1, cy1 = 55, 330
    d1 = ((cx1-x)**2+(cy1-y)**2)**0.5
    cx2, cy2 = 55, 360
    d2 = ((cx2-x)**2+(cy2-y)**2)**0.5
    cx3, cy3 = 55, 390
    d3 = ((cx3-x)**2+(cy3-y)**2)**0.5
    if d1 < r1:
        weight = 3
    elif d2 < r2:
        weight = 6
    elif d3 < r3:
        weight = 9
        
def inBoard(pos):
    #helper function that check the pen is in canvas
    global boardbound
    mx, my = pos
    (x0, y0, x1, y1) = boardbound
    if x0 < mx < x1 and y0 < my < y1:
        return True

def updatescreen(pos): 
    global strokecolor, weight, mode
    (x, y) = pos
    x1, x2, y1, y2 = 570, 610, 0, 40
    x3, x4, y3, y4 = 530, 560, 0, 40
    if x1 < x < x2 and y1 < y < y2:
        background(255)
        initSplash()
        mode = "splash"
        boardbound = 100, 40, 600, 400
        boardStart = x0, y0 = 100, 40
        boardWid, boardHei = 500, 360
        fill(22, 24, 70, 255)
        rect(x0, y0, boardWid, boardHei)
    elif x3<x< x4 and y3< y< y4 :
        strokecolor = color(22, 24, 70)
        weight = 10
    elif 480 < x < 510 and 0 < y < 40:
        saveFrame("MyOwnStarryNight.png")
    
def clean():
    noStroke()
    fill(10, 12, 57)
    rect(0, 0, width, height)
    
def setInitColor():
    #color function that sets individual stroke
    # darkblues
    db1 = color(40, 70, 140)
    db2 = color(52, 86, 163)
    db3 = color(70, 130, 180)
    db4 = color(65, 105, 225)
    # lightblues
    lb1 = color(94, 184, 219)
    lb2 = color(93, 153, 187)
    lb3 = color(72, 92, 151)
    lb4 = color(117, 143, 170)
    # yellows
    y1 = color(229, 226, 173)
    y2 = color(234, 234, 226)
    y3 = color(255, 250, 194)
    y4 = color(240, 229, 163)
    colors = [db1, db2, db3, db4,lb1,lb2,lb3,lb4,y1,y2,y3,y4]
    colindex = int(random(12))
    thiscolor = colors[colindex]
    return thiscolor

def drawStrokeSelection():
    fill(color(234, 234, 226))
    h1, h2, h3 = 330, 360, 390
    w1 = 55
    r1 = 8
    r2 = 12
    r3 = 16
    ellipse(w1, h1, r1, r1)
    ellipse(w1, h2, r2, r2)
    ellipse(w1, h3, r3, r3)

def drawIcons():
    global arrow, eraser, saveimg
    #import icons
    arrow = loadImage("arrow_left.png")
    eraser = loadImage("eraser.png")
    saveimg = loadImage("save.png")
    image(arrow,570, 0, 40, 40)
    image(eraser, 530, 5, 30, 30)
    image(saveimg, 480, 5, 30, 30)

def drawPaint():
    global mode, poslist, pList, lines, firstpos, secondpos, paintmode
    if mode == "paint":
        global weight, strokecolor, positions
        global firstpos, secondpos, lines
        stroke(strokecolor)
        pos = mouseX, mouseY
        updates(pos)
        drawInstruction()
        drawMode()
        if inBoard(pos):
            if mousePressed and paintmode == "Stroke":
                noStroke()
                fill(strokecolor)
                ellipse(mouseX,mouseY,weight*2,weight*2)
                col = strokecolor
                new = Pen(PVector(mouseX,mouseY), col, weight*2)
                poslist.append(new)
            elif paintmode == "Line":
                pos =  mouseX, mouseY
                updatescreen(pos)
                global lines
                for lineSeg in lines:
                    lineSeg.display()
                """
                for i in range(len(secondpos)):
                    (x0, y0) = firstpos[i]
                    (x1, y1) = secondpos[i]
                    col = strokecolor
                    stroke(strokecolor)
                    strokeWeight(weight)
                    line(x0, y0, x1, y1)
                """

def updates(pos):
    #helper that controls 3 buttons
    updatemode(pos)
    updatescreen(pos)
    updatecolors(pos)
    updateweight(pos)

def updatemode(pos):
    global paintmode
    sX1, sX2, sY1, sY2 = 540, 600, 420,440
    lX1, lX2, lY1, lY2 = 610, 640, 420, 440
    (x, y) = pos
    #stroke
    if sX1 < x < sX2 and sY1 < y < sY2:
        paintmode = "Stroke"
    elif lX1 < x < lX2 and lY1 < y < lY2:
        paintmode = "Line"
                    
def drawInstruction():
    #instruction board
    global f4
    db2 = color(52, 86, 163)
    fill(db2)
    textFont(f4)
    textAlign(LEFT, CENTER)
    posx, posy = 40, 15
    text("Press ENTER to animate", posx, posy)       

class LineSeg(object):
    def __init__(self, pos, col, weight):
        (x0, y0, x1, y1) = pos
        self.vector = PVector(x0, y0)
        dx, dy = (x1-x0)/50+0.2, (y1-y0)/50+0.2
        self.lenx, self.leny = (x1-x0), (y1-y0)
        self.v = PVector(dx, dy)
        self.col = col
        self.init = pos
        self.weight = weight
    
    def display(self):
        pushMatrix()
        (x0, y0) = self.vector.x, self.vector.y
        stroke(self.col)
        strokeWeight(self.weight) 
        line(x0, y0, x0 + self.lenx, y0+ self.leny)
        popMatrix()
    
    def clean(self):
        pushMatrix()
        (x0, y0) = self.vector.x, self.vector.y
        backgroundcol = color(22, 24, 70, 255)
        stroke(backgroundcol)
        strokeWeight(5) 
        line(x0, y0, x0 + self.lenx, y0+ self.leny)
        popMatrix()
    
    def move(self):
        (bx1, by1, bx2, by2) = (100, 40, 600, 400)
        (ix, iy, ix1, iy1) = self.init
        (x, y) = self.vector.x, self.vector.y
        (sx, sy) =self.v.x, self.v.y
        (x2, y2) =x+self.lenx, y+ self.leny
        if sx + x  < bx1 or sx + x > bx2:
            self.v.x *= -1
        elif sy + y  < by1 or sy + y > by2:
            self.v.y *= -1
        elif sx + x2  < bx1 or sx + x2> bx2:
            self.v.x *= -1
        elif sy + y2  < by1 or sy + y2 > by2:
            self.v.y *= -1
        self.vector.add(self.v)
        