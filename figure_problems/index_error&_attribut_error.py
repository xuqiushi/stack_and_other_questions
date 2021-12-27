if __name__ == '__main__':
    import re
    with open("../tmp/Data Penjualan1.csv", "r") as f:
        lines = [re.sub("\s+", "\t", line).strip() for line in f.readlines()]
    with open("../tmp/Data Penjualan1.csv", "w") as f:
        for line in lines:
            f.write(line + "\n")
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import sklearn

    dataset = pd.read_csv('../tmp/Data Penjualan1.csv', sep=" ")
    x = dataset.iloc[:, :-1:].values
    y = dataset.iloc[:, 1].values
    dataku = pd.DataFrame(dataset)
    plt.scatter(dataku.BiayaProduksi, dataku.NilaiPenjualan)
    plt.xlabel("Biaya Produksi")
    plt.ylabel("Nilai Penjualan")
    plt.title("Grafik Biaya Produksi VS Nilai Penjualan")
    plt.show()