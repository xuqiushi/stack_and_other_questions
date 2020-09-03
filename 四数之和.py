from typing import List


class Solution:
    def get_all_two_combinations(self, nums):
        cache = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                sum_value = nums[i] + nums[j]
                if sum_value not in cache:
                    cache[sum_value] = [{i, j}]
                else:
                    cache[sum_value].append({i, j})
        return cache

    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        two_combinations = self.get_all_two_combinations(nums)
        results = set()
        for value in two_combinations:
            other = target - value
            if other not in two_combinations:
                continue
            current_combinations = two_combinations[value]
            other_combinations = two_combinations[other]
            for combination in current_combinations:
                for other_combination in other_combinations:
                    if not combination & other_combination:
                        total_combination = combination | other_combination
                        results.add(
                            tuple(sorted([nums[comb] for comb in total_combination]))
                        )
        return [list(result) for result in results]


if __name__ == "__main__":
    test_nums = [-5, 5, 4, -3, 0, 0, 4, -2]
    test_target = 4
    print(Solution().four_sum(test_nums, test_target))
