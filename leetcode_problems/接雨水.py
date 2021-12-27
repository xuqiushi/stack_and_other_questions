from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        maximum_height = []
        for num_index, num in enumerate(height):
            if num_index == 0:
                left = 0
                right = height[num_index + 1]
            elif num_index == len(height) - 1:
                right = 0
                left = height[num_index - 1]
            else:
                left = height[num_index - 1]
                right = height[num_index + 1]
            if num >= left and num >= right:
                maximum_height.append((num_index, num))
        no_cut = False
        while not no_cut:
            cut_index = []
            for i in range(1, len(maximum_height) - 1):
                if (
                    maximum_height[i][1] <= maximum_height[i - 1][1]
                    and maximum_height[i][1] <= maximum_height[i + 1][1]
                ):
                    cut_index.append(i)
            if not cut_index:
                no_cut = True
            else:
                no_cut = False
            while cut_index:
                maximum_height.pop(cut_index.pop())
        s = 0
        for height_index in range(1, len(maximum_height)):
            last_height = maximum_height[height_index - 1]
            current_height = maximum_height[height_index]
            min_height = min(last_height[1], current_height[1])
            s += min_height * (current_height[0] - last_height[0]) - sum(
                [
                    item if item < min_height else min_height
                    for item in height[last_height[0] : current_height[0]]
                ]
            )
        return s


if __name__ == "__main__":
    test_height = [5, 5, 1, 7, 1, 1, 5, 2, 7, 6]
    print(Solution().trap(test_height))
