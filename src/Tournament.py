import random
import math
import copy
import numpy
import Individual as ID
import EvolutionaryAlgorithm as EA

class TournamentSelection:

    def __init__(self, aTournamentSize = 2):
        self.tournament_size = aTournamentSize;

    def setTournamentSize():
        self.tournament_size = aTournamentSize;
        
    def getTournamentSize():
        return self.tournament_size;
    
    def select(self, anIndividualSet):
        return self.selectGood(anIndividualSet);
        
    def selectGood(self, anIndividualSet):
        return self.__select__(anIndividualSet, True);

    def selectBad(self, anIndividualSet):
        return self.__select__(anIndividualSet, False);
    
    def preProcess(self, anIndividualSet):
        return
        
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


