import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
        [1, 1970, np.nan, np.nan],
        [1, 1971, np.nan, np.nan],
        [1, 1972, 0.135, 0.081],
        [1, 1973, 0.222, 0],
        [1, 1974, np.nan, 0],
        [1, 1975, np.nan, 0],
        [1, 1976, np.nan, 0],
        [1, 1977, np.nan, 0],
        [2, 1970, np.nan, np.nan],
        [2, 1971, np.nan, np.nan],
        [2, 1972, 0.135, 0.081],
        [2, 1973, 0.222, 0],
        [2, 1974, np.nan, 0],
        [2, 1975, np.nan, 0],
        [2, 1976, np.nan, 0],
        [2, 1977, np.nan, 0],
    ],
    columns=["id", "t", "y", "x"],
)
if __name__ == "__main__":
    y_shift = df["y"].shift(-1)
    print("x")
