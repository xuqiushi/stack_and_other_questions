from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.rows = {i: set() for i in range(9)}
        self.columns = {i: set() for i in range(9)}
        self.blocks = {i: set() for i in range(9)}

    def get_total_set(self, position):
        return (
            self.rows[position[0]]
            | self.columns[position[1]]
            | self.blocks[3 * (position[0] // 3) + position[1] // 3]
        )

    def add_total_set(self, position, value):
        i = position[0]
        j = position[1]
        for item in [self.rows[i], self.columns[j], self.blocks[3 * (i // 3) + j // 3]]:
            item.add(value)

    def del_total_set(self, position, value):
        i = position[0]
        j = position[1]
        for item in [self.rows[i], self.columns[j], self.blocks[3 * (i // 3) + j // 3]]:
            item.remove(value)

    def solve_sudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        blanks = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    self.add_total_set((i, j), board[i][j])
                else:
                    blanks.append((i, j))
        cache = deque()
        cache.append(None)
        result = deque()
        while cache:
            current_blank = cache.pop()
            if not current_blank:
                current_blank_position = blanks[0]
                for i in set([str(num) for num in range(1, 10)]) - self.get_total_set(
                    current_blank_position
                ):
                    cache.append((i, 0))
            else:
                while result and result[-1][1] >= current_blank[1]:
                    revert_point = result.pop()
                    self.del_total_set(blanks[revert_point[1]], revert_point[0])
                result.append(current_blank)
                self.add_total_set(blanks[current_blank[1]], current_blank[0])
                next_blank_index = current_blank[1] + 1
                if next_blank_index == len(blanks):
                    for sub_result in result:
                        board_position = blanks[sub_result[1]]
                        board[board_position[0]][board_position[1]] = sub_result[0]
                    return
                next_blank_position = blanks[next_blank_index]
                remaining_values = set(
                    [str(num) for num in range(1, 10)]
                ) - self.get_total_set(next_blank_position)
                if remaining_values:
                    next_blank_index = current_blank[1] + 1
                    for i in remaining_values:
                        cache.append((i, next_blank_index))
                else:
                    continue


if __name__ == "__main__":
    test_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    Solution().solve_sudoku(test_board)
    print(test_board)
