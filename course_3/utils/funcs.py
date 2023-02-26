import requests
import datetime as dt


def load_data(data_path):
    """Получает json файл операций по ссылке, возвращает список"""
    try:
        response = requests.get(data_path)
        if response.status_code == 200:
            return response.json()
        else:
            return None, f"Код ошибки: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return None, f"Ошибка: ConnectionError"


def data_filter(data):
    """Получает список всех операций,
    возвращает список операций со статусом EXECUTED,
    объекты, не содержащие статус операции - пропускает"""
    filter_data = []
    for i in data:
        if "state" in i and i["state"] == "EXECUTED":
            filter_data.append(i)
        else:
            continue
    return filter_data


def time_filter(data):
    """Сортирует элементы списка data по значению ключа "date"
    от новых к старым, возвращает первые пять значений data"""
    data = sorted(data, key=lambda k: k["date"], reverse=True)
    return data[:5]


def format_date(data):
    """Получает список с датами в формате год-месяц-день-час-минуты-секунды,
    возвращает список с датами в формате: день.месяц.год"""
    for i in data:
        i["date"] = dt.datetime.strptime(i["date"], '%Y-%m-%dT%H:%M:%S.%f')
        i["date"] = dt.date.strftime(i["date"], '%d.%m.%Y')
    return data
