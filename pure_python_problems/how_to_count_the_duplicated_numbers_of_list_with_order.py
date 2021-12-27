if __name__ == "__main__":
    from collections import OrderedDict

    numbers = [5, 10, 10, 10, 15, 15, 8, 8, 8, 8]
    answer = [1, 3, 2, 4]
    result_map = OrderedDict()
    for item in numbers:
        if item in result_map:
            result_map[item] += 1
        else:
            result_map[item] = 1
    result = list(result_map.values())
    print(result)

    result = []
    last_value = None
    for item in numbers:
        if last_value == item:
            result[-1] += 1
        else:
            result.append(1)
            last_value = item
    print(result)
