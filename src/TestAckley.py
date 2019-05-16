#!/usr/bin/env python3

import math

from ObjectiveFunction import *

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




class AckleyFunction(ObjectiveFunction):
    def __init__(self):

        number_of_dimensions = 2;

        boundaries = [];
        for i in range(number_of_dimensions):
            boundaries.append([-5,5]);

        super().__init__(number_of_dimensions,
                         boundaries,
                         self.objectiveFunction,
                         1);

    def objectiveFunction(self, aSolution):

        # Function:
        #   f(x,y)=-20&amp;\exp \left[-0.2{\sqrt {0.5\left(x^{2}+y^{2}\right)}}\right]\\&amp;{}-\exp \left[0.5\left(\cos 2\pi x+\cos 2\pi y\right)\right]+e+20}}
        # In LaTeX

        cost = 0.0;
        cost += -20.0 * math.exp(0.2 * -(math.sqrt(math.pow(aSolution[0], 2) + math.pow(aSolution[1], 2))));
        cost += - math.exp(0.5 * (math.cos(2.0 * math.pi * aSolution[0]) + math.cos(2.0 * math.pi * aSolution[1])));
        cost += math.e + 20.0;

        return cost;


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
    print(g_current_sigma)



# Optimisation and visualisation
optimiser = EvolutionaryAlgorithm(test_problem, g_number_of_individuals)

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

test_problem.number_of_evaluation = 0;
optimiser.plotAnimation(g_iterations, visualisationCallback);
print("EA.number_of_evaluation:\t", test_problem.number_of_evaluation)

# Optimisation and visualisation
test_problem.number_of_evaluation = 0;
optimiser = PSO(test_problem, g_number_of_individuals);
optimiser.plotAnimation(g_iterations);
print("PSO.number_of_evaluation:\t", test_problem.number_of_evaluation)



# Optimisation and visualisation
test_problem.number_of_evaluation = 0;
optimiser = SimulatedAnnealing(test_problem, 5000, 0.04);
optimiser.plotAnimation(211);
print("SA.number_of_evaluation:\t", test_problem.number_of_evaluation)
