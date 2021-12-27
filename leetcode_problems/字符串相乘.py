from collections import deque


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        left = [int(num1[::-1][i]) if i < len(num1) else 0 for i in range(len(num1))]
        right = [int(num2[::-1][i]) if i < len(num2) else 0 for i in range(len(num2))]
        result = {}
        for i, i_value in enumerate(left):
            for j, j_value in enumerate(right):
                current_result = i_value * j_value
                result_min_index = i + j
                for z in range(len(str(current_result))):
                    if result_min_index + z in result:
                        result[result_min_index + z].append(
                            int(str(current_result)[::-1][z])
                        )
                    else:
                        result[result_min_index + z] = [
                            int(str(current_result)[::-1][z])
                        ]
        string_result_list = []
        max_digit = max(result.keys())
        last_carry = 0
        for digit in range(max_digit + 1):
            current_sum = sum(result[digit])
            current_little_part = (current_sum + last_carry) % 10
            string_result_list.append(str(current_little_part))
            last_carry = (current_sum + last_carry) // 10
        if last_carry != 0:
            string_result_list.append(str(last_carry))
        return "".join(string_result_list[::-1])


if __name__ == "__main__":
    test_num1 = "9133"
    test_num2 = "0"
    solution = Solution()
    print(solution.multiply(test_num1, test_num2))
