import numpy as np
import numpy.random as rand
#from Bike import Bike
#from Vector import Vector

class Evolver:

    def generateInitialPopulation():
        pass

    def fitness(bike):
        pass

    # def sortBikes():
    #    pass

    def genParents(population):
        names = np.array([t[0] for t in population])
        tot = sum(t[1] for t in population)
        prob = []
        for i in range(len(population)):
            prob.append(population[i][1]/tot)

        select = np.random.choice(names,2,p=prob)
        #par1 = np.array(select[0].vertices)
        #par2 = np.array(select[1].vertices)
        #child = 
        return select
            


    def mutate(bike):
        pass

        
        


    def nextGeneration():
        p1, p2 = selectParents()
        child = breed(p1, p2)
        mutate(child)
        return child

