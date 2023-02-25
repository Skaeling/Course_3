import requests, datetime


def load_data(data_path):
    """Получает json файл операций по ссылке возвращает список словарей"""
    raw_data = requests.get(data_path)
    data = raw_data.json()
    return data

