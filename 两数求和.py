import math
from datetime import datetime
import numpy as np
from line_profiler import LineProfiler


class SolutionDict:
    def twoSum(self, nums, target):
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None


class SolutionBack:
    def twoSum(self, nums, target):
        nums = np.array(nums)
        num_index_list = np.indices(nums.shape)[0]
        equal_half_list = num_index_list[nums == target / 2]
        less_half_index_list = num_index_list[nums < target / 2]
        bigger_half_index_list = num_index_list[nums >= target / 2]
        bigger_half_value_list = nums[bigger_half_index_list]
        if equal_half_list.shape[0] > 1:
            return [equal_half_list[0], equal_half_list[1]]
        for num_index in less_half_index_list:
            other_value = target - nums[num_index]
            other_bool_index = bigger_half_value_list == other_value
            other_index = bigger_half_index_list[other_bool_index]
            if other_index.shape[0] > 0:
                return [num_index, other_index[0]]


class Solution:
    def twoSum(self, nums, target):
        sortedList = sorted(range(len(nums)), key=lambda k: nums[k])
        head = 0
        tail = -1
        sumRes = nums[sortedList[head]] + nums[sortedList[tail]]

        while sumRes != target:
            if sumRes > target:
                tail -= 1
            elif sumRes < target:
                head += 1
            sumRes = nums[sortedList[head]] + nums[sortedList[tail]]

        return [sortedList[head], sortedList[tail]]


if __name__ == "__main__":
    np.random.seed(2)
    start = datetime.now()
    test_nums = list(np.random.choice(range(1000000), 100000, replace=False))
    # SolutionBack().twoSum(test_nums, 444)
    lp = LineProfiler()
    lp_wrapper = lp(Solution().twoSum)
    lp_wrapper(test_nums, 32324)
    lp.print_stats()
    print(datetime.now() - start)
    start = datetime.now()
    lp = LineProfiler()
    lp_wrapper = lp(SolutionBack().twoSum)
    lp_wrapper(test_nums, 32324)
    lp.print_stats()
    print(datetime.now() - start)
