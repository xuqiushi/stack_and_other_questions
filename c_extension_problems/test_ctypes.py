from ctypes import cdll, c_double, CDLL
from math import sqrt

test_sqrt = CDLL(
    "/Users/xuqiushi/workspace/stack_overflow_questions/c_utils/libtest_library.dylib"
)


if __name__ == "__main__":
    from datetime import datetime

    test_num = 1000000000000
    start = datetime.now()
    result = sqrt(test_num)
    print(datetime.now() - start)
    start = datetime.now()
    result = test_sqrt.my_sqrt(c_double(test_num))
    print(datetime.now() - start)
