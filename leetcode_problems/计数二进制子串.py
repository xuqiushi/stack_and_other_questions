from collections import OrderedDict


class Solution:
    def get_char_counts(self, word):
        char_count = []
        last_char = word[0]
        last_count = 0
        for char_index, char in enumerate(word):
            if char != last_char:
                char_count.append((last_char, last_count))
                last_char = char
                last_count = 1
            else:
                last_count += 1
            if char_index == len(word) - 1:
                char_count.append((last_char, last_count))
        return char_count

    def countBinarySubstrings(self, s: str) -> int:
        total_count = 0
        char_counts = self.get_char_counts(s)
        last_char_count = char_counts[0]
        for char_count in char_counts[1:]:
            min_length = min(last_char_count[1], char_count[1])
            total_count += min_length
            last_char_count = char_count
        return total_count


if __name__ == "__main__":
    test_string = "00100"
    solution = Solution()
    print(solution.countBinarySubstrings(test_string))
