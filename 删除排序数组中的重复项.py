from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        last_num = None
        current_num_index = 0
        total_length = len(nums)
        while current_num_index < total_length:
            current_num = nums[current_num_index]
            if current_num == last_num:
                nums.pop(current_num_index)
                total_length -= 1
            else:
                current_num_index += 1
                last_num = current_num
        return len(nums)


if __name__ == "__main__":
    test_nums = [1,1,2]
    print(Solution().remove_duplicates(test_nums))
