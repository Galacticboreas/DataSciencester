# Every Python class has a set of predefined "magic" methods. 
# Yes, it is such a common name. Magical methods begin and 
# end with two underscores:

# __ method name__

# In particular , there are two such methods:

# __init__(self) – initializer of the class object
# __del__(self) – class finalizer
# The first one is called immediately after creating an instance
#  of the class, and the second one is called before deleting it
#  directly. Let's see how they work and why they are needed.

class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0) -> None:
        print("call __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("deleting an instance")

    def set_coords(self, x, y):
        self.x = x
        self.y = y
    
    def get_coords(self):
        return (self.x, self.y)

pt = Point()
print(pt.__dict__)

pt.set_coords(1, 2)
print(pt.__dict__)
