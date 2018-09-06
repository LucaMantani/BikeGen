import math

class Vector():

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self): return self._x

    @property
    def y(self): return self._y

    @property
    def r(self): return math.sqrt(self._x * self._x + self._y * self._y)

    @property
    def phi(self): return math.atan2(self._y, self._x)

    def unitVector(self): 
        return self / self.r

    def scalarProduct(self, vertex):
        return self.x * vertex.x + self.y * vertex.y

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def __sub__(self, other):
        return Vector(self._x - other._x, self._y - other._y)

    def __neg__(self):
        return Vector(-self._x, -self._y)

    def __mul__(self, scale):
        return Vector(self._x * scale, self._y * scale)

    def __rmul__(self, scale):
        return Vector(self._x * scale, self._y * scale)

    def __truediv__(self, scale):
        return Vector(self._x / scale, self._y / scale)

    def __str__(self):
        return "({}, {})".format(self._x, self._y)
