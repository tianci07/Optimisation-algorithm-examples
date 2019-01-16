
import random
import Individual as IND

class EvolutionaryAlgorithm:

    def __init__(self, aNumberOfGenes, aBoundarySet, aFitnessFunction, aNumberOfIndividuals, aGlobalFitnessFunction = 0):

        # Probability of operators
        self.cross_over_probability  = 0.8;
        self.mutation_probability  = 0.0;
        self.new_blood_probability  = 0.2;
        
        #Set the individual operater
        self.genes_number = aNumberOfGenes
        self.boundary_set = aBoundarySet
        self.local_fitness = aFitnessFunction

        # Store the population
        self.individual_set = [];

        # Keep track of the best individual
        self.individual_set.append(IND.Individual(aNumberOfGenes, aBoundarySet, aFitnessFunction));

        # Create the population
        while (len(self.individual_set) < aNumberOfIndividuals):
            self.individual_set.append(IND.Individual(aNumberOfGenes, aBoundarySet, aFitnessFunction))

        # Compute the global fitness
        self.global_fitness = 0;
        self.global_fitness_function = 0;
        if aGlobalFitnessFunction:

            set_of_individuals = [];
            for ind in self.individual_set:
                for gene in ind.genes:
                    set_of_individuals.append(gene);

            self.global_fitness_function = aGlobalFitnessFunction;
            self.global_fitness = self.global_fitness_function(set_of_individuals);
            print (self.global_fitness)

        # Compute the fitness value of all the individual
        # And keep track of who is the best individual
        best_individual_index = 0;
        for i in range(len(self.individual_set)):
            self.individual_set[i].computeFitnessFunction();
            if (self.individual_set[best_individual_index].fitness < self.individual_set[i].fitness):
                best_individual_index = i;

        # Store the best individual
        self.best_individual = self.individual_set[best_individual_index].copy();

    '''
    def BestIndividual(self):

        best_individual = IND.Individual()
        best_individual = self.individual_set[0]

        # Find the best individual in the popoulation
        for best_ind in self.individual_set:

            if (best_individual.fitness > best_ind.fitness):

                best_individual.copy(best_ind)

        return best_individual
        '''

    def run(self, aMutationRate):

        offspring_population = [];

        offspring_population.append(self.best_individual.copy())
        best_individual_index = 0;

        # Evolutionary loop
        while (len(offspring_population) < len(self.individual_set)):

            # Draw a random number between 0 and 1
            chosen_operator = random.uniform(0.0, 1.0)
            
            # Crossover
            if (chosen_operator < self.cross_over_probability):

                # Select the parents from the population
                parent1_index = parent2_index = self.TournmentSelection()

                # Make sure parent 1 is different from parent2
                while parent2_index == parent1_index:
                    parent2_index = self.TournmentSelection();

                # Perform the crossover
                offspring_population.append(self.BlendCrossover(parent1_index, parent2_index));

                # Mutate the child
                offspring_population[-1].gaussianMutation(aMutationRate)

            # Mutation only
            elif (chosen_operator < self.cross_over_probability +  self.mutation_probability ):
    
                # Select the parents from the population
                parent_index = self.TournmentSelection()
                
                # Copy the parent into a child
                offspring_population.append(self.set_of_individuals[parent_index]);

                # Mutate the child
                offspring_population[-1].gaussianMutation(aMutationRate)

            # New blood
            else:
                offspring_population.append(IND.Individual(self.genes_number, self.boundary_set, self.local_fitness))


        # Compute the global fitness
        if self.global_fitness:

            set_of_individuals = [];
            for ind in self.individual_set:
                for gene in ind.genes:
                    set_of_individuals.append(gene);

            self.global_fitness = self.global_fitness_function(set_of_individuals);

        # Compute the fitness value of all the individual
        # And keep track of who is the best individual
        best_individual_index = 0;
        for i in range(len(offspring_population)):
            offspring_population[i].computeFitnessFunction();
            if (offspring_population[best_individual_index].fitness < offspring_population[i].fitness):
                best_individual_index = i;

        # Replace the parents by the offspring
        self.individual_set = offspring_population;

        # Store the best individual
        self.best_individual = self.individual_set[best_individual_index].copy();

        # Return the best individual
        return self.best_individual;

    def TournmentSelection(self):

        max_ind = len(self.individual_set) - 1;

        # Choose the first individual randomly
        best = random.randint(0, max_ind)

        # Choose the second individual randomly
        index = random.randint(0, max_ind)

        # Find the best individual depened on the fitness
        # (maxiumisation)
        if (self.individual_set[index].fitness > self.individual_set[best].fitness):
            best = index

        # Return the index of the best individual
        return (best)

    def BlendCrossover(self, aParent1Index, aParent2Index):

        child_gene = [];

        for p1_gene, p2_gene in zip(self.individual_set[aParent1Index].genes, self.individual_set[aParent2Index].genes):

            alpha = random.uniform(0.0, 1.0);
            child_gene.append(alpha * p1_gene + (1.0 - alpha) * p2_gene);


        return IND.Individual(
                len(child_gene),
                self.individual_set[aParent1Index].boundary_set,
                self.individual_set[aParent1Index].fitness_function,
                child_gene
        );


    def __repr__(self):
        value = ""

        for ind in self.individual_set:
            value += ind.__repr__();
            value += '\n';

        return value;
