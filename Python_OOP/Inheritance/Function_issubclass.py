class Geom(object):
    pass

class Line(Geom):
    pass

l = Line()

print(l.__class__)
print(issubclass(Line, Geom))
# <class '__main__.Line'>
# True

print(issubclass(Geom, Line))
# False

# print(issubclass(l, Geom))
# TypeError: issubclass() arg 1 must be a class

print(isinstance(l, object))
# True

print(issubclass(int, object))
# True

class Vector(list):
    def __str__(self):
        return " ".join(map(str, self))

v = Vector([1, 2, 3])
print(v)
# 1 2 3
print(type(v))
# <class '__main__.Vector'>
