if __name__ == "__main__":
    from gevent.pywsgi import WSGIServer
    from basic_flask_app import app

    http_server = WSGIServer(("", 8888), app)
    http_server.serve_forever()
