from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_length = len(nums)
        dp = [0 for _ in range(max_length)]
        result = nums[0]
        for i in range(max_length):
            if i == 0:
                dp[i] = nums[i]
            else:
                if dp[i - 1] > 0:
                    dp[i] = nums[i] + dp[i - 1]
                else:
                    dp[i] = nums[i]
            if result < dp[i]:
                result = dp[i]
        return result


if __name__ == "__main__":
    test_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().max_sub_array(test_nums))
