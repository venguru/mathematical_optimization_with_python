"""
2-15. CCRモデルを解くためのコード
"""

import numpy as np
from pulp import *


MEPS = 1.0e-6


def DEA_CCR(x, y, DMUs):
    m, n = x.shape
    s, n = y.shape

    res = []
    for o in range(n):
        prob = LpProblem('DMU_' + str(o), LpMaximize)
        v = [LpVariable('v'+str(i), lowBound=0,
                        cat='Continuous') for i in range(m)]
        u = [LpVariable('u'+str(i), lowBound=0,
                        cat='Continuous') for i in range(s)]

        prob += lpDot(u, y[:,o]) # 目的関数

        # 制約条件
        prob += lpDot(v, x[:,o]) == 1, 'Normalize' + str(o)
        for j in range(n):
            prob += lpDot(u, y[:,j]) <= lpDot(v, x[:,j])

        prob.solve()
        vs = np.array([v[i].varValue for i in range(m)]) # v*
        us = np.array([u[i].varValue for i in range(s)]) # u*

        # 参照集合作成
        (eo, ) = np.where(np.abs(np.dot(vs,x)-np.dot(us,y))<=MEPS)
        res.append([DMUs[o], value(prob.objective),
                    set(eo), tuple(vs), tuple(us)])

    return res
