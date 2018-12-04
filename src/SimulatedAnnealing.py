import math; # For exp
import copy; # For deepcopy
import random; # For uniform

class SimulatedAnnealing:


    def __init__(self, aNumberOfDimensions, aBoundarySet, aCostFunction, aTemperature = 10000, aCoolingRate = 0.003):

        # Initialise attributes
        self.best_energy = float("inf");
        self.best_solution = [];

        self.min_energy =  float("inf");
        self.max_energy = -float("inf");

        self.temperature_set = [];

        self.current_solution_set = [];
        self.best_solution_set = [];

        self.current_energy_set = [];
        self.best_energy_set = [];

        # and copy input parameters
        self.number_of_dimensions = aNumberOfDimensions;
        self.boundary_set = copy.deepcopy(aBoundarySet);
        self.cost_function = aCostFunction;
        self.initial_temperature = aTemperature;
        self.cooling_rate = aCoolingRate;

        # Create the current solution
        self.current_solution = [];
        for i in range(aNumberOfDimensions):
            self.current_solution.append(random.uniform(self.boundary_set[i][0], self.boundary_set[i][1]));

    def computeEnergy(self, aSolution):
        energy = self.cost_function(aSolution);
        self.min_energy = min(self.min_energy, energy);
        self.max_energy = max(self.max_energy, energy);
        return energy;

    def acceptanceProbability(self, aNewEnergy):
        # The new soluation is better, keep it
        if aNewEnergy < self.current_energy:
            return 1.0;
        # The new soluation is worse, calculate an acceptance probability
        else:
            return math.exp((self.current_energy - aNewEnergy) / self.current_temperature);

    def getRandomNeighbour(self, aSolution):
        new_solution = [];
        for i in range(self.number_of_dimensions):
            min_val = self.boundary_set[i][0];
            max_val = self.boundary_set[i][1];
            range_val = max_val - min_val;
            new_solution.append(random.gauss(min_val + range_val / 2, range_val * 0.1));

        return (copy.deepcopy(new_solution))

    def run(self, aRetartFlag = False, aVerboseFlag = False):

        self.current_temperature = self.initial_temperature;

        self.min_energy =  float("inf");
        self.max_energy = -float("inf");

        self.temperature_set = [];

        self.current_solution_set = [];
        self.best_solution_set = [];

        self.current_energy_set = [];
        self.best_energy_set = [];

        # Compute its energy using the cost function
        self.current_energy = self.computeEnergy(self.current_solution);

        # This is also the best solution so far
        self.best_solution = copy.deepcopy(self.current_solution);
        self.best_energy = self.current_energy;

        iteration = 0;
        if aVerboseFlag:
            header  = "iteration";
            header += " temperature";
            for i in range(self.number_of_dimensions):
                header += " best_solution[" + str(i) + "]";
            header += " best_solution_energy";
            for i in range(self.number_of_dimensions):
                header += " current_solution[" + str(i) + "]";
            header += " current_solution_energy";
            print(header);
            print (iteration, self.current_temperature, ' '.join(str(e) for e in self.best_solution), self.best_energy, ' '.join(str(e) for e in self.current_solution), self.current_energy)


        self.temperature_set.append(self.current_temperature);
        self.current_solution_set.append(self.current_solution);
        self.best_solution_set.append(self.best_solution);
        self.current_energy_set.append(self.current_energy);
        self.best_energy_set.append(self.best_energy);

        # Loop until system has cooled
        while self.current_temperature > 1.0:

            if aRetartFlag:
                if iteration != 0:
                    if (self.current_energy - self.min_energy) / (self.max_energy - self.min_energy) > 0.9:
                        #print("Restart")
                        self.current_solution = self.best_solution;
                        self.current_energy   = self.best_energy;

            # Create a new solution depending on the current solution,
            # i.e. a neighbour
            neighbour = self.getRandomNeighbour(self.current_solution);

            # Get its energy (cost function)
            neighbour_energy = self.computeEnergy(neighbour);

            # Accept the neighbour or not depending on the acceptance probability
            if self.acceptanceProbability(neighbour_energy) > random.uniform(0, 1):
                self.current_solution = copy.deepcopy(neighbour);
                self.current_energy = neighbour_energy;

            # The neighbour is better thant the current element
            if self.best_energy > self.current_energy:
                #print("Best energy was ", self.best_energy, "it is now ", self.current_energy)
                self.best_solution = copy.deepcopy(self.current_solution);
                self.best_energy = self.current_energy;

            iteration = iteration + 1;

            if aVerboseFlag:
                print (iteration, self.current_temperature, ' '.join(str(e) for e in self.best_solution), self.best_energy, ' '.join(str(e) for e in self.current_solution), self.current_energy)

            self.temperature_set.append(self.current_temperature);
            self.current_solution_set.append(self.current_solution);
            self.best_solution_set.append(self.best_solution);
            self.current_energy_set.append(self.current_energy);
            self.best_energy_set.append(self.best_energy);

            # Cool the system
            self.current_temperature *= 1.0 - self.cooling_rate;

        self.current_solution = copy.deepcopy(self.best_solution);
        self.current_energy = self.best_energy;


    def __repr__(self):
        value = "Best solution: ";
        value += ' '.join(str(e) for e in self.best_solution)
        value += "\tCorresponding cost: ";
        value += str(self.best_energy);
        return value;
