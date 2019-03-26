#!/usr/bin/env python3

#import cProfile

import math;

import numpy as np

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

import EvolutionaryAlgorithm  as EA
import Individual

g_number_of_individuals = 10;
g_iterations            = 20;
g_number_of_genes       = 2;

g_max_mutation_sigma = 0.5;
g_min_mutation_sigma = 0.01;

boundaries = [];
for i in range(g_number_of_genes):
    boundaries.append([-5,5]);

def fitnessFunction(aSolution):
    fitness = 0.0;
    #
    #for i in range(g_number_of_dimensions):
    #    sum += aSolution[i] * aSolution[i];
    #
    fitness += math.exp(-(math.pow(aSolution[0], 2) + math.pow(aSolution[1], 2)));
    fitness += 2.0 * math.exp(-(math.pow(aSolution[0]-1.7, 2) + math.pow(aSolution[1]-1.7, 2)));
    fitness *= -1.0;
    #
    return -fitness;

optimiser = EA.EvolutionaryAlgorithm(g_number_of_genes, boundaries, fitnessFunction, g_number_of_individuals)


def frange(start, stop, step):
    i = start
    while i < stop:
         yield i
         i += step


def plot(anOptimiser):
    global best_individual_x;
    global best_individual_y;
    global best_individual_z;

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = [];
    Y = [];
    Z = [];

    linear_x = [];
    linear_y = [];
    linear_z = [];

    for y in frange(boundaries[0][0], boundaries[0][1], 0.05):
        #
        Temp_X = [];
        Temp_Y = [];
        Temp_Z = [];
        #
        for x in frange(boundaries[1][0], boundaries[1][1], 0.05):
            genes = [x, y];
            energy = fitnessFunction(genes);
            Temp_X.append(x);
            Temp_Y.append(y);
            Temp_Z.append(-energy);
        #
        X.append(Temp_X);
        Y.append(Temp_Y);
        Z.append(Temp_Z);

    # Plot a basic wireframe.
    ax.plot_wireframe(np.array(X), np.array(Y), np.array(Z), rstride=10, cstride=10)

    numframes = len(best_individual_x)

    xdata1, ydata1, zdata1 = [], [], [];
    xdata2, ydata2, zdata2 = [], [], [];

    scat1 = ax.scatter([], [], [], marker='o', c='r', s=30) # Best solution
    scat2 = ax.scatter([], [], [], marker='o', c='g', s=10) # All the current solutions


    def update(i):
        global xdata1, ydata1, zdata1;
        global xdata2, ydata2, zdata2;

        global best_individual_x;
        global best_individual_y;
        global best_individual_z;

        global set_individual_set_x;
        global set_individual_set_y;
        global set_individual_set_z;

        xdata1, ydata1, zdata1 = [], [], [];

        # Best solution in red
        xdata1.append(best_individual_x[i]);
        ydata1.append(best_individual_y[i]);
        zdata1.append(best_individual_z[i]);

        # All the current solution
        xdata2 = set_individual_set_x[i];
        ydata2 = set_individual_set_y[i];
        zdata2 = set_individual_set_z[i];

        scat1._offsets3d = (xdata1, ydata1, zdata1)
        scat2._offsets3d = (xdata2, ydata2, zdata2)

        return

    ani = animation.FuncAnimation(fig, update, frames=range(numframes), repeat=False)
    plt.show()


best_individual_x = [];
best_individual_y = [];
best_individual_z = [];

set_individual_set_x = [];
set_individual_set_y = [];
set_individual_set_z = [];

for i in range(g_iterations):
    sigma = g_min_mutation_sigma + (g_iterations - 1 - i) / (g_iterations - 1) * (g_max_mutation_sigma - g_min_mutation_sigma);
    optimiser.run(sigma);

    # Store the best individual
    best_individual_x.append(optimiser.best_individual.genes[0])
    best_individual_y.append(optimiser.best_individual.genes[1])
    best_individual_z.append(-optimiser.best_individual.fitness)

    # Store the current swarm
    individual_set_x = [];
    individual_set_y = [];
    individual_set_z = [];

    for individual in optimiser.individual_set:
        individual_set_x.append(individual.genes[0])
        individual_set_y.append(individual.genes[1])
        individual_set_z.append(-individual.fitness)

    set_individual_set_x.append(individual_set_x);
    set_individual_set_y.append(individual_set_y);
    set_individual_set_z.append(individual_set_z);

print(optimiser)
print(optimiser.best_individual)

plot(optimiser)
