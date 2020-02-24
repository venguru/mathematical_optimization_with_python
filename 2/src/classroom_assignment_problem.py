"""
2-13. クラス編成最適化
"""

from itertools import product # 繰り返しのため
import math # floor, ceil関数のため

from pulp import * # 最適化ソルバー


MEPS = 1.0e-6

n = len(df.index) # 学生の人数
m = len(df.columns) # クラスの数

lb = math.floor(n/m) # 1クラス人数の下限
ub = math.ceil(n/m) # 1クラス人数の上限

# 満足度 希望順位:点数 のフォーマット
score = {1:100, 2:50, 3:20, 4:0}
ngscore = -100000 # 希望外

prob = LbProblem('ClassAssignment', sense=LpMaximize)

# 変数xと満足度関数pを同時に設定
x = {}
p = {}

for i, j in product(df.index, df.columns):
    x[i, j] = LpVariable('x('+str(i)+','+str(j)+')', lowBound=0)
    p[i, j] = score[int(df.loc[i,j])] \
        if df.loc[i, j] > MEPS else ngscore

# 目的関数
prob += lpSum(p[i,j]*x[i,j] \
              for i,j in product(df.index, df.columns))

# 制約式
for i in df.index:
    prob += lpSum(x[i,j] for j in df.columns) == 1

for j in df.columns:
    prob += lpSum(x[i,j] for i in df.index) >= lb
    prob += lpSum(x[i,j] for i in df.index) <= ub

# 最適化
prob.solve()

# 解の出力
print(LpStatus[prob.status])
print('学生の満足度の総計は', int(value(prob.objective)))
print('学生1人あたりの平均満足度は', int(value(prob.objective))/90.0)
