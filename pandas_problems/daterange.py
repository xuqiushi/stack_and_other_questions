if __name__ == "__main__":
    import pandas as pd

    df = pd.DataFrame(
        {
            "Date": pd.date_range(
                start="2020-06-21", end="2020-06-22", freq="min", closed="left"
            )
        }
    )
    df["Dummy 1"] = 1000
    df["Dummy 2"] = 500
    print(df)
