#!/usr/bin/env python3

import math;
from SimulatedAnnealing import *;

g_number_of_dimensions = 2;

g_boundaries = [];
for i in range(g_number_of_dimensions):
    g_boundaries.append([-5,5]);

def costFunction(aSolution):

    # Function:
    #   -((exp(-(x^2 + y^2))) + 2 (exp(-((x-1.7)^2 + (y-1.7)^2))))
    # In LaTeX

    cost = 0.0;
    cost += math.exp(-(math.pow(aSolution[0], 2) + math.pow(aSolution[1], 2)));
    cost += 2.0 * math.exp(-(math.pow(aSolution[0]-1.7, 2) + math.pow(aSolution[1]-1.7, 2)));
    cost *= -1.0;

    return cost;

optimiser = SimulatedAnnealing(g_number_of_dimensions, g_boundaries, costFunction, 5000, 0.04);

# Run the optimisation loop
optimiser.run();

# Print the current state in the console
optimiser.printCurrentStates("");
