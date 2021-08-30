## Matthew Jackson
## Aug 29, 2021
## Phys 510

# Reference hw1.pdf

# Python version 3.7+ compatible

import numpy as np
import matplotlib.pyplot as plt
import math


def forwardDiff(f: np.ndarray, h: np.ndarray) -> np.ndarray:
    '''

    :param f: function with numerical data (size N,)
    :param h: numerical grid of the function (size N,)
    :return: gradient from forward difference scheme (size N-1,)
    '''
    diffF = f[1:]-f[:-1]
    return (diffF / h).squeeze()


def centralDiff(f: np.ndarray, h: np.ndarray) -> np.ndarray:
    '''

    :param f:
    :param h:
        Note, assume grid is uniform
    :return:
    '''
    diffF = f[2:] - f[:-2]
    return (diffF / (2*h)).squeeze()


if __name__ == "__main__":
    K = 16
    k = np.arange(K+1)
    h = 10.0 ** -k
    x = np.ones((3, k.size))
    x[0] = x[0] - h
    x[-1] = x[-1] + h
    truth = np.full(k.size, np.cos(1) ** (-2)) # secant squared
    f = np.tan(x)
    dfdx_1 = forwardDiff(f[1:], h)
    dfdx_2 = centralDiff(f, h)

    fig, axes = plt.subplots(1, 2, sharey=True)
    err1 = np.abs((dfdx_1 - truth) / truth)
    axes[0].loglog(h, err1 * 100)
    axes[0].set_title('Error in Forward Difference')
    axes[0].set_ylabel('Percent Error')
    axes[0].set_xlim(h.max(), h.min())

    err2 = np.abs((dfdx_2 - truth) / truth)
    axes[1].loglog(h, err2 * 100)
    axes[1].set_title("Error in Central Difference")
    axes[1].set_ylabel('Percent Error')
    axes[1].set_xlim(h.max(), h.min())


