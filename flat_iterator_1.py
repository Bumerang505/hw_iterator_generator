class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.index_sublist = 0
        self.index_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        while len(self.list_of_list) > self.index_sublist:
            if len(self.list_of_list[self.index_sublist]) > self.index_item:
                item = self.list_of_list[self.index_sublist][self.index_item]
                self.index_item += 1
                return item
            else:
                self.index_sublist += 1
                self.index_item = 0
        raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
