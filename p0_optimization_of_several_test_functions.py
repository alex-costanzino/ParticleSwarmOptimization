'''
Alex Costanzino
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
March, 2021
'''

''' A set of examples of optimization of some test functions, with their specific search domains and hyperparameters tuned. '''

import particle_swarm_optimization as pso
import test_functions as tf
from plotter import plot_fcn

''' Function that has several local minima. It is highly multimodal, but locations of the minima are regularly distributed. '''
def op_rastrigin():
    plot_fcn(tf.rastrigin)
    
    initial_position = [2, 3]              
    boundaries = [(-5.12, 5.12), (-5.12, 5.12)] 
    
    pso.optimize(tf.rastrigin, initial_position, boundaries, n_particles = 1500, max_iter = 300)
    print("Expected: F(x) = 0, at x = [0, 0]")

''' Function characterized by a nearly flat outer region, and a large hole at the centre. The function poses a risk for optimization algorithms, to be trapped in one of its many local minima. '''
def op_ackley():
    plot_fcn(tf.ackley)
    
    initial_position = [5, 5]              
    boundaries = [(-3.2768, 3.276), (-32.768, 32.768)] 
    
    pso.optimize(tf.ackley, initial_position, boundaries, n_particles = 1500, max_iter = 1500)
    print("Expected: F(x) = 0, at x = [0, 0]")

''' Nice valley-shaped function to test multivariate optimization, here proposed a 4-dimensional case with asymmetric search domains.'''
def op_rosenbrock():
    plot_fcn(tf.rosenbrock)
    
    initial_position = [2, 0 , 4, 0.5]              
    boundaries = [(-2.048, 3), (-1.845, 2.5), (-5, 10), (-2.3, 1.2)]
    
    pso.optimize(tf.rosenbrock, initial_position, boundaries, n_particles = 300, max_iter = 2000)
    print("Expected: F(x) = 0, at x = [1, 1, 1, 1]")

''' A multimodal function with sharp peaks at the corners of the input domain. Very precise search. '''    
def op_beale():
    plot_fcn(tf.beale)
    
    initial_position = [0, 0]              
    boundaries = [(-4.5, 4.5), (-4.5, 4.5)]
    
    pso.optimize(tf.beale, initial_position, boundaries, n_particles = 1500, max_iter = 300)
    print("Expected: F(x) = 0, at x = [3, 0.5]")

''' Function that has many local minima, all of which lie in a ridge. Hard to tune with PSO, computation requires time.'''
def op_bukin():
    plot_fcn(tf.bukin)
    
    initial_position = [-9, 0]              
    boundaries = [(-12, -8),(-2, 2)] 
    
    pso.optimize(tf.bukin, initial_position, boundaries, n_particles = 2500, max_iter = 2400)
    print("Expected: F(x) = 0, at x = [-10, 1]")

''' Function with many local minima. '''
def op_levi():
    plot_fcn(tf.levi)
    
    initial_position = [5, 5]              
    boundaries = [(-10, 10), (-10, 10)] 
    
    pso.optimize(tf.levi, initial_position, boundaries, n_particles = 700, max_iter = 220)
    print("Expected: F(x) = 0, at x = [1, 1]")

''' The function has several local minima. It is unimodal, and the global minimum has a small area relative to the search space. Very precise search. '''
def op_easom():
    plot_fcn(tf.easom)
    
    initial_position = [5, 5]              
    boundaries = [(-100, 100), (-100, 100)]
    
    pso.optimize(tf.easom, initial_position, boundaries, n_particles = 400, max_iter = 250)
    print("Expected: F(x) = -1, at x = [pi, pi]")

''' Difficult function to optimize, because of the large number of local minima.  
def op_eggholder():
    plot_fcn(tf.eggholder)

    initial_position = [500, 450]
    boundaries = [(-512, 512), (-512, 512)]

    pso.optimize(tf.eggholder, initial_position, boundaries, n_particles = 150, max_iter = 30)
    print("Expected: F(x) = -959.6407, at x = [512, 404.2319]")
'''

''' Plate-shaped function, search with asymmetric domains. Pretty fast and precise with PSO.'''
def op_cormick():
    plot_fcn(tf.cormick)
    
    initial_position = [0, 0]
    boundaries = [(-1.5, 4), (-3, 4)]
    
    pso.optimize(tf.cormick, initial_position, boundaries, n_particles = 500, max_iter = 400)
    print("Expected: F(x) = -1.9133, at x = [-0.54719, -1.54719]")

''' Function with many local minima and a large domain. '''
def op_schaffer():
    plot_fcn(tf.schaffer)
    
    initial_position = [5, 5]              
    boundaries = [(-100, 100), (-100, 100)]
    
    pso.optimize(tf.schaffer, initial_position, boundaries, n_particles = 1500, max_iter = 300)
    print("Expected: F(x) = 0, at x = [0, 0]")
