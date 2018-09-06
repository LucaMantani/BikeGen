from Bike import Bike
from Vector import Vector
from Visualiser import Visualiser
import Genetics
from Ground import Ground
import Physics
import copy


theBike = Genetics.generateBike(0.25)
bikes = Genetics.generateInitialPopulation(0.25, 10)
maxlifetime = 100

theGround = Ground([ Vector(-1, -1), Vector(-1, -1), Vector(-1, -1), Vector(-1, -1) ])

def simulate(bike):
    bike = copy.deepcopy(bike)
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
    else:
        Physics.timestep(theBike)


v = Visualiser(theBike, theGround, updateVertices)
v.run()
