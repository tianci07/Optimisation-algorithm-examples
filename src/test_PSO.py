#!/usr/bin/env python3

#import cProfile

from AckleyFunction import *
from PSO import PSO

g_number_of_particle   = 20;
g_iterations           = 40;

# Create a PSO
optimiser = PSO(AckleyFunction(), g_number_of_particle);

# Optimisation and visualisation
optimiser.plotAnimation(g_iterations);

print("Solution:\t", optimiser.best_solution);
