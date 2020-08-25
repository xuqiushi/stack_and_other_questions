from collections import deque


class Solution:

    roman_int_mapping = [
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1),
    ]

    special_mapping = {
        "DCCCC": "CM",
        "CCCC": "CD",
        "LXXXX": "XC",
        "XXXX": "XL",
        "VIIII": "IX",
        "IIII": "IV",
    }

    def int_to_roman(self, num: int) -> str:
        result = deque()
        current_remaining = num
        for map_index, map_value in enumerate(self.roman_int_mapping):
            roman, current_value = map_value
            current_count, current_remaining = divmod(current_remaining, current_value)
            if roman in ("C", "X", "I") and current_count == 4:
                last_roman = result.pop()
                if last_roman and last_roman in ("D", "L", "V"):
                    current_string = (
                        f"{roman}{self.roman_int_mapping[map_index - 2][0]}"
                    )
                else:
                    current_string = f"{roman}{self.roman_int_mapping[map_index - 1][0]}"
            else:
                current_string = roman * current_count
            result.append(current_string)
        return "".join(result)


if __name__ == "__main__":
    test_string = 4
    print(Solution().int_to_roman(test_string))
