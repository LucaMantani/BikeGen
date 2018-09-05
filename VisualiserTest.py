from Vector import Vector
from Bike import Bike
from Visualiser import Visualiser

bike = Bike([ Vector(0.4, 0.4), Vector(0.6, 0.4), Vector(0.55, 0.5), Vector(0.45, 0.45) ])

def updateVertices(frameNumber):
    for i in range(len(bike.vertices)):
        bike.vertices[i] += Vector(0, -0.003)

v = Visualiser(bike, updateVertices)

v.run()
