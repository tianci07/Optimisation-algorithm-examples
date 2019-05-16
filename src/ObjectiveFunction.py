import copy

class ObjectiveFunction:
    def __init__(self,
                 aNumberOfDimensions,
                 aBoundarySet,
                 anObjectiveFunction,
                 aFlag = 0):

        # aFlag is 1 for Minimisation
        # aFlag is 2 for Maximisation
        self.boundary_set = copy.deepcopy(aBoundarySet);
        self.number_of_dimensions = aNumberOfDimensions;
        self.objective_function = anObjectiveFunction;
        self.number_of_evaluation = 0;
        self.flag = aFlag;

    def evaluate(self, aParameterSet, aFlag):
        self.number_of_evaluation += 1;

        objective_value = self.objective_function(aParameterSet);
        if aFlag != self.flag:
            objective_value *= -1;

        return objective_value;
