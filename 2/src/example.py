"""
2-1. 例題を解くためのコード
"""


from pulp import *


prob = LpProblem(name='LP-Sample', sense=LpMaximize)
x1 = LpVariable('x1', lowBound=0.0)
x2 = LpVariable('x2', lowBound=0.0)

prob += 2 * x1 + 3 * x2 # 目的関数の設定
prob += x1 + 3 * x2 <= 9, 'ineq1'
prob += x1 + x2 <= 4, 'ineq2'
prob += x1 + x2 <= 10, 'ineq3'

print(prob) # 問題を出力
prob.solve() # 求解

# 結果を表示
print(LpStatus[prob.status])
print('Optimal value = ', value(prob.objective))
for v in prob.variables():
    print(v.name, '=', value(v))
