from typing import List


class Solution:
    @classmethod
    def generate_edge_points(cls, n, k):
        top_points = [(k, i) for i in range(k, n - k)]
        right_points = [(i, n - k - 1) for i in range(k, n - k)]
        bottom_points = list(reversed([(n - k - 1, i) for i in range(k, n - k)]))
        left_points = list(reversed([(i, k) for i in range(k, n - k)]))
        return top_points, right_points, bottom_points, left_points

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        rounds = len(matrix) // 2
        for i in range(rounds):
            top, right, bottom, left = self.generate_edge_points(length, i)
            for j in range(len(top) - 1):
                left_value = matrix[left[j][0]][left[j][1]]
                matrix[left[j][0]][left[j][1]] = matrix[bottom[j][0]][bottom[j][1]]
                matrix[bottom[j][0]][bottom[j][1]] = matrix[right[j][0]][right[j][1]]
                matrix[right[j][0]][right[j][1]] = matrix[top[j][0]][top[j][1]]
                matrix[top[j][0]][top[j][1]] = left_value


if __name__ == "__main__":
    import numpy as np

    test_matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(np.array(test_matrix))
    Solution().rotate(test_matrix)
    print(np.array(test_matrix))
