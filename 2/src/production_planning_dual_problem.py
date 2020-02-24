"""
2-3. 生産計画の双対問題を解くためのコード
"""


import numpy as np
from pulp import *


# 2_2のＡを転置
A = np.array([[3, 1, 2], [1, 3, 0], [0, 2, 4]])
c = np.array([150, 200, 300])
b = np.array([60, 36, 48])
(m, n) = A.shape # mはＡの行数, nはＡの列数

AT = A.T

dual = LpProblem(name='Dual_Production', sense=LpMinimize)

y = [LpVariable('y'+str(i+1), lowBound=0) for i in range(m)]

dual += lpDot(b, y)

for j in range(n):
    dual += lpDot(AT[j], y) >= c[j], 'ineq'+str(j)

# 求解して結果を表示
dual.solve()

print(LpStatus[dual.status])
print('Optimal value of dual problem =', value(dual.objective))
for v in dual.variables():
    print(v.name, '=', v.varValue)

# 実行可能解の検証
Y = np.array([v.varValue for v in dual.variables()])
print('Feasible solution:', np.all(np.abs(np.dot(AT, Y) - c) <= 1.0e-5))
