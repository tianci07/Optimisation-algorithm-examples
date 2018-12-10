import math; # For exp
import copy; # For deepcopy
import random; # For uniform

import Particle as PA

class PSO:

    def __init__(self, aNumberOfDimensions, aBoundarySet, aCostFunction, aNumberOfParticles):
        print("__init__(self)")

        # Store the swarm
        self.particle_set = [];

        # Save the best particle at each iteration
        self.best_particle_set = [];

        # and copy input parameters
        self.number_of_dimensions = aNumberOfDimensions;
        self.boundary_set = copy.deepcopy(aBoundarySet);

        # Keep track of the best particle
        best_particle = PA.Particle();

        # Create the particles
        for i in range(aNumberOfParticles):
            self.particle_set.append(PA.Particle())
            self.particle_set[-1].set(aNumberOfDimensions, aBoundarySet, aCostFunction, self)

            # The new particle is better
            if best_particle.cost > self.particle_set[-1].cost:
                best_particle = self.particle_set[-1];

        # Store the best particle
        self.best_particle_set.append(copy.deepcopy(best_particle))

    def run(self):

        # Keep track of the best particle
        best_particle = PA.Particle();

        # For each partical
        for particle in self.particle_set:

            # update the particales' positions and velocities
            particle.update()

            # The new particle is better
            if best_particle.cost > particle.cost:
                best_particle = particle;

        # Store the best particle
        self.best_particle_set.append(copy.deepcopy(best_particle))

        return self.best_particle_set[-1];



    def __repr__(self):
        value = "Best particle: ";
        value += self.best_particle_set[-1].__repr__();
        return value;
