from math import floor
from typing import List


class Solution:
    @classmethod
    def _is_palindrome(cls, word_part):
        half_length = floor(len(word_part) / 2)
        return (
            True
            if len(word_part) == 1
            else word_part[:half_length] == word_part[-half_length:][::-1]
        )

    @classmethod
    def _get_palindrome_part(cls, word, word_index, restore_dict):
        palindrome_part_list = []
        for char_index in range(len(word)):
            left = word[:char_index]
            right = word[char_index:]
            if (
                left
                and left[::-1] in restore_dict
                and restore_dict[left[::-1]] != word_index
                and cls._is_palindrome(right)
            ):
                palindrome_part_list.append([word_index, restore_dict[left[::-1]]])
            if (
                right[::-1] in restore_dict
                and restore_dict[right[::-1]] != word_index
                and cls._is_palindrome(left)
            ):
                palindrome_part_list.append([restore_dict[right[::-1]], word_index])
        return palindrome_part_list

    @classmethod
    def palindrome_pairs(cls, words: List[str]) -> List[List[int]]:
        restore_dict = {}
        palindrome_word = {}
        result = []
        for word_index, word in enumerate(words):
            restore_dict[word] = word_index
            if word and word == word[::-1]:
                palindrome_word[word] = word_index
        for word_index, word in enumerate(words):
            if not word:
                for value in palindrome_word.values():
                    result += [[value, word_index], [word_index, value]]
                continue
            result += cls._get_palindrome_part(
                word, word_index, restore_dict
            )
        return result


if __name__ == "__main__":
    test_list = ["a",""]
    print(Solution().palindrome_pairs(test_list))
    # start = datetime.now()
    # lp = LineProfiler()
    # lp_wrapper = lp(Solution().palindrome_pairs)
    # lp_wrapper(test_list)
    # lp.print_stats()
    # print(datetime.now() - start)
