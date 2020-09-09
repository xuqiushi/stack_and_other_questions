from typing import List


class Solution:
    @classmethod
    def get_middle_three(cls, left_index, right_index):
        total_length = right_index - left_index + 1
        odd = total_length % 2 != 0
        if odd:
            middle_left = total_length // 2
            middle_right = total_length // 2 + 2
            return (
                left_index + middle_left - 1,
                left_index + middle_right - 1,
                left_index + middle_left,
            )
        else:
            middle_left = total_length / 2 - 1
            middle_right = total_length / 2
            return int(left_index + middle_left), int(left_index + middle_right), None

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return -1 if target != nums[0] else 0
        left_index = 0
        right_index = len(nums) - 1
        while 0 <= left_index < right_index <= len(nums) - 1:
            middle_left, middle_right, middle = self.get_middle_three(
                left_index, right_index
            )
            if middle and nums[middle] == target:
                return middle
            elif nums[middle_left] == target:
                return middle_left
            elif nums[middle_right] == target:
                return middle_right
            elif nums[left_index] == target:
                return left_index
            elif nums[right_index] == target:
                return right_index
            if nums[middle_left] < nums[middle_right]:
                if nums[middle_right] > nums[right_index]:
                    if nums[left_index] < target < nums[middle_left]:
                        right_index = middle_left
                    else:
                        left_index = middle_right
                elif nums[left_index] > nums[middle_left]:
                    if nums[right_index] > target > nums[middle_right]:
                        left_index = middle_right
                    else:
                        right_index = middle_left
                elif nums[left_index] < nums[middle_left] and nums[right_index] > nums[middle_right]:
                    if target > nums[middle_right]:
                        left_index = middle_right
                    else:
                        right_index = middle_left
                else:
                    return -1
            else:
                if nums[left_index] < target < nums[middle_left]:
                    right_index = middle_left
                elif nums[middle_right] < target < nums[right_index]:
                    left_index = middle_right
                else:
                    return -1
        return -1


if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6]
    test_target = 5
    print(Solution().search(test_nums, test_target))
