import math


def test(m, x, n):
    # M, X are given as numpy arrays
    G = np.zeros((n, n))
    for i in range(0, n):
        for j in range(i, n):
            xi = x[i]
            if i == j:
                G[i, j] = abs(xi)
            else:
                xi2 = xi * xi
                xj = x[j]
                xj2 = xj * xj
                mij = m[i, j]
                mid = (xi - xj) / mij
                top = mij * mij + mid * mid + 2 * xi2 + 2 * xj2
                G[i, j] = math.sqrt(top) / 2
    return G


if __name__ == "__main__":
    import numpy as np

    test_m = np.array(
        [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ]
    )
    test_x = np.array([5, 6, 7, 8, 9])
    print(test(test_m, test_x, 5))

    def test2(m, x):
        x_size = x.shape[0]
        x = x.reshape(1, -1)
        reshaped_x = x.reshape(-1, 1)
        result = np.sqrt(
            m ** 2
            + ((reshaped_x - x) / m) ** 2
            + 2 * reshaped_x ** 2
            + 2 * x ** 2
        ) / 2
        return result

    print(test2(test_m, test_x))
