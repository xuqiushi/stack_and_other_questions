if __name__ == "__main__":
    import pandas as pd
    import numpy as np

    test_data = [
        [(0, 1), 1],
        [(0, 2), 3],
        [(0, 3), 19],
        [(0, 4), 1],
        [(0, 5), 3],
        [(0, 6), 1],
        [(0, 8), 6],
        [(0, 11), 1],
        [(0, 12), 36],
        [(0, 15), 1],
        [(0, 16), 1],
        [(0, 20), 56],
        [(0, 21), 4],
        [(0, 22), 1],
        [(0, 24), 4],
        [(0, 25), 2],
        [(0, 26), 3],
        [(0, 27), 18],
        [(0, 28), 25],
        [(0, 30), 4],
        [(1, 1), 12],
        [(1, 2), 2],
        [(1, 3), 9],
        [(1, 4), 1],
        [(1, 5), 15],
        [(1, 6), 4],
        [(1, 7), 6],
        [(1, 8), 13],
        [(1, 10), 3],
        [(1, 11), 14],
        [(1, 12), 2],
        [(1, 13), 9],
        [(1, 14), 3],
        [(1, 15), 10],
        [(1, 16), 6],
        [(1, 18), 2],
        [(1, 19), 7],
        [(1, 20), 3],
        [(1, 21), 2],
        [(1, 22), 1],
        [(1, 23), 1],
        [(1, 24), 1],
        [(1, 25), 3],
        [(1, 26), 1],
        [(1, 27), 2],
        [(1, 28), 13],
        [(1, 29), 10],
    ]
    formatted_test_data = [[row[0][0], row[0][1], row[1]] for row in test_data]
    df = pd.DataFrame(formatted_test_data, columns=["hour", "day", "total_clicks"])
    min_day = df["day"].min()
    max_day = df["day"].max()
    frame_df = pd.DataFrame(
        {
            "day": np.repeat(np.arange(min_day, max_day + 1), 24),
            "hour": np.repeat(
                np.arange(24).reshape(1, -1), max_day - min_day + 1, axis=0
            ).flatten(),
        }
    )
    result = frame_df.merge(
        df.groupby(["day", "hour"]).sum().reset_index(), on=["day", "hour"], how="left"
    ).fillna(0)
    pass
