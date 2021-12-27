from itertools import count


def gen_stream(total, sorted_iterable, extractor=lambda x: x):
    sorted_iterator = iter(sorted_iterable)  # transform to iterator
    iterable = count() if total is None else range(total)
    try:  # get first value
        current_extracted_record = extractor(next(sorted_iterator))
    except StopIteration:
        current_extracted_record = None
    for i in iterable:
        if current_extracted_record:
            if i == current_extracted_record[0]:
                try:  # get next value
                    yield current_extracted_record[1]
                    current_extracted_record = extractor(next(sorted_iterator))
                except StopIteration:
                    current_extracted_record = None
            else:
                yield 0
        else:
            yield 0


if __name__ == "__main__":
    gen = gen_stream(9, [(4, 111), (7, 12)])

    print(list(gen))
