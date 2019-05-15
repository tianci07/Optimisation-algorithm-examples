#!/usr/bin/env python3

#import cProfile

import math;
from PSO import PSO


g_number_of_particle   = 10;
g_iterations           = 20;
g_number_of_dimensions = 2;

g_boundaries = [];
for i in range(g_number_of_dimensions):
    g_boundaries.append([-5,5]);

def costFunction(aSolution):
    cost = 0.0;
    #
    #for i in range(g_number_of_dimensions):
    #    sum += aSolution[i] * aSolution[i];
    #
    cost += math.exp(-(math.pow(aSolution[0], 2) + math.pow(aSolution[1], 2)));
    cost += 2.0 * math.exp(-(math.pow(aSolution[0]-1.7, 2) + math.pow(aSolution[1]-1.7, 2)));
    cost *= -1.0;
    #
    return cost;

# Create a PSO
optimiser = PSO(g_number_of_dimensions, g_boundaries, costFunction, g_number_of_particle);

# Print the current state in the console
optimiser.printCurrentStates(0);

# Optimisation
for i in range(g_iterations):
    # Run the optimisation loop
    optimiser.runIteration();

    # Print the current state in the console
    optimiser.printCurrentStates(i + 1);
