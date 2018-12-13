
import random
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
    
    def NewGeneration(self):
    
        offspring_ppopulation = []
        offspring_ppopulation.append(self.best_individual)
        # Genetic operatore
        #while (len(offspring_ppopulation) < len(self.individual_set)):
    
        # Select the parent from the population
        offspring1 = self.TournmentSelection()
        offspring2 = self.TournmentSelection()
        print("offspring1 ", offspring1)
        print("offspring2 ", offspring2)
        print()
        self.Crossover(offspring1, offspring2)
    
        print("offspring1 ", offspring1)
        print("offspring2 ", offspring2)
    
    def TournmentSelection(self):
    
        # Choose the first individual randomly
        max_ind = self.individual_set[0].boundary_set[0][1]
        best = random.randint(0, max_ind-1)
    
        # Choose the second individual randomly
        index = random.randint(0, max_ind-1)
    
        # Find the best individual depened on the fitness
        if (self.individual_set[index].fitness < self.individual_set[best].fitness):
            best = index

        # Return the best individual
        return (self.individual_set[best])
    
    def Crossover(self, aOffspring1, aOffspring2):
    
        ind_len = len(self.individual_set[0].genes)
        # Choose random position for crossover
        crossover_cut = random.randint(0, ind_len)
        print("crossover_cut: ", crossover_cut)

        offspring1 = aOffspring1
        offspring2 = aOffspring2

        for i in range(ind_len-1):
            #Replace the genes
            if (i == crossover_cut):
                offspring1.genes.append(aOffspring2.genes[i])
                offspring2.genes.append(aOffspring1.genes[i])
            else:
                offspring1.genes.append(aOffspring1.genes[i])
                offspring2.genes.append(aOffspring2.genes[i])

        aOffspring1.copy(offspring1)
        aOffspring2.copy(offspring2)
    
    
    def __repr__(self):
        value = "The population: "
        value += ' '.join(str(e) for e in self.individual_set)
        value += "\tBest Individual: ";
        value += self.best_individual.__repr__();
        return value;
