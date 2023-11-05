import doctest


def example_two(num_list: list):
    """
    Функция принимает на вход пользовательский список и возврашает
    уникальное количество элементов, которое в нем встретилось
    :param num_list:
    :return: count_unique_number

    >>> example_two([1, 1, 2, 2, 3, 3, 5, 5, 6, 6, 6])
    5

    >>> example_two([1, 2, 5, 10])
    4

    >>> example_two([1, 1, 2, 2, 2])
    2

    """
    count_unique_number = len(set(num_list))
    return count_unique_number


doctest.testmod()
help(example_two)