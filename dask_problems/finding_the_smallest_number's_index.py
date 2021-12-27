import multiprocessing
import time

if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    import dask.dataframe as dd
    from tqdm import tqdm

    test_data = {}
    for i in tqdm(range(2000)):
        test_data[i] = np.random.randint(0, 10000, 600000)

    # test one
    # print(test_data)
    now = time.time()
    df = pd.DataFrame(test_data)
    min_idx = df.idxmin(axis=0)
    result_one = dict(zip(df.columns, min_idx.tolist()))
    # print(result_one)
    print(time.time() - now)

    # test two
    now = time.time()
    df = pd.DataFrame(test_data)
    ddf = dd.from_pandas(df, npartitions=multiprocessing.cpu_count())
    min_idx = ddf.idxmin(axis=0).compute(scheduler="processes")
    result_two = dict(zip(df.columns, min_idx.tolist()))
    # print(result_two)
    print(time.time() - now)
