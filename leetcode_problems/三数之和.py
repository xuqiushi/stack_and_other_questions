from typing import List


class Solution:
    def two_sum(self, nums, target):
        cache = {}
        result = []
        for num_index, num_value in enumerate(nums):
            other_value = target - num_value
            if other_value in cache:
                result.append([other_value, num_value])
            cache[num_value] = num_index
        return result

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        zeros_count = 0
        singe_zero_list = []
        for num in nums:
            if num == 0:
                zeros_count += 1
            else:
                singe_zero_list.append(num)
        if zeros_count > 0:
            singe_zero_list.append(0)
        if zeros_count >= 3:
            result = {(0, 0, 0)}
        else:
            result = set()
        nums = singe_zero_list
        for num_index, num_value in enumerate(nums):
            other = -num_value
            other_combination = self.two_sum(nums[num_index + 1 :], other)
            for combination in other_combination:
                result.add(
                    tuple(sorted([nums[num_index], combination[0], combination[1]]))
                )
        return [list(combination) for combination in result]


if __name__ == "__main__":
    test_nums = [1, -1]
    print(Solution().three_sum(test_nums))
