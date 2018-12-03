#!/usr/bin/env python3

import PSO;
import Particle;

g_number_of_dimensions = 3;

def costFunction(aPosition):
    
    #Compute the eqation (2x + y + 5z = 10)
    sum = (2.0 * aPosition[0]) + aPosition[1] + (5.0 * aPosition[2])
    
    return (abs(sum - 10))

boundaries = [[0, 10],[0, 10],[0, 10]];

#my_pso = PSO.PSO(number_of_particle, dimensions, boundaries, costFunction);
my_pso = PSO.PSO();

my_particle = Particle.Particle(g_number_of_dimensions, boundaries, costFunction, my_pso);
print(my_particle);

#solution = my_pso.run();
#print(solution);
#print(solution);
