# Waves: 
# this object uses inheritance
# lower/upper waves inherit and override methods in Wave

class Wave(object):
    def __init__(self, startpos, endpos, angle, expo, col):
        self.startpos = startpos
        x, y = startpos
        self.locx, self.locy = x, y
        self.expo = expo
        self.endpos = endpos
        self.incre = 5  # distance to move each time
        self.step = 0
        self.angle = angle
        self.wid = random(30,50)
        self.col = col
        
    def display(self):
        noStroke()
        pushMatrix()
        fill(self.col)
        ellipse(self.locx, self.locy, 4, 4)
        popMatrix()

    def updatemode():
        strokeCap(ROUND)
        strokeWeight(6)
        x1 = self.locx + self.wid * cos(self.angle)
        y1 = self.locy + self.wid * sin(self.angle)
        line(self.locx, self.locy, x1, y1)
        
    def move(self):
        pass
    
    def reset(self):
        (x,y) = self.startpos
        self.locx, self.locy = self.startpos
        self.step = 0
        
class LowerWave(Wave):
    def __init__(self, startpos, endpos, angle, expo, col):
        super(LowerWave, self).__init__(startpos, endpos, angle, expo, col)
        
    def move(self):
        (endx, endy) = self.endpos
        (startx, starty) = self.startpos
        xmove = self.incre * self.step
        offset = 0.05
        ymove = pow(offset * xmove, self.expo)
        self.step += 0.1
        self.locx = startx + xmove
        self.locy = starty + ymove
        (boundx, boundy) = self.endpos
        if self.locx > boundx or self.locy > boundy:
            self.reset()
            
class UpperWave(Wave):
    def __init__(self, startpos, endpos, angle, expo, col):
        super(UpperWave, self).__init__(startpos, endpos, angle, expo, col)
        
    def move(self):
        (endx, endy) = self.endpos
        (startx, starty) = self.startpos
        xmove = self.incre * self.step
        offset = 0.06
        ymove = -1* pow(offset * xmove, self.expo)
        self.step += 0.1
        self.locx = startx + xmove
        self.locy = starty + ymove
        (boundx, boundy) = self.endpos
        if self.locx > boundx or self.locy < boundy:
            self.reset()
        
    