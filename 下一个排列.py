from typing import List


class Solution:
    def next_permutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        not_changed = True
        for i in range(len(nums) - 2, -1, -1):
            if not not_changed:
                break
            if nums[i] >= nums[i + 1]:
                continue
            else:
                current = nums[i]
                for j in range(len(nums) - 1, i, -1):
                    if current < nums[j]:
                        second = j
                        not_changed = False
                        nums[i], nums[second] = nums[second], nums[i]
                        nums[i + 1 :] = sorted(nums[i + 1 :])
                        break
        if not_changed:
            nums.reverse()


if __name__ == "__main__":
    test_nums = [2, 3, 1]
    print(Solution().next_permutation(test_nums))
    print(test_nums)
