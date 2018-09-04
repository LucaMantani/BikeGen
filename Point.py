import math

class Point():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def x(self): return self._x
    def y(self): return self._y
    def r(self): return math.sqrt(self._x * self._x + self._y * self._y)
    def phi(self): return math.atan2(self._y, self._x)

    def __add__(self, other):
        return Point(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Point(self._x - other._x, self._y - other._y)

    def __mul__(self, scale):
        return Point(self._x * scale, self._y * scale)

    def __rmul__(self, scale):
        return Point(self._x * scale, self._y * scale)

    def __str__(self):
        return "({}, {})".format(self._x, self._y)
