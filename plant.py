#the willows that swing in the animation

def setColorOfPlants():
    #darkgreens
    dg1 = color(52, 26, 26)
    dg2 = color(40, 29, 35)
    dg3 = color(60, 38, 44)
    dgs = [dg1, dg2, dg3]
    index = int(random(0, 3))
    return dgs[index]

class Plant(object):
    def __init__(self, loc, tall):
        self.col = setColorOfPlants()
        self.tall = tall
        self.loc = loc
        
    def display(self):
        for i in range(0, self.tall, 2):
            rad = radians(self.tall + frameCount*2 - i)
            offset = 0.4
            angle = offset * cos(rad) * i 
            #using sin curves, continue to draw the circles
            # tutorial about drawing sin waves in processing:
            # https://www.youtube.com/watch?v=4v2NkbUJEks
            x = sin(radians(angle)*offset)*(i*3)
            y = cos(radians(angle)*offset)*(i*3)
            fill(self.col)
            noStroke()
            r = (self.tall-i)* offset
            ellipse(self.loc.x + x, self.loc.y-y, r, r)