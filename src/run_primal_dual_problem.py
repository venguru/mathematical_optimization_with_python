"""
主双対パス追跡法を実行するコード
"""


from primal_dual_path_following_methods import *

c = np.array([150, 200, 300])
A = np.array([[3,1,2], [1,3,0], [0,2,4]])
b = np.array([60, 36, 48])

PrimalDualPathFollowing(c, A, b)
