class Test:
    pass


def swap(list_item, i, j):
    temp = list_item[i]
    list_item[i] = list_item[j]
    list_item[j] = temp


def ins_sort_with_tmp(list_item):
    count = 0
    for i in range(len(list_item)):
        j = i
        while j > 0 and list_item[j - 1] > list_item[j]:
            count = count + 1
            print(count)
            swap(list_item, j - 1, j)
            j = j - 1
    return list_item


def ins_sort(list_item):
    count = 0
    for i in range(len(list_item)):
        while i > 0 and list_item[i - 1] > list_item[i]:
            count = count + 1
            print(count)
            swap(list_item, i - 1, i)
            i = i - 1

    return list_item


if __name__ == "__main__":
    test_list = [1, 5, 4, 3, 1]
    print(ins_sort(test_list))
    # print(ins_sort_with_tmp(test_list))
