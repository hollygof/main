# Пример входных данных для проверки функции
list_dict = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

def filter_by_state(list_dict: list, state: str='EXECUTED') -> list:
    '''Функция, выозврата словарей по ссответсвующиму ключу state'''
    filtered_list = []
    for item in list_dict:
        if item.get('state') == state:
            filtered_list.append(item)
    return filtered_list

def sort_by_date(list_dict: list, type_sort: bool=True) -> list:
    '''Функция, сортировки списка словарей по дате'''
    return sorted(list_dict, key=lambda x: x['date'], reverse=type_sort)

