import numpy as np
from Vector import Vector

class Ground:

    def __init__(self, vertices):
        self.vertices = vertices

    def getHeight(self, x):
        if x > self.vertices[-1].x:
            return self.vertices[-1].y

        for i in range(len(self.vertices)-2, -1, -1):
            if self.vertices[i].x < x:
                t = (x - self.vertices[i].x) / (self.vertices[i + 1].x - self.vertices[i].x)
                return (1 - t) * self.vertices[i].y + t * self.vertices[i + 1].y
            
        return self.vertices[0].y

    def distance(self, vertex):
    
        for i in range(len(self.vertices)-2, -1, -1):
            if self.vertices[i].x < vertex.x:

                v0 = self.vertices[i]
                dv = (self.vertices[i + 1] - self.vertices[i]).unitVector()

                nPerp = Vector(-dv.y, dv.x)
                dist = (vertex - v0).scalarProduct(nPerp)

                return dist * nPerp

        if vertex.x < 0:
            return Vector(0, vertex.y - self.vertices[0].y)
        else:
            return Vector(0, vertex.y - self.vertices[-1].y)
            
