import random
import math
import copy
import numpy

from SelectionOperator import *

class RouletteWheel(SelectionOperator):

    def __init__(self):
        super().__init__("Roulette wheel selection");
        self.probability_set = [];

    def preProcess(self, anIndividualSet):
        # Compute fitness sumation
        sum_fitness = 0.0
        for individual in anIndividualSet:
            sum_fitness += individual.fitness

        # Compute the probability for each individual
        self.probability_set = [];
        sum_probability = 0.0
        for individual in anIndividualSet:
            self.probability_set.append(sum_probability + (individual.fitness / sum_fitness))
            sum_probability += self.probability_set[-1]

    def __select__(self, anIndividualSet, aFlag): # aFlag == True for selecting good individuals,
                                                  # aFlag == False for selecting bad individuals,

        # Random number between(0 - 1)
        random_number = random.uniform(0.0, 1.0)

        # Select the individual depending on the probability
        for probability in self.probability_set:
            if random_number < probability:
                #Return the best individual
                return(self.probability_set.index(probability))
