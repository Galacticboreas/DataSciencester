class Geom:
    name = 'Geom'
 
    def __init__(self, x1, y1, x2, y2):
        print(f"Geom initializer for {self.__class__}")
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
 
 
class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self.__fill = fill

r = Rect(0, 0, 10, 20)
print(r.__dict__)
# {'_Geom__x1': 0, '_Geom__y1': 0, '_Geom__x2': 10, 
# '_Geom__y2': 20, '_Rect__fill': 'red'}

class Geom2:
    name = "Geom2"

    def __init__(self, x1, y1, x2, y2):
        print(f"Geom2 initializer for {self.__class__}")
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2


class Rect2(Geom2):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)
        self._fill = fill
 
    def get_coords(self):
        return (self._x1, self._y1, self._x2, self._y2)

r = Rect2(0, 0, 10, 20)
print(r.__dict__)
# Geom2 initializer for <class '__main__.Rect2'>
# {'_x1': 0, '_y1': 0, '_x2': 10, '_y2': 20, '_fill': 'red'}

r.get_coords()
