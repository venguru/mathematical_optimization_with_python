"""
2-4. $B2~D{%7%s%W%l%C%/%9K!$r<B9T$9$k%3!<%I(B
"""


import numpy as np


from revised_simplex_2_4 import *


A = np.array([[2,2,-1], [2,-2,3], [0,2,-1]])
c = np.array([4,3,5])
b = np.array([6,8,4])

lp_RevisedSimplex(c, A, b)
