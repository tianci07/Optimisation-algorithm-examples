import math; # For exp
import copy; # For deepcopy
import random; # For uniform

import Particle as PA

class PSO:
    
    
    def __init__(self, aNumberOfDimensions, aBoundarySet, aCostFunction, aNumberOfParticles):
        
        # Initialise attributes
        self.particle_set = [];
        self.best_particle_set = [];
        self.best_cost_set = [];
        self.best_cost = float('inf')
        
        # and copy input parameters
        self.number_of_dimensions = aNumberOfDimensions;
        self.boundary_set = copy.deepcopy(aBoundarySet);
        #self.cost_function = aCostFunction;

        # Create the particles
        for i in range(aNumberOfParticles):
            self.particle_set.append(PA.Particle(aNumberOfDimensions, aBoundarySet, aCostFunction, self))

    def computeCost(self, aParticle):
        
        if self.best_cost > aParticle.cost:
            self.best_cost = aParticle.cost;
            self.best_particle = PA.Particle(aParticle);
            self.best_particle_set.append(copy.deepcopy(aParticle.position))
            self.best_cost_set.append(cost)

        return cost;
   
    def run(self):
        # For each partical
        for i in range(aNumberOfParticles):
            # update the particales' positions and velocities
            Particle.update()

            if (self.best_cost_set[i] < self.best_cost):
                #Update partical's best known position
                self.best_particle = self.best_particle_set[i]

                if (self.best_cost < self.best_cost_set[i+1]):
                    # Update the swarm's best known position
                    self.best_cost_set[i+1] = self.best_cost


                
    
    def __repr__(self):
        value = "Best particle: ";
        value += ' '.join(str(e) for e in self.best_particle)
        value += "\tCorresponding cost: ";
        value += str(self.best_cost);
        return value;


'''import random
import numpy as np
import sys
import traceback
import random
import math
import copy

import Particle as PA


# Global variables
g_swarm_size  = 5
g_Dimention   = 3
g_repeatation = 10
Epsilon       = 0.00005
g_swarm       = []

particle  = PA.Particle()



# main() function
def main():

    global g_swarm
    global particle
    
    # Set the range for each particle
    boundaryset = []
    for i in range(g_Dimention):
        boundaryset.append([0,10])
    
    # Creat the swarm
    for i in range(g_swarm_size):
    
        particle.Particle(g_Dimention, boundaryset, 0.0, g_swarm)
        
        g_swarm.append(copy.deepcopy(particle.getPosition()))

        particle.printing()

    print("the swarm ", g_swarm)

# Call the main() function to begin the program.
if __name__ == '__main__':
    main()
'''

