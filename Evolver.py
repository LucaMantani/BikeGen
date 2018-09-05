

class Evolver:

    def generateInitialPopulation():
        pass

    def fitness(bike):
        pass

    # def sortBikes():
    #    pass

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

