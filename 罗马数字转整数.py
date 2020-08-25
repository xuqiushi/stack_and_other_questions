import re


class Solution:
    roman_int_mapping = dict([
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1),
    ])

    special_mapping = {
        "CM": "DCCCC",
        "CD": "CCCC",
        "XC": "LXXXX",
        "XL": "XXXX",
        "IX": "VIIII",
        "IV": "IIII",
    }

    def roman_to_int(self, s: str) -> int:
        special_pattern = re.compile(f"{'|'.join(self.special_mapping)}")
        common_string = re.sub(special_pattern, lambda match: self.special_mapping[match.group()], s)
        result = 0
        for char in common_string:
            result += self.roman_int_mapping[char]
        return result


if __name__ == "__main__":
    test_roman = "MCMXCIV"
    print(Solution().roman_to_int(test_roman))
