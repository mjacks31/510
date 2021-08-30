## Matthew Jackson
## Aug 29, 2021
## Phys 510

# Reference hw1.pdf

# Python version 3.7+ compatible

import numpy as np
import matplotlib.pyplot as plt


def S1(n: np.ndarray) -> np.ndarray:
    """

    :param n:
    :return:
    """
    N = np.arange(1, 2 * n.max()+1, dtype=n.dtype)
    ind = np.isin(N, 2 * n)
    series = ((-1) ** N) * N / (N + 1)
    return np.cumsum(series)[ind]


def S2(n: np.ndarray) -> np.ndarray:
    """

    :param n:
    :return:
    """
    series_1 = (2 * n - 1) / (2 * n)
    series_2 = (2 * n) / (2 * n + 1)
    return -np.cumsum(series_1) + np.cumsum(series_2)


def S3(n) -> np.ndarray:
    """

    :param n:
    :return:
    """
    series = 1 / (2 * n * (2 * n + 1))
    return np.cumsum(series)


if __name__ == "__main__":
    N = 1000000
    n = np.arange(1, N+1).astype(np.float32)

    ans1 = S1(n)
    ans2 = S2(n)
    ans3 = S3(n)

    fig, axes = plt.subplots(1, 2, sharey=True)
    err1 = np.abs((ans1 - ans3) / ans3)
    axes[0].loglog(n, err1 * 100)
    axes[0].set_title('Error in S1')
    axes[0].set_ylabel('Percent Error')

    err2 = np.abs((ans2 - ans3) / ans3)
    axes[1].loglog(n, err2 * 100)
    axes[1].set_title("Error in S2")
    axes[1].set_ylabel('Percent Error')

