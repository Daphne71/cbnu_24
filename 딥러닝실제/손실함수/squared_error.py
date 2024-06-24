import numpy as np

def sum_squares_error(y, t): 
    return 0.5*np.sum((y-t)**2)


def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t*np.log(y+delta))


t = [ 0,0,1,0,0,0,0,0,0,0]
y = [ 0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1,0.0, 0.0]

a = sum_squares_error(np.array(y), np.array(t))

a2 = cross_entropy_error(np.array(y), np.array(t))
print(a2)

y = [ 0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]
b = sum_squares_error(np.array(y), np.array(t))
b2 = cross_entropy_error(np.array(y), np.array(t))

print(b2)



