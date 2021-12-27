from typing import List
from collections import Counter
import heapq


class Solution:
    @classmethod
    def local_package_method(cls, nums, k):
        return [item[0] for item in Counter(nums).most_common(k)]

    @classmethod
    def custom_method(cls, nums, k):
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, (value, key))
        result = heapq.nlargest(k, heap)
        return [item[1] for item in result]

    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        return self.custom_method(nums, k)


if __name__ == "__main__":
    test_nums = [1, 1, 1, 2, 2, 3]
    test_k = 2
    print(Solution().top_k_frequent(test_nums, test_k))
