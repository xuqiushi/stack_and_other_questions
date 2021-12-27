if __name__ == "__main__":

    class CustomList(list):
        def __init__(self, seq=()):
            self.last_equal_items = []
            super().__init__(seq)

        def append(self, some_item):
            if self.last_equal_items and some_item != self.last_equal_items[-1]:
                self.last_equal_items = []
            self.last_equal_items.append(some_item)
            if len(self.last_equal_items) >= 3:
                raise ValueError("Last equal_items larger that 3")
            else:
                super(CustomList, self).append(some_item)

    test = CustomList([])
    test.append(1)
    test.append(1)
    test.append(2)
    test.append(2)
    test.append(2)
    print(test)
