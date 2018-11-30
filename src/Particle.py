import random;

class Particle:
    self.position = [];
    self.velocity = [];
    self.cost = float('inf');
    self.best_known_position = [];
    self.best_known_cost = float('inf');
    self.boundary_set = [];
    
    def Particle(self, aNumberOfDimentions, aBoundarySet, aCostFunction, aPSO):
        # Store the boundary set
        # e.g. [[min_0, max_0][min_1, max_1][min_2, max_2]]
        self.boundary_set = aBoundarySet;
        
        # Store the cost function
        self.cost_function = aCostFunction;
        
        # Store the PSO
        self.pso = aPSO;

        # Initialise the particle's position and velocity
        for i in range(aNumberOfDimentions):
            # Get the boundaries
            min_i = self.boundary_set[i][0];
            max_i = self.boundary_set[i][1];

            # Compute the position
            self.position.append(random.uniform(min_i, max_i));
        
            # Compute the velocity
            self.velocity.append((random.uniform(min_i, max_i) - self.position[i]) / 2.0)
            
            
        # Compute the cost function
        computeCostFunction();

    def computeCostFunction(self):
        # Compute the cost function
        self.cost = self.cost_function(self.position);
        
        # Update the particle's best known position if needed
        if self.best_known_cost > self.cost:
            self.best_known_cost = self.cost;
            self.best_known_position = self.position;

    def update(self):
        self.updateVelocity();
        self.updatePosition();
    
    def updateVelocity(self):
    
        w = 0.721
        c = 1.193
        for pos_i, part_best_pos_i, swarm_best_pos_i, vel_i in zip(self.position, self.best_known_position, self.pso.best_particle.position, self.velocity):
            vel_i = w * vel_i +
                             random.uniform(0.0, c) * (part_best_pos_i - pos_i) +
                             random.uniform(0.0, c) * (swarm_best_pos_i - pos_i) +

    def updatePosition(self):
        # for each partical update the position
        for pos_i, vel_i in zip(self.position, self.velocity):
            pos_i += vel_i;
        
    
    def print(self):
        # Print the position
        # Print the velocity
        # Print the cost
        # Print the position
