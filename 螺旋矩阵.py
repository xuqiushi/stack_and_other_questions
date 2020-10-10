from typing import List
from math import ceil


class Solution:
    @classmethod
    def generate_edge_points(cls, width, height, k):
        top_points = [(k, i) for i in range(k, width - k)]
        right_points = [(i, width - k - 1) for i in range(k, height - k)]
        bottom_points = list(
            reversed([(height - k - 1, i) for i in range(k, width - k)])
        )
        left_points = list(reversed([(i, k) for i in range(k, height - k)]))
        if set(top_points) == set(bottom_points):
            return top_points
        if set(left_points) == set(right_points):
            return right_points
        return (
            top_points[:-1] + right_points[:-1] + bottom_points[:-1] + left_points[:-1]
        )

    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        matrix_height = len(matrix)
        matrix_width = len(matrix[0])
        min_round = ceil(min(matrix_height, matrix_width) / 2)
        result = []
        for i in range(min_round):
            result += self.generate_edge_points(matrix_width, matrix_height, i)
        return [matrix[point[0]][point[1]] for point in result]


if __name__ == "__main__":
    test_matrix = [[3], [2]]
    print(Solution().spiral_order(test_matrix))
