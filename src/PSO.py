import Particle as PA

class PSO:

    def __init__(self, aNumberOfDimensions, aBoundarySet, aCostFunction, aNumberOfParticles):
        print("__init__(self)")

        # Store the swarm
        self.particle_set = [];

        # Save the best particle at each iteration
        #self.best_particle_set = [];

        # and copy input parameters
        self.number_of_dimensions = aNumberOfDimensions;

        # Add a particle
        self.particle_set.append(PA.Particle(aNumberOfDimensions, aBoundarySet, aCostFunction, self))

        # Keep track of the best particle
        best_particle_index = 0;

        # Create the particles
        while len(self.particle_set) < aNumberOfParticles:
            self.particle_set.append(PA.Particle(aNumberOfDimensions, aBoundarySet, aCostFunction, self))

            # The new particle is better
            # Minimisation
            if self.particle_set[best_particle_index].cost > self.particle_set[-1].cost:
                best_particle_index = len(self.particle_set) - 1;

        # Store the best particle
        #self.best_particle_set.append(copy.deepcopy(best_particle))
        self.best_particle = self.particle_set[best_particle_index].copy();

    def run(self):

        # Keep track of the best particle
        best_cost = self.best_particle.cost;
        best_particle_index = -1;

        # For each partical
        for i in range(len(self.particle_set)):

            # update the particales' positions and velocities
            self.particle_set[i].update()

            # The new particle is better
            if best_cost > self.particle_set[i].cost:
                best_cost = self.particle_set[i].cost
                best_particle_index = i;

        # The new particle is better
        if best_particle_index != -1:
            self.best_particle = self.particle_set[best_particle_index].copy();

        return self.best_particle;
        #return self.best_particle_set[-1];



    def __repr__(self):
        value = ""

        for particle in self.particle_set:
            value += particle.__repr__();
            value += '\n';

        return value;
