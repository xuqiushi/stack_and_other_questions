from typing import List


class Solution:
    def get_two_closest(self, nums, target):
        if len(nums) < 2:
            return None
        forward_index = 0
        backward_index = len(nums) - 1
        last_sum = nums[forward_index] + nums[backward_index]
        last_bias = abs(target - last_sum)
        while backward_index > forward_index:
            current_sum = nums[forward_index] + nums[backward_index]
            current_bias = abs(current_sum - target)
            if current_bias < last_bias:
                last_bias = current_bias
                last_sum = current_sum
            if current_sum < target:
                forward_index += 1
            elif current_sum > target:
                backward_index -= 1
            else:
                break
        return last_bias, last_sum

    def three_sum_closest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            raise ValueError("长度要大于3")
        sorted_nums = sorted(nums)
        bias = abs(sorted_nums[0] + sorted_nums[1] + sorted_nums[-1] - target)
        sum_result = sorted_nums[0] + sorted_nums[1] + sorted_nums[-1]
        for num_index in range(len(sorted_nums) - 2):
            other_value = target - sorted_nums[num_index]
            current_bias, current_sum = self.get_two_closest(
                sorted_nums[num_index + 1 :], other_value
            )
            if current_bias < bias:
                bias = current_bias
                sum_result = sorted_nums[num_index] + current_sum
        return sum_result


if __name__ == "__main__":
    test_nums = [1, 2, 5, 10, 11]
    test_target = 12
    print(Solution().three_sum_closest(test_nums, test_target))
