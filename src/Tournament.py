import random
import math
import copy
import numpy
import Individual as ID
import EvolutionaryAlgorithm as EA
import SelectionOperator


class TournamentSelection(SelectionOperator.SelectionOperator):

    def __init__(self, aTournamentSize = 2):
        super().__init__("Tournament selection");
        self.tournament_size = aTournamentSize;

    def setTournamentSize():
        self.tournament_size = aTournamentSize;
        
    def getTournamentSize():
        return self.tournament_size;
    

    def preProcess(self, anIndividualSet):
        return
    
    def __str__(self):
        return super().__str__() + "\t" + "tournament_size:\t" + str(self.tournament_size);
        
    def __select__(self, anIndividualSet, aFlag): # aFlag == True for selecting good individuals,
                                                  # aFlag == False for selecting bad individuals,
        
        max_ind = len(anIndividualSet) - 1;

        fitness_set = [];
        for i in range(self.tournament_size):
            index = random.randint(0, max_ind)
            fitness = anIndividualSet[index].fitness
            fitness_set.append(fitness)
        
        # Find the best individual depending on the fitness
        # (maxiumisation)
        # good individual
        if aFlag == True:
            return numpy.argmax(fitness_set)
        # bad individual
        else:
            return numpy.argmin(fitness_set)


