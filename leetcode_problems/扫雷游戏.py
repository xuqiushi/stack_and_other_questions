from typing import List
from collections import deque


class Solution:
    @classmethod
    def computed_landmine(cls, position, board, already_click):
        already_click[position] = True
        mine_count = 0
        safe_position = deque()
        for i in range(position[0] - 1, position[0] + 2):
            for j in range(position[1] - 1, position[1] + 2):
                if 0 <= i < len(board) and 0 <= j < len(board[0]):
                    if (i, j) in already_click:
                        continue
                    elif board[i][j] == "M":
                        mine_count += 1
                    elif board[i][j] == "E":
                        safe_position.append((i, j))
        return mine_count, safe_position

    @classmethod
    def click_landmine(cls, position, board):
        board[position[0]][position[1]] = "X"

    def update_board(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        click = tuple(click)
        already_click = {}
        to_click_point = deque()
        to_click_point.append(click)
        while to_click_point:
            point = to_click_point.pop()
            if board[point[0]][point[1]] == "M":
                board[point[0]][point[1]] = "X"
            else:
                mine_count, safe_position = self.computed_landmine(
                    point, board, already_click
                )
                if mine_count > 0:
                    board[point[0]][point[1]] = str(mine_count)
                else:
                    board[point[0]][point[1]] = "B"
                    for item in safe_position:
                        if item not in already_click:
                            to_click_point.append(item)
        return board


if __name__ == "__main__":
    test_board = [
        ["E", "E", "E", "E", "E"],
        ["E", "E", "M", "E", "E"],
        ["E", "E", "E", "E", "E"],
        ["E", "E", "E", "E", "E"],
    ]
    test_click = [3, 0]
    print(Solution().update_board(test_board, test_click))
