class Sphere(object):
    def __init__(self, timeOffset, palette):
        self.timeOffset = timeOffset
        self.palette = palette
        self.segments = [Segment(i, i, i, self.palette) for i in range(5)]

    def update(self, time, timecount, sRadius):
        for seg in self.segments:
            seg.calc((time - self.timeOffset) - (seg.timeinterval * timecount),
                     sRadius)
            if seg.id != len(self.segments) - 1:
                # Draw from this segment to the next segment.
                seg.drawSelf(self.segments[seg.id + 1])
                
class Segment(object):
    def __init__(self, id, timeinterval, alti, col):
        self.id = id
        self.timeinterval = timeinterval
        self.col = col
        self.loc = PVector(0.0, 0.0, 0.0)
        timeinter = 5
        self.timeinterval *= timeinter

    def calc(self, time, sRadius):
        offset1 = 0.31
        offset2 = 0.83
        offset3 = 0.02
        lon = (sin(time + sin(time * offset1)) * 2
               + cos(time * offset2)
               * 6 + time * offset3)
        lat = (sin(time * 0.7)
               - cos(3 + time * 0.3) * 3)
        self.loc.set(cos(lon) * cos(lat) * (sRadius ),
                     sin(lon) * cos(lat) * (sRadius),
                     sin(lat) * (sRadius ))

    def drawSelf(self, other):
        strokeCap(ROUND)
        stroke(self.col)
        line(self.loc.x, self.loc.y, self.loc.z,
             other.loc.x, other.loc.y, other.loc.z)