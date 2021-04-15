'''
Alex Costanzino
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
March, 2021
'''

import random

class Particle:
    def __init__(self, x0):
        self.velocity = list()
        
        self.position = list()
        self.best_position = list()
        
        # Default values to force the first iteration
        self.fitness = -1
        self.best_fitness = -1
        
        ''' Initialize random velocity and the user-defined initial position '''
        for i in range(0, swarm_dimension):
            self.velocity.append(random.uniform(-1,1))
            self.position.append(x0[i])
        
    def evaluation(self, fitness):
        ''' Compute the value of the fitness function at the current position '''
        self.fitness = fitness(self.position)
        
        ''' Chech if the current position is better than the previous, if so update the best position and the best fitness '''
        if (self.fitness < self.best_fitness) or (self.best_fitness == -1):
            self.best_position = self.position
            self.best_fitness = self.fitness
            
    def update_velocity(self, swarm_best_position):
        ''' Hyperparameters setup: inertia, cognitive term, social term '''
        omega, phi_c, phi_s = 0.25, 2, 4
    
        for i in range(0, swarm_dimension):
            rand1, rand2 = random.random(), random.random()
            
            ''' Cognitive velocity is based on the individual behaviour, while the social velocity is based on the swarm behaviour ''' 
            cognitive_velocity = phi_c * rand1 * (self.best_position[i] - self.position[i])
            social_velocity = phi_s * rand2 * (swarm_best_position[i] - self.position[i])
            
            self.velocity[i] = (omega * self.velocity[i]) + cognitive_velocity + social_velocity
            
    def update_position(self, bounds):
        for i in range(0, swarm_dimension):
            self.position[i] = self.position[i] + self.velocity[i]
            
            ''' If the position it's out of the user-defined boundaries we can push the particle in (it's an improvement of the algorithm) '''
            if self.position[i] > bounds[i][1]:
                self.position[i] = bounds[i][1]
                
            if self.position[i] < bounds[i][0]:
                self.position[i] = bounds[i][0]
                
def optimize(fitness, x0, bounds, n_particles, max_iter):
    global swarm_dimension
    swarm_dimension = len(x0)
    
    swarm_best_position = list()
    swarm_best_fitness = -1
    
    ''' Initialization of the swarm '''
    swarm = list()
    for _ in range(0, n_particles):
        swarm.append(Particle(x0))
        
    ''' Optimization loop '''
    i = 0
    while i < max_iter:
        ''' Evaluate the fitness of each particle in the swarm and update the individual best position'''
        for k in range(0, n_particles):
            swarm[k].evaluation(fitness)
            
            ''' Check if the current particle it's the best of the swarm, if so, update best position and best fitness of the swarm'''
            if (swarm[k].fitness < swarm_best_fitness) or swarm_best_fitness == -1:
                swarm_best_position = list(swarm[k].position)
                swarm_best_fitness = float(swarm[k].fitness)
        
        ''' Update positions and velocities of the swarm '''
        for k in range(0, n_particles):
            swarm[k].update_velocity(swarm_best_position)
            swarm[k].update_position(bounds)
            
        i += 1
        
    print('Results: the best fitness value is F(x*) = {}, at x* = {}.'.format(swarm_best_fitness, swarm_best_position))
    