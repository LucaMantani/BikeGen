from Vector import Vector

class Spring:
    def __init__(self, i1, i2, k, damping):
        self.i1 = i1
        self.i2 = i2
        self.k = k
        self.damping = damping


class Bike:

    idxs = [ (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3) ]

    def __init__(self, vertices, springConstants, springDampings, masses, radii):
        self.vertices = vertices
        self.velocities = [ Vector(0, 0) for _ in vertices ]
        self.springs = [ Spring(Bike.idxs[i][0], Bike.idxs[i][1], springConstants[i], springDampings[i])
                         for i in range(len(springConstants)) ]
        self.masses = masses
        self.radii = radii

    def springVertices(self):
        return [ 
            (self.vertices[0], self.vertices[1]), 
            (self.vertices[1], self.vertices[2]), 
            (self.vertices[2], self.vertices[3]), 
            (self.vertices[3], self.vertices[0]), 
            (self.vertices[0], self.vertices[2]), 
            (self.vertices[1], self.vertices[3])
        ]
