from typing import List


class Solution:
    def group_anagrams(self, str_list: List[str]) -> List[List[str]]:
        result = {}
        for string in str_list:
            tag = "".join(sorted(list(string)))
            if tag in result:
                result[tag].append(string)
            else:
                result[tag] = [string]
        return list(result.values())


if __name__ == "__main__":
    test_str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().group_anagrams(test_str_list))
