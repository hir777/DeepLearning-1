def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y  = AND(s1, s2)

    return y


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def NAND(x1, x2):
    w1, w2, theta = -0.5, -0.5, -0.7
    tmp = x1 * w1 + x2 * w2

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

def OR(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.2
    tmp = x1 * w1 + x2 * w2

    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1

print("in1 : %2d, in2 : %2d     out : %2d" % (0, 0, XOR(0, 0) ))
print("in1 : %2d, in2 : %2d     out : %2d" % (0, 1, XOR(0, 1) ))
print("in1 : %2d, in2 : %2d     out : %2d" % (1, 0, XOR(1, 0) ))
print("in1 : %2d, in2 : %2d     out : %2d" % (1, 1, XOR(1, 1) ))
