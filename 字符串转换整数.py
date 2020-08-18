import re


class Solution:
    def my_atoi(self, string: str) -> int:
        number = re.search("^[-+]?[0-9]+", string.strip())
        if number:
            result = int(number.group())
            if -2**31 <= result <= 2**31-1:
                return result
            elif result < -2**31:
                return -2**31
            else:
                return 2**31-1
        else:
            return 0


if __name__ == "__main__":
    test_string = "+1"
    print(Solution().my_atoi(test_string))