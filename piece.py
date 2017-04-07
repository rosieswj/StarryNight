#piece used for the puzzle mode
#can move can detect its own mode(solved or unsolved)

class Piece(object):
    def __init__(self, pos, targetpos,boxsize, surface):
        self.pos = pos
        self.targetpos = targetpos
        self.over = False
        self.locked = False
        self.xoffset, self.yoffset = None, None
        self.boxsize = boxsize
        self.solved = False 
        dirx = random(-1.2, 1)
        diry = random(-1.2, 1)
        self.dir = (dirx, diry)
        self.surface = surface
        
    def display(self):
        global p1
        if not self.solved:
            (x0, y0) = self.pos
            (x1, y1) = self.boxsize
            image(self.surface, x0, y0, x1, y1)
        if self.solved:
            #if solved, place in target pos
            (x2, y2) = self.targetpos
            (x1, y1) = self.boxsize
            image(self.surface, x2, y2, x1, y1)

    def update(self):
        if not self.solved:
            x = mouseX - self.xoffset
            y = mouseY - self.yoffset
            self.pos = (x, y)
            (tx, ty) = self.targetpos
            bound = 20
            if tx-bound <self.pos[0]< tx +bound and ty-bound<self.pos[1]<ty+bound:
                #update status, so that its position is fixed 
                self.solved = True 
                
    def move(self):
        # only move if it's not unsolved!
        if not self.solved:
            (x, y) = self.pos
            (dirx, diry) = self.dir
            (newx, newy) = (x + dirx, y + diry)
            if newx+self.boxsize[0]/2 <= 0 or newx+self.boxsize[0]/2  >= width:
                # this makes pieces bounce around
                self.dir = (-1 * dirx, diry)
                self.pos = (0, newy)
            if newy+self.boxsize[1]/2<= 0 or newy+self.boxsize[1]/2 >= height:
                self.dir = (dirx, -1 * diry)
                self.pos = (newx, 0)
            self.pos = (newx, newy)
                
    def containspoint(self, x, y):
        #check if the mouse position is in its bound
        (x0, y0) = self.pos
        (w,h) =  self.boxsize
        (x1, y1) = x0+w, y0+h
        if x0 < mouseX < x1 and y0 < mouseY < y1:
            return True 
        