from Vector import Vector

class Bike:

    def __init__(self, vertices):
        self.vertices = vertices
        self.velocities = [Vector(0,0) for y in range(4)]
    
    def springs(self):
        return [ 
            (self.vertices[0], self.vertices[1]), 
            (self.vertices[1], self.vertices[2]), 
            (self.vertices[2], self.vertices[3]), 
            (self.vertices[3], self.vertices[0]), 
            (self.vertices[0], self.vertices[2]), 
            (self.vertices[1], self.vertices[3])
        ]
