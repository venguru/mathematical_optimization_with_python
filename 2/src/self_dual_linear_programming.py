"""
2-5. 自己双対型線形最適化問題への変換
"""

import numpy as np


def make_Mq_from_cAb(c, A, b):
    m, k = A.shape
    m1 = np.hstack((np.zeros((m,m)), -A, b.reshape(m,-1)))
    m2 = np.hstack((A.T, np.zeros((k,k)), -c.reshape(k,-1)))
    m3 = np.append(np.append(-b,c),0)

    M = np.vstack((m1, m2, m3))
    q = np.zeros(m+k+1)

    return M, q
