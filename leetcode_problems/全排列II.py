from collections import deque
from typing import List


class Solution:
    def permute_unique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        cache = deque([[]])
        standby_index_set = set(range(len(nums)))
        total_length = len(nums)
        result = set()
        while cache:
            current_combination = cache.pop()
            current_length = len(current_combination)
            current_standby_nums_index = standby_index_set - set(current_combination)
            for num_index in current_standby_nums_index:
                if current_length == total_length - 1:
                    result.add(
                        tuple(
                            [nums[index] for index in current_combination]
                            + [nums[num_index]]
                        )
                    )
                else:
                    cache.append(current_combination + [num_index])
        return [list(combination) for combination in result]


if __name__ == "__main__":
    test_nums = [1, 1, 2]
    print(Solution().permute_unique(test_nums))
