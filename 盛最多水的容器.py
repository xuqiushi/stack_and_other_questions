from typing import List


class Solution:
    def compute_s(self, left, right, height):
        return min(height[left], height[right]) * (right - left)

    def max_area(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        current_s = self.compute_s(left_index, right_index, height)
        while left_index < right_index:
            if height[left_index] <= height[right_index]:
                left_index += 1
                if self.compute_s(left_index, right_index, height) > current_s:
                    current_s = self.compute_s(left_index, right_index, height)
            else:
                right_index -= 1
                if self.compute_s(left_index, right_index, height) > current_s:
                    current_s = self.compute_s(left_index, right_index, height)
        return current_s


if __name__ == "__main__":
    test_height = [2, 3, 4, 5, 18, 17, 6]
    print(Solution().max_area(test_height))
