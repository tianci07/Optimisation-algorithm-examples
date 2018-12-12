import Individual as IND

class EvolutionaryAlgorithm:

    def __init__(self, aNumberOfPopulation, aNumberOfGenes, aBoundarySet):
        print("__init__(self)")

        # Store the population
        self.individual_set = [];

        # Keep track of the best individual
        best_individual = IND.Individual();
        self.best_individual = IND.Individual();

        # Create the population
        for i in range(aNumberOfPopulation):
            
            self.individual_set.append(IND.Individual())
            self.individual_set[-1].setIndividual(aNumberOfGenes, aBoundarySet)

        # Find the best individual
        best_individual = self.BestIndividual()
        self.best_individual.copy(best_individual)
    
    def BestIndividual(self):
        
        best_individual = IND.Individual()
        best_individual = self.individual_set[0]
        
        # Find the best individual in the popoulation
        for best_ind in self.individual_set:

            if (best_individual.fitness > best_ind.fitness):
        
                best_individual.copy(best_ind)
    
        return best_individual
        

    def __repr__(self):
        value = "The population: "
        value += ' '.join(str(e) for e in self.individual_set)
        value += "\tBest Individual: ";
        value += self.best_individual.__repr__();
        return value;