from typing import List
from collections import deque


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        if n == k == 1:
            return [[1]]
        cache = deque([[i + 1] for i in range(n)])
        result = []
        while cache:
            current_combination = cache.pop()
            if len(current_combination) == k:
                result.append(current_combination)
            else:
                for i in range(current_combination[-1] + 1, n + 1):
                    new_combination = current_combination + [i]
                    if len(new_combination) == k:
                        result.append(new_combination)
                    else:
                        cache.append(new_combination)
        return result


if __name__ == "__main__":
    test_n = 2
    test_k = 1
    print(Solution().combine(test_n, test_k))
