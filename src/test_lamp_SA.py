#!/usr/bin/env python3

import math;

import numpy as np

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

import cv2

from SimulatedAnnealing import *;
from lampProblem import *;

number_of_lamps = 10;

objective_function = LampProblem(100, 100, 15, 0.2, 10);
objective_function.verbose = True;
optimiser = SimulatedAnnealing(objective_function, 5000, 0.04);
optimiser.verbose = True;
optimiser.run(False, False);

# Store the best individual
overlay_image = objective_function.createLampMap(optimiser.best_solution.parameter_set);
cv2.imshow("Best solution", overlay_image);
cv2.waitKey(0);
#print(optimiser)
print(optimiser.best_solution);
