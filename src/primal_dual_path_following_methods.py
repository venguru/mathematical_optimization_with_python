"""
2-7. 主双対パス追跡法
"""

from binary_search import *
from generate_problem_and_initial_interior_point import *
from self_dual_linear_programming import *

MEPS = 1.0e-10


def PrimalDualPathFollowing(c, A, b):
    (M0, q0) = make_Mq_from_cAb(c, A, b)
    (M, q, x, z) = make_artProb_initialPoint(M0, q0)
    m, k = A.shape
    n, n = M.shape

    count = 0
    mu = np.dot(z,x) / n
    print('初期目的関数値:', mu)
    while mu > MEPS:
        count += 1
        print(count, '回目: ', end=' ')
        # 予測ステップ
        delta = 0
        dx = np.dot(np.linalg.inv(M+np.diag(z/x)),
                    delta*mu*(1/x)-z)
        dz = delta * mu * (1/x) - z - np.dot(np.diag(1/x), z*dx)
        th = binarysearch_theta(x, z, dx, dz, 0.5, 0.001)
        print('theta = ', th, end=', ')
        x = x + th * dx
        z = z + th * dz
        mu = np.dot(z,x) / n
        # 修正ステップ
        delta = 1
        dx = np.dot(np.linalg.inv(M+np.diag(z/x)),
                    delta*mu*(1/x)-z)
        dz = delta * mu * (1/x) - z - np.dot(np.diag(1/x), z*dx)
        x = x + dx
        z = z + dz
        mu = np.dot(z,x) / n
        print('目的関数値:', mu)

    if x[n-2] > MEPS:
        print('Optimal solution:', x[m:m+k]/x[n-2],
              ' has been found.')
        print('Optimal value = ', np.dot(c,x[m:m+k]/x[n-2]))
        print('Optimal solution(dual) ', x[:m]/x[n-2],
              ' has been found.')
        print('Optimal value = ', np.dot(b,x[:m]/x[n-2]))
