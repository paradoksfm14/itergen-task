nested_list = [
    ['a', 'b', 'c', ['a', ['i', ['a', ['i', ['a', ['i']]]]]]],
    [[1, [2, [3, 4]]], 'd', 'e', 'f', 'h', False],
    [1, 2, None], 4, 4,
]


def flat_generator(nested_list):
    for items in nested_list:
        if isinstance(items, list):
            yield from flat_generator(items)
        else:
            yield items


class FlatIterator:

    def __init__(self, nested_list):
        self.nested_list = nested_list
        self.flat_list = []
        self.cursor = -1
        self.flat(self.nested_list)

    def flat(self, nested):
        if isinstance(nested, list):
            for items in nested:
                self.flat(items)
        else:
            self.flat_list.append(nested)
        return

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.flat_list) == (self.cursor + 1):
            raise StopIteration
        self.cursor += 1
        return self.flat_list[self.cursor]


if __name__ == '__main__':

    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)