import doctest

num_list = [1, 2, 3, 4, 5]


def example_one(num_list: list) -> int:
    """
    Функция принимает на вход список чисел, а возвращает
    список только с четными индексами исходного списка
    :param num_list:
    :return: array_chetn

    >>> example_one([1, 2, 3, 4, 5])
    [1, 3, 5]

    >>> example_one([1, 2, 3])
    [1, 3]

    >>> example_one([1, 2, 3, 4, 5, 6, 7, 10])
    [1, 3, 5, 7]

    """
    array_chetn = []
    for item in range(0, len(num_list), 2):
        array_chetn.append(num_list[item])
    return array_chetn


print(example_one(num_list))
help(example_one)