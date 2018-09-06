from Vector import Vector

class Ground:

    def __init__(self, vertices):
        self.vertices = vertices

    def getHeight(self, x):
        if x < self.vertices[0].x:
            return self.vertices[0].y

        for i in range(len(self.vertices) - 1):
            if self.vertices[i].x < x:
                t = (x - self.vertices[i].x) / (self.vertices[i + 1].x - self.vertices[i].x)
                return (1 - t) * self.vertices[i].y + t * self.vertices[i + 1].y
            
        return self.vertices[-1].y
                