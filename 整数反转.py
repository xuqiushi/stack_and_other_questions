class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return x
        string_int = str(x)
        if string_int[0] == "-":
            prefix = string_int[0] if string_int[0] == "-" else ""
            remaining = string_int[1:]
        else:
            prefix = ""
            remaining = string_int
        result = int(f"{prefix}{remaining[::-1]}")
        return result if -(2 ** 31) < result < 2 ** 31 - 1 else 0


if __name__ == "__main__":
    solution = Solution()
    test_int = 1534236469
    print(solution.reverse(test_int))
