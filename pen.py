# stroke object that would vibrate in the painting mode

class Pen(object):
    def __init__(self, pos, col, weight):
        self.pos = pos
        self.col = col
        self.v = PVector(random(-0.2, 0.2), random(-0.2, 0.2))
        self.origin = (pos.x, pos.y)
        self.weight = weight
        
    def display(self):
        pushMatrix()
        #strokeWeight(5)
        noStroke()
        strokeWeight(0)
        fill(self.col, 230)
        ellipse(self.pos.x, self.pos.y,self.weight, self.weight)
        popMatrix()
        
    def move(self):
        if self.outBound():
            self.pos = PVector(self.origin[0], self.origin[1])
        self.pos.add(self.v)
            
    def outBound(self):
        pv1 = self.pos
        pv2 = self.origin
        d = sqrt(sq(self.origin[0]-self.pos.x)+sq(self.origin[1]-self.pos.y))
        if d > 5:
            return True
        
    def clear(self):
        pushMatrix()
        #strokeWeight(5)
        noStroke()
        strokeWeight(0)
        fill(c(22, 24, 70, 255))
        ellipse(self.pos.x, self.pos.y, 4, 4)
        popMatrix()