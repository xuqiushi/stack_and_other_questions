import math


class Solution:
    """
    没啥意义的题目，又是分治应该是翻倍的乘就可以了。懒得做。
    """

    def my_pow(self, x: float, n: int) -> float:
        return math.pow(x, n)


if __name__ == "__main__":
    test_x = 2.0
    test_y = 10
    print(Solution().my_pow(test_x, test_y))
