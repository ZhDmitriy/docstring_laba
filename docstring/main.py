"""
Модуль содержит решения трех задач лабораторной работы номер 7.
Две функции из трех покрыты доктестами.
"""

import doctest
import pandas as pd

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

res_file = """Ivanov paper 10
Petrov pens 5
Ivanov marker 3
Ivanov paper 7
Petrov envelope 20
Ivanov envelope 5"""


def count_goods_on_customer(res_file: str) -> pd.DataFrame:
    """
    Функция возвращает количество покупок на одного клиента по видам продуктов
    :return: data_result
    """
    client = []
    goods = []
    count_goods = []

    for item in res_file.split("\n"):
        client.append(item.split(" ")[0])
        goods.append(item.split(" ")[1])
        count_goods.append(item.split(" ")[2])

    data_result = {'client': client, 'goods': goods, 'count_goods': count_goods}
    data_result = pd.DataFrame(data_result)
    data_result = data_result.groupby(['client', 'goods']).sum()

    return data_result