if __name__ == "__main__":
    from io import StringIO
    import pandas as pd

    raw = f"""
$
SPC           10  507901  123456     0.0
SPC           10  507902  123456     0.0
SPC           10  507903  123456     0.0
$
GRID      100001  100000 8.17119-0.68585 1.92194  100010
GRID      100002  100000 7.73198-0.94529 1.73439  100010
GRID      100003  100000 7.28772-0.97244 1.54514  100010
GRID      100004  100000 6.76982-0.71715 1.32471  100010
    """
    raw_io = StringIO(raw)
    model_without_grid = list()
    model_just_grid = list()

    for line in raw_io.readlines():
        if line.startswith("GRID"):
            model_just_grid.append(line.strip())
        else:
            model_without_grid.append(line)
    print(model_just_grid)

    grid_pd = pd.DataFrame(model_just_grid)
    print(grid_pd)
    grid_pd = (
        grid_pd[0]
        .str.replace(r"(-\d+.?\d*)", " \\1", regex=True)
        .str.split(r"\s+", expand=True)
    )
    print(grid_pd)
