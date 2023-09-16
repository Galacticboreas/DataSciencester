
from xml.etree.ElementTree import PI


class Point:
    color = "red"
    circle = 2

Point.color = 'black'

a = Point()
b = Point()

print(a.circle)

a.color = 'green'

print(a.color)

print(a.__dict__)

Point.type_pt = 'Hello!'

print(Point.type_pt)
print(a.type_pt)

setattr(Point, 'prop', 1)

print(Point.prop)

print(getattr(Point, 'a', False))

print(getattr(Point, 'color'))

