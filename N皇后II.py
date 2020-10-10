from collections import deque


class Solution:
    @classmethod
    def _same_right_line(cls, point_a, point_b):
        return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0]) == 1

    @classmethod
    def _same_left_line(cls, point_a, point_b):
        return (point_b[1] - point_a[1]) / (point_b[0] - point_a[0]) == -1

    @classmethod
    def _same_row(cls, point_a, point_b):
        return point_a[0] == point_b[0]

    @classmethod
    def _same_column(cls, point_a, point_b):
        return point_a[1] == point_b[1]

    @classmethod
    def valid_points(cls, point, existed_points):
        for existed_point in existed_points:
            if cls._same_row(point, existed_point):
                return False
            if cls._same_column(point, existed_point):
                return False
            if cls._same_right_line(point, existed_point):
                return False
            if cls._same_left_line(point, existed_point):
                return False
        return True

    @classmethod
    def generate_matrix_from_nodes(cls, n, points):
        result = []
        for point in points:
            current_queen = point[1]
            current_row = "".join(
                ["." if i != current_queen else "Q" for i in range(n)]
            )
            result.append(current_row)
        return result

    def total_n_queens(self, n: int) -> int:
        cache_que = deque()
        current_solution = deque()
        result = []
        cache_que.append(None)
        while cache_que:
            current_point = cache_que.pop()
            if not current_point:
                current_row = -1
            else:
                current_row = current_point[0]
                while current_solution:
                    if current_solution[-1][0] >= current_row:
                        current_solution.pop()
                    else:
                        break
                current_solution.append(current_point)
            if len(current_solution) == n:
                result.append(list(current_solution))
            had_least_one_valid = False
            for i in range(n):
                new_point = (current_row + 1, i)
                if self.valid_points(new_point, current_solution):
                    cache_que.append((current_row + 1, i))
                    had_least_one_valid = True
            if not had_least_one_valid:
                current_solution.pop()

        return len(result)


if __name__ == "__main__":
    test_n = 4
    print(Solution().total_n_queens(test_n))
