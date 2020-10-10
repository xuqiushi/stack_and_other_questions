from collections import deque
from typing import List


class Solution:
    def combination_sum3(self, k: int, n: int) -> List[List[int]]:
        if k > n:
            return []
        if n == 0:
            return []
        if k == 0:
            return []
        cache = deque([[]])
        result = []
        while cache:
            current_combination = cache.pop()
            if current_combination:
                current_index = current_combination[-1] - 1
            else:
                current_index = -1
            for i in range(current_index + 2, 10):
                sum_result = sum(current_combination) + i
                if len(current_combination) == k - 1:
                    if sum_result == n:
                        result.append(list(current_combination + [i]))
                        break
                else:
                    if sum_result < n:
                        cache.append(current_combination + [i])
        return result


if __name__ == "__main__":
    test_k = 3
    test_n = 7
    print(Solution().combination_sum3(test_k, test_n))
