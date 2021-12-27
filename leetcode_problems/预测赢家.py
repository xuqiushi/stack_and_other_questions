from typing import List
import numpy as np


class Solution:
    def first_chose_max_sum(self, nums):
        if len(nums) == 2:
            return max(nums) - min(nums)
        max_value = max(
            nums[0] - self.first_chose_max_sum(nums[1:]),
            nums[-1] - self.first_chose_max_sum(nums[:-1]),
        )
        return max_value

    def compute_dp(self, nums):
        dp = np.zeros((len(nums), len(nums)))
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                idx = (i, j)
                if idx[0] > idx[1]:
                    continue
                elif idx[0] == idx[1]:
                    dp[idx] = nums[idx[0]]
                else:
                    dp[idx] = max(
                        nums[idx[0]] - dp[idx[0] + 1, idx[1]],
                        nums[idx[1]] - dp[idx[0], idx[1] - 1],
                    )
        return dp[0, -1] >= 0

    def predict_the_winner(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        return bool(self.compute_dp(nums))


if __name__ == "__main__":
    test_nums = [1, 5, 2, 4, 6]
    print(Solution().predict_the_winner(test_nums))
