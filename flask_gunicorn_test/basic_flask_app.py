import numpy as np

from flask import Flask, request
import time
import requests
from do_request import IS_SMALL_DATA, WIDTH, HEIGHT

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    buffer = request.data
    numpy_bytes = np.frombuffer(buffer, np.float32)
    if IS_SMALL_DATA:
        numpy_image = np.zeros((HEIGHT, WIDTH)) + numpy_bytes
    else:
        numpy_image = numpy_bytes.reshape(HEIGHT, WIDTH)
        print(numpy_image.shape)
    result = numpy_image.mean(axis=1).std(axis=0)
    return result.tobytes()


if __name__ == "__main__":
    from gunicorn.http.body import Body
    from werkzeug.wsgi import LimitedStream

    from gunicorn.http.body import LengthReader

    app.run(host="localhost", port=8888, threaded=False, processes=1)
    # n = WIDTH * HEIGHT
    # requests.post('http://127.0.0.1:8888/predict', data=np.arange(n).astype(np.float32) / np.float32(n).tobytes())
