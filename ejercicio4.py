import math
import random

# evaluated montecarlo function in a single point
def evaluated_func(x):
    # esto es lo que esta malo
    # return math.e ** (-1 * (x ** 2))
    return 2 * math.e ** (-1 * (1/x - 1)**2)/(x ** 2) 

# get a uniform random in the given inverval
def rand_float(l_bound, u_bound):
    range = u_bound - l_bound
    choice = random.uniform(0, 1)
    return l_bound + range * choice
 
# peform a montecarlo aprroximation for provided func on provided bounds 
def montecarlo(iterations, function, l_bound, u_bound):
    sum = 0
    for i in range(iterations):
        x = rand_float(l_bound, u_bound)
        sum += function(x)
    return(u_bound - l_bound) * float(sum / iterations)
    

print("Testing with 100 iterations: ", montecarlo(100, evaluated_func, 0, 1))
print("Testing with 10000 iterations: ", montecarlo(10000, evaluated_func, 0, 1))
print("Testing with 1000000 iterations: ", montecarlo(1000000, evaluated_func, 0, 1))