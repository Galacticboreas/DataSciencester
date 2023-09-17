class Point:
    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0

        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("The coordinates must be numbers")
    
    def get_coord(self):
        return self.__x, self.__y

    @classmethod
    def __check_value(cls, value):
        return type(value) in (int, float)
    

pt = Point(1, 2)

pt.set_coord(5, 10)

# pt.set_coord("1", 2)
#  File "<string>", line 11, in set_coord
#     raise ValueError("The coordinates must be numbers")
# ValueError: The coordinates must be numbers

print(pt.get_coord())
# >>> (5, 10)

print(dir(pt))
# >>>:
# ['_Point__check_value', '_Point__x', '_Point__y', 
# '__class__', '__delattr__', '__dict__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__gt__', '__hash__', '__init__', 
# '__init_subclass__', '__le__', '__lt__', 
# '__module__', '__ne__', '__new__', '__reduce__', 
# '__reduce_ex__', '__repr__', '__setattr__', 
# '__sizeof__', '__str__', '__subclasshook__', 
# '__weakref__', 'get_coord', 'set_coord']


print(pt._Point__x, pt._Point__y)
# >>> 5 10

# If you have a need to better protect class methods 
# from external access, then this can be done using 
# the accessify module. To install it, run the command:

# pip install accessify

# And, then, import two decorators from it:

# from accessify import private, protected
# Next, we simply apply the necessary decorator to the
#  method and it becomes either private or protected:

#     @private
#     @classmethod
#     def check_value(cls, x):
#         return type(x) in (int, float)
# That's it, now we can access check_value only inside 
# the class, but not from the outside:

# pt.check_value(5)
