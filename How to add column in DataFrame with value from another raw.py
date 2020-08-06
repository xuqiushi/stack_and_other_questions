if __name__ == "__main__":
    import io
    import pandas as pd

    raw_str = """
DATE,TIME,Value
20200103,100500,255
20200103,101000,356
20200103,101500,546
20200104,100500,652
20200104,101000,321
20200104,101500,632
    """
    raw = pd.read_csv(io.StringIO(raw_str))
    print(raw)
