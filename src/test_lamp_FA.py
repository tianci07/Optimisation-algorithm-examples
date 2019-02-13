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

g_number_of_individuals = 10;
g_iterations            = 20;
g_max_mutation_sigma = 0.25;
g_min_mutation_sigma = 0.01;

number_of_lamps = g_number_of_individuals;

LP.room_width = 100;
LP.room_height = 100;
LP.lamp_radius = 15;


boundaries = [];
boundaries.append([0,LP.room_width-1]);
boundaries.append([0,LP.room_height-1]);
boundaries.append([0,1]);


def localFitnessFunction(aSetOfGenes, W=1):
    # aSetOfGenes[0]: position along the x-axis
    # aSetOfGenes[1]: position along the y-axis
    # aSetOfGenes[2]: on/off: if > 0.5, then the lamp is on

    local_fitness = 0;

    if aSetOfGenes[2] > 0.5:
        # Remove fly from image
        LP.addLampToImage(int(aSetOfGenes[0]), int(aSetOfGenes[1]), -1);
        global_fitness_without_fly = LP.computeFitnessFunction(1)
        LP.addLampToImage(int(aSetOfGenes[0]), int(aSetOfGenes[1]), 1);

        local_fitness = global_fitness_without_fly - LP.global_fitness;

    return local_fitness;




optimiser = EA.EvolutionaryAlgorithm(len(boundaries), boundaries, localFitnessFunction, g_number_of_individuals, LP.fitnessFunction);
#print(LP.global_fitness, optimiser)


for i in range(g_iterations):
    sigma = g_min_mutation_sigma + (g_iterations - 1 - i) / (g_iterations - 1) * (g_max_mutation_sigma - g_min_mutation_sigma);
    optimiser.run(sigma);
    #print(LP.global_fitness, "optimiser", optimiser)
    
    # Store the best individual
    #best_individual = optimiser.best_individual.genes;
    #LP.fitnessFunction(best_individual);
    cv2.imshow("Best individual so far", LP.overlay_image);
    cv2.imwrite("overlay_image" + str(i) + ".png",  LP.overlay_image)
    cv2.waitKey(1);
    #print(optimiser.best_individual);

# print population
population = optimiser.individual_set
for i in range(len(population)):

    print(population[i])

# Regenerate the image here
black_image = np.zeros((LP.room_height, LP.room_width, 1), np.float32)

for i in range(len(population)):

    x = int(population[i].genes[0])
    y = int(population[i].genes[1])
    on_off = population[i].genes[1]
    
    if on_off > 0.5:
        cv2.circle(black_image, (x,y), LP.lamp_radius, (1, 1, 1), -1)

cv2.imshow("Regenerate", black_image);


# print global fitness
print(LP.global_fitness)

# Save the image
cv2.imwrite("Final_image.png",  black_image)
cv2.waitKey(0);
