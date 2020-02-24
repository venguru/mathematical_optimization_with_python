"""
3-3. ビンパッキング問題への列生成法への適用
"""

import sys

import numpy as np
from pulp import *

from solve_knapsack import *

MEPS = 1.0e-8

def binpacking(capacity, w, method="branch"):
    m = len(w)
    items = set(range(m))
    A = np.identity(m)

    solved = False
    columns = 0
    dual = LpProblem(name='D(K)', sense=LpMaximize)
    y = [LpVariable('y'+str(i), lowBound=0) for i in items]

    dual += lpSum(y[i] for i in items) # 目的関数の設定
    for j in range(len(A.T)) : # 制約条件の付加
        dual += lpDot(A.T[j],y) <= 1, 'ineq'+str(j)

    while not(solved):
        # dual
        dual.solve()

        costs = {i: y[i].varValue for i in items}
        weights = {i:w[i] for i in items}

        if method == 'zero_one':
            (state, val, sol) = KPS(capacity, items, costs, weights)
        else:
            (state, val, sol) = KnapsackProblemSolve(capacity, items, costs, weights)

        if val >= 1.0 + MEPS:
            a = np.array([int(sol[i]) for i in items])
            dual += lpDot(a, y) <= 1, 'ineq'+str(m+columns)
            A = np.hstack((A, a.reshape((-1,1))))
            columns += 1
        else:
            solved = True

    print('Method: ', method)
    print('Generated columns: ', columns)
    m, n = A.shape
    primal = LpProblem(name='P(K)', sense=LpMinimize)
    x = [LpVariable('x'+str(j), lowBound = 0, cat='Binary') for j in range(n)]

    primal += lpSum(x[j] for j in range(n)) # 目的関数の設定
    for i in range(m): # 制約条件の付加
        primal += lpDot(A[i], x) >= 1, 'ineq'+str(i)

    primal.solve()
    if value(primal.objective) - value(dual.objective) < 1.0 - MEPS:
        print('Optimal solution found: ')
    else:
        print('Approximated solution found: ')

    K = [j for j in range(n) if x[j].varValue > MEPS]
    result = []
    itms = set(range(m))
    for j in K:
        J = {i for i in range(m) if A[i,j] > MEPS and i in itms}
        r = [w[i] for i in J]
        itms -= J
        result.append(r)
    print(result)


def KPS(capacity, items, costs, weights):
    knapsack = LpProblem(name='kanpsack', sense=LpMaximize)
    x = {j: LpVariable('x'+str(j), lowBound=0, cat='Binary') for j in items}

    knapsack += lpSum(costs[j]*x[j] for j in items) # 目的関数の設定
    knapsack += lpSum(weights[j]*x[j] for j in items) <= capacity, 'weights'

    knapsack.solve()
    xx = {j: int(x[j].varValue) for j in items}
    return LpStatus[knapsack.status], value(knapsack.objective), xx


if __name__ == '__main__':
    capacity = 25
    items = set(range(10))
    np.random.seed(1)
    w = {i:np.random.randint(5,10) for i in items}
    w2 = [w[i] for i in items]
    print(w2)

    if len(sys.argv) == 2:
        if sys.argv[1] == 'zero_one':
            binpacking(capacity, w, method='zero_one')
        else:
            binpacking(capacity, w, method='branch')
    else:
        binpacking(capacity, w, method='branch')
