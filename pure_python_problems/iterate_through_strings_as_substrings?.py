if __name__ == "__main__":
    from collections import Counter

    def sub_string_counter(raw_string, sub_string_length, include_cross):
        if include_cross:
            return dict(
                Counter(
                    [
                        raw_string[i:j]
                        for i in range(len(raw_string))
                        for j in range(i + 1, len(raw_string) + 1)
                        if len(raw_string[i:j]) == sub_string_length
                    ]
                )
            )
        else:
            return dict(
                Counter(
                    [
                        raw_string[i:j]
                        for i in range(0, len(raw_string), sub_string_length)
                        for j in range(i + sub_string_length, len(raw_string) + 1)
                        if len(raw_string[i:j]) == sub_string_length
                    ]
                )
            )

    test_string = "ABCDEFGHIJKLMNOPQRSTUVABCSDLSFKJJKLOP"
    sub_string_count = 3

    print(sub_string_counter(test_string, sub_string_count, True))
    print(sub_string_counter(test_string, sub_string_count, False))
