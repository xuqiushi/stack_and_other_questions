if __name__ == '__main__':
    import numpy as np
    import pandas as pd
    df = {'eqmt_id': [1, 1, 1, 2, 2],
          'brand_no': ['BH40 122', 'BH40 200', 'BH40 541', 'BH40 619', 'BH40 649'],
          'ndt': ['2021-03-28 05:10:00', '2021-04-25 20:31:00', '2020-09-13 11:33:00', '2020-11-08 22:53:00',
                  '2020-12-02 04:46:00'],
          'min': ['2021-03-28 05:30:00', '2021-04-25 21:00:00', '2020-09-13 12:00:00', '2020-11-08 23:00:00',
                  '2020-11-17 05:00:00'],
          'max': ['2021-04-06 08:00:00', '2021-05-03 18:30:00', '2020-09-23 12:30:00', '2020-11-18 10:30:00',
                  '2020-12-09 18:00:00']}

    # Create DataFrame
    df = pd.DataFrame(df)
    # to date time
    df['ndt'] = pd.to_datetime(df['ndt'])
    df['min'] = pd.to_datetime(df['min'])
    df['max'] = pd.to_datetime(df['max'])
    # following two lines generate two (df.shape[0], df.shape[0]) matrix.
    # first matrix min_judge[i][j] means if i 'max' larger than j 'min'
    min_judge = df["max"].astype(int).values >= df["min"].astype(int).values.reshape(-1, 1)
    # second matrix max_judge[i][j] means if i 'max' smaller than j 'max'
    max_judge = df["max"].astype(int).values <= df["max"].astype(int).values.reshape(-1, 1)
    # result should minus 1(line itself)
    result_column_values = np.array(min_judge & max_judge).sum(axis=0) - 1
    # assign values
    df.loc[:, "counter"] = result_column_values
    print(df)