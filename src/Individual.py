import random
import math
import numpy as np
import copy
import sys


class Individual:

    def __init__(self, aNumberOfGenes, aBoundarySet, aFitnessFunction, aGeneSet = []):

        # Set the genes
        self.genes = [];

        # Set fitness value
        self.fitness = -float('inf')

        # Set the fitness function
        self.fitness_function = aFitnessFunction;

        # Set boundaries
        self.boundary_set = copy.deepcopy(aBoundarySet)

        if len(aGeneSet) == aNumberOfGenes:
            self.genes = copy.deepcopy(aGeneSet);
        else:
            # Initialise the Individual's genes and fitness
            for i in range(aNumberOfGenes):
                # Get the boundaries
                min_i = self.boundary_set[i][0];
                max_i = self.boundary_set[i][1];

                # Get random value to each gene
                self.genes.append(random.uniform(min_i, max_i));

        # Store the fitness function
        self.fitness = self.FitnessFunction()

    def copy(self):

        return Individual(
                len(self.genes),
                self.boundary_set,
                self.fitness_function,
                self.genes
        );

    def FitnessFunction(self):

        # Compute the fitness function
        self.fitness = self.fitness_function(self.genes);

        return self.fitness;


    def gaussianMutation(self, aMutationRate):
        for i in range(len(self.genes)):
            self.genes[i] = random.gauss(self.genes[i], aMutationRate);
            self.genes[i] = max(self.boundary_set[i][0], self.genes[i]);
            self.genes[i] = min(self.boundary_set[i][1], self.genes[i]);

        self.FitnessFunction();

        return self;


    def __repr__(self):

        value = "Genes: ";
        value += ' '.join(str(e) for e in self.genes)
        value += "\tFitness: ";
        value += str(self.fitness)

        return value;
