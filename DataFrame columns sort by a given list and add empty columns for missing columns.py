if __name__ == "__main__":
    import numpy as np
    import pandas as pd

    df = pd.DataFrame(
        {
            "code": ["AA", "BB", "CC", "DD"],
            "YA": [2, 1, 1, np.nan],
            "YD": [1, np.nan, np.nan, 1],
            "ZB": [1, np.nan, np.nan, np.nan],
            "ZD": [1, np.nan, np.nan, 1],
        }
    )
    sort_list = ["YD", "YA", "ZD", "YB", "ZA", "ZB"]
    result = (
        df.T.reset_index()
        .merge(
            pd.DataFrame({"index": sort_list}).astype(str),
            left_on="index",
            right_on="index",
            how="outer",
        )
        .T
    )
    result.columns = result.iloc[0]
    result = result.drop("index")[["code"] + sort_list]
