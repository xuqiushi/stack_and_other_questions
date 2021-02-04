if __name__ == "__main__":
    import pandas as pd

    ID = [1111, 1111, 2222, 2222, 2222, 3333, 3333, 3333]
    year = [2017, 2017, 2017, 2017, 2016, 2017, 2017, 2015]
    month = [7, 9, 6, 6, 6, 3, 3, 8]
    test = [1, 0, 1, 0, 0, 1, 0, 0]
    df = pd.DataFrame({"ID": ID, "year": year, "month": month, "test": test})
    df.loc[:, "group_count"] = (
        df.groupby(["ID", "year", "month"])["ID"].transform("count").values
    )
    df.loc[:, "check"] = ((df["test"] > 0) & (df["group_count"] > 1)).astype(int)
    print(df)

    import numpy as np

    def cov1(a, b):
        a_mean = np.mean(a)
        b_mean = np.mean(b)
        sum = 0
        for i in range(0, a.size):
            sum = ((a[i] - a_mean) * (b[i] - b_mean)) + sum
        return sum / (len(a) - 1)

    def cov(a, b):
        a_mean = np.mean(a)
        b_mean = np.mean(b)
        for i in range(0, a.size):
            summation = np.sum((a[i] - a_mean) * (b[i] - b_mean))
        return summation / (len(a) - 1)

    a = np.arange(0, 11, 1)
    b = np.arange(10, 21, 1)
    print(cov1(a, b))
    print(cov(a, b))
    print(np.cov(a, b))
