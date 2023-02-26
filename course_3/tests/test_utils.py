from utils import funcs

def test_url():
    assert type(funcs.load_data("https://www.jsonkeeper.com/b/DVZ1")) == list
    assert funcs.load_data("https://www.jsonkeeper.com/b/DVZ1/в") == (None, 'Код ошибки: 404')
    assert funcs.load_data("https://ww.jsonkeeper.com/b/DVZ1") == (None, "Ошибка: ConnectionError")
