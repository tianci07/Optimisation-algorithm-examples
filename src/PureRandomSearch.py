import random
import copy
from RotateBones import bone_rotation

class PureRandomSearch:
    '''
    @parameters:
    aNumberOfDimensions: Number of variables.
    aBoundarySet: bounds for each parameters.
    anObjectiveFunction: Objective function used in optimisation
    aFlag: 0 for errors (minimising erros), 1 for SSIM and ZNCC (maximising index score).
    iterations: number of iterations for optimisation.
    '''
    def __init__(self,
                 aNumberOfDimensions,
                 aBoundarySet,
                 anObjectiveFunction,
                 aFlag,
                 iterations=100
                 ):

        self.number_of_dimensions = aNumberOfDimensions;
        self.boundaries = copy.deepcopy(aBoundarySet);
        self.objective_function = anObjectiveFunction;
        self.niter = iterations;
        self.flag = aFlag;

        if self.flag == 0:
            self.error = 1;
            print('Minimising...');
        else:
            self.error = 0;
            print('Maximising...');

        # Initialse rotating angle sets
        self.angles = [];
        for i in range(self.number_of_dimensions-2):
            self.angles.append(0);

        # Initialise temporary and final solution sets
        self.best_solution = [];
        self.params = [];
        for i in range(self.number_of_dimensions):
            self.params.append(0);
            self.best_solution.append(0);

        self.optimise();

    def optimise(self):

        for i in range(self.niter):
            SOD = random.uniform(self.boundaries[0][0], self.boundaries[0][1]);
            SDD = random.randint(self.boundaries[1][0], self.boundaries[1][1]);
            SOD = round(SOD*SDD);
            self.params[0] = SOD;
            self.params[1] = SDD;

            self.best_error = self.objective_function(self.params);

            if self.error == 1:

                if self.best_error < self.error:

                    self.error = self.best_error;
                    self.best_solution[0] = self.params[0];
                    self.best_solution[1] = self.params[1];

            else:

                if self.best_error > self.error:

                    self.error = self.best_error;
                    self.best_solution[0] = self.params[0];
                    self.best_solution[1] = self.params[1];

        for j in range(3):

            self.params[2+j] = random.randint(-10, 10);

        for m in range(self.niter):

             self.best_error = self.objective_function(self.params);

             if self.flag == 0:
                 self.error = 1;
             else:
                 self.error = 0;

             if self.error == 1:

                 if self.best_error < self.error:

                     self.error = self.best_error;
                     for n in range(3):
                         self.best_solution[2+n] = self.params[2+n];


             else:

                 if self.best_error > self.error:

                     self.error = self.best_error;
                     for n in range(3):
                         self.best_solution[2+n] = self.params[2+n];

        for n in range(self.niter):

            for l in range(self.number_of_dimensions-5):

                self.params[5+l] = random.randint(-10, 10);

            self.best_error = self.objective_function(self.params);

            if self.flag == 0:
                self.error = 1;
            else:
                self.error = 0;

            if self.error == 1:

                if self.best_error < self.error:

                    self.error = self.best_error;
                    for k in range(self.number_of_dimensions-5):
                        self.best_solution[5+k] = self.params[5+k];


            else:

                if self.best_error > self.error:

                    self.error = self.best_error;
                    for k in range(self.number_of_dimensions-5):
                        self.best_solution[5+k] = self.params[5+k];
