##############################
"""
Wave: this is the vectors for animation part
"""
##############################

from wave import Wave, UpperWave, LowerWave

def setcolor(colorrange):
    #darkblues 
    db1 = color(40, 70, 140)
    db2 = color(52, 86, 163)
    db3 = color(70, 130, 180)
    db4 = color(65, 105, 225)
    db = [db1, db2, db3, db4]
    #lightblues
    lb1 = color(94, 184, 219)
    lb2 = color(93, 153, 187)
    lb3 = color(72, 92, 151)
    lb4 = color(117, 143, 170)
    lb = [lb1, lb2, lb3, lb4]
    #yellows
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
    return listOfColor[colind]

class UpperWaves(object):
    def __init__(self, posrange, bound, angle, expo, num, cr):
        self.listOfS = []
        (x0, y0, x1, y1) = posrange
        for i in range(num):
            x = random(x0, x1)
            y = random(y0, y1)
            thispos = (x, y)
            thiscolor = setcolor(cr)
            this = UpperWave(thispos, bound, angle, expo, thiscolor)
            self.listOfS.append(this)
        
    def display(self):
        for upperwave in self.listOfS:
            upperwave.move()
            upperwave.display()

class LowerWaves(object):
    def __init__(self, posrange, bound, angle, expo, num, cr):
        self.listOfS = []
        (x0, y0, x1, y1) = posrange
        for i in range(num):
            x = random(x0, x1)
            y = random(y0, y1)
            thispos = (x, y)
            thiscolor = setcolor(cr)
            this = LowerWave(thispos, bound, angle, expo, thiscolor)
            self.listOfS.append(this)
        
    def display(self):
        for lw in self.listOfS:
            lw.move()
            lw.display()
            