from vector import Vector

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
    thiscolor = listOfColor[colind]
    return thiscolor

class VectorField(object):
    #this a collecion of vectors
    def __init__(self, bound, number, colorrange, v):
        self.bound = bound
        (lb, rb, tb, bb) = self.bound
        self.v = v
        self.vecs = []
        for i in range(number):
            locx = random(lb-100, rb)
            locy = random(tb, bb)
            pos = (locx, locy)
            colind = int(random(4))
            thiscolor = setcolor(colorrange)
            new = Vector(pos, self.v, thiscolor, self.bound)
            self.vecs.append(new)
            
    def display(self):
        #display them all at once so it looks like they are moving together
        for vec in self.vecs:
            vec.move()
            vec.display()
        
class VF2(VectorField):
    def __init__(self, bound, number, colorrange, v):
        self.bound = bound
        (lb, rb, tb, bb) = self.bound
        self.v = v
        self.vecs = []
        for i in range(number):
            locx = random(lb, rb)
            locy = random(tb, bb)
            pos = (locx, locy)
            colind = int(random(4))
            thiscolor = setcolor(colorrange)
            new = Vector(pos, self.v, thiscolor, self.bound)
            self.vecs.append(new)
            
    def display(self):
        super(VF2, self).display()
        
            
            
    
            
        