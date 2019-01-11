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
import EvolutionaryAlgorithm as EA;
import lampProblem as LP;

g_number_of_individuals = 5;
g_iterations            = 20;
g_max_mutation_sigma = 0.25;
g_min_mutation_sigma = 0.01;

number_of_lamps = 10;

LP.room_width = 100;
LP.room_height = 100;
LP.lamp_radius = 15;


boundaries = [];
for i in range(number_of_lamps):
    boundaries.append([0,LP.room_width-1]);
    boundaries.append([0,LP.room_height-1]);
    boundaries.append([0,1]);



optimiser = EA.EvolutionaryAlgorithm(len(boundaries), boundaries, LP.fitnessFunction, g_number_of_individuals);


for i in range(g_iterations):
    sigma = g_min_mutation_sigma + (g_iterations - 1 - i) / (g_iterations - 1) * (g_max_mutation_sigma - g_min_mutation_sigma);
    optimiser.run(sigma);
    
    # Store the best individual
    best_individual = optimiser.best_individual.genes;
    LP.fitnessFunction(best_individual);
    cv2.imshow("Best individual so far", LP.overlay_image);
    cv2.waitKey(1);
    print(optimiser.best_individual);
    
print(optimiser)

