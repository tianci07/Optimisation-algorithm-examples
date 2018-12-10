#!/usr/bin/env python3

import math;

import numpy as np

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

from PSO import PSO
import Particle

g_number_of_dimensions = 3;
g_number_of_particle   = 10;
g_iteratio             = 100;


def costFunction(aPosition):

    #Compute the eqation (2x + y + 5z = 10)
    sum = (2.0 * aPosition[0]) + aPosition[1] + (5.0 * aPosition[2])

    return (abs(sum - 10))

boundaries = []

for i in range(g_number_of_dimensions):
    boundaries.append([0,10]);

#my_particle = my_particle.Particle(g_number_of_dimensions, boundaries, costFunction, my_pso);

my_pso = PSO(g_number_of_dimensions, boundaries, costFunction, g_number_of_particle);
#my_pso = PSO.PSO();


#print(my_particle);
#print()
print(my_pso)

# Run the algorithm for 100 iteration
for i in range(g_iteratio):
    solution = my_pso.run();

    position_x = [];
    position_y = [];
    position_z = [];

    for particle in my_pso.particle_set:
        position_x.append(particle.position[0]);
        position_y.append(particle.position[1]);
        position_z.append(particle.position[2]);

    # Plot here the swarm


    print(i, solution);
#print(solution);
print(my_pso)
