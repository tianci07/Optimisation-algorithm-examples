import random
import numpy as np
import sys
import traceback
import random
import math
import copy

import Particle as PA


# Global variables
g_swarm_size  = 5
g_Dimention   = 3
g_repeatation = 10
Epsilon       = 0.00005

g_population  = PA.Particle()



# main() function
def main():

    global g_population

    # Set the range for the particle
    boundaryset = []
    for i in range(g_Dimention):
        boundaryset[i][0] = 0
        boundaryset[i][1] = 10

    print(boundaryset)
    # Creat the Swarm
    #for i in range(g_swarm_size):
    
        #g_population.Particle(g_Dimention,

# Call the main() function to begin the program.
if __name__ == '__main__':
    main()


