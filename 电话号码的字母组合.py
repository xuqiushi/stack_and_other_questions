from typing import List
from collections import deque


class Solution:
    digit_letter_mapping = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letter_combinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        cache = deque()
        total_length = len(digits)
        for letter in self.digit_letter_mapping[digits[0]]:
            cache.append(letter)
        while cache:
            current_string = cache.pop()
            if len(current_string) == total_length:
                result.append(current_string)
            else:
                current_length = len(current_string)
                next_letter = digits[current_length]
                for letter in self.digit_letter_mapping[next_letter]:
                    cache.append(f"{current_string}{letter}")
        return result


if __name__ == "__main__":
    test_digits = "23"
    print(Solution().letter_combinations(test_digits))