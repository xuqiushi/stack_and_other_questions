from collections import Counter


class Solution:
    def judge_circle(self, moves: str) -> bool:
        moves_counter = Counter(moves)
        up = moves_counter.get("U", 0)
        down = moves_counter.get("D", 0)
        right = moves_counter.get("R", 0)
        left = moves_counter.get("L", 0)
        return up == down and right == left


if __name__ == "__main__":
    test_moves = "UD"
    print(Solution().judge_circle(test_moves))
