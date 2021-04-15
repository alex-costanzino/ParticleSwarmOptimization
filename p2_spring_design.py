'''
Alex Costanzino
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
March, 2021
'''

'''
The problem minimizes the weight of a tension/compression spring,
subject to:
- Constraints of minimum deflection,
- Shear stress,
- Surge frequency,
- Limits on outside diameter and on design variables.

There are three design variables:
- The wire diameter x_1,
- The mean coil diameter x_2,
- The number of active coils x_3.
'''

import particle_swarm_optimization_var as pso
import math
import numpy as np

def spring_design(x, it):
    t = 0
    for i in range(len(x)-2):
        t += (x[i+2] + 2)*x[i+1]*x[i]**2 + \
             math.sqrt(it)*(max(0,(1 - ((x[i+1]**3)*x[i+2]/(7.178*x[i]**4))))**2 + \
                            max(0,(((4*x[i+1]**2 - x[i]*x[i+1])/(12.566*(x[i+1]*x[i]**3) - x[i]**4)) + (1/(5.108*x[i]**2))))**2 + \
                            max(0,(1 - ((140.45*x[i])/(x[i+1]**2*x[i+2]))))**2 + \
                            max(0,(((x[i+1] + x[i])/1.5) - 1))**2)
            
    return t

if __name__ == "__main__":
    pen = 0.0000025
    initial_position = [12, 654, 54]              
    boundaries = [(0.05, 2.0), (0.25, 1.3), (10.0, 12.0)] 

    pso.optimize(spring_design, pen,
                 initial_position, boundaries,
                 n_particles = 1500, max_iter = 100)
    
    print("Expected: F(x) = 0.012665, at x = [0.051690, 0.356750, 11.287126]")

