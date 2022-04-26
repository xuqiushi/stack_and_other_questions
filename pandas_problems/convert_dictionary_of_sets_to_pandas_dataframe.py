"""
https://stackoverflow.com/q/71246412/11004559
"""
if __name__ == "__main__":
    import pandas as pd

    test_dict = {
        "+++": {"---", "--0", "-00", "0--", "00-", "000"},
        "0++": {"+--", "+0-", "---", "--0", "-00", "0--", "00-", "000"},
    }
    for key, value in test_dict.items():
        test_dict[key] = [value]
    print(test_dict)
    test_df = pd.DataFrame.from_dict(test_dict, orient="index").reset_index()
    print(test_df)
