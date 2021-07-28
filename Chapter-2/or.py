import numpy as np

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])        # weight
    b = -0.2                        # bias

    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# Main part
print("(in1, in2) = %2d, %2d    out = %2d" % (0, 0, OR(0, 0)))
print("(in1, in2) = %2d, %2d    out = %2d" % (0, 1, OR(0, 1)))
print("(in1, in2) = %2d, %2d    out = %2d" % (1, 0, OR(1, 0)))
print("(in1, in2) = %2d, %2d    out = %2d" % (1, 1, OR(1, 1)))
