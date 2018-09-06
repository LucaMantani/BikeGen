from Bike import Wheel, Spring, Bike
from Ground import Ground
from Vector import Vector
from Visualiser import Visualiser
import Physics

theBike = Bike([ 
                    Wheel(Vector(-0.4, -0.3), 1, 0.03),
                    Wheel(Vector(-0.45, -0.3), 1, 0.03),
                    Wheel(Vector(-0.4, -0.25), 1, 0.01),
                    Wheel(Vector(-0.45, -0.25), 1, 0.01)
               ],
               [
                    Spring(0, 1, 0.1, 0.01),
                    Spring(0, 2, 0.1, 0.01),
                    Spring(0, 3, 0.1, 0.01),
                    Spring(1, 2, 0.1, 0.01),
                    Spring(1, 3, 0.1, 0.01),
                    Spring(2, 3, 0.1, 0.01)
               ])

ground = Ground([ Vector(-1, -0.5), Vector(-0.75, -0.75), Vector(-0.25, -0.5), Vector(0.25, -0.75), Vector(0.5, -0.8), Vector(1, -0.5) ])

def updateBike(frameNumber):
    Physics.timestep(theBike, ground)

v = Visualiser(theBike, ground, updateBike)
v.run()
