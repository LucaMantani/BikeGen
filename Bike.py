
class Bike:

    def __init__(self, vertices):
        self.vertices = vertices
    
    def springs(self):
        return [ 
            (self.vertices[0], self.vertices[1]), 
            (self.vertices[1], self.vertices[2]), 
            (self.vertices[2], self.vertices[3]), 
            (self.vertices[3], self.vertices[0]), 
            (self.vertices[0], self.vertices[2]), 
            (self.vertices[1], self.vertices[3])
        ]
