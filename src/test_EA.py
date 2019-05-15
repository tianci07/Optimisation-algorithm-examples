#!/usr/bin/env python3

#import cProfile

import math;

from EvolutionaryAlgorithm import *

# Selection operators
from TournamentSelection      import *
from RouletteWheel            import *
from RankSelection            import *

# Genetic operators
from ElitismOperator          import *
from BlendCrossoverOperator   import *
from GaussianMutationOperator import *
from NewBloodOperator         import *

g_number_of_individuals = 10;
g_iterations            = 20;
g_number_of_genes       = 2;

g_max_mutation_sigma = 0.5;
g_min_mutation_sigma = 0.01;

g_current_sigma = g_max_mutation_sigma;

g_boundaries = [];
for i in range(g_number_of_genes):
    g_boundaries.append([-5,5]);

def fitnessFunction(aSolution):
    fitness = 0.0;
    #
    #for i in range(g_number_of_dimensions):
    #    sum += aSolution[i] * aSolution[i];
    #
    fitness += math.exp(-(math.pow(aSolution[0], 2) + math.pow(aSolution[1], 2)));
    fitness += 2.0 * math.exp(-(math.pow(aSolution[0]-1.7, 2) + math.pow(aSolution[1]-1.7, 2)));
    fitness *= -1.0;
    #
    return -fitness;

# Print the current state in the console
def printCurrentStates(anIteration, anOptimiser):
    print("Iteration:\t", anIteration);
    print(optimiser);
    print();

def visualisationCallback():
    global g_current_sigma;
    
    # Update the mutation variance so that it varies linearly from g_max_mutation_sigma to
    # g_min_mutation_sigma
    g_current_sigma -= (g_max_mutation_sigma - g_min_mutation_sigma) / (g_iterations - 1);

    # Make sure the mutation variance is up-to-date
    gaussian_mutation.setMutationVariance(g_current_sigma);
    print(g_current_sigma)


# Create an EA
optimiser = EvolutionaryAlgorithm(g_number_of_genes, g_boundaries, fitnessFunction, g_number_of_individuals)

# Set the selection operator
#optimiser.setSelectionOperator(TournamentSelection(2));
#optimiser.setSelectionOperator(RouletteWheel());
optimiser.setSelectionOperator(RankSelection());

# Create the genetic operators
elitism = ElitismOperator(0.1);
new_blood = NewBloodOperator(0.3);
gaussian_mutation = GaussianMutationOperator(0.1, 0.4);
blend_cross_over = BlendCrossoverOperator(0.5, gaussian_mutation);

# Add the genetic operators to the EA
optimiser.addGeneticOperator(new_blood);
optimiser.addGeneticOperator(gaussian_mutation);
optimiser.addGeneticOperator(blend_cross_over);
optimiser.addGeneticOperator(elitism);

# Optimisation and visualisation
optimiser.plotAnimation(g_iterations, visualisationCallback);
