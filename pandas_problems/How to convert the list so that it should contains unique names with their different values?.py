if __name__ == "__main__":
    import pandas as pd

    votes = [
        ["Y AFGHANISTAN", "Y INDIA", "Y NEPAL", "N UNITED STATES"],
        ["Y AFGHANISTAN", "N INDIA", "Y NEPAL", "      MALI", "Y UNITED STATES"],
        ["N AFGHANISTAN", "Y INDIA", "Y NEPAL", "      MONGOLIA", " N UNITED STATES"],
    ]
    flatten_votes = [vote for vote_list in votes for vote in vote_list]
    votes_df = (
        pd.Series(flatten_votes)
        .str.replace(r"^\s", "")
        .str.split(r"\s+", expand=True, n=1)
    )
    votes_df.columns = ["judge", "type"]
    votes_df.loc[:, "appear_index"] = votes_df.groupby("type").cumcount()
    result = votes_df.pivot(
        index="appear_index", columns="type", values="judge"
    ).fillna("")
    print(result)
