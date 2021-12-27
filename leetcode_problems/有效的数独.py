from typing import List


class Solution:
    def is_valid_sudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        columns = {i: set() for i in range(9)}
        blocks = {i: set() for i in range(9)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    for item in [rows[i], columns[j], blocks[3 * (i // 3) + j // 3]]:
                        if board[i][j] in item:
                            return False
                        else:
                            item.add(board[i][j])
        return True


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
    print(Solution().is_valid_sudoku(test_board))
    pass
