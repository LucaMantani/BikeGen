import numpy as np
import numpy.random as rand
from Bike import Bike
from Vector import Vector

class Evolver:

    def generateWheel(sigma):
        phi = rand.uniform(0, 2 * np.pi)
        r = rand.normal(0, sigma)
        return Vector(r * np.cos(phi), r * np.sin(phi))

    def generateBike(sigma):
        return Bike([ Evolver.generateWheel(sigma) for _ in range(4) ])

    def generateInitialPopulation(sigma, nIndividuals):
        return [ Evolver.generateBike(sigma) for _ in range(nIndividuals) ]

    def fitness(bike):
        invFitness = sum([ 
            ((v1 - v2).r - 1) ** 2 for (v1, v2) in bike.springs()
        ])
        return 1.0 / invFitness

    def sortBikes(bikes):
        bikes.sort(key = Evolver.fitness, reverse = True)
        return bikes

    def selectParents(population):
        pass

    def mutate(bike):
        pass

    def breed(parent1, parent2):
        pass

    def nextGeneration():
        p1, p2 = selectParents()
        child = breed(p1, p2)
        mutate(child)
        return child

