#!/usr/bin/env python3

import math;

import numpy as np

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation


import SimulatedAnnealing as SA;






g_number_of_dimensions = 2;
boundaries = [];
for i in range(g_number_of_dimensions):
    boundaries.append([-5,5]);

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

    for best_solution, best_energy, current_solution, current_energy in zip(anOptimiser.best_solution_set, anOptimiser.best_energy_set, anOptimiser.current_solution_set, anOptimiser.current_energy_set):
        linear_x.append(best_solution[0]);
        linear_y.append(best_solution[1]);
        linear_z.append(best_energy);

    #    ax.scatter(   best_solution[0],    best_solution[1],    best_energy, c='r');
    #    ax.scatter(current_solution[0], current_solution[1], current_energy, c='g');

    # Plot a basic wireframe.
    ax.plot_wireframe(np.array(X), np.array(Y), np.array(Z), rstride=10, cstride=10)





    numframes = len(optimiser.best_solution_set)

    xdata1, ydata1, zdata1 = [], [], [];
    xdata2, ydata2, zdata2 = [], [], [];
    xdata3, ydata3, zdata3 = [], [], [];

    scat1 = ax.scatter([], [], [], marker='o', c='r', s=30) # Best solution
    scat2 = ax.scatter([], [], [], marker='o', c='g', s=10) # All the current solutions
    scat3 = ax.scatter([], [], [], marker='o', c='black', s=30) # The last current solution

    positions = [];
    def update(i):
        global xdata1, ydata1, zdata1;
        global xdata2, ydata2, zdata2;
        global xdata3, ydata3, zdata3;

        #positions.append([optimiser.best_solution_set[i][0], optimiser.best_solution_set[i][1], optimiser.best_energy_set[i]]);

        xdata1, ydata1, zdata1 = [], [], [];
        xdata3, ydata3, zdata3 = [], [], [];

        if i == 0:
            xdata2, ydata2, zdata2 = [], [], [];


        #xdata1, ydata1, zdata1 = [], [], [];

        # Best solution in red
        xdata1.append(optimiser.best_solution_set[i][0]);
        ydata1.append(optimiser.best_solution_set[i][1]);
        zdata1.append(optimiser.best_energy_set[i]);

        # All the current solution
        xdata2.append(optimiser.current_solution_set[i][0]);
        ydata2.append(optimiser.current_solution_set[i][1]);
        zdata2.append(optimiser.current_energy_set[i]);

        # The last current solution
        xdata3.append(optimiser.current_solution_set[i][0]);
        ydata3.append(optimiser.current_solution_set[i][1]);
        zdata3.append(optimiser.current_energy_set[i]);

        scat1._offsets3d = (xdata1, ydata1, zdata1)
        scat2._offsets3d = (xdata2, ydata2, zdata2)
        scat3._offsets3d = (xdata3, ydata3, zdata3)

        return

    ani = animation.FuncAnimation(fig, update, frames=range(numframes), repeat=False)
    plt.show()



optimiser = SA.SimulatedAnnealing(g_number_of_dimensions, boundaries, costFunction, 5000, 0.1);
optimiser.run(False, False);
print(optimiser)
plot(optimiser);

exit();