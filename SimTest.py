from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
import Genetics
from Ground import Ground
import Physics



theBike = Genetics.generateBike(0.5)
bikes = Genetics.generateInitialPopulation(0.5, 100)
maxlifetime = 100

theGround = Ground([ Vector(-1, -1), Vector(-1, -1), Vector(-1, -1), Vector(-1, -1) ])

def simulate(bike):
    for i in range(1,maxlifetime):
        if not Physics.timestep(bike):
            #record the distance travelled and then break
            return i
    return maxlifetime
            

#for i in range(10):
#     bikes = Genetics.evolve(bikes,simulate)
        


def updateVertices(frameNumber):
    global bikes
    if frameNumber % maxlifetime == 0:
        bikes = Genetics.evolve(bikes,simulate)
        theBike.wheels = bikes[0].wheels
        print(simulate(bikes[1]))
    else:
        Physics.timestep(theBike)


v = Visualiser(theBike, theGround, updateVertices)
v.run()
