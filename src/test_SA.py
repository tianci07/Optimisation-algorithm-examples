#!/usr/bin/env python3

from SimulatedAnnealing import *;
from AckleyFunction import *

optimiser = SimulatedAnnealing(AckleyFunction(), 5000, 0.04);

# Optimisation and visualisation
optimiser.plotAnimation(200);

print("Solution:\t", optimiser.best_solution);
