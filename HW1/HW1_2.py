## Matthew Jackson
## Aug 29, 2021
## Phys 510

# Reference hw1.pdf

# Python version 3.7+ compatible

import numpy as np
import matplotlib.pyplot as plt

def contractedPolynomial(x : np.ndarray) -> np.ndarray:
    """

    :param x:
    :return:
    """
    f_x = (x-1)**6
    return f_x

def expandedPolynomial(x : np.ndarray) -> np.ndarray:
    """

    :param x:
    :return:
    """
    f_x = x**6 - 6*x**5 + 15*x**4 - 20*x**3 + 15*x**2 - 6*x + 1
    return f_x


if __name__=='__main__':
    N = 101
    x_grid = np.linspace(0.995, 1.005, N)
    f_1 = contractedPolynomial(x_grid)
    f_2 = expandedPolynomial(x_grid)
    plt.plot(x_grid, f_1, '--', label='Contracted')
    plt.plot(x_grid, f_2, '--', label='Expanded')
    ymin = np.min([f_1.min(), f_2.min()])
    ymax = np.max([f_1.max(), f_2.max()])
    plt.ylim([ymin, ymax])
    plt.legend()
    plt.ylabel('F(x) value')
    plt.xlabel('X')




