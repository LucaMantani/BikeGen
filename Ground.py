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
                if self.vertices[i].y - self.vertices[i+1].y == 0:
                    return vertex.y - self.getHeight(vertex.x)

                a = 1/(self.vertices[i+1].x-self.vertices[i].x)
                b = -1/(self.vertices[i+1].y-self.vertices[i].y)
                c = self.vertices[i].y/(self.vertices[i+1].y-self.vertices[i].y) -self.vertices[i].x/(self.vertices[i+1].x-self.vertices[i].x)

                direction = self.vertices[i+1] - self.vertices[i]
                m = -direction.y/direction.x
                perp_vec = Vector(1.0, m*1.0).unitVector()

                return (abs(a*vertex.x + b*vertex.y + c)/np.sqrt(a**2 + b**2)) * perp_vec


# a = Ground([Vector(0.0,0.0),Vector(0.3,0.0), Vector(0.5, 0.5), Vector(1.0, 0.0)])

# b = Vector(0.1, 0.5)

# print(a.distance(b))