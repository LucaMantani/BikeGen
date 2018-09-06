from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
import Genetics


theBike = Genetics.generateBike(0.5)
bikes = Genetics.generateInitialPopulation(0.5, 100)


def fitness(bike):
    invFitness = sum([ 
        ((bike.vertices[s.i1] - bike.vertices[s.i2]).r - 1) ** 2 
        for s in bike.springs
    ])
    return 1.0 / invFitness

def updateVertices(frameNumber):
    global bikes
    if frameNumber % 20 == 0:
        bikes = Genetics.evolve(bikes, fitness)
        theBike.wheels = bikes[0].wheels
    

v = Visualiser(theBike, updateVertices)
v.run()
