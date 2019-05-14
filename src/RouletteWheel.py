import random
import math
import copy

import Individual as ID
import EvolutionaryAlgorithm as EA

class RouletWheeiSelection:

    def Select(self, aIndividualSet):
        
        sum_fitness = 0.0
        #Compute fitnesses sumation
        for i in range(len(aIndividualSet)):
            sum_fitness += aIndividualSet[i].fitness

        #Compute the probability for each individual
        sum_probability = 0.0
        for i in range(len(aIndividualSet)):
            probability = sum_probability + (aIndividualSet[i].fitness / sum_fitness)
            sum_probability += probability

        # Select the individual depending on the probability
        for i in range(len(aIndividualSet)):
            #Random number between(0 - 1)
            random_number = random.uniform(0.0, 1.0)
            if (random_number > probability[i]) and (random_number < probability[i+1]):
                #Return the best individual
                return(aIndividualSet[i])
                break
