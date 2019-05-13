import random
import math
import copy
import numpy as np

class RankSelection:
    
    def __init__(self):
        
        self.individual_set = EA.EvolutionaryAlgorithm()

    def Select(self, self.individual_set):

        negative_fitness_parents = []
        # Sort index of individuals based on their fitness
        # (we use the negative of the fitness so that np.argsort returns
        # the array of indices in the right order)
        for i in range(len(self.individual_set)):
            negative_fitness_parents.append(-self.individual_set[i].fitness)

        # Sort the array of negative fitnesses
        index_sorted = np.argsort((negative_fitness_parents))

        # Return the first index
        return (self.individual_set[index_sorted[0]])

