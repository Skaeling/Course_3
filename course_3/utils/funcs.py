import requests
import datetime as dt


def load_data(data_path):
    """Получает json файл операций по ссылке возвращает список"""
    data = requests.get(data_path)
    return data.json()


def data_filter(data):
    """Получает список всех операций, возвращает список операций со статусом EXECUTED"""
    filter_data = []
    for i in data:
        # сейчас попадают операции без ключа from
        if "state" in i:
            if i["state"] == "EXECUTED":
                filter_data.append(i)
        else:
            continue
    return filter_data


def time_filter(data):
    """Сортирует элементы по ключу "date" от новых к старым,
    возвращает первые пять значений data"""
    data = sorted(data, key=lambda k: k["date"], reverse=True)
    return data[:5]

