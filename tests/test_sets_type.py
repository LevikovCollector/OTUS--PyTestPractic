import pytest


@pytest.fixture
def fix_set():
    return {'I', 'like', 'python'}


def test_copy_fun(fix_set):
    '''Проверка функции copy'''
    new_set = fix_set.copy()
    assert new_set == fix_set


def test_remove_fun(fix_set):
    '''Проверка функции remove'''
    fix_set.remove('like')
    assert 'like' not in fix_set


@pytest.mark.parametrize('add_param', ['test1', 'test2'])
def test_add_fun(fix_set, add_param):
    '''Проверка функции add'''
    fix_set.add(add_param)
    assert add_param in fix_set


def test_inter_fun(fix_set):
    '''Проверка пересечения множества'''
    new_set = {'I', 'like', 'orange'}
    assert fix_set.intersection(new_set) == {'I', 'like'}


def test_clear_fun(fix_set):
    '''Проверка функции clear'''
    assert fix_set.clear() is None
