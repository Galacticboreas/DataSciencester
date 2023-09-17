class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    def __init__(self, x, y):
        self.x = self.y = 0
        if Vector.validate(x) and Vector.validate(y):
        # Note that we are referring to the class method 
        # here via the Vector namespace. But we can also 
        # prescribe self:
        # if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
    
    def get_coord(self):
        return self.x, self.y

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    @staticmethod
    def norm2(x, y):
        return x*x + y*y
    

v = Vector(10, 20)
coord = v.get_coord()
print(coord)

coord2 = Vector.get_coord(v)
print(coord2)

res = Vector.validate(5)
print(res)

res = Vector.norm2(5, 6)
# So it is inside the class:

#     def __init__(self, x, y):
#         self.x = self.y = 0
#         if self.validate(x) and self.validate(y):
#             self.x = x
#             self.y = y
 
#         print(Vector.norm2(self.x, self.y))
#         Or, also refer to this method via self:
#         print(self.norm2(self.x, self.y))
print(res)
