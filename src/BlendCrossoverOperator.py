import GeneticOperator
import Individual as IND


class BlendCrossoverOperator(GeneticOperator.GeneticOperator):

    # Contructor
    def __init__(self, aProbability, aMutationOperator = None):
        # Apply the constructor of the abstract class
        super().__init__(aProbability);

        # Set the name of the new operator
        self.__name__ = "Blend crossover operator";

        # Save the mutation operator
        self.mutation_operator = aMutationOperator;

    def apply(self, anEA):

        self.use_count += 1;
        
        # Select the parents from the population
        parent1_index = parent2_index = anEA.selection_operator.select(anEA.individual_set)

        # Make sure parent 1 is different from parent2
        while parent2_index == parent1_index:
            parent2_index = anEA.selection_operator.select(anEA.individual_set);

        # Perform the crossover
        child = anEA.BlendCrossover(parent1_index, parent2_index);

        # Mutate the child
        if self.mutation_operator != None:
            self.mutation_operator.mutate(child)

        return child;
