def setSmokeCol():
    #helper that chooses color of the smokes
    y1 = color(229, 226, 173, 60)
    y2 = color(234, 234, 226, 60)
    y3 = color(255, 250, 194, 60)
    y4 = color(240, 229, 163, 60)
    y = [y1, y2, y3, y4]
    index = int(random(4))
    return y[index]

class Smoke(object):
    def __init__(self, vec, velo, siz):
        self.loc = vec
        self.velo = velo
        self.ms = siz
        self.siz = siz
        self.col = setSmokeCol()
    
    def display(self):
        fill(self.col)
        noStroke()
        #strokeWeight(1+ self.siz/10)
        ellipse(self.loc.x, self.loc.y, self.siz, self.siz)
        if self.siz >0:
            self.siz -= 0.3
        else:
            self.siz = self.ms
            new = PVector(mouseX-pmouseX, 0)
            new.normalize()
            new.mult(2)
            new.y = random(-1, 1)
            new.x += random(-1, 1)
            this = PVector(mouseX, mouseY)
            self.update(this, new)
            
    def update(self, v1, v2):
        #get() allows us to update the current pos/condition of vector
        self.loc = v1.get() 
        self.velo = v2.get()
        
    def move(self):
        self.loc.add(self.velo)