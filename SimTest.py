from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
import Genetics
from Ground import Ground
import Physics



theBike = Genetics.generateBike(0.5)
bikes = Genetics.generateInitialPopulation(0.5, 100)

theGround = Ground([ Vector(-1, -1), Vector(-1, -1), Vector(-1, -1), Vector(-1, -1) ])

def updateVertices(frameNumber):
    global bikes
    Physics.timestep(theBike)
    
    if frameNumber % 100 == 0:
        bikes = Genetics.evolve(bikes)
        theBike.wheels = bikes[0].wheels
    

#def updateBike(frameNumber):
#    Physics.timestep(theBike)

v = Visualiser(theBike, theGround, updateVertices)
v.run()
