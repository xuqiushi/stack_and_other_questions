from collections import deque
import numpy as np


class Solution:
    @classmethod
    def dp_search(cls, s):
        length = len(s)
        dp = [[0 for _ in range(length)] for _ in range(length)]
        max_length = 0
        for i in range(length - 1, -1, -1):
            for j in range(i + 1, length, 2):
                if j - i == 1:
                    if s[i] == "(" and s[j] == ")":
                        dp[i][j] = True
                    else:
                        dp[i][j] = False
                else:
                    if (j - i + 1) % 2 != 0:
                        dp[i][j] = False
                    if s[i] == s[j] == "(":
                        dp[i][j] = False
                    elif s[i] == s[j] == ")":
                        dp[i][j] = False
                    elif s[i] == ")" and s[j] == "(":
                        dp[i][j] = False
                    elif s[i] == "(" and s[j] == ")":
                        tmp_judge = dp[i + 1][j - 1]
                        for k in range(j - 2, i - 1, -2):
                            if dp[k + 1][j] and dp[i][k]:
                                tmp_judge = True
                                break
                        dp[i][j] = tmp_judge
                if dp[i][j]:
                    if j - i + 1 > max_length:
                        max_length = j - i + 1
        return max_length

    @classmethod
    def stack_search(cls, s):
        if not s:
            return 0
        current_left_que = deque()
        result = []
        for i in range(len(s)):
            if s[i] == "(":
                current_left_que.append(i)
            elif current_left_que and s[i] == ")":
                left = current_left_que.pop()
                right = i
                if not result:
                    result.append((left, right))
                else:
                    last = result[-1]
                    if left < last[0] and right > last[1]:
                        result.pop()
                        result.append((left, right))
                    else:
                        result.append((left, right))
                    if len(result) < 2:
                        continue
                    last = result[-1]
                    last_last = result[-2]
                    if last_last[1] + 1 == last[0]:
                        result.pop()
                        result.pop()
                        result.append((last_last[0], last[1]))
        return max([x[1] - x[0] + 1 if x else 0 for x in result]) if result else 0

    def longest_valid_parentheses(self, s: str) -> int:
        return self.dp_search(s)


if __name__ == "__main__":
    test_s = ")(((((()())()()))()(()))("
    print(Solution().longest_valid_parentheses(test_s))
