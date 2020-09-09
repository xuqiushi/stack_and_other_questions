from collections import deque
from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        cache = deque()
        cache.append(None)
        current_select_que = deque()
        while cache:
            current_number = cache.pop()
            if current_number:
                current_number_level = current_number[1] + 1
                while (
                    current_select_que
                    and current_select_que[-1][1] >= current_number_level - 1
                ):
                    current_select_que.pop()
                current_select_que.append(current_number)
            else:
                current_number_level = 0
            current_sum = sum([num[0] for num in current_select_que])
            current_number_candidate_index = (
                0 if not current_number else candidates.index(current_number[0])
            )
            for candidate in candidates[current_number_candidate_index:]:
                if candidate + current_sum < target:
                    cache.append((candidate, current_number_level))
                elif candidate + current_sum == target:
                    result.append([num[0] for num in current_select_que] + [candidate])
                else:
                    continue
        return result


if __name__ == "__main__":
    test_candidates = [2, 3, 6, 7]
    test_target = 7
    print(Solution().combination_sum(test_candidates, test_target))
