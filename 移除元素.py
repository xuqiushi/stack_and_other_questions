from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        current_index = 0
        total_length = len(nums)
        while current_index < total_length:
            current_num = nums[current_index]
            if current_num == val:
                total_length -= 1
                nums.pop(current_index)
            else:
                current_index += 1
        return total_length


if __name__ == "__main__":
    test_list = [3, 2, 2, 3]
    test_val = 2
    print(Solution().remove_element(test_list, test_val))
