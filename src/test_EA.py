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

g_number_of_population = 10;
g_iterations           = 100;
g_number_of_genes      = 3;

boundaries = [];
for i in range(g_number_of_genes):
    boundaries.append([0,10]);


optimiser = EA.EvolutionaryAlgorithm(g_number_of_population, g_number_of_genes, boundaries)

print(optimiser)

'''
def frange(start, stop, step):
    i = start
    while i < stop:
         yield i
         i += step

def costFunction(aSolution):
    sum = 0.0;
    #
    #for i in range(g_number_of_dimensions):
    #    sum += aSolution[i] * aSolution[i];
    #
    sum += math.exp(-(math.pow(aSolution[0], 2) + math.pow(aSolution[1], 2)));
    sum += 2.0 * math.exp(-(math.pow(aSolution[0]-1.7, 2) + math.pow(aSolution[1]-1.7, 2)));
    sum *= -1.0;
    #
    return sum;


def plot(anOptimiser):
    global best_particle_x;
    global best_particle_y;
    global best_particle_z;

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
            position = [x, y];
            energy = costFunction(position);
            Temp_X.append(x);
            Temp_Y.append(y);
            Temp_Z.append(energy);
        #
        X.append(Temp_X);
        Y.append(Temp_Y);
        Z.append(Temp_Z);

    # Plot a basic wireframe.
    ax.plot_wireframe(np.array(X), np.array(Y), np.array(Z), rstride=10, cstride=10)

    numframes = len(best_particle_x)

    xdata1, ydata1, zdata1 = [], [], [];
    xdata2, ydata2, zdata2 = [], [], [];

    scat1 = ax.scatter([], [], [], marker='o', c='r', s=30) # Best solution
    scat2 = ax.scatter([], [], [], marker='o', c='g', s=10) # All the current solutions


    def update(i):
        global xdata1, ydata1, zdata1;
        global xdata2, ydata2, zdata2;

        global best_particle_x;
        global best_particle_y;
        global best_particle_z;

        global set_particle_set_x;
        global set_particle_set_y;
        global set_particle_set_z;

        xdata1, ydata1, zdata1 = [], [], [];

        # Best solution in red
        xdata1.append(best_particle_x[i]);
        ydata1.append(best_particle_y[i]);
        zdata1.append(best_particle_z[i]);

        # All the current solution
        xdata2 = set_particle_set_x[i];
        ydata2 = set_particle_set_y[i];
        zdata2 = set_particle_set_z[i];

        scat1._offsets3d = (xdata1, ydata1, zdata1)
        scat2._offsets3d = (xdata2, ydata2, zdata2)

        return

    ani = animation.FuncAnimation(fig, update, frames=range(numframes), repeat=False)
    plt.show()


optimiser = PSO(g_number_of_dimensions, boundaries, costFunction, g_number_of_particle);
best_particle_x = [];
best_particle_y = [];
best_particle_z = [];

set_particle_set_x = [];
set_particle_set_y = [];
set_particle_set_z = [];

for i in range(g_iterations):
    optimiser.run();

    # Store the best particle
    best_particle_x.append(optimiser.best_particle.position[0])
    best_particle_y.append(optimiser.best_particle.position[1])
    best_particle_z.append(optimiser.best_particle.cost)

    # Store the current swarm
    particle_set_x = [];
    particle_set_y = [];
    particle_set_z = [];

    for particle in optimiser.particle_set:
        particle_set_x.append(particle.position[0])
        particle_set_y.append(particle.position[1])
        particle_set_z.append(particle.cost)

    set_particle_set_x.append(particle_set_x);
    set_particle_set_y.append(particle_set_y);
    set_particle_set_z.append(particle_set_z);

plot(optimiser)
'''
