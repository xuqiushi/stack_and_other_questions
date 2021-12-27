from typing import List
import bisect


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        current_index = 0
        while current_index < len(intervals) - 1:
            if intervals[current_index][1] >= intervals[current_index + 1][0]:
                right = max(
                    intervals[current_index][1], intervals[current_index + 1][1]
                )
                intervals.pop(current_index + 1)
                intervals[current_index][1] = right
            else:
                current_index += 1
        return intervals


if __name__ == "__main__":
    import timeit

    test_intervals = [[1, 4], [4, 5]]
    print(Solution().merge(test_intervals))
    print(timeit.timeit("Solution().merge(test_intervals)", globals=globals()))
