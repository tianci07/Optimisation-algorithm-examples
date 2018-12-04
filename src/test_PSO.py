#!/usr/bin/env python3

import PSO;
import Particle;

g_number_of_dimensions = 3;
g_number_of_particle   = 10;
g_iteratio             = 10;

def costFunction(aPosition):
    
    #Compute the eqation (2x + y + 5z = 10)
    sum = (2.0 * aPosition[0]) + aPosition[1] + (5.0 * aPosition[2])
    
    return (abs(sum - 10))

boundaries = [[0, 10],[0, 10],[0, 10]];

my_pso = PSO.PSO(g_number_of_dimensions, boundaries, costFunction, g_number_of_particle);
my_pso = PSO.PSO();

my_particle = Particle.Particle(g_number_of_dimensions, boundaries, costFunction, my_pso);
print(my_particle);
print()
print(my_pso)

#solution = my_pso.run(g_iteratio);
#print(solution);
#print(solution);
