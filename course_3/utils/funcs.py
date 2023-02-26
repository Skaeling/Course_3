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


def format_date(data):
    """Получает дату в формате год-месяц-день-час-минуты-секунды,
    возвращает дату в формате: день.месяц.год"""
    for i in data:
        i["date"] = dt.datetime.strptime(i["date"], '%Y-%m-%dT%H:%M:%S.%f')
        i["date"] = dt.date.strftime(i["date"], '%d.%m.%Y')
    return data
