from collections import deque
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        cache = deque([[]])
        standby_set = set(nums)
        total_length = len(nums)
        result = []
        while cache:
            current_combination = cache.pop()
            current_length = len(current_combination)
            current_standby_nums = standby_set - set(current_combination)
            for num in current_standby_nums:
                if current_length == total_length - 1:
                    result.append(current_combination + [num])
                else:
                    cache.append(current_combination + [num])
        return result


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    print(Solution().permute(test_nums))
