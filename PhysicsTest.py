from Bike import Wheel, Spring, Bike
from Ground import Ground
from Vector import Vector
from Visualiser import Visualiser
import Physics

theBike = Bike([ 
                    Wheel(Vector(-0.4, -0.4), 1, 0.05),
                    Wheel(Vector(0.8, -0.9), 1, 0.05),
                    Wheel(Vector(0.55, 0.5), 10, 0.01),
                    Wheel(Vector(-0.45, 0.45), 10, 0.01)
               ],
               [
                    Spring(0, 1, 0.01, 0.01),
                    Spring(0, 2, 0.01, 0.01),
                    Spring(0, 3, 0.01, 0.01),
                    Spring(1, 2, 0.01, 0.01),
                    Spring(1, 3, 0.1, 0.001),
                    Spring(2, 3, 0.001, 0.001)
               ])

theGround = Ground([ Vector(-1, -1), Vector(-0.25, -0.5), Vector(0.25, -0.75), Vector(1, -0.8) ])

def updateBike(frameNumber):
    Physics.timestep(theBike)

v = Visualiser(theBike, theGround, updateBike)
v.run()
