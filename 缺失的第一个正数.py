from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        existed_positive = set()
        left = {1}
        right = set()
        for num in nums:
            if num > 0:
                existed_positive.add(num)
                if num - 1 > 0:
                    left.add(num - 1)
                right.add(num + 1)
        result = min((left | right) - existed_positive)
        return result


if __name__ == "__main__":
    test_nums = [4, 1, 2, 3]
    print(Solution().first_missing_positive(test_nums))
