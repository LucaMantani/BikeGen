from Ground import Ground
from Vector import Vector
from Visualiser import Visualiser
import Genetics
import Physics
import copy
import numpy as np

bikes = Genetics.generateInitialPopulation(0.25, 30)

theGround = Ground([ Vector(-3, -0.9), Vector(3, -0.9) ])
#theGround = Ground([Vector(-3,-0.5), Vector(-1, -0.5), Vector(-0.75, -0.75), Vector(-0.25, -0.5), Vector(0.25, -0.3), Vector(0.5, -0.4), Vector(1, -0.2), Vector(3, -0.2) ])

def distanceSim(bike):
    bike = copy.deepcopy(bike)
    for _ in range(200):
        if Physics.timestep(bike, theGround):
            break
    return np.mean([ w.pos.x for w in bike.wheels ]) + 1


# for _ in range(10):
#     print(_)
#     bikes = Genetics.evolve(bikes, distanceSim)


theBike = bikes[0]

isAlive = True
countdown = 300

def animationFrame(frameIndex):
    global isAlive, bikes, countdown
    if isAlive and Physics.timestep(theBike, theGround):
        isAlive = False

    countdown -= 1
    if countdown < 0:
        for _ in range(10):
            print(_)
            bikes = Genetics.evolve(bikes, distanceSim)
        newBike = np.random.choice(bikes)
        theBike.wheels = newBike.wheels
        theBike.springs = newBike.springs
        isAlive = True
        countdown = 300
    

vis = Visualiser(theBike, theGround, animationFrame)
vis.run()

