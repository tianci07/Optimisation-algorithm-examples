import math; # For exp
import copy; # For deepcopy
import random; # For uniform

import Particle as PA

class PSO:

    def __init__(self, aNumberOfDimensions, aBoundarySet, aCostFunction, aNumberOfParticles):
        print("__init__(self)")
        # Initialise attributes
        self.particle_set = [];
        # Save the best partical
        self.best_particle_set = [];
        self.best_cost_set = [];

        print("PSO(...)")
        # Initialise attributes
        self.particle_set = [];

        # Save the best partical
        self.best_particle_set = [];
        self.best_cost_set = [];

        # and copy input parameters
        self.number_of_dimensions = aNumberOfDimensions;
        self.boundary_set = copy.deepcopy(aBoundarySet);
        #self.cost_function = aCostFunction;

        # Create the particles
        for i in range(aNumberOfParticles):
            self.particle_set.append(PA.Particle())
            self.particle_set[-1].set(aNumberOfDimensions, aBoundarySet, aCostFunction, self)

            if len(self.best_cost_set) == 0:
                self.best_cost_set.append(self.particle_set[-1].cost)
                self.best_particle_set.append(copy.deepcopy(self.particle_set[-1].position))

            elif self.best_cost_set[-1] > self.particle_set[-1].cost:
                self.best_cost_set.append(self.particle_set[-1].cost)
                self.best_particle_set.append(copy.deepcopy(self.particle_set[-1].position))

    def run(self):

        # For each partical
        for particle in self.particle_set:

            # update the particales' positions and velocities
            particle.update()

            if len(self.best_cost_set) == 0:
                self.best_cost_set.append(particle.cost)
                self.best_particle_set.append(copy.deepcopy(particle.position))

            elif self.best_cost_set[-1] > self.particle_set[-1].cost:
                self.best_cost_set.append(particle.cost)
                self.best_particle_set.append(copy.deepcopy(particle.position))

        return self.best_particle_set[-1]

    def __repr__(self):
        value = "Best particle: ";
        value += ' '.join(str(e) for e in self.best_particle_set[-1])
        value += "\tCorresponding cost: ";
        value += str(self.best_cost_set[-1]);
        return value;
