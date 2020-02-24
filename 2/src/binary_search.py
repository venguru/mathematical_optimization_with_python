"""
2-8. 予測ステップでのステップサイズを決定する binarysearch_theta
"""

import numpy as np


def binarysearch_theta(x, z, dx, dz, beta=0.5, precision=0.001):
    n = np.alen(x)

    th_low = 0.0
    th_high = 1.0

    if np.alen(-x[dx<0]/dx[dx<0]) > 0:
        th_high = min(th_high, np.min(-x[dx<0]/dx[dx<0]))
    if np.alen(-z[dz<0]/dz[dz<0]) > 0:
        th_high = min(th_high, np.min(-z[dz<0]/dz[dz<0]))

    x_low = x + th_low * dx
    z_low = z + th_low + dz
    x_high = x + th_high * dx
    z_high = z + th_high * dz
    mu_high = np.dot(x_high, z_high) / n

    if (beta * mu_high >= 
        np.linalg.norm(x_high * z_high - mu_high * np.ones(n))):
        return th_high

    while th_high - th_low > precision:
        th_mid = (th_high + th_low) / 2
        x_mid = x + th_mid * dx
        z_mid = z + th_mid * dz
        mu_mid = np.dot(x_mid, z_mid) / n

        if (beta * mu_mid >=
            np.linalg.norm(x_mid * z_mid - mu_mid * np.ones(n))):
            th_low = th_mid
        else:
            th_high = th_mid
    return th_low
