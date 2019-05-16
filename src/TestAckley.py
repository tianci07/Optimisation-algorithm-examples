#!/usr/bin/env python3

import math

from AckleyFunction import *

from PSO import *
from SimulatedAnnealing import *
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


test_problem = AckleyFunction();


# Parameters for EA
g_number_of_individuals = 20;
g_iterations            = int(211 / 20);

g_max_mutation_sigma = 0.1;
g_min_mutation_sigma = 0.01;

g_current_sigma = g_max_mutation_sigma;

def visualisationCallback():
    global g_current_sigma;

    # Update the mutation variance so that it varies linearly from g_max_mutation_sigma to
    # g_min_mutation_sigma
    g_current_sigma -= (g_max_mutation_sigma - g_min_mutation_sigma) / (g_iterations - 1);

    # Make sure the mutation variance is up-to-date
    gaussian_mutation.setMutationVariance(g_current_sigma);



# Optimisation and visualisation
optimiser = EvolutionaryAlgorithm(test_problem, g_number_of_individuals)

# Set the selection operator
#optimiser.setSelectionOperator(TournamentSelection(2));
#optimiser.setSelectionOperator(RouletteWheel());
optimiser.setSelectionOperator(RankSelection());

# Create the genetic operators
elitism = ElitismOperator(0.1);
new_blood = NewBloodOperator(0.1);
gaussian_mutation = GaussianMutationOperator(0.1, 0.2);
blend_cross_over = BlendCrossoverOperator(0.6, gaussian_mutation);

# Add the genetic operators to the EA
optimiser.addGeneticOperator(new_blood);
optimiser.addGeneticOperator(gaussian_mutation);
optimiser.addGeneticOperator(blend_cross_over);
optimiser.addGeneticOperator(elitism);

test_problem.number_of_evaluation = 0;
optimiser.plotAnimation(g_iterations, visualisationCallback);
EA_number_of_evaluation = test_problem.number_of_evaluation
EA_solution = optimiser.best_solution;

# Optimisation and visualisation
test_problem.number_of_evaluation = 0;
optimiser = PSO(test_problem, g_number_of_individuals);
optimiser.plotAnimation(g_iterations);
PSO_number_of_evaluation = test_problem.number_of_evaluation
PSO_solution = optimiser.best_solution;


# Optimisation and visualisation
test_problem.number_of_evaluation = 0;
optimiser = SimulatedAnnealing(test_problem, 5000, 0.04);
optimiser.plotAnimation(211);
SA_number_of_evaluation = test_problem.number_of_evaluation
SA_solution = optimiser.best_solution;

print("EA.number_of_evaluation:\t", EA_number_of_evaluation)
print("EA solution:\t", EA_solution);
print()
print("PSO.number_of_evaluation:\t", PSO_number_of_evaluation)
print("PSO solution:\t", PSO_solution);
print()
print("SA.number_of_evaluation:\t", SA_number_of_evaluation)
print("SA solution:\t", SA_solution);
print()
