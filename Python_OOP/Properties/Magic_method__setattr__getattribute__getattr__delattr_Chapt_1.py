class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y
    
    def set_bound(self, left):
        self.MIN_COORD = left

pt1 = Point(1, 2)
pt2 = Point(10, 20)

print(pt1.MAX_COORD)

# Let's assume that we need a method that would change 
# the value of the attribute of the MIN_COORD class. 
# Let's write it as a normal method:

#     def set_bound(self, left):
#         self.MIN_COORD = left
# Sometimes it is wrong to reason like this here. 
# We access the attribute of the MIN_COORD class and 
# assign it a new value left. Those of you who have 
# carefully watched the previous classes understand 
# the fallacy of such reasoning. Yes, when we write 
# the name of an attribute through self (a reference 
# to an object) and assign it a value, the assignment 
# operator creates this attribute in the local scope, 
# that is, in the object itself. As a result, we have 
# a new local property in the instance of the class:
pt1.set_bound(-100)
print(pt1.__dict__)
#>>> {'x': 1, 'y': 2, 'MIN_COORD': -100}
print(Point.__dict__)
#>>> {'__module__': '__main__', 
# 'MAX_COORD': 100, 
# 'MIN_COORD': 0, ...}

# Therefore, it would be more correct to declare a class-level 
# method here and use it to change the values of the MIN_COORD 
# and MAX_COORD attributes:

#     @classmethod
#     def set_bound(class, left):
#         cls.MIN_COORD = left
