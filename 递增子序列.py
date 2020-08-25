from typing import List


class Solution:
    def find_sub_sequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        pass


if __name__ == "__main__":
    test_nums = [4, 6, 7, 7]
    print(Solution().find_sub_sequences(test_nums))
