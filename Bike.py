from Vector import Vector


class Wheel:

    def __init__(self, pos, mass, radius, speed, isFragile):

        self.pos = pos
        self.vel = Vector(0, 0)
        self.mass = mass
        self.radius = radius

        self.speed = speed

        self.isFragile = isFragile


class Spring:
    def __init__(self, i1, i2, k, damping):
        self.i1 = i1
        self.i2 = i2
        self.k = k
        self.damping = damping


class Bike:

    def __init__(self, wheels, springs):
        self.wheels = wheels
        self.springs = springs

    @property
    def vertices(self): 
        return [ w.pos for w in self.wheels ]

    def springLines(self):
        return [ (self.vertices[s.i1], self.vertices[s.i2]) for s in self.springs ]
        
