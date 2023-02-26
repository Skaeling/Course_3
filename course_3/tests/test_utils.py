from utils import funcs
import pytest


def test_url():
    assert type(funcs.load_data("https://www.jsonkeeper.com/b/DVZ1")) == list
    assert funcs.load_data("https://www.jsonkeeper.com/b/DVZ1/в") == (None, 'Код ошибки: 404')
    assert funcs.load_data("https://ww.jsonkeeper.com/b/DVZ1") == (None, "Ошибка: ConnectionError")


@pytest.fixture
def coll():
    return [{'id': 214024827, 'state': 'EXECUTED', 'date': '2018-12-20T16:43:26.929246',
             'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Счет 10848359769870775355',
             'to': 'Счет 21969751544412966366'},
            {},

            {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582',
             'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},

            {'id': 970724427, 'state': 'CANCELED', 'date': '2019-01-15T17:58:27.064377',
             'operationAmount': {'amount': '90688.44', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'Visa Platinum 2241653116508487',
             'to': 'Счет 26494285169417058486'}
            ]


def test_filter(coll):
    assert len(funcs.data_filter(coll)) == 2
    assert "CANCELED" not in funcs.data_filter(coll)
    assert {} not in funcs.data_filter(coll)


def test_ops(coll):
    assert funcs.time_filter(funcs.data_filter(coll))[0] == coll[2]


def test_date(coll):
    with pytest.raises(KeyError):
        assert funcs.format_date(coll)
