if __name__ == "__main__":
    import json

    with open("tmp/test_input.json", "r") as f:
        test_data = json.load(f)
    print(test_data)
