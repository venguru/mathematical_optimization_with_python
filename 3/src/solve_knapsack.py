"""
3-2. ナップサック問題に対する分枝限定法
"""

from pulp import *

from knapsack import *


def KnapsackProblemSolve(capacity, items, costs, weights):
    from collections import deque
    queue = deque()
    root = KnapsackProblem('KP', capacity = capacity,
                           items = items, costs = costs,
                           weights = weights,
                           zeros = set(), ones = set())
    root.getbounds()
    best = root
    queue.append(root)
    while queue != deque([]):
        p = queue.popleft()
        p.getbounds()

        if p.ub > best.lb: # bestを更新する可能性がある
            if p.lb > best.lb: # bestを更新する
                best = p
            if p.ub > p.lb: # 子問題を作って分枝する
                k = p.bi
                p1 = KnapsackProblem(p.name+'+'+str(k),
                                     capacity = p.capacity,
                                     items = p.items,
                                     costs = p.costs,
                                     weights = p.weights,
                                     zeros = p.zeros,
                                     ones = p.ones.union({k}))
                queue.append(p1)
                p2 = KnapsackProblem(p.name+'-'+str(k),
                                     capacity = p.capacity,
                                     items = p.items,
                                     costs = p.costs,
                                     weights = p.weights,
                                     zeros = p.zeros.union({k}),
                                     ones = p.ones)
                queue.append(p2)
    return 'Optimal', best.lb, best.xlb

if __name__ == '__main__':
    capacity = 15
    items = {1, 2, 3, 4, 5}
    c = {1:50, 2:40, 3:10, 4:70, 5:55}
    w = {1:7, 2:5, 3:1, 4:9, 5:6}

    res = KnapsackProblemSolve(capacity=capacity,
                          items=items, costs=c,
                          weights=w)
    print('Optinal value = ', res[1])
    print('Optimal solution = ', res[2])
