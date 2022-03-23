import numpy as np
from math import pi, perm
from sympy import symbols, factor

__all__ = ['pi', 'range', ]

def range(*args):
    return list(np.arange(*args))

combinaison = perm

pi = pi