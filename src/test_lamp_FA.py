#!/usr/bin/env python3

import math;
import copy;

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
LP.W = 2;

boundaries = [];
boundaries.append([0,LP.room_width-1]);
boundaries.append([0,LP.room_height-1]);
boundaries.append([0,1]);


def localFitnessFunction(aSetOfGenes):
    # aSetOfGenes[0]: position along the x-axis
    # aSetOfGenes[1]: position along the y-axis
    # aSetOfGenes[2]: on/off: if > 0.5, then the lamp is on

    local_fitness = 0;

    if True:
    #if aSetOfGenes[2] > 0.5:
        # Remove fly from image
        LP.addLampToImage(int(aSetOfGenes[0]), int(aSetOfGenes[1]), -1);
    
    global_fitness_without_fly = LP.computeFitnessFunction()

    if True:
    #if aSetOfGenes[2] > 0.5:
        LP.addLampToImage(int(aSetOfGenes[0]), int(aSetOfGenes[1]), 1);

        local_fitness = LP.global_fitness - global_fitness_without_fly;
        
        #print(global_fitness_without_fly, LP.global_fitness, local_fitness)

    return local_fitness;




optimiser = EA.EvolutionaryAlgorithm(len(boundaries), boundaries, localFitnessFunction, g_number_of_individuals, LP.fitnessFunction);

optimiser.elitism_probability     = 0.0;
optimiser.cross_over_probability  = 0.1;
optimiser.mutation_probability    = 0.5;
optimiser.new_blood_probability   = 0.3;

#print(LP.global_fitness, optimiser)

#for i in optimiser.individual_set:
#    print("\t", i)

# Store the current population as it is the best one so far
best_population_id      = 0;
best_population_fitness = optimiser.global_fitness;
best_population         = copy.deepcopy(optimiser.individual_set);
best_population_image   = copy.deepcopy(LP.overlay_image);
cv2.imwrite("best_population_0.png",    best_population_image)
cv2.imwrite("current_population_0.png", LP.overlay_image)


print(0, optimiser.global_fitness, best_population_fitness);

steady_state = True;

# Compute g_iterations new generations
for i in range(g_iterations):

    # Update sigma (it linearly decreases over time)
    sigma = g_min_mutation_sigma + (g_iterations - 1 - i) / (g_iterations - 1) * (g_max_mutation_sigma - g_min_mutation_sigma);
    
    # Compute the new generation
    if steady_state:
        for j in range(g_number_of_individuals):
            optimiser.deleteAdd(sigma);

            # The new population is better than the previous one
            if best_population_fitness < optimiser.global_fitness:
                best_population_id      = i;
                best_population_fitness = optimiser.global_fitness;
                best_population         = copy.deepcopy(optimiser.individual_set);
                best_population_image   = copy.deepcopy(LP.overlay_image);
                cv2.imwrite("best_population_"    + str(i) + "_" + str(j) + ".png",  best_population_image)
    else:
        optimiser.run(sigma);

        # The new population is better than the previous one
        if best_population_fitness < optimiser.global_fitness:
            best_population_id      = i;
            best_population_fitness = optimiser.global_fitness;
            best_population         = copy.deepcopy(optimiser.individual_set);
            best_population_image   = copy.deepcopy(LP.overlay_image);
            cv2.imwrite("best_population_"    + str(i) + ".png",  best_population_image)
    
    cv2.imwrite("current_population_" + str(i) + ".png",  LP.overlay_image)

    print(i, optimiser.global_fitness, best_population_id, best_population_fitness);
    
    cv2.waitKey(1);
    

# print the best population
for ind in best_population:

    print(ind)

# Regenerate the image here
final_image = np.zeros((LP.room_height, LP.room_width, 1), np.float32)
population  = copy.deepcopy(optimiser.individual_set);

for i in range(len(population)):

    x = int(population[i].genes[0])
    y = int(population[i].genes[1])
    on_off = population[i].genes[2]
    
    if on_off > 0.5:
        black_image = np.zeros((LP.room_height, LP.room_width, 1), np.float32)
        cv2.circle(black_image, (x,y), LP.lamp_radius, (1, 1, 1), -1)
        np.add(final_image, black_image, final_image);


cv2.imshow("Regenerate", final_image );


# print global fitness
print(LP.global_fitness)

# Save the image
cv2.imwrite("Final_image.png",  final_image)
cv2.waitKey(0);
