from math import ceil
from typing import List


class Solution:
    def get_middle(self, left_index, right_index):
        return ceil((left_index + right_index) / 2)

    def search_insert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left_index, right_index = 0, len(nums) - 1
        middle_index = self.get_middle(left_index, right_index)
        while left_index < right_index - 1:
            if nums[middle_index] >= target:
                right_index = middle_index
            else:
                left_index = middle_index
            middle_index = self.get_middle(left_index, right_index)
        if target <= nums[left_index]:
            return left_index
        elif target > nums[right_index]:
            return right_index + 1
        else:
            return right_index


if __name__ == "__main__":
    test_nums = [1, 3]
    test_target = 1
    print(Solution().search_insert(test_nums, test_target))
