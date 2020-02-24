# -*- coding: utf-8 -*-

"""
2-4. 改訂シンプレックス法を実行するコード
"""


import numpy as np


from revised_simplex import *


A = np.array([[2,2,-1], [2,-2,3], [0,2,-1]])
c = np.array([4,3,5])
b = np.array([6,8,4])

lp_RevisedSimplex(c, A, b)
