from Point import Point
from Bike import Bike
from Visualiser import Visualiser

bike = Bike([ Point(0.4, 0.4), Point(0.6, 0.4), Point(0.55, 0.5), Point(0.45, 0.45) ])

def updatePoints():
    for i in range(len(bike.vertices)):
        bike.vertices[i] += Point(0, -0.003)

v = Visualiser(bike, updatePoints)

v.run()
