#!/usr/bin/env python3

import math;

import numpy as np

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation


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
print(optimiser)
