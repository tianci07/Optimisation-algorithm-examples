import random
import math
import copy

class Particle:

    # Get a SystemRandom instance out of random package
    system_random = random.SystemRandom();

    def __init__(self, aNumberOfDimentions, aBoundarySet, aCostFunction, aPSO, aPosition = None, aVelocity = None):

        self.position = []
        self.velocity = []
        self.cost = float('inf')
        self.best_known_position = []
        self.best_known_cost = float('inf')

        # Store the boundary set
        # e.g. [[min_0, max_0][min_1, max_1][min_2, max_2]]
        self.boundary_set = copy.deepcopy(aBoundarySet);

        # Store the cost function
        self.cost_function = aCostFunction

        # Store the PSO
        self.pso = aPSO;

        # Copy the particle position and velocity
        if aPosition != None and aVelocity != None:
            if len(aPosition) == aNumberOfDimentions and len(aVelocity) == aNumberOfDimentions:
                self.position = copy.deepcopy(aPosition);
                self.velocity = copy.deepcopy(aVelocity);

        # Initialise the particle's position and velocity
        if len(self.position) == 0 or len(self.velocity) == 0:

            self.position = []
            self.velocity = []

            for i in range(aNumberOfDimentions):
                # Get the boundaries
                min_i = self.boundary_set[i][0];
                max_i = self.boundary_set[i][1];

                # Compute the position
                self.position.append(Particle.system_random.uniform(min_i, max_i));

                # Compute the velocity
                self.velocity.append((Particle.system_random.uniform(min_i, max_i) - self.position[i]) / 2.0);

        # Compute the cost function
        self.computeCostFunction();

    def copy(self):

        return (Particle(
                len(self.boundary_set),
                self.boundary_set,
                self.cost_function,
                self.pso,
                self.position,
                self.velocity));

    def computeCostFunction(self):
        # Compute the cost function
        self.cost = self.cost_function(self.position)

        # Update the particle's best known position if needed
        if self.best_known_cost > self.cost:
            self.best_known_cost = self.cost;
            self.best_known_position = copy.deepcopy(self.position);

        return self.cost;

    def update(self):
        self.updateVelocity();
        self.updatePosition();

    def updateVelocity(self):

        w =  1.0 / (2.0 * math.log(2.0))
        c = (1.0 / 2.0) + math.log(2.0)

        new_velocity = [];

        for pos_i, part_best_pos_i, swarm_best_pos_i, vel_i in zip(self.position, self.best_known_position, self.pso.best_solution.position, self.velocity):
            vel_i = w * vel_i + Particle.system_random.uniform(0.0, c) * (part_best_pos_i - pos_i) + Particle.system_random.uniform(0.0, c) * (swarm_best_pos_i - pos_i)

            new_velocity.append(vel_i);

        self.velocity = copy.deepcopy(new_velocity);


    def updatePosition(self):

        # for each partical update the position
        new_position = []

        for pos_i, vel_i in zip(self.position, self.velocity):
            pos_i += vel_i;
            new_position.append(pos_i)

        self.position = copy.deepcopy(new_position)

        self.computeCostFunction();

    def __repr__(self):
        value = "Position: ";
        value += ' '.join(str(e) for e in self.position)
        value += "\tVelocity: ";
        value += ' '.join(str(e) for e in self.velocity)
        value += "\tCost: ";
        value += str(self.cost);
        return value;
