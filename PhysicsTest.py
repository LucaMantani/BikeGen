from Bike import Bike, Spring
from Vector import Vector
from Visualiser import Visualiser
import Physics

theBike = Bike([ Vector(-0.4, -0.4), Vector(0.8, -0.9), Vector(0.55, 0.5), Vector(-0.45, 0.45) ],
               [
                   Spring(0, 1, 0.01, 0.01),
                   Spring(0, 2, 0.01, 0.01),
                   Spring(0, 3, 0.01, 0.01),
                   Spring(1, 2, 0.01, 0.01),
                   Spring(1, 3, 0.01, 0.001),
                   Spring(2, 3, 0.001, 0.001)
               ],
               [1, 1, 10, 10],
               [ 0.05, 0.05, 0.01, 0.01 ])

def updateBike(frameNumber):
    Physics.timestep(theBike)

v = Visualiser(theBike, updateBike)
v.run()
