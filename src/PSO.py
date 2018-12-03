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
g_swarm       = []

particle  = PA.Particle()



# main() function
def main():

    global g_swarm
    global particle
    
    # Set the range for each particle
    boundaryset = []
    for i in range(g_Dimention):
        boundaryset.append([0,10])
    
    # Creat the swarm
    for i in range(g_swarm_size):
    
        particle.Particle(g_Dimention, boundaryset, 0.0, g_swarm)
        
        g_swarm.append(copy.deepcopy(particle.getPosition()))

        particle.printing()

    print("the swarm ", g_swarm)

# Call the main() function to begin the program.
if __name__ == '__main__':
    main()


