import random
import math
import numpy as np
import copy
import sys


class Individual:

    def __init__(self, aNumberOfGenes, aBoundarySet):
        
        # Set individual
        self.genes = []
        # Set fitness value
        self.fitness = 0.0
        # Set boundaries
        self.boundary_set = []
        
        self.boundary_set = copy.deepcopy(aBoundarySet)
        
        # Initialise the Individual's genes and fitness
        for i in range(aNumberOfGenes):
            # Get the boundaries
            min_i = self.boundary_set[i][0];
            max_i = self.boundary_set[i][1];

            # Get random value to each gene
            self.genes.append(random.uniform(min_i, max_i));

        # Store the fitness function
        self.fitness = self.FitnessFunction()
    
    def copy(self, aIndividual):
        
        self.genes = copy.deepcopy(aIndividual.genes)
        
        self.boundary_set = copy.deepcopy(aIndividual.boundary_set)
        
        self.fitness = aIndividual.fitness
    

    def FitnessFunction(self):
        
        # Compute the fitness function
        sum = 0.0

        sum = (2.0 * self.genes[0]) + self.genes[1] + (5.0 + self.genes[2])
        
        self.fitness = sum
        
        return self.fitness;


    def __repr__(self):
        
        value = "Genes: ";
        value += ' '.join(str(e) for e in self.genes)
        value += "\tFitness: ";
        value += str(self.fitness)
       
        return value;
