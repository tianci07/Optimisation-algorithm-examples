import random
import math
import copy
import numpy as np

class RankSelection:

    def select(self, aIndividualSet):

        negative_fitness_parents = []
        # Sort index of individuals based on their fitness
        # (we use the negative of the fitness so that np.argsort returns
        # the array of indices in the right order)
        for i in range(len(aIndividualSet)):
            negative_fitness_parents.append(-aIndividualSet[i].fitness)

        # Sort the array of negative fitnesses
        index_sorted = np.argsort((negative_fitness_parents))

        # Return the first index
        return (aIndividualSet[index_sorted[0]])

