'''
Alex Costanzino
MSc student in Artificial Intelligence
@ Alma Mater Studiorum, University of Bologna
March, 2021
'''

''' A gamma of various test functions for optimization, based on: https://www.sfu.ca/~ssurjano/optimization.html.'''

# import mpmath as math # A more precise math library, for some reason it doesn't work correctly with plots
import math

def rastrigin(x):
    t = 0
    for i in range(len(x)):
        t += x[i]**2 - 10*math.cos(2*math.pi*x[i])
    return t + 10*len(x)

def ackley(x):
    t = 0
    for i in range(len(x)-1):
        t += -20*math.exp(-0.2*math.sqrt(0.5*(x[i]**2 + x[i+1]**2))) - math.exp(0.5*(math.cos(2*math.pi*x[i]) + math.cos(2*math.pi*x[i+1]))) + math.e + 20 
    return t

def rosenbrock(x):
    t = 0
    for i in range(len(x)-1):
        t += 100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2
    return t

def beale(x):
    t = 0
    for i in range(len(x)-1):
        t += (1.5 - x[i] + x[i]*x[i+1])**2 + (2.25 - x[i] + x[i]*x[i+1]**2)**2 + (2.625 - x[i] + x[i]*x[i+1]**3)**2
    return t

def bukin(x):
    t = 0
    for i in range(len(x)-1):
        t = 100*math.sqrt(abs(x[i+1] - 0.01*x[i]**2)) + 0.01*abs(x[i] + 10) 
    return t

def levi(x):
    t = 0
    for i in range(len(x)-1):
        t = math.sin(3*math.pi*x[i])**2 + ((x[i] - 1)**2)*(1 + math.sin(3*math.pi*x[i+1])**2) + ((x[i+1] - 1)**2)*(1 + math.sin(2*math.pi*x[i+1])**2)  
    return t

def easom(x):
    t = 0
    for i in range(len(x)-1):
        t += -math.cos(x[i])*math.cos(x[i+1])*math.exp(-((x[i] - math.pi)**2 + (x[i+1] - math.pi)**2))
    return t

def eggholder(x):
    t = 0
    for i in range(len(x)-1):
        t += -(x[i+1] + 47)*math.sin(math.sqrt(abs((x[i]/2) + x[i+1] + 47))) - x[i]*math.sin(math.sqrt(abs(x[i] - (x[i+1] + 47))))
    return t

def cormick(x):
    t = 0
    for i in range(len(x)-1):
        t += math.sin(x[i] + x[i+1]) + (x[i] - x[i+1])**2 - 1.5*x[i] + 2.5*x[i+1] + 1
    return t

def schaffer(x):
    t = 0
    for i in range(len(x)-1):
        t += (math.sin(x[i]**2 - x[i+1]**2)**2 - 0.5)/(1 + 0.001*(x[i]**2 + x[i+1]**2))**2
    return t + 0.5