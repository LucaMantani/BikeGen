from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
import Evolver

theBike = Bike([ Vector(-0.5, -0.5), Vector(0.5, -0.5), Vector(0.5, 0.5), Vector(-0.5, 0.5) ])
print(1.0 / Evolver.fitness(theBike))

bikes = Evolver.generateInitialPopulation(0.2, 100)
Evolver.sortBikes(bikes)
theBike = Evolver.generateBike(0.2)

def updateVertices(frameNumber):
    theBike.vertices = bikes[frameNumber].vertices
    print(Evolver.fitness(theBike))

v = Visualiser(theBike, updateVertices)
v.run()
