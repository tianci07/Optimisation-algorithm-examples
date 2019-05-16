#!/usr/bin/env python3

from AckleyFunction import *
from SimulatedAnnealing import *;

optimiser = SimulatedAnnealing(AckleyFunction(), 5000, 0.04);

# Run the optimisation loop
optimiser.run();

# Print the current state in the console
optimiser.printCurrentStates("");

print("Solution:\t", optimiser.best_solution);
