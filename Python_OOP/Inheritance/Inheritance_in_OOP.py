class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.x2 = x2
    
    def draw(self):
        print("Drawing a primitive!")


class Line(Geom):
    def draw(self):
        print("Drawing a line!")


class React(Geom):
  
    def draw(self):
        print("Drawing a rectangle!")

l = Line()
r = React()
l.set_coords(1, 2, 3, 4)
r.set_coords(1, 2, 3, 4)

l.draw()
r.draw()

g = Geom()

g.set_coords(0, 0, 0, 0)

g.draw()

