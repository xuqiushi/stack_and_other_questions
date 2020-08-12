from math import floor, ceil
from typing import List
import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_list = np.array(nums1 + nums2)
        return float(np.median(total_list))


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        middle_position = (len(nums1) + len(nums2)) / 2
        if middle_position == floor(middle_position):
            middle_left = middle_position - 1
            middle_right = middle_position
        else:
            middle_left = floor(middle_position)
            middle_right = floor(middle_position)
        if len(nums1) < len(nums2):
            little_list = nums1
            bigger_list = nums2
        else:
            little_list = nums2
            bigger_list = nums1
        total_list_index = 0
        middle_left_value = 0
        while total_list_index <= middle_right:
            if not little_list:
                current_value = bigger_list.pop(0)
            elif not bigger_list:
                current_value = little_list.pop(0)
            elif little_list[0] < bigger_list[0]:
                current_value = little_list.pop(0)
            else:
                current_value = bigger_list.pop(0)
            if middle_left == middle_right and total_list_index == middle_left:
                return current_value
            elif middle_left != middle_right and total_list_index == middle_left:
                middle_left_value = current_value
            elif middle_left != middle_right and total_list_index == middle_right:
                return (middle_left_value + current_value) / 2
            total_list_index += 1


class Solution3(object):
    @classmethod
    def get_median(cls, nums):
        return (
            nums[(len(nums) - 1) / 2]
            if len(nums) % 2 != 0
            else (nums[len(nums) / 2 - 1] + nums[len(nums) / 2]) / 2
        )

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first_middle_position = len(nums1) / 2
        second_middle_position = len(nums2) / 2
        first_start = 0
        first_end = len(nums1)
        second_start = 0
        second_end = len(nums2)
        pass


if __name__ == "__main__":
    param_1 = [1, 3]
    param_2 = [2]
    solution = Solution3().findMedianSortedArrays(param_1, param_2)
    print(solution)
