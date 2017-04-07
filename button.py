##############################
"""
Button object
Set the two button(flowers) on init screen

"""
##############################

def setColor():
    #darkgreens
    y1 = color(229, 226, 173)
    y2 = color(240, 246, 240)
    y3 = color(255, 250, 194)
    y4 = color(240, 229, 163)
    db = [y1, y2, y3, y4]
    index = int(random(0, 3))
    return db[index]

class Button(object):
    def __init__(self, pos):
        self.pos = pos
        #each time select a random color
        self.col = setColor() 
    
    def display(self):
        pushMatrix()
        (x, y) = self.pos
        translate(x, y)
        for i in range(15):
            incre = 3
            j = i*incre
            step = 30
            for angle in range(0, 360, step):
                x = sin(radians(angle))*j
                y = cos(radians(angle))*j
                f = frameCount
                offset = 0.8
                m = offset+ sin(radians(sin(radians(f))*j+angle*incre*1.8+f*incre))
                if m > 0:
                    fill(self.col)
                    r = m*i
                    noStroke()
                    ellipse(x, y,r, r)
        popMatrix()
    