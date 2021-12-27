if __name__ == "__main__":
    import numpy as np
    import pandas as pd

    raw_df = pd.DataFrame(
        {
            "Hour": [1, 2, 4, 12, 0, 2, 7, 13],
            "Site": ["x", "x", "x", "x", "y", "y", "y", "y"],
            "Value": [1, 1, 1, 1, 1, 1, 1, 1],
        }
    )
    unique_site_count = len(raw_df["Hour"].unique())
    full_hour = pd.DataFrame(
        {
            "Hour": np.concatenate(
                [range(24) for site_name in raw_df["Site"].unique()]
            ),
            "Site": np.concatenate(
                [[site_name] * 24 for site_name in raw_df["Site"].unique()]
            ),
        }
    )
    result = full_hour.merge(raw_df, on=["Hour", "Site"], how="left").fillna(0)
    print("x")
