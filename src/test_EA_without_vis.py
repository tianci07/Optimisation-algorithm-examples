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

# Print the current state in the console
optimiser.printCurrentStates(0);

# Run the optimisation loop g_iterations times,
# with the mutation variance varying linearly from g_max_mutation_sigma to
# g_min_mutation_sigma
for i in range(g_iterations):
    # Compute the value of the mutation variance
    sigma = g_min_mutation_sigma + (g_iterations - 1 - i) / (g_iterations - 1) * (g_max_mutation_sigma - g_min_mutation_sigma);

    # Set the mutation variance
    gaussian_mutation.setMutationVariance(sigma);

    # Run the optimisation loop
    optimiser.runIteration();

    # Print the current state in the console
    optimiser.printCurrentStates(i + 1);

# Get the solution to the optimisation problem
print("Best individual:\t", optimiser.best_solution);
