class Solution:
    def is_number(self, s: str) -> bool:
        try:
            float(s)
        except ValueError:
            return False
        else:
            return True


if __name__ == "__main__":
    test_nums = ["+100", "5e2", "-123", "3.1416", "-1E-16", "0123"]
    for num in test_nums:
        print(Solution().is_number(num))
