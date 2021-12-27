from typing import List


class Solution:
    @classmethod
    def get_middle_two(cls, left_index, right_index):
        middle_left = (right_index + left_index) // 2
        return middle_left, middle_left + 1

    @classmethod
    def find_left(cls, nums, left_index, right_index, target):
        middle_left, middle_right = cls.get_middle_two(left_index, right_index)
        while left_index < right_index:
            if nums[middle_left] != target:
                left_index = middle_right
            else:
                right_index = middle_left
            middle_left, middle_right = cls.get_middle_two(left_index, right_index)
        return left_index

    @classmethod
    def find_right(cls, nums, left_index, right_index, target):
        middle_left, middle_right = cls.get_middle_two(left_index, right_index)
        while left_index < right_index:
            if nums[middle_right] != target:
                right_index = middle_left
            else:
                left_index = middle_right
            middle_left, middle_right = cls.get_middle_two(left_index, right_index)
        return right_index

    def search_range(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        if len(nums) == 1:
            return [0, 0] if target == nums[0] else [-1, -1]

        left_index, right_index = 0, len(nums) - 1
        middle_left, middle_right = self.get_middle_two(0, right_index)
        while left_index < right_index and (
            nums[middle_left] != target or nums[middle_right] != target
        ):
            if target < nums[left_index] or target > nums[right_index]:
                return [-1, -1]
            if nums[middle_left] >= target:
                right_index = middle_left
            elif nums[middle_right] <= target:
                left_index = middle_right
            else:
                return [-1, -1]
            if right_index - left_index == 1:
                if target not in nums[left_index : right_index + 1]:
                    return [-1, -1]
            middle_left, middle_right = self.get_middle_two(left_index, right_index)
        if left_index == right_index:
            return [left_index, right_index]
        start = self.find_left(nums, left_index, middle_left, target)
        end = self.find_right(nums, middle_right, right_index, target)
        return [start, end]


if __name__ == "__main__":
    test_nums = [1, 1, 1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 9, 9, 9]
    test_target = 7
    print(Solution().search_range(test_nums, test_target))
