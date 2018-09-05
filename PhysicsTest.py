from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
import Physics

theBike = Bike([ Vector(-0.4, -0.4), Vector(0.8, -0.9), Vector(0.55, 0.5), Vector(-0.45, 0.45) ],
               [ 0.01, 0.01, 0.01, 0.01, 0.1, 0.001 ])

def updateBike(frameNumber):
    Physics.timestep(theBike)

v = Visualiser(theBike, updateBike)
v.run()
