#!/usr/bin/env python3

#import cProfile

import math;

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

from EvolutionaryAlgorithm import *

# Selection operators
from TournamentSelection      import *
from RouletteWheel            import *
from RankSelection            import *

# Genetic operators
from ElitismOperator          import *
from BlendCrossoverOperator   import *
from GaussianMutationOperator import *
from NewBloodOperator         import *

g_number_of_individuals = 10;
g_iterations            = 20;
g_number_of_genes       = 2;

g_max_mutation_sigma = 0.5;
g_min_mutation_sigma = 0.01;

g_current_sigma = g_max_mutation_sigma;

g_boundaries = [];
for i in range(g_number_of_genes):
    g_boundaries.append([-5,5]);

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

# Print the current state in the console
def printCurrentStates(anIteration, anOptimiser):
    print("Iteration:\t", anIteration);
    print(optimiser);
    print();

def frange(start, stop, step):
    i = start
    while i < stop:
         yield i
         i += step

def createFigure():
    # Create the figure and axes
    fig = plt.figure();
    ax = fig.add_subplot(111, projection='3d');

    # Create the wireframe
    X = [];
    Y = [];
    Z = [];

    for y in frange(g_boundaries[0][0], g_boundaries[0][1], 0.05):
        #
        Temp_X = [];
        Temp_Y = [];
        Temp_Z = [];
        #
        for x in frange(g_boundaries[1][0], g_boundaries[1][1], 0.05):
            genes = [x, y];
            fitness = fitnessFunction(genes);
            Temp_X.append(x);
            Temp_Y.append(y);
            Temp_Z.append(-fitness);
        #
        X.append(Temp_X);
        Y.append(Temp_Y);
        Z.append(Temp_Z);

    # Plot a basic wireframe.
    ax.plot_wireframe(np.array(X), np.array(Y), np.array(Z), rstride=10, cstride=10)

    # Plot the current best
    scat1 = ax.scatter([], [], [], marker='o', c='r', s=30)

    # Plot the current population
    scat2 = ax.scatter([], [], [], marker='o', c='g', s=10)

    return fig, ax, scat1, scat2;

def update(i):
    global g_current_sigma;
    global optimiser;
    global gaussian_mutation;
    global scat1;

    # Print the current state in the console
    printCurrentStates(i, optimiser);

    # This is not the initial population
    if i != 0:
        # Make sure the mutation variance is up-to-date
        gaussian_mutation.setMutationVariance(g_current_sigma);

        # Run the optimisation loop
        optimiser.run();

        # Print the current state in the console
        printCurrentStates(i, optimiser);

        # Update the mutation variance so that it varies linearly from g_max_mutation_sigma to
        # g_min_mutation_sigma
        g_current_sigma -= (g_max_mutation_sigma - g_min_mutation_sigma) / (g_iterations - 1);

    # Best solution in red
    xdata1, ydata1, zdata1 = [], [], [];
    xdata1.append(optimiser.best_individual.genes[0]);
    ydata1.append(optimiser.best_individual.genes[1]);
    zdata1.append(-optimiser.best_individual.fitness);
    scat1._offsets3d = (xdata1, ydata1, zdata1)

    # All the current solution
    xdata2, ydata2, zdata2 = [], [], [];
    for individual in optimiser.individual_set:
        xdata2.append(individual.genes[0]);
        ydata2.append(individual.genes[1]);
        zdata2.append(-individual.fitness);
    scat2._offsets3d = (xdata2, ydata2, zdata2)

# Create an EA
optimiser = EvolutionaryAlgorithm(g_number_of_genes, g_boundaries, fitnessFunction, g_number_of_individuals)

# Set the selection operator
#optimiser.setSelectionOperator(TournamentSelection(2));
#optimiser.setSelectionOperator(RouletteWheel());
optimiser.setSelectionOperator(RankSelection());

# Create the genetic operators
elitism = ElitismOperator(0.1);
new_blood = NewBloodOperator(0.3);
gaussian_mutation = GaussianMutationOperator(0.1, 0.4);
blend_cross_over = BlendCrossoverOperator(0.5, gaussian_mutation);

# Add the genetic operators to the EA
optimiser.addGeneticOperator(new_blood);
optimiser.addGeneticOperator(gaussian_mutation);
optimiser.addGeneticOperator(blend_cross_over);
optimiser.addGeneticOperator(elitism);

# Create a figure (Matplotlib)
fig, ax, scat1, scat2 = createFigure();

# Run the visualisation
numframes = g_iterations + 1;
ani = animation.FuncAnimation(fig, update, frames=range(numframes), repeat=False)
plt.show()
