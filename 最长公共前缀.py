from typing import List


class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        for i in range(min([len(word) for word in strs])):
            current_char = strs[0][i]
            current_satisfied = True
            for word in strs:
                if word[i] != current_char:
                    current_satisfied = False
                    break
            if current_satisfied:
                prefix += current_char
            else:
                break
        return prefix


if __name__ == "__main__":
    test_strs = ["flower", "flow", "flight"]
    print(Solution().longest_common_prefix(test_strs))
