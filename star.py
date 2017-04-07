# star object for drawing program that animates 

class Star(object):
    def __init__(self, pos, col):
        dirx = random(-1.2, 1)
        diry = random(-1.2, 1)
        self.dir = (dirx, diry)
        self.pos = pos
        self.col = col
        self.radius = int(random(3, 5))
        self.v = random(1.3, 2.3)
        self.bound = 100, 40, 600, 400

    def display(self):
        pushMatrix()
        lights()
        (x, y) = self.pos
        translate(x, y)
        fill(self.col)
        sphere(self.radius)
        popMatrix()

    def move(self):
        (bx0, by0, bx1, by1) = self.bound 
        (x, y) = self.pos
        (dirx, diry) = self.dir
        (newx, newy) = (x + dirx, y + diry)
        if newx - self.radius <= bx0 or newx + self.radius >= bx1:
            self.dir = (-1 * dirx, diry)
            self.pos = (-self.radius, newy)
        if newy - self.radius <= by0 or newy + self.radius >= by1:
            self.dir = (dirx, -1 * diry)
            self.pos = (newx, 0)
        self.pos = (newx, newy)