## Matthew Jackson
## Aug 29, 2021
## Phys 510

# Reference hw1.pdf

# Python version 3.7+ compatible

import numpy as np
import matplotlib.pyplot as plt


def solution3_2(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    x_1 = (-b + np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x_2 = (-b - np.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x_1, x_2


def solution3_3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    """

    :param a:
    :param b:
    :param c:
    :return:
    """
    x_1 = (-2 * c) / (b + np.sqrt(b ** 2 - 4 * a * c))
    x_2 = (-2 * c) / (b - np.sqrt(b ** 2 - 4 * a * c))
    return x_1, x_2


if __name__ == "__main__":
    ## Question 3.a is the functions above

    ## Question 3.b
    n = np.arange(1, 20)
    c = 10.0 ** -n
    a = np.ones(c.shape)
    b = a[:]
    x_1, x_2 = solution3_2(a, b, c)
    xp_1, xp_2 = solution3_3(a, b, c)
    # Solution 1
    print()
    print('# Solution 1')
    print('3.2\t\t3.3')
    for iii, (x1, x2) in enumerate(zip(x_1, xp_1)):
        print(f'{iii + 1}\t{x1}\t\t{x2}')
    # Solution 2
    print('# Solution 2')
    print('3.2\t\t3.3')
    for iii, (x1, x2) in enumerate(zip(x_2, xp_2)):
        print(f'{iii + 1}\t{x1}\t\t{x2}')
    ERROR_IND = 17

    ## Question 3.d
    # Error in x1
    fig, axes = plt.subplots(1, 2, sharey=True)
    ac4 = 4 * a * c
    err1 = np.abs((x_1[:-3] - xp_1[:-3]) / xp_1[:-3])
    axes[0].loglog(ac4[:-3], err1*100)
    axes[0].set_title('Error in X_1')
    axes[0].set_ylabel('Percent Error')
    axes[0].set_xlim(c.max()*100, c[-3])

    err2 = np.abs((xp_2[:-3] - x_2[:-3]) / x_2[:-3])
    axes[1].loglog(ac4[:-3], err2*100)
    axes[1].set_title("Error in X'_2")
    axes[1].set_ylabel('Percent Error')
    axes[1].set_xlim(c.max()*100, c[-3])

