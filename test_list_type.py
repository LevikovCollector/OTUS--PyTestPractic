import pytest


# Добавление новых элементов (параметизированный)
@pytest.fixture
def fix_list():
    return [1, 2, 3, 4, 5]

@pytest.mark.parametrize('add_params', [6, 7, 8, 9])
def test_append_func(fix_list, add_params):
    fix_list.append(add_params)
    assert fix_list[-1] == add_params


# Проверка длинны списка
def test_len_fun(fix_list):
    assert len(fix_list) > 3


# Проверка функции clear
def test_clear_fun(fix_list):
    assert fix_list.clear() is None


# Проверкeа функции revers
def test_revers_fun(fix_list):
    fix_list.reverse()
    assert  fix_list == [5, 4, 3, 2, 1]
