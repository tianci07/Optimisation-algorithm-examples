#!/usr/bin/env python3

import math;
import SimulatedAnnealing as SA;

g_number_of_dimensions = 2;
boundaries = [];
for i in range(g_number_of_dimensions):
    boundaries.append([-5,5]);

def costFunction(aSolution):
    sum = 0.0;
    #
    #for i in range(g_number_of_dimensions):
    #    sum += aSolution[i] * aSolution[i];
    #
    # Function:
    #   -((exp(-(x^2 + y^2))) + 2 (exp(-((x-1.7)^2 + (y-1.7)^2))))
    # In LaTeX
    #
    sum += math.exp(-(math.pow(aSolution[0], 2) + math.pow(aSolution[1], 2)));
    sum += 2.0 * math.exp(-(math.pow(aSolution[0]-1.7, 2) + math.pow(aSolution[1]-1.7, 2)));
    sum *= -1.0;
    #
    return sum;

optimiser = SA.SimulatedAnnealing(g_number_of_dimensions, boundaries, costFunction, 5000, 0.04);
optimiser.run(False, False);
print(optimiser)

