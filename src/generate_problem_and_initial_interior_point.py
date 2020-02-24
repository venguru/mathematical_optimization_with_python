"""
2-6. 人工問題と初期内点の生成
"""

import numpy as np


def make_artProb_initialPoint(M, q):
    n, n = M.shape

    x0 = np.ones(n)
    mu0 = np.dot(q,x0)/(n+1)+1
    z0 = mu0 / x0
    r = z0 - np.dot(M, x0) - q
    qn1 = (n + 1) * mu0

    MM = np.hstack((M, r.reshape((-1,1))))
    MM = np.vstack((MM, np.append(-r, 0)))

    qq = np.append(q, qn1)
    xx0 = np.append(x0, 1)
    zz0 = np.append(z0, mu0)

    return MM, qq, xx0, zz0
