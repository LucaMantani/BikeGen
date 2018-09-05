from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
import Genetics

theBike = Bike([ Vector(-0.5, -0.5), Vector(0.5, -0.5), Vector(0.5, 0.5), Vector(-0.5, 0.5) ])
print(1.0 / Genetics.fitness(theBike))

bikes = Genetics.generateInitialPopulation(0.2, 100)
Genetics.sortBikes(bikes)
theBike = Genetics.generateBike(0.2)

def updateVertices(frameNumber):
    if frameNumber % 20 == 0:
        theBike.vertices = bikes[int(frameNumber / 20)].vertices
    

v = Visualiser(theBike, updateVertices)
v.run()
