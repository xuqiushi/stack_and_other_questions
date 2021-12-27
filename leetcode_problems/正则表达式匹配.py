import re
from collections import deque


class Solution:
    @classmethod
    def match_char(cls, char_1, pattern_1):
        if pattern_1 == "." and char_1:
            return True
        else:
            return char_1 == pattern_1

    def is_match(self, s: str, p: str) -> bool:
        return not not re.fullmatch(p, s)

    def isMatch(self, s, p):
        pattern_que = deque(list(p))
        formatted_que = deque()
        extra_length = 0
        while pattern_que:
            current_char = pattern_que.popleft()
            if current_char == "*":
                last_char = formatted_que.pop()
                current_char = f"{last_char}*"
                formatted_que.append(current_char)
                extra_length -= 1
            else:
                formatted_que.append(current_char)
                extra_length += 1
        formatted_que = list(formatted_que)
        compare_que = deque([(s, formatted_que)])
        while compare_que:
            current_compared_pair = compare_que.pop()
            if current_compared_pair[1] == [] and len(current_compared_pair[0]) > 0:
                continue
            elif not current_compared_pair[0] and not current_compared_pair[1]:
                return True
            last_char = (
                current_compared_pair[0][-1]
                if len(current_compared_pair[0]) > 0
                else ""
            )
            last_pattern = current_compared_pair[1][-1]
            if "*" not in last_pattern:
                if not self.match_char(last_char, last_pattern):
                    continue
                else:
                    compare_que.append(
                        (current_compared_pair[0][:-1], current_compared_pair[1][:-1])
                    )
            else:
                if not self.match_char(last_char, last_pattern[0]):
                    compare_que.append(
                        (current_compared_pair[0], current_compared_pair[1][:-1])
                    )
                else:
                    if current_compared_pair[0]:
                        compare_que.append(
                            (current_compared_pair[0][:-1], current_compared_pair[1])
                        )
                    compare_que.append(
                        (current_compared_pair[0], current_compared_pair[1][:-1])
                    )
        return False


if __name__ == "__main__":
    test_s = "a"
    test_p = ".*..a*"
    print(Solution().isMatch(test_s, test_p))
