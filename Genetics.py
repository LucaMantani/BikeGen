import numpy as np
import numpy.random
from Bike import Wheel, Spring, Bike
from Vector import Vector

wheelDistanceExtension = 0.2
mutationRate = 0.1

wheelPosMutationAmount = 0.25
springkMutationAmount = 0.025
springDampingMutationAmount = 0.025


def randomVector(sigma):
    phi = np.random.uniform(0, 2 * np.pi)
    r = np.random.normal(0, sigma)
    return Vector(r * np.cos(phi), r * np.sin(phi))

def generateBike(sigma):
    return Bike(
        [ 
            Wheel(randomVector(sigma), 1, 0.05, 0.01, False),
            Wheel(randomVector(sigma), 1, 0.05, 0, False),
            Wheel(randomVector(sigma), 2, 0.01, 0, True),
            Wheel(randomVector(sigma), 2, 0.01, 0, True)
        ], [
            Spring(0, 1, 0.1, 0.01),
            Spring(0, 2, 0.1, 0.01),
            Spring(0, 3, 0.1, 0.01),
            Spring(1, 2, 0.1, 0.01),
            Spring(1, 3, 0.1, 0.01),
            Spring(2, 3, 0.1, 0.01)
        ])

def generateInitialPopulation(sigma, nIndividuals):
    return [ generateBike(sigma) for _ in range(nIndividuals) ]


def crossoverWheel(w1, w2):
    t = np.random.uniform(-wheelDistanceExtension, 1.0 + wheelDistanceExtension)
    vertex = (1 - t) * w1.pos + t * w2.pos
    # TODO: Evolve mass and radius if relevant
    return Wheel(vertex, w1.mass, w1.radius, w1.speed, w1.isFragile)


def crossoverSpring(s1, s2):
    # Use better crossover
    return Spring(s1.i1, s1.i2, 0.5 * (s1.k + s2.k), 0.5 * (s1.damping + s2.damping))


def mutate(child):
    for wheel in child.wheels:
        if np.random.rand() < mutationRate:
            phi = np.random.rand() * 2 * np.pi
            r = np.random.normal(0, wheelPosMutationAmount)
            wheel.pos += Vector(r * np.cos(phi), r * np.sin(phi))
    for spring in child.springs:
        if np.random.rand() < mutationRate:
            kNew = np.random.normal(spring.k, springkMutationAmount)
            if kNew > 0: spring.k = kNew
            dampingNew = np.random.normal(spring.damping, springDampingMutationAmount)
            if dampingNew > 0: spring.damping = dampingNew
            

def generateOffspring(parents):

    newWheels = [ crossoverWheel(w1, w2) 
                  for (w1, w2) in zip(parents[0].wheels, parents[1].wheels) ]
    
    newSprings = [ crossoverSpring(s1, s2)
                   for (s1, s2) in zip(parents[0].springs, parents[1].springs) ]

    # TODO crossover springs
    child = Bike(newWheels, newSprings)
    mutate(child)

    centerOfMass = sum([ wheel.pos for wheel in child.wheels ], Vector(0, 0))
    for wheel in child.wheels:
        wheel.pos -= centerOfMass / len(child.wheels)

    return child


def evolve(population, fitnessFunc):
    scores = [ fitnessFunc(bike) for bike in population ]
    totalScore = sum(scores)
    probs = [ score / totalScore for score in scores ]

    children = [ generateOffspring(np.random.choice(population, 2, p=probs)) 
                 for _ in population ]

    return children





