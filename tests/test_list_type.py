import pytest


@pytest.fixture
def fix_list():
    return [1, 2, 3, 4, 5]


@pytest.mark.parametrize('add_params', [6, 7, 8, 9])
def test_append_func(fix_list, add_params):
    '''Добавление новых элементов (параметизированный)'''
    fix_list.append(add_params)
    assert fix_list[-1] == add_params


def test_len_fun(fix_list):
    '''Проверка длинны списка'''
    assert len(fix_list) > 3


def test_clear_fun(fix_list):
    '''Проверка функции clear'''
    assert fix_list.clear() is None


def test_revers_fun(fix_list):
    '''Проверкeа функции revers'''
    fix_list.reverse()
    assert fix_list == [5, 4, 3, 2, 1]


def test_insert_fun(fix_list):
    '''Проверкeа функции insert'''
    fix_list.insert(3, 'otus')
    assert fix_list[3] == 'otus'
