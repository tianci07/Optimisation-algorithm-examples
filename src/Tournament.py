import random
import math
import copy
import Individual as ID
import EvolutionaryAlgorithm as EA

class TournmentSelection:

    def __init__(self):
        
        self.individual_set = EA.EvolutionaryAlgorithm()
    

    def Select(self, self.individual_set):

        max_ind = len(self.individual_set) - 1;
        
        # Choose the first individual randomly
        best = random.randint(0, max_ind)
        
        # Choose the second individual randomly
        index = random.randint(0, max_ind)

        # Find the best individual depened on the fitness
        # (maxiumisation)
        # good individual
        if BestBad == 0:
            if (self.individual_set[index].fitness > self.individual_set[best].fitness):
                best = index
            
            elif (self.individual_set[index].fitness < self.individual_set[best].fitness):
                best = index

        # bad individual
        else:
            if (self.individual_set[index].fitness < self.individual_set[best].fitness):
                best = index
            
            elif (self.individual_set[index].fitness > self.individual_set[best].fitness):
                best = index
        
        # Return the index of the best individual
        return (best);


