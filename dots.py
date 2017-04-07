# Dot = the star objects on the sky in the animation part

class Dot(object):
    def __init__(self, col, phi=0, theta=0,ray=100, t=0, v=0):
        #angle phi, theta, ray controls the 3D movement
        self.phi = phi
        self.theta = theta
        self.ray = ray
        self.t = int(random(50))
        self.v = random(0.05, 0.9)
        self.col = col
        
    def display(self):
        with pushMatrix():
            stroke(self.col)
            strokeWeight(5)
            self.t -= self.v
            if self.t <0:
                self.t = 50
            #strokeWeight(map(self.t, 0, 50, 0.5, 8))
            x = (sin(self.phi)*cos(self.theta))*self.ray
            y = (sin(self.phi)*sin(self.theta))*self.ray
            z = (cos(self.phi))* self.ray
            point(x, y, z)

            