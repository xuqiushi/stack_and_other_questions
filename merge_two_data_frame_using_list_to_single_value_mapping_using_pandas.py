if __name__ == "__main__":
    import pandas as pd

    df1 = pd.DataFrame({"col1": ["A", "B", "C"], "col2": [[1, 2], [3, 4], [1, 4, 5]]})
    df2 = pd.DataFrame({"col3": [1, 2, 3, 4], "col4": ["X", "Y", "Z", "W"]})
    result = (
        df1.explode("col2")
        .merge(df2, left_on="col2", right_on="col3", how="left")
        .groupby("col1", as_index=False)
        .agg(
            {
                "col2": lambda col: [item for item in col[col.notnull()]],
                "col4": lambda col: [item for item in col[col.notnull()]],
            }
        )
    )
    print(result)
