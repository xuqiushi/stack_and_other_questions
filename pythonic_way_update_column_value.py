import numpy as np
import pandas as pd


class ColumnUpdater(object):
    def __init__(self, to_update_df, prefix="Record"):
        self.to_update_df = to_update_df
        self.prefix = prefix
        self.current_index = 0
        self.match_checker = None

    def update_func(self, util_id):
        if isinstance(util_id, pd.DataFrame):
            return
        util_id = util_id.iloc[0]
        self.to_update_df.loc[:, "match_checker"] = self.to_update_df["ID"] == util_id
        current_match = f"{self.prefix} {self.current_index}"
        self.current_index += 1
        return current_match

    def process(self):
        self.to_update_df.loc[:, "match_checker"] = np.nan
        self.to_update_df.loc[:, "util_id"] = self.to_update_df["ID"]
        self.to_update_df.loc[:, "match"] = self.to_update_df.groupby("ID")[
            "util_id"
        ].transform(self.update_func)
        return self.to_update_df.drop(columns="util_id")


if __name__ == "__main__":
    data = np.repeat(
        [["tom", 10, 111], ["nick", 15, 112], ["juli", 14, 113], ["mary", 17, 114]],
        5,
        axis=0,
    )
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns=["Name", "Age", "ID"])
    result = ColumnUpdater(df).process()
    print(result)
