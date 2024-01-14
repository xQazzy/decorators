import os
from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            log_data = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'function_name': old_function.__name__,
                'arguments': {
                    'args': args,
                    'kwargs': kwargs
                },
                'result': result
            }

            with open(path, 'a') as log_file:
                log_file.write(str(log_data) + '\n')

            return result

        return new_function

    return __logger


class FlatIterator:
    @logger('flat_iterator.log')
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flatten_list = self.flatten()

    @logger('flat_iterator.log')
    def __iter__(self):
        self.current_index = 0
        return self

    @logger('flat_iterator.log')
    def __next__(self):
        if self.current_index < len(self.flatten_list):
            item = self.flatten_list[self.current_index]
            self.current_index += 1
            return item
        else:
            raise StopIteration

    @logger('flat_iterator.log')
    def flatten(self):
        flattened_list = []
        for sublist in self.list_of_list:
            for item in sublist:
                flattened_list.append(item)
        return flattened_list


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