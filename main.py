import os
import types
import datetime


def logger(old_function):
    pass

    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        date_time = datetime.datetime.now()
        with open('HW_generator.log', 'a', encoding='utf8') as file:
            file.writelines(
                f'date_time: {date_time}, name_function: {old_function.__name__}, value: {args, kwargs}, result: {result}\n')
        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists('generator.log'):
        os.remove('generator.log')

    @logger
    def flat_generator(list_of_lists):
        for check_list in list_of_lists:
            for item in check_list:
                yield item

    @logger
    def test_2():

        list_of_lists_1 = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None]
        ]

        for flat_iterator_item, check_item in zip(
                flat_generator(list_of_lists_1),
                ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
        ):
            print(flat_iterator_item, check_item)

            assert flat_iterator_item == check_item

        assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

        assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    test_2()


if __name__ == '__main__':
    test_1()