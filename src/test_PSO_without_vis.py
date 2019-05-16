#!/usr/bin/env python3

#import cProfile

from AckleyFunction import *
from PSO import PSO

g_number_of_particle   = 20;
g_iterations           = 40;

# Create a PSO
optimiser = PSO(AckleyFunction(), g_number_of_particle);

# Print the current state in the console
optimiser.printCurrentStates(0);

# Optimisation
for i in range(g_iterations):
    # Run the optimisation loop
    optimiser.runIteration();

    # Print the current state in the console
    optimiser.printCurrentStates(i + 1);

print("Solution:\t", optimiser.best_solution);
