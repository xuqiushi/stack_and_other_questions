import requests

if __name__ == "__main__":
    # Download the file via GET request of the Telegram API.
    with open("tmp/response.bin", "rb") as f:
        content = f.read()
        files = [
            ("file", ("test", open(content, "rb"), "application/octet-stream"))  # error
        ]

    # Upload the file via POST request.
    # response = requests.post(FILE_STORAGE_SERVICE_API_URL, files={'file': response.content})
