"""
2-4. 改定インプレックス法
"""


# -*- coding: utf-8 -*-

import numpy as np
import scipy.linalg as linalg


MEPS = 1.0e-10


def lp_RevisedSimplex(c, A, b):
    np.seterr(divide='ignore')
    (m, n) = A.shape # mはAの行数, nはAの列数
    AI = np.hstack((A, np.identity(m)))
    c0 = np.r_[c, np.zeros(m)]
    basis = [n+i for i in range(m)]
    nonbasis = [j for j in range(n)]

    while True:
        y = linalg.solve(AI[:,basis].T, c0[basis])
        cc = c0[nonbasis] - np.dot(y, AI[:,nonbasis])

        if np.all(cc <= MEPS):
            x = np.zeros(n+m)
            x[basis] = linalg.solve(AI[:,basis], b)
            print('Optimal')
            print('Oputimal value =', np.dot(c0[basis], x[basis]))
            for i in range(m):
                print('x', i, '=', x[i])
            break
        else:
            s = np.argmax(cc)
        d = linalg.solve(AI[:,basis], AI[:,nonbasis[s]])
        if np.all(d <= MEPS):
            print('Unbounded')
            break
        else:
            bb = linalg.solve(AI[:,basis], b)
            ratio = bb / d
            ratio[ratio<-MEPS] = np.inf
            r = np.argmin(ratio)
            nonbasis[s], basis[r] = basis[r], nonbasis[s]
