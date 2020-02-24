"""
2-16. 端点列挙のためのコード
"""

from itertools import combinations

import cdd
import numpy as np


MEPS = 1.0e-6

# 多面体を定義する不等式の作成
np.random.seed(2)
n, d = 40, 3

A = np.random.randint(0, 100, (n,d))
b = np.sqrt(np.dot(A**2,np.ones(d))).astype(np.int64)
m, n = np.shape(A)

# pycddlib用のフォーマットに合わせる
eb = np.hstack((b, np.zeros(n))).reshape(-1,1)
eA = np.vstack((-A,np.identity(n)))
ar = np.hstack((eb, eA))
mat = cdd.Matrix(ar, number_type='fraction')
# 端点列挙実行
poly = cdd.Polyhedron(mat)
ext = poly.get_generators()
vl = np.array([np.array(v[1:])/v[0] for v in ext if v[0] != 0])
vlist = vl.astype(np.float64)
# 付加情報の計算
zerosets = [set([i for i in range(m+n)
                 if abs(eb[i]+np.dot(eA[i],v)) <= MEPS]) for v in vl]
elist = [[i,j] for i,j in combinations(range(len(vl)),2)
        if len(zerosets[i].intersection(zerosets[j])) >= 2]
