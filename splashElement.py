class Element(object):
    #these are the circles in the background of splash screen
    def __init__(self, col, loc, initSize, angle):
        self.col = col
        self.x, self.y = random(-10, 10), random(-10, 10)
        self.loc = loc
        self.angle = angle
        self.initSize = initSize
        dirs = [-1, 1]
        index = int(random(-1, 2))
        self.dir = dirs[index]

    def display(self):
        fill(self.col, int(random(90, 100)))
        pushMatrix()
        (x, y) = self.loc
        translate(x, y)
        rotate(self.angle)
        offset = 10
        currentSize = map(sin(self.angle), -1, 1, 10, self.initSize * offset)
        ellipse(self.x, self.y, currentSize, currentSize)
        popMatrix()
        self.angle += 0.05 * self.dir