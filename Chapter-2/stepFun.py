import numpy as np
from numpy.core.defchararray import array

def step_function(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([-1, 1, -2, 3, 4])
y = step_function(x)
print(x)
print(y)
