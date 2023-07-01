import math


def u_triangle(x, a, b, c):
    if x <= a or x >= c:
        return 0
    if a <= x <= b:
        return (x - a) / (b - a)
    if b <= x <= c:
        return (c - x) / (c - b)

def u_sigmoid(x, slope, midpoint):
    exponent = slope * (x - midpoint)
    return 1 / (1 + (math.exp(exponent * -1)))

def u_generalized_bell(x, a, b, c):
    exponent = ((x - c) / a) ** (2 * b)
    return 1 / (1 + abs(exponent))

