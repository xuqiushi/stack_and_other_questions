if __name__ == "__main__":
    import joblib
    from io import BytesIO
    import base64

    with BytesIO() as tmp_bytes:
        joblib.dump({"test": "test"}, tmp_bytes)
        bytes_obj = tmp_bytes.getvalue()
        base64_obj = base64.b64encode(bytes_obj)
