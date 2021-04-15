'''
Alex Costanzino
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
March, 2021
'''
# Adapted from matplotlib documentation.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def plot_fcn(function):
    fig = plt.figure()
    
    ax = fig.add_subplot(111, projection = '3d')
    x = [np.arange(-10.0, 10.0, 0.05), np.arange(-10.0, 10.0, 0.05)]
    X, Y = np.meshgrid(x[0], x[1])
    
    zs = np.array([function(x) for x in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    ax.plot_surface(X, Y, Z,
                    cmap = cm.coolwarm,
                    antialiased = False)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show(block = False) # In this way the computation won't be suspended