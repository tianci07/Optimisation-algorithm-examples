import random
import math
import copy
import numpy as np

from SelectionOperator import *

class RouletteWheel(SelectionOperator):

    def __init__(self):
        super().__init__("Roulette wheel selection");
        self.sum_fitness = 0.0

    def preProcess(self, anIndividualSet):
        # Compute fitness sumation
        self.sum_fitness = 0.0
        for individual in anIndividualSet:
            self.sum_fitness += individual.fitness

    def __select__(self, anIndividualSet, aFlag): # aFlag == True for selecting good individuals,
                                                  # aFlag == False for selecting bad individuals,

        # Random number between(0 - self.sum_fitness)
        random_number = random.uniform(0.0, self.sum_fitness)

        # Select the individual depending on the probability
        accumulator = 0.0;
        for individual in anIndividualSet:
            accumulator += individual.fitness;
            if accumulator >= random_number:
                return anIndividualSet.index(individual)
