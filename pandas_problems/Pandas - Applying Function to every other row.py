if __name__ == "__main__":
    import pandas as pd

    raw_df = pd.DataFrame(
        {
            "GameId": [1, 1, 2, 2],
            "Team": ["Spirit", "Rockets", "Lighting", "Flames"],
            "Home": [1, 0, 1, 0],
            "Score": [81, 66, 73, 82],
        }
    )
    print(raw_df)
    raw_df.loc[:, "Home"] = raw_df.Home.map({1: "Home", 0: "Away"})
    result = raw_df.pivot_table(
        index=["GameId"],
        columns=["Home"],
        values=["Team", "Score"],
        aggfunc={
            "Team": lambda team: " ".join(team.tolist()),
            "Score": lambda score: score,
        },
    )
    result = result.sort_index(axis="columns", level=[0, "Home"], ascending=False)
    result.columns = [" ".join(reversed(col)) for col in result.columns]
    print(result)
    # from datetime import datetime
    # for repeat_count in range(100, 10000, 100):
    #     start = datetime.now()
    #     test_df = pd.concat([raw_df]*repeat_count)
    #     test_df.loc[:, "Home"] = test_df.Home.map({
    #         1: "Home",
    #         0: "Away"
    #     })
    #     map_cost = datetime.now() - start
    #     start = datetime.now()
    #     test_df = pd.concat([raw_df] * repeat_count)
    #     test_df.loc[raw_df.Home == 0, "Home"] = "Away"
    #     test_df.loc[raw_df.Home == 1, "Home"] = "Home"
    #     loc_cost = datetime.now() - start
    #     print(f"Map cost: {map_cost}, Loc cost: {loc_cost}")
