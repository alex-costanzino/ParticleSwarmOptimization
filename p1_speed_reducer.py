'''
Alex Costanzino
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
March, 2021
'''

'''
The design of a speed reducer, is considered with:
- The face width x_1;
- Module of teeth x_2;
- Number of teeth on pinion x_3;
- Length of the first shaft between bearings x_4;
- Length of the second shaft between bearings x_5;
- Diameter of the first shaft x_6;
- Diameter of the second shaft x_7.

The weight of the speed reducer is to be minimized subject to constraints on:
- Bending stress of the gear teeth;
- Surface stress;
- Transverse deflections of the shafts and stresses in the shaft.
'''

import particle_swarm_optimization_var as pso
import math
import numpy as np

def speed_reducer(x, it):
    t = 0
    for i in range(len(x)-6):
        t += 0.7854*x[i]*x[i+1]**2*(3.3333*x[i+2]**2 + 14.9334*x[i+2] - 43.0934) - \
             1.508*x[i]*(x[i+5]**2 + x[i+6]**2) + 7.4777*(x[i+5]**3 + x[i+6]**3) + \
             0.7854*(x[i+3]*x[i+5]**2 + x[i+4]*x[i+6]**2) + \
             math.sqrt(it)*(max(0,((27/(x[i]*x[i+1]**2*x[i+2])) - 1))**2 + \
                            max(0,((397.5/(x[i]*x[i+1]**2*x[i+2]**2)) - 1))**2 + \
                            max(0,(((1.93*x[i+3]**3)/(x[i+1]*x[i+2]*x[i+5]**4)) - 1))**2 + \
                            max(0,(((1.93*x[i+4]**3)/(x[i+1]*x[i+2]*x[i+6]**4)) - 1))**2 + \
                            max(0,((x[i+1]*x[i+2])/40 - 1))**2 + \
                            max(0,((5*x[i+1])/x[i] - 1))**2 + \
                            max(0,((x[i])/12*x[i+1] - 1))**2 + \
                            max(0,((1.5*x[i+5] + 1.9)/x[i+3] - 1))**2 + \
                            max(0,((1.1*x[i+6] + 1.9)/x[i+4] - 1))**2 + \
                            max(0,((1/(110*x[i+5]**3))*math.sqrt((745*x[i+3]/x[i+1]*x[i+2])**2 + 16900000) - 1))**2 + \
                            max(0,((1/(85*x[i+6]**3))*math.sqrt((745*x[i+4]/x[i+1]*x[i+2])**2 + 157500000) - 1))**2)
    return t

if __name__ == "__main__":
    pen = 0.47474747474
    initial_position = [51, 645, 12, 65, 14, 87, 27]              
    boundaries = [(2.6, 3.6), (0.7, 0.8), (17, 28), (7.3, 8.3), (7.8, 8.3), (2.9, 3.9), (5.0, 5.5)] 

    pso.optimize(speed_reducer, pen, initial_position, boundaries, n_particles = 150, max_iter = 150)
    print("Expected: F(x) = 2996.348165, at x = [2.500000, 0.7, 17, 7.300000, 7.800000, 3.350214, 5.286683]")

'''
Improvement:
- Adaptative PSO (change inertia and social and congitive terms at runtime);
- Use of barrier function;
'''