import requests, datetime


def load_data(data_path):
    """Получает json файл операций по ссылке возвращает список словарей"""
    raw_data = requests.get(data_path)
    data = raw_data.json()
    return data


def data_filter(load_data):
    """Получает список всех операций, возвращает список операций со статусом EXECUTED"""
    filter_data = []
    for dict in load_data:
        if "state" in dict:
            if dict["state"] == "EXECUTED":
                filter_data.append(dict)
        else:
            continue
    return filter_data

