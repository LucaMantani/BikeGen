import numpy as np
import numpy.random as rand
from Bike import Bike
from Vector import Vector


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

def sortBikes(bikes):
    bikes.sort(key = fitness, reverse = True)
    return bikes

 def evolve(population):
        length = len(population) #number of bikes, perheps this can be a global class variable
        names = [t[0] for t in population] #the list of bikes, also a potential global
        tot = sum(t[1] for t in population) #total fitness score
        prob = []
        pred = []
        for i in range(length):
            prob.append(population[i][1]/tot)
            pred.append((bikes[i],population[i][1]/tot))

        dic = dict(pred)
        child = []
        for i in range(length):
            select = np.random.choice(names,2,p=prob)
            mute = np.random.rand()
            #if mute <=0.01:  #how likely the child is going to mutate
             #   child.append
                
            child.append((dic[select[0]]/(dic[select[0]]+dic[select[1]]))*select[0] + (dic[select[1]]/(dic[select[0]]+dic[select[1]]))*select[1])
  
        return child
            


    def mutate(bike):
        pass

        
        


    def nextGeneration():
        p1, p2 = selectParents()
        child = breed(p1, p2)
        mutate(child)
        return child


