def filter_list(target_list, **kwargs):
    filtered_list = target_list
    for k, v in kwargs.items():
        for target in filtered_list:
            if target[k] < v[0] or target[k] > v[1]:
                filtered_list.remove(target)

    return filtered_list


def filter_list_with_copy(target_list, **kwargs):
    filtered_list = []
    for target in target_list:
        all_satisfied = True
        for k, v in kwargs.items():
            if target[k] < v[0] or target[k] > v[1]:
                all_satisfied = False
                break
        if all_satisfied:
            filtered_list.append(target)
    return filtered_list


def filter_list_with_while(target_list, **kwargs):
    filtered_list = target_list
    for k, v in kwargs.items():
        filtered_index = 0
        filtered_list_length = len(filtered_list)
        while filtered_index < filtered_list_length:
            target = filtered_list[filtered_index]
            if target[k] < v[0] or target[k] > v[1]:
                filtered_list.remove(target)
                filtered_list_length = len(filtered_list)
            else:
                filtered_index += 1
    return filtered_list


if __name__ == "__main__":
    import time

    test_list = [
        {"hello": 1, "goodbye": 4},
        {"hello": 7, "goodbye": 6},
        {"hello": 4, "goodbye": 2},
    ]
    params = {"hello": [1, 6], "goodbye": [5, 8]}
    filter_it = filter_list(test_list, **params)
    print(filter_it)
    filter_it_2 = filter_list_with_copy(test_list, **params)
    print(filter_it_2)
    filter_it_3 = filter_list_with_while(test_list, **params)
    print(filter_it_3)
