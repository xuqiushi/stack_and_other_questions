from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        right_reverse = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        left_reverse = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        left = deque()
        for char in s:
            if char in left_reverse:
                left.append(char)
            else:
                if not left:
                    return False
                if left.pop() == right_reverse[char]:
                    continue
                else:
                    return False
        return not left


if __name__ == "__main__":
    test_string = "]"
    print(Solution().isValid(test_string))