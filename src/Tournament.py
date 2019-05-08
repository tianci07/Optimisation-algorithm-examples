import random
import math
import copy
import Individual as IND
import EvolutionaryAlgorithm as EV

class :TournmentSelection

    def Select(self, aIndividualSet):

        max_ind = len(aIndividualSet) - 1;
        
        # Choose the first individual randomly
        best = random.randint(0, max_ind)
        
        # Choose the second individual randomly
        index = random.randint(0, max_ind)

        # Find the best individual depened on the fitness
        # (maxiumisation)
        # good individual
        if BestBad == 0:
            if (aIndividualSet[index].fitness > aIndividualSet[best].fitness):
                best = index
            
            elif (aIndividualSet[index].fitness < aIndividualSet[best].fitness):
                best = index

        # bad individual
        else:
            if (aIndividualSet[index].fitness < aIndividualSet[best].fitness):
                best = index
            
            elif (aIndividualSet[index].fitness > aIndividualSet[best].fitness):
                best = index
        
        # Return the index of the best individual
        return (best)


