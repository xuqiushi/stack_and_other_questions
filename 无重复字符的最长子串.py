from collections import Counter, OrderedDict
import numpy as np


class CharTokenizer(object):
    def __init__(self, word):
        self.token = {
            item: item_index
            for item_index, item in enumerate(Counter(list(word)).keys())
        }

    def encode(self, word):
        encoded_list = []
        for char in word:
            encoded_list.append(self.token[char])
        return encoded_list


class SolutionOne:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        tokenizer = CharTokenizer(s)
        max_word = len(tokenizer.token)
        encoded_chars = tokenizer.encode(s)
        binary_word = np.eye(max_word)[encoded_chars, :]
        for length in range(max_word, 1, -1):
            for index in range(len(s) - length + 1):
                sub_binary = binary_word[index : index + length]
                if (sub_binary.sum(axis=0) < 2).all():
                    return length
        return 1


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        current_sub_word = OrderedDict({})
        current_sub_word_char_index = 0
        current_start = 0
        all_max_length = []
        max_length = len(set(list(s)))
        if max_length == len(s):
            return max_length
        for char_index, char in enumerate(s):
            if char not in current_sub_word:
                current_sub_word[char] = current_sub_word_char_index
                current_sub_word_char_index += 1
            else:
                if len(current_sub_word) == max_length:
                    return max_length
                all_max_length.append(len(current_sub_word))
                old_same_char_position = current_sub_word[char]
                new_start = old_same_char_position + 1
                current_sub_word = OrderedDict(
                    list(current_sub_word.items())[new_start - current_start:]
                )
                current_start = new_start
                current_sub_word[char] = current_sub_word_char_index
                current_sub_word_char_index += 1
        return max(all_max_length + [len(current_sub_word)])


if __name__ == "__main__":
    test_string = "bpfbhmipx"
    print(Solution().lengthOfLongestSubstring(test_string))
