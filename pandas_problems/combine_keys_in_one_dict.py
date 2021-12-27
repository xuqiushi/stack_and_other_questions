import json
import pandas as pd


if __name__ == "__main__":
    matches = [
        {"15477084": [1]},
        {"360418": [2]},
        {"15477084": [1]},
        {"15477084": [3, 4]},
    ]
    matches_df = pd.DataFrame(matches, dtype=str)
    matches_df = (
        matches_df.fillna("[]")
        .transpose()
        .astype(str)
        .apply(
            lambda x: list(
                set([record for sub in x.tolist() for record in json.loads(sub)])
            ),
            axis=1,
        )
    )
    result = matches_df.to_dict()
    print(result)
