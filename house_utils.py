import csv

import conf


def get_data():
    """
    :return: All data,type = list
    """
    data = []
    with open('house_data.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for d in reader:
            data.append(d)
    return data


DATA_LIST = get_data()


def select_by_column(column_name: str, select_data=None):
    """
    :param
        select_data: find data in select_data
    :param column_name: column's name
    :return: column data in (column_name),type = list
    """
    if select_data is None:
        select_data = DATA_LIST
    assert column_name in conf.TITLE, "title name not found!"

    selected_data = []
    index = conf.TITLE.index(column_name)
    for i in select_data:
        selected_data.append(i[index])
    return selected_data


def select_by_name(name: str):
    """
    :param name: city's name
    :return: all house data in (city_name),type = list
    """
    global name_index
    if name in conf.CITY_LIST:
        name_index = 10
    elif name in conf.ORIENTATION_LIST:
        name_index = 8
    elif name in conf.REGION_LIST:
        name_index = 1
    elif name in conf.HOUSE_TYPE_LIST:
        name_index = 7
    else:
        raise NameError(f'no name is {name}')
    selected_data = []
    for i in DATA_LIST:
        if name == i[name_index]:
            selected_data.append(i)
    return selected_data


def convert_traffic_to_digital(traffic_flag: str) -> int:
    if traffic_flag == '空':
        return 0
    return 1


if __name__ == '__main__':
    for i in select_by_name('朝南'):
        print(i)
    print('end')
