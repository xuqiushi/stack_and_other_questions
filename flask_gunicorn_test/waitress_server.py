if __name__ == "__main__":
    from waitress import serve
    import basic_flask_app

    serve(basic_flask_app.app, host="127.0.0.1", port=8888, threads=1)
