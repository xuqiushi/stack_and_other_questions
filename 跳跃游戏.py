from typing import List
import numpy as np


class Solution:
    def reachable_method(self, nums):
        neighbour = np.zeros((len(nums), len(nums)))
        for num_index, num in enumerate(nums):
            neighbour[num_index, num_index] = 1
            for i in range(0, num + 1):
                if num_index + i < len(nums):
                    neighbour[num_index, num_index + i] = 1
        last_neighbour = np.array([])
        new_neighbour = neighbour.copy()
        while not np.array_equal(last_neighbour, new_neighbour):
            last_neighbour = new_neighbour
            new_neighbour = last_neighbour.dot(neighbour)
            new_neighbour[new_neighbour > 0] = 1
        return new_neighbour[0, len(nums) - 1] == 1

    def custom_method(self, nums):
        current_position = 0
        while current_position < len(nums):
            num = nums[current_position]
            next_step = 0
            for i in range(1, num + 1):
                if current_position + i >= len(nums) - 1:
                    return True
                if (
                    next_step + nums[current_position + next_step]
                    < i + nums[current_position + i]
                ):
                    next_step = i
            if next_step > 0:
                current_position = current_position + next_step
            else:
                return False
        return True

    def can_jump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return True
        return self.custom_method(nums)


if __name__ == "__main__":
    test_nums = [2, 5, 0, 0]
    print(Solution().can_jump(test_nums))
