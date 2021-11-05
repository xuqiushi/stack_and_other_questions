import requests
import numpy as np
from tqdm import trange
import time

WIDTH = 2500
HEIGHT = 3000
IS_SMALL_DATA = False


def main(url="http://127.0.0.1:8888/predict"):
    n = WIDTH * HEIGHT
    if IS_SMALL_DATA:
        np_image = np.zeros(1, dtype=np.float32)
    else:
        np_image = np.arange(n).astype(np.float32) / np.float32(n)
    results = []
    means = []
    image_bytes = np_image.tobytes()
    for _ in trange(50):
        now = time.time()
        results.append(requests.post(url, data=image_bytes))
        current_time = time.time() - now
        means.append(current_time)
        print(current_time)
    print(sum(means) / len(means))


if __name__ == "__main__":
    main()
