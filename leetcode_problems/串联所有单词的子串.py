from typing import List
from copy import copy
from collections import Counter


class Solution:
    @classmethod
    def get_part_matched_values(cls, words):
        result = []
        word_length = len(words[0])
        for word in words:
            sub_part_matched_values = []
            prefix = []
            suffix = []
            for i in range(word_length):
                if i == 0:
                    sub_part_matched_values.append(0)
                else:
                    prefix.append(word[: i - 1])
                    for suffix_index in range(len(suffix)):
                        suffix[suffix_index] += word[i]
                    suffix.append(word[i])
                    current_same_fix = set(prefix) & set(suffix)
                    if len(current_same_fix) == 0:
                        current_value = 0
                    else:
                        current_value = max([len(word) for word in current_same_fix])
                    sub_part_matched_values.append(current_value)
            result.append(sub_part_matched_values)
        return result

    @classmethod
    def get_matched_count(cls, s, words):
        sub_matched_count = [0 for _ in words]
        for i in range(len(words[0])):
            sub_match_count = 0
            for word_index in range(len(words)):
                if words[word_index][i] == s[i]:
                    sub_matched_count[word_index] += 1
                    sub_match_count += 1
            if sub_match_count == 0:
                break
        return sub_matched_count

    def find_substring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        result = []
        part_matched_values = self.get_part_matched_values(words)
        word_length = len(words[0])
        word_count = len(words)
        char_index = 0
        while char_index <= len(s) - word_count * word_length:
            sub_match_count = self.get_matched_count(
                s[char_index : char_index + word_length], words
            )
            if max(sub_match_count) < word_length:
                min_steps = []
                for sub_index, sub_count in enumerate(sub_match_count):
                    part_matched_value = part_matched_values[sub_index][sub_count - 1]
                    new_step = sub_count - part_matched_value
                    if new_step < 0:
                        continue
                    else:
                        min_steps.append(new_step)
                if min_steps:
                    new_step = min(min_steps)
                else:
                    new_step = 1
                char_index += new_step if new_step > 0 else 1
            else:
                cache_word_list = copy(words)
                remaining_s = s[
                    char_index + word_length : char_index + word_length * word_count
                ]
                remaining_s_list = [
                    remaining_s[i : i + word_length]
                    for i in range(0, len(remaining_s), word_length)
                ]
                for word_index in range(len(cache_word_list)):
                    if sub_match_count[word_index] == word_length:
                        cache_word_list.pop(word_index)
                        break
                if Counter(remaining_s_list) == Counter(cache_word_list):
                    success = True
                else:
                    success = False
                if success:
                    result.append(char_index)
                char_index += 1
        return result


if __name__ == "__main__":
    test_string = "aabbaabbaabb"

    test_words = ["bb", "aa", "bb", "aa", "bb"]
    print(Solution().find_substring(test_string, test_words))
