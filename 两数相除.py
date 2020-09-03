class Solution:
    def shift_div(self, dividend, divisor):
        if divisor > dividend:
            return 0
        time = 0
        current_value = 0
        while current_value <= dividend:
            time += 1
            current_value = divisor << time
        remaining = dividend - (divisor << (time - 1))
        if remaining == 0:
            return 1 << (time - 1)
        else:
            return (1 << (time - 1)) + self.shift_div(remaining, divisor)

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        if dividend == divisor:
            return 1
        abs_result = self.shift_div(abs(dividend), abs(divisor))
        if dividend > 0 and divisor > 0:
            if abs_result >= 2 ** 31:
                return 2 ** 31 - 1
            else:
                return abs_result
        elif dividend > 0 > divisor:
            if abs_result > 2 ** 31:
                return -(2 ** 31)
            else:
                return -abs_result
        elif dividend < 0 < divisor:
            if abs_result > 2 ** 31:
                return -(2 ** 31)
            else:
                return -abs_result
        else:
            if abs_result >= 2 ** 31:
                return 2 ** 31 - 1
            else:
                return abs_result


if __name__ == "__main__":
    test_dividend = 2147483648
    test_divisor = 1
    print(Solution().divide(test_dividend, test_divisor))
