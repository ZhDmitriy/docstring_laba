import pandas as pd

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


