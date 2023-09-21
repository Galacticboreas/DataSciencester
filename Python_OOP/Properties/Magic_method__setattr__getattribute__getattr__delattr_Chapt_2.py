class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __getattribute__(self, item):
        print("__getattribute__")
        return object.__getattribute__(self, item)
    
    # A new magic method __getattribute__ has been added here. 
    # It is automatically called when an attribute is read 
    # through an instance of the class. For example, when 
    # accessing the MIN_COORD property:

    # print(pt1.MIN_COORD)

    # Or to a private property through a special name:

    # print(pt1._Point__x)

    # But since this is the case, then let's explicitly prohibit 
    # reading such an attribute from an instance of the class. 
    # To do this, we will write a check in the 
    # __getattribute__ method:

    # def __getattribute__(self, item):
    #     if item == "_Point__x":
    #         raise ValueError("Private attribute")
    #     else:
    #         return object.__getattribute__(self, item)
    
    def __setattr__(self, key, value):
        print("__setattr__")
        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        object.__delattr__(self, item)

    @classmethod
    def set_bound(cls, left):
        cls.MIN_COORD = left
    # No additional properties will be created in the 
    # object itself, and the value of the MIN_COORD 
    # variable will change in the class, just as we 
    # wanted it to.

pt1 = Point(1, 10)
pt2 = Point(10, 100)

print(pt1.MIN_COORD)
# >>> __getattribute__
#     0

print(pt1._Point__x)
# >>> __getattribute__
#     1
print(pt1.a)
