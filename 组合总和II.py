from collections import deque
from typing import List


class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        result = set()
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
            selected_index = [item[2] for item in current_select_que]
            next_index = 0 if not current_select_que else max(selected_index)
            for candidate_index, candidate in enumerate(candidates[next_index:]):
                real_index = candidate_index + next_index + 1
                if real_index in selected_index:
                    continue
                if candidate + current_sum < target:
                    cache.append((candidate, current_number_level, real_index))
                elif candidate + current_sum == target:
                    result.add(
                        tuple(
                            sorted([num[0] for num in current_select_que] + [candidate])
                        )
                    )
                else:
                    continue
        return [list(item) for item in result]


if __name__ == "__main__":
    test_candidates = [10, 1, 2, 7, 6, 1, 5]
    test_target = 8
    print(Solution().combination_sum(test_candidates, test_target))
