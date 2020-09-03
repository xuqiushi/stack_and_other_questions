from typing import List
from copy import copy


class Solution:
    def get_all_sub_increased_seq(self, nums):
        sub_seq = []
        for num in nums:
            new_sub_seq = []
            for seq in sub_seq:
                if seq[-1] <= num:
                    new_seq = copy(seq)
                    new_seq.append(num)
                    new_sub_seq.append(new_seq)
            sub_seq += new_sub_seq
            sub_seq.append([num])
        return sub_seq

    def find_sub_sequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        sub_increased_seq = self.get_all_sub_increased_seq(nums)
        unique_seq = set()
        for seq in sub_increased_seq:
            if len(seq) > 1:
                unique_seq.add(tuple(seq))
        return [list(seq) for seq in unique_seq]


if __name__ == "__main__":
    test_nums = [4, 6, 7, 7]
    print(Solution().find_sub_sequences(test_nums))
