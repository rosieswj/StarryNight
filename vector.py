# PVECTOR objects 
# used in animation
# has vel, location, color, bound, etc.

class Vector(object):
    def __init__(self, loc, velocity, col, bound):
        self.velocity = (vx, vy) = velocity
        self.v = PVector(vx, vy)
        locx, locy = loc
        self.loc = PVector(locx, locy)
        self.wid = random(100, 120)
        self.angle = self.v.heading()
        self.origin = locx, locy
        self.col = col
        self.bound = bound

    def display(self):
        pushMatrix()
        ellipse(self.loc.x, self.loc.y, 6, 5)
        fill(self.col)
        popMatrix()

    def move(self):
        self.loc.add(self.v)
        (bx1, bx2, by1, by2) = self.bound
        if ( self.loc.x > bx2 or self.loc.x < bx1 or
            self.loc.y < by1 or self.loc.y > by2):
            self.loc.x = self.origin[0] 
            self.loc.y = self.origin[1] 