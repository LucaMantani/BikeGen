import numpy as np
import numpy.random
from Bike import Wheel, Spring, Bike
from Vector import Vector

wheelDistanceExtension = 0.2
mutationRate = 0.1
mutationAmount = 0.25

def generateWheel(sigma):
    phi = np.random.uniform(0, 2 * np.pi)
    r = np.random.normal(0, sigma)
    return Wheel(Vector(r * np.cos(phi), r * np.sin(phi)), 1, 0.1) 

def generateBike(sigma):
    return Bike(
        [ generateWheel(sigma) for _ in range(4) ],
        [
            Spring(0, 1, 0.01, 0.01),
            Spring(0, 2, 0.01, 0.01),
            Spring(0, 3, 0.01, 0.01),
            Spring(1, 2, 0.01, 0.01),
            Spring(1, 3, 0.01, 0.01),
            Spring(2, 3, 0.01, 0.01)
        ])

def generateInitialPopulation(sigma, nIndividuals):
    return [ generateBike(sigma) for _ in range(nIndividuals) ]

def fitness(bike):
    invFitness = sum([ 
        ((bike.vertices[s.i1] - bike.vertices[s.i2]).r - 1) ** 2 
        for s in bike.springs
    ])
    return 1.0 / invFitness


def crossoverWheel(w1, w2):
    t = np.random.uniform(-wheelDistanceExtension, 1.0 + wheelDistanceExtension)
    vertex = (1 - t) * w1.pos + t * w2.pos
    # TODO: Evolve mass and radius if relevant
    return Wheel(vertex, w1.mass, w1.radius)

def mutate(child):
    for wheel in child.wheels:
        if np.random.rand() < mutationRate:
            phi = np.random.rand() * 2 * np.pi
            r = np.random.normal(0, mutationAmount)
            wheel.pos += Vector(r * np.cos(phi), r * np.sin(phi))
    

def generateOffspring(parents):

    newWheels = [ crossoverWheel(w1, w2) 
                  for (w1, w2) in zip(parents[0].wheels, parents[1].wheels) ]

    # TODO crossover springs
    child = Bike(newWheels, parents[0].springs)
    mutate(child)
    return child


def evolve(population):
    scores = [ fitness(bike) for bike in population ]
    totalScore = sum(scores)
    probs = [ score / totalScore for score in scores ]

    children = [ generateOffspring(np.random.choice(population, 2, p=probs)) 
                 for _ in population ]

    return children





