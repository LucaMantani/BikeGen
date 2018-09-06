from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
from Genetics import Genetics
from Ground import Ground
from Physics import Physics



theBike = Genetics.generateBike(0.5)
bikes = Genetics.generateInitialPopulation(0.5, 100)

theGround = Ground([ Vector(-1, -1), Vector(-0.25, -0.5), Vector(0.25, -0.75), Vector(1, -0.8) ])

def updateVertices(frameNumber):
    global bikes
    if frameNumber % 20 == 0:
        bikes = Genetics.evolve(bikes)
        theBike.wheels = bikes[0].wheels
    

def updateBike(frameNumber):
    Physics.timestep(theBike)

v = Visualiser(theBike, theGround, updateBike)
v.run()
