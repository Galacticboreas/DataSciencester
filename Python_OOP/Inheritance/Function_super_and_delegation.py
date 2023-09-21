# See, if we have some kind of Geom base class and we 
# create a child class Line, which additionally contains 
# the draw() method, then this is called an extension of 
# the base class:

# Geom class:
#     name = 'Geometrija'
 
 
# class Line(Geom):
#     def draw(self):
#       print("Drawing a line")

# As a rule, child classes are created specifically to 
# extend the functionality of base classes. However, if 
# you also write the draw() method in the Geom class:

# Geom class:
#     name = 'Geometrija'
 
#     def draw(self):
#       print ("Drawing a primitive")

# then now the Line class only overrides the behavior 
# of the base class, without changing its principle of 
# functioning. Therefore, when they talk about expansion, 
# they mean adding new attributes in child classes, 
# and when redefining (usually methods), changing 
# the behavior of an already existing functional.

class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Geom initializer for {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Line(Geom):

    def draw(self):
        print("Draw line!")

class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        print('Rect initializer')
        self.fill = fill
    def draw(self):
        print('Drawing a rectangle!')

l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
# Geom initializer for <class '__main__.Line'>
# Geom initializer for <class '__main__.Rect'>
# Rect initializer

