from Vector import Vector

class Bike:

    def __init__(self, vertices):
        self.vertices = vertices
        self.velocities = [ Vector(0, 0) for _ in vertices ]

    def pairs(self):
        return [ (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3) ]

    def springs(self):
        return [ 
            (self.vertices[0], self.vertices[1]), 
            (self.vertices[1], self.vertices[2]), 
            (self.vertices[2], self.vertices[3]), 
            (self.vertices[3], self.vertices[0]), 
            (self.vertices[0], self.vertices[2]), 
            (self.vertices[1], self.vertices[3])
        ]
