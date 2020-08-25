class Solution:
    def repeated_substring_pattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        for sub_len in range(1, int(len(s) / 2 + 1)):
            if len(s) % sub_len == 0:
                sub_starts = range(0, len(s), sub_len)
                break_sign = False
                for i in range(sub_len):
                    if break_sign:
                        break
                    current_char = s[i]
                    for sub_index in sub_starts:
                        if break_sign:
                            break
                        if s[sub_index + i] != current_char:
                            break_sign = True
                if not break_sign:
                    return True
        return False

    def repeated_substring_pattern2(self, s):
        if len(s) == 0:
            return False

        new_string = (s + s)[1: -1]
        return new_string.find(s) != -1


if __name__ == "__main__":
    test_string = "aba"
    print(Solution().repeated_substring_pattern2(test_string))
