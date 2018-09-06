import numpy as np
import numpy.random as rand
from Bike import Bike
from Vector import Vector

wheelDistanceExtension = 0.2
mutationRate = 0.1
mutationAmount = 0.25

def generateWheel(sigma):
    phi = rand.uniform(0, 2 * np.pi)
    r = rand.normal(0, sigma)
    return Vector(r * np.cos(phi), r * np.sin(phi))

def generateBike(sigma):
    return Bike([ generateWheel(sigma) for _ in range(4) ])

def generateInitialPopulation(sigma, nIndividuals):
    return [ generateBike(sigma) for _ in range(nIndividuals) ]

def fitness(bike):
    invFitness = sum([ 
        ((v1 - v2).r - 1) ** 2 for (v1, v2) in bike.springs()
    ])
    return 1.0 / invFitness


def crossoverWheel(w1, w2):
    t = np.random.uniform(-wheelDistanceExtension, 1.0 + wheelDistanceExtension)
    return (1 - t) * w1 + t * w2

def mutate(child):
    for i in range(len(child.vertices)):
        if np.random.rand() < mutationRate:
            phi = np.random.rand() * 2 * np.pi
            r = np.random.normal(0, mutationAmount)
            child.vertices[i] += Vector(r * np.cos(phi), r * np.sin(phi))
    

def generateOffspring(parents):
    newWheels = []
    for i in range(len(parents[0].vertices)):
        newWheels.append(crossoverWheel(parents[0].vertices[i], parents[1].vertices[i]))
    
    child = Bike(newWheels)
    mutate(child)
    return child


def evolve(population):
    scores = [ fitness(bike) for bike in population ]
    totalScore = sum(scores)
    probs = [ score / totalScore for score in scores ]

    children = [ generateOffspring(np.random.choice(population, 2, p=probs)) 
                 for _ in population ]

    return children





