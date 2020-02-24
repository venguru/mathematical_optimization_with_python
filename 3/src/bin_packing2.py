"""
3-6. ビンパッキング問題のもう1つの定式化によるコード
"""

import numpy as np
from pulp import *


MEPS = 1.0e-8

def binpacking2(capacity, w):
    n = len(w)
    items = range(n)
    bpprob = LpProblem(name='BinPacking2', sense=LpMinimize)
    z = [LpVariable('z'+str(j), lowBound=0, cat='Binary') for j in items]
    x = [[LpVariable('x'+str(i)+str(j), lowBound=0, cat='Binary') 
            for j in items] for i in items]

    bpprob += lpSum(z[i] for i in items)
    for i in items:
        bpprob += lpSum(x[i][j] for j in items) == 1
    for j in items:
        bpprob += lpSum(x[i][j]*w[i] for i in items) <= capacity*z[j]

    bpprob.solve()
    result = []
    for j in items:
        if z[j].varValue > MEPS:
            r = [w[i] for i in items if x[i][j].varValue > MEPS]
            result.append(r)
    print(result)


if __name__ == '__main__':
    capacity = 25
    items = set(range(10))
    np.random.seed(1)
    w = {i:np.random.randint(5,10) for i in items}
    w2 = [w[i] for i in items]
    print(w2)

    binpacking2(capacity, w)
