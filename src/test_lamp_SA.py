#!/usr/bin/env python3

import math;

import numpy as np

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

import cv2

import SimulatedAnnealing as SA;
import lampProblem as LP;

number_of_lamps = 10;

LP.room_width = 100;
LP.room_height = 100;
LP.lamp_radius = 15;


boundaries = [];
for i in range(number_of_lamps):
    boundaries.append([0,LP.room_width-1]);
    boundaries.append([0,LP.room_height-1]);
    boundaries.append([0,1]);


optimiser = SA.SimulatedAnnealing(len(boundaries), boundaries, LP.fitnessFunction, 5000, 0.04);
optimiser.run(False, False);

# Store the best individual
LP.fitnessFunction(optimiser.best_solution);
cv2.imshow("Best solution", LP.overlay_image);
cv2.waitKey(0);
print(optimiser)
print(optimiser.best_solution);

