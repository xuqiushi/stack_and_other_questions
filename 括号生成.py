from typing import List


class Solution:
    def generate_parenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        result = set()
        for i in range(n):
            if i == 0:
                for sub_result in self.generate_parenthesis(n - 1):
                    result.add(f"({sub_result})")
            else:
                for sub_result_1 in self.generate_parenthesis(i):
                    for sub_result_2 in self.generate_parenthesis(n - i):
                        result.add(f"{sub_result_1}{sub_result_2}")
        return list(result)


if __name__ == "__main__":
    test_n = 3
    print(Solution().generate_parenthesis(test_n))
