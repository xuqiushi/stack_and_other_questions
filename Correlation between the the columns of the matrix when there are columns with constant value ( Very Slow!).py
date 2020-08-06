import scipy.stats
import numpy as np
import pandas as pd


def getCorreCustom(matrix, columns=30):
    A = np.zeros((columns, columns))
    for i in range(columns):
        for j in range(columns):
            if i == j:
                A[i, j] = 1
            else:
                a = matrix[:, i]
                b = matrix[:, j]

                if np.std(a) == 0 or np.std(b) == 0:
                    A[i, j] = 0
                else:
                    A[i, j] = scipy.stats.spearmanr(a, b).correlation
    return A


if __name__ == "__main__":
    from datetime import datetime

    Test = np.random.random((50, 30))
    Test[:, 0] = 1
    Test[:, 10] = 1
    start_time = datetime.now()
    R = getCorreCustom(Test)
    print("Custom Method")
    print(datetime.now() - start_time)
    print(R.shape)
    start_time = datetime.now()
    P = pd.DataFrame(Test)
    print("Pandas Method")
    print(datetime.now() - start_time)
    print(P.corr(method="spearman").shape)
