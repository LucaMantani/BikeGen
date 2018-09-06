from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
import Genetics


theBike = Genetics.generateBike(0.5)
bikes = Genetics.generateInitialPopulation(0.5, 100)


def updateVertices(frameNumber):
    global bikes
    if frameNumber % 20 == 0:
        bikes = Genetics.evolve(bikes)
        theBike.wheels = bikes[0].wheels
    

v = Visualiser(theBike, updateVertices)
v.run()
